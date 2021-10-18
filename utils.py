import pandas as pd
import  matplotlib.pyplot as plt
import database.database as db

from dataset import Dataset
from features_handler import Features_handler
from dotenv import load_dotenv, find_dotenv

def create_csv(csv_data):
    load_dotenv(find_dotenv())
    
    results = db.getAll()

    longs = []
    lats = []
    noises = []
 
    for res in results:
        longs.append(res.longitude)
        lats.append(res.latitude)
        noises.append(res.noise)

    data = pd.DataFrame({'latitude':lats, 'longitude': longs, 'noise':noises})

    print('Noises data saved at path {0}'.format(csv_data))
    
    data.to_csv(csv_data, index=False)

def create_csv_features(csv_data, csv_train_data, csv_test_data):
    ''' Also returns the Dataset object containig the data'''
    dataset = Dataset()
    dataset.load_data(csv_data)
    
    dataset.split(0.20, 42)

    featurehandler = Features_handler()   
   
    # convert altitude and longitude to radiants -> for haversine
    dataset.x_train = featurehandler.to_radiants(dataset.x_train)
    dataset.y_train = featurehandler.round_values(dataset.y_train)

    featurehandler.init_learners(dataset.x_train[['latitude', 'longitude']], [5, 10])
    
    new_neighbors_features = featurehandler.get_neighbors_features(
        dataset.x_train[['latitude', 'longitude']],
        dataset.y_train)

    for feature_name, values in new_neighbors_features.items():
        dataset.add_column_to_train(feature_name, values)
    
    dataset.train_to_csv(csv_train_data)
    print('Train data saved at path {0}'.format(csv_train_data))
    
    dataset.test_to_csv(csv_test_data)
    print('Test data saved at path {0}'.format(csv_test_data))
    
    return dataset

def plot(x_label, y_label, title, file_name):
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title)
    plt.savefig("./plots/{}.png".format(file_name))

    plt.clf()
