import os
import utils

from dataset import Dataset
from features_extraction import Features_handler

csv_data =  "./data/noises.csv"
csv_data_new_features = "./data/noises_features.csv"

def main():    
    if not os.path.exists(csv_data_new_features):
        
        if not os.path.exists(csv_data):
            utils.create_csv()

        utils.create_csv_features(csv_data, csv_data_new_features)



# def create_csv_features( ):
#     dataset = Dataset(csv_data)
#     dataset.split(0.20, 42)

#     featurehandler = Features_handler()   
   
#     # convert to radiants -> for haversine
#     dataset.x_train = featurehandler.to_radiants(dataset.x_train)
#     dataset.y_train = featurehandler.round_lvalues(dataset.y_train)

#     featurehandler.init_learners(dataset.x_train, [5, 10])
    
#     new_neighbors_features = featurehandler.get_neighbors_features(
#         dataset.x_train,
#         dataset.y_train)

#     for feature_name, values in new_neighbors_features.items():
#         dataset.x_train[feature_name] = values
    
#     dataset.train_to_csv(csv_data_new_features)


if __name__ == '__main__':
    main()
