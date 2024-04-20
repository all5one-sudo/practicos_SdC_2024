import requests
import json
from ctypes import CDLL, c_float, c_int
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Cargamos la libreria
lib = CDLL('./TP2_mac_arm.so') #para ejecutar en arm64
#lib = CDLL('./TP2.so') #

# Definimos los tipos de los argumentos y el tipo de retorno de la funcion
lib.process_data.argtypes = [c_float]
lib.process_data.restype = c_int

# Definimos la funcion que se encargara de obtener los datos para un determinado countryiso3code
def get_gini_index(country):
    url = f"https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
    response = requests.get(url)
    data = response.json()
    return data[1]

# se puede agregar un manejo de errores para el caso de que el pais no exista try except

# Definimos la funcion que se encargara de imprimir los paises y sus codigos iso3
def print_countries():
    url = 'https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22'
    response = requests.get(url)
    data = response.json()
    country_list = []
    # Verificamos que los datos esten en el formato esperado
    if isinstance(data, list) and isinstance(data[0], dict):
        for item in data[1]:
            if 'country' in item and 'value' in item['country'] and 'countryiso3code' in item:
                country_and_code = f"{item['country']['value']}, {item['countryiso3code']}"
                if country_and_code not in country_list:
                    country_list.append(country_and_code)
    else:
        print('Data is not in the expected format')
    # Imprimimos los paises y sus codigos iso3
    for i in range(len(country_list)):
        print(country_list[i])

# Funcion principal
if __name__ == "__main__":
    print('A continuacion se listan los paises y sus codigos iso3:')
    print_countries()
    print('Ingrese el codigo iso3 del pais que desea consultar (\'-\' para terminar):')
    # Iteramos hasta que el usuario ingrese '-'
    while(True):
        country = str(input())
        if country != '-':
            if len(country) <= 3 and len(country) > 1:
                # Obtenemos los datos del pais y graficamos el Gini Index
                json_data = get_gini_index(country)
                values = [json_data[i]['value'] for i in range(len(json_data)) if json_data[i]['value'] is not None]
                years = [json_data[i]['date'] for i in range(len(json_data)) if json_data[i]['value'] is not None]
                processed_values = []
                for i in range(len(values)):
                    aux_value = lib.process_data(values[i])
                    processed_values.append(aux_value)
                df = pd.DataFrame({'year': years, 'values': values, 'processed_values': processed_values})
                plt.figure()
                plt.plot(df['year'], df['values'], label='Gini Index')
                plt.plot(df['year'], df['processed_values'], label='Processed Gini Index')
                plt.xlabel('Year')
                plt.ylabel('Gini Index')
                plt.title(f'Gini Index for {country}')
                plt.legend()
                # Guardamos la imagen
                plt.savefig(f'Gini_Index_{country}.png')
                #plt.show()
            else:
                print('El codigo ingresado no es valido, por favor ingrese un codigo iso3 valido:')
        else:
            break

# probar integracion, sistema, validacion de usuario

# Para probar el sistema tendria que probar levantar un servidor para probar que las apis y las conexiones funciones, pruebo el uso de requests y los response
