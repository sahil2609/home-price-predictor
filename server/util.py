from glob import glob
from warnings import catch_warnings
import numpy as np 
import json
import pickle
from shutil import which

__locations = None
__model = None
__data_columns = None


def predict_price(location, sqft, bhk, bath):
    try:
        location_index = __data_columns.index(location.lower())
    except:
        location_index = -1

    x = np.zeros(len(__data_columns))
    x[0] = sqft
    x[1] = bhk
    x[2] = bath
    if(location_index > 2):
        x[location_index] = 1


    return round(__model.predict([x])[0],2)

def get_location_names():
    return __locations
#rb for binary model
def load_saved_artifacts():
    print("loading saved artifacts")
    global __locations
    global __data_columns
    global __model

    with open("./artifacts/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __locations = __data_columns[3:]  # first 3 columns are sqft, bath, bhk
        
    with open("./artifacts/banglore_home_prices_model.pickle", "rb") as f:
        __model = pickle.load(f)

    print("huisha")
    print("done")

if __name__ == "__main__":
    load_saved_artifacts()
    
    print(predict_price('1st Phase JP Nagar',1000, 3, 3))
    print(predict_price('1st Phase JP Nagar', 1000, 2, 2))
    print(predict_price('Kalhalli', 1000, 2, 2)) # other location
    print(predict_price('Ejipura', 1000, 2, 2))  # other location
    print(get_location_names())
