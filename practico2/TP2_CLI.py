import requests
from ctypes import CDLL, c_float, c_int
import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn-v0_8-dark')

# Cargamos la libreria
# lib = CDLL('./TP2_mac_arm.so') # para ejecutar en arm64
lib = CDLL('./TP2.so') # para linux
# lib = CDLL("./TP2_windows.so")  # para windows

lib.process_data.argtypes = [c_float]
lib.process_data.restype = c_int


def get_data_from_url(url):
    response = requests.get(url)
    data = response.json()
    return data[1]


def process_values(values):
    processed_values = []
    for i in range(len(values)):
        aux_value = lib.process_data(values[i])
        processed_values.append(aux_value)
    return processed_values


def plot_data(years, values, processed_values, country):
    df = pd.DataFrame(
        {"year": years, "values": values, "processed_values": processed_values}
    )
    fig, ax = plt.subplots()
    ax.plot(df["year"], df["values"], label="Gini Index")
    ax.plot(df["year"], df["processed_values"], label="Processed Gini Index")
    ax.set_xlabel("Year")
    ax.set_ylabel("Gini Index")
    ax.set_title(f"Gini Index for {country}")
    ax.legend()
    plt.savefig(f"Gini_Index_{country}.png")
    return (years, values, processed_values), fig, ax


def get_gini_index(country):
    try:
        url = f"https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
        data = get_data_from_url(url)
        years = [item["date"] for item in data if item["value"] is not None]
        years.reverse()
        values = [item["value"] for item in data if item["value"] is not None]
        values.reverse()
        processed_values = process_values(values)
        plot_data(years, values, processed_values, country)
    except:
        raise Exception('El pais no existe o no se pudo obtener el Gini Index, intente nuevamente')


def print_countries():
    url = "https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22"
    data = get_data_from_url(url)
    country_list = []
    if isinstance(data, list) and isinstance(data[0], dict):
        for item in data:
            if (
                "country" in item
                and "value" in item["country"]
                and "countryiso3code" in item
            ):
                country_and_code = (
                    f"{item['country']['value']}, {item['countryiso3code']}"
                )
                if country_and_code not in country_list:
                    country_list.append(country_and_code)
    else:
        print("Data is not in the expected format")
    # Imprimimos los paises y sus codigos iso3
    for i in range(len(country_list)):
        print(country_list[i])


if __name__ == "__main__":
    print("Se listan los paises y sus codigos iso3:")
    print_countries()
    print("Ingrese el codigo iso3 del pais que desea consultar ('-' para terminar):")
    while True:
        country = str(input())
        if country != "-":
            try:
                if len(country) <= 3 and len(country) > 1:
                    get_gini_index(country)
                else:
                    print("Codigo iso3 invalido")
            except:
                print('El pais no existe o no se pudo obtener el Gini Index, intente nuevamente')
        else:
            break
    print("Fin del programa")
