import pandas as pd 

df = pd.read_csv(r"C:\Users\BabitaTiwari\Downloads\Delhi-Electricity-SubStations.csv")

print(df)

def split_telephones(series):
    split_series = series.str.split('/').apply(pd.Series)
    split_series.columns= ['Telephone Numbers_{}'.format(i+1) for i in range(split_series.shape[1])]
    return split_series

# Applying the above function. 

new_columns = split_telephones(df['Telephone Numbers'])

df = df.drop('Telephone Numbers', axis=1).join(new_columns)

print(df)

import geopy 
from geopy.distance import geodesic
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent = "geoapiExercises")

def find_coordinates(address):
    location = geolocator.geocode(address)
    return (location.latitude, location.longitude)

def calculate_accuracy(given_coordinates, found_coordinates):
    distance = geodesic(given_coordinates, found_coordinates).meters
    accuracy = 100 - (distance/10)* 10
    if accuracy< 0:
        accuracy = 0
        return round(accuracy, 2)
    
    # example usage 

given_coordinates  = (28.79568, 77.0723)
address = "Bawana, Sector-5, Delhi"
found_coordinates = find_coordinates(address)
accuracy = calculate_accuracy(given_coordinates, found_coordinates)
print (f"Accuracy: {accuracy}%")