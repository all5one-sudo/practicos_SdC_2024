import requests
import json
from ctypes import CDLL, c_float, c_int

# Cargamos la libreria 
lib = CDLL('./TP2_mac_arm.so')
#lib = CDLL('./TP2.so') #

lib.process_data.argtypes = [c_float]
lib.process_data.restype = c_int

def get_gini_index(country):
    url = f"https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
    response = requests.get(url)
    data = response.json()
    return data[1]

json_data = get_gini_index("AR")

#print(json.dumps(json_data,indent=2)) #imprime todos los datos que coincidieron con "AR"

values = [json_data[i]['value'] for i in range(len(json_data)) if json_data[i]['value'] is not None]
years = [json_data[i]['date'] for i in range(len(json_data)) if json_data[i]['value'] is not None]

print(values) #imprime los valores de "value" que no son nulos

result = lib.process_data(4.2)

print(result)


#print(years) #imprime los valores de "date" que no son nulos