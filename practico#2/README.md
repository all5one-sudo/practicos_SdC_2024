# Informe sobre Stack Frame en Sistemas de Computación

En el ámbito de la informática, la interacción entre hardware y software es fundamental para el desarrollo de sistemas complejos. Los sistemas compuestos por capas de hardware y software utilizan diferentes niveles de abstracción para facilitar la programación y la interacción con el hardware subyacente.

## Arquitectura de Capas en Software Embebido

Se destaca la importancia de la arquitectura de capas en el desarrollo de software embebido para gestionar el crecimiento de la lógica a implementar en productos con múltiples funcionalidades.

## API RESTful

Se describe en detalle el funcionamiento de una API RESTful, incluyendo la transferencia de representaciones de recursos solicitados a través de HTTP en formatos como JSON, HTML, entre otros. Se explican los criterios que una API debe cumplir para considerarse RESTful, así como sus ventajas en comparación con otros protocolos como SOAP.

## Índice GINI

Se introduce el concepto del coeficiente de Gini como medida de desigualdad, especialmente en la evaluación de disparidades de ingresos dentro de un país. Se menciona la escala de 0 a 1 en la que opera este coeficiente, así como su adaptación a una escala de hasta 100 para mayor claridad.

## Lenguajes de Programación y Convenciones de Llamadas

Se explora la interacción entre lenguajes de programación de alto y bajo nivel, destacando cómo los lenguajes de bajo nivel actúan como puente entre el hardware y los lenguajes de alto nivel. Se mencionan las convenciones de llamadas a función que rigen esta interacción.

## Propuesta del Trabajo Práctico #2

El Trabajo Práctico #2 tiene como objetivo diseñar e implementar una interfaz que muestre el índice GINI utilizando datos del Banco Mundial. La propuesta incluye la obtención de información a través de una API REST y Python, seguida de la manipulación de datos en un programa en C que convoca rutinas en ensamblador para realizar cálculos específicos. Se plantea una primera iteración utilizando C con Python, sin involucrar ensamblador, siguiendo las convenciones de llamadas de lenguajes de alto nivel a bajo nivel.

### Códigos utilizados

#### Python

```python
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
            if len(country) <= 3:
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
```

#### C

```c
#include <stdio.h>
#include <stdlib.h>

int process_data(float data) {
    return (int) (data+1);
}

int main() {
    return 0;
}
```
