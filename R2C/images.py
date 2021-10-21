from numpy.lib.type_check import imag
import pandas as pd
from serpapi import GoogleSearch

import csv

cols_list = ["Medicine Name"]
df = pd.read_csv("drugs.csv", encoding = "ISO-8859-1", usecols= cols_list)

medicines = df["Medicine Name"][20:40]
images = []

for medicine in medicines:
    q = medicine
    params = {
    "engine": "google",
    "q": q,
    "api_key": "e15a872831cb5358a4e1cf10d8150edb9ef26c93256fccc49d2e9c15647fe892",
    "tbm" : "isch",
    "ijn" : 0,
    }
    search = GoogleSearch(params)    
    results = search.get_dict()
    if results['search_metadata']['status']=='Success':        
        img = results['images_results'][0]['original']
        images.append(img)


df = pd.read_csv("drugs.csv", encoding = "ISO-8859-1")
rows = images
file = open('images.csv', 'w+') 
with file:     
    write = csv.writer(file) 
    write.writerow(rows) 

