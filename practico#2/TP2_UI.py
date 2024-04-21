import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QListWidget, QVBoxLayout, QPushButton, QWidget, QLabel, QVBoxLayout, QSizePolicy, QGridLayout
from PyQt5.QtCore import Qt
import requests
import json
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from ctypes import CDLL, c_float, c_int
import zipfile
import os
from PyQt5.QtWidgets import QListWidgetItem
import time
import pandas as pd

# Se crea una ventana principal
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GINI Index Calculator")
        self.setGeometry(100, 100, 800, 600)

        self.list_widget = QListWidget()
        self.start_button = QPushButton("Get GINI Index")
        self.save_button = QPushButton("Save Images")
        self.info_label = QLabel("Select countries to calculate GINI index and click 'Get GINI Index' to generate plots.")
        self.plot_canvas = PlotCanvas(self, width=5, height=4)

        # Se crea un layout de cuadrícula
        layout = QGridLayout()
        layout.addWidget(self.info_label, 0, 0, 1, 2)  # fila, columna, rowspan, columnspan
        layout.addWidget(self.list_widget, 1, 0)
        layout.addWidget(self.start_button, 2, 0)
        layout.addWidget(self.save_button, 3, 0)
        layout.addWidget(self.plot_canvas, 1, 1, 3, 1)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.start_button.clicked.connect(self.start)
        self.save_button.clicked.connect(self.save_images)

        self.load_countries()

    # Se obtienen los índices y los respectivos años de un país
    def get_gini_index(self, country):
        url = f"https://api.worldbank.org/v2/en/country/{country}/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
        response = requests.get(url)
        data = response.json()
        return data[1]

    # Se cargan los países en la lista para mostrar en forma de checkbox
    def load_countries(self):
        url = 'https://api.worldbank.org/v2/en/country/all/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1&country=%22Argentina%22'
        response = requests.get(url)
        data = response.json()
        country_list = []
        if isinstance(data, list) and isinstance(data[0], dict):
            for item in data[1]:
                if 'country' in item and 'value' in item['country'] and 'countryiso3code' in item:
                    country_and_code = f"{item['country']['value']}, {item['countryiso3code']}"
                    if country_and_code not in country_list:
                        country_list.append(country_and_code)
                        item = QListWidgetItem(country_and_code)
                        item.setFlags(item.flags() | Qt.ItemIsUserCheckable)
                        item.setCheckState(Qt.Unchecked)
                        self.list_widget.addItem(item)

    # Se inicia el proceso de obtención de los índices y se grafican
    def start(self):
        lib = CDLL('./TP2_mac_arm.so')
        lib.process_data.argtypes = [c_float]
        lib.process_data.restype = c_int
        for index in range(self.list_widget.count()):
            item = self.list_widget.item(index)
            if item.checkState() == Qt.Checked:
                country = item.text().split(", ")[1]
                json_data = self.get_gini_index(country)
                values = [json_data[i]['value'] for i in range(len(json_data)) if json_data[i]['value'] is not None]
                years = [json_data[i]['date'] for i in range(len(json_data)) if json_data[i]['value'] is not None]
                processed_values = []
                for i in range(len(values)):
                    aux_value = lib.process_data(values[i])
                    processed_values.append(aux_value)
                df = pd.DataFrame({'year': years, 'values': values, 'processed_values': processed_values})
                self.plot_canvas.plot(df['year'], df['values'], df['processed_values'], country)

    # Se guardan las imágenes en un archivo zip
    def save_images(self):
        with zipfile.ZipFile('Gini_Index_Images.zip', 'w') as zipf:
            for file in os.listdir():
                if file.endswith('.png'):
                    zipf.write(file)
                    time.sleep(0.1)
                    os.remove(file)


# Clase para el lienzo del plot
class PlotCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig, self.ax = plt.subplots(figsize=(width, height), dpi=dpi)
        super().__init__(fig)
        self.setParent(parent)
    def plot(self, years, values, processed_values, country):
        self.ax.clear()
        self.ax.plot(years, values, label='Gini Index')
        self.ax.plot(years, processed_values, label='Processed Gini Index')
        self.ax.set_xlabel('Year')
        self.ax.set_ylabel('Gini Index')
        self.ax.set_title(f'Gini Index for {country}')
        self.ax.legend()
        self.draw()

# Función principal
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
