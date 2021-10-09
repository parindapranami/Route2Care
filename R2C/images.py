from numpy.lib.type_check import imag
import pandas as pd
from serpapi import GoogleSearch

cols_list = ["Medicine Name"]
df = pd.read_csv("R2C/drugs.csv", encoding = "ISO-8859-1", usecols= cols_list)
# print(df)
medicines = df["Medicine Name"].head()
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
        # print(results)
        img = results['images_results'][0]['original']
        images.append(img)
    # print(img)
print(images)

# for image in images:
#     df[]