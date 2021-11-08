import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_regression

class Dataset:
    def __init__(self):
        self.data = None

        self.x_train = None
        self.y_train = None
        
        self.x_test = None
        self.t_test = None

        # features subset indices
        self.feat_subset_indices = None
    
    @property
    def x_train_base(self):
        return self.x_train[['latitude', 'longitude']]
    
    @property
    def y_test_base(self):
        return self.x_test[['latitude', 'longitude']]

    @property
    def x_train_subset(self):
        return self.x_train.iloc[:, self.feat_subset_indices]
    
    @property
    def y_test_subset(self):
        return self.x_test.iloc[:, self.feat_subset_indices]


    def load_data(self, csv_path):
        ''' Load general data from csv'''
        self.data = pd.read_csv(csv_path)
    
    def load_train_test_data(self, csv_train, csv_test):
        ''' Load train and test data from specific csv'''
        train_data = pd.read_csv(csv_train)
        self.x_train = train_data[train_data.columns.drop('noise')]
        self.y_train = train_data['noise']
        
        test_data = pd.read_csv(csv_test)
        self.x_test = test_data[test_data.columns.drop('noise')]
        self.y_test = test_data['noise']


    def split(self, test_size, random_state):
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(
        self.data[self.data.columns.drop('noise')], # all columns except noise
        self.data['noise'],
        test_size=test_size,
        random_state=random_state)

    def add_column_to_train(self, name, values):
        self.x_train[name] = values

    def add_column_to_test(self, name, values):
        self.x_test[name] = values

    def train_to_csv(self, path):
        to_save = self.x_train.join(self.y_train)
        to_save.to_csv(path, index = False)

    def test_to_csv(self, path):
        to_save = self.x_test.join(self.y_test)
        to_save.to_csv(path, index = False)
    
    def select_best_features(self, k_value):
        ''' from train data '''
        features_selector = SelectKBest(f_regression, k = k_value).fit(self.x_train, self.y_train)
        self.feat_subset_indices = features_selector.get_support(indices=True)

