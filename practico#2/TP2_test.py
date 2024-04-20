# test_TP2.py
import unittest
from unittest.mock import patch, MagicMock
from TP2_CLI import *
import matplotlib
matplotlib.use('Agg')


'''
Pruebas del sistema:
Individualmente se prueban las funciones del codigo TP2_CLI.py
- Se prueba la función get_data_from_url con un mock de requests.get para verificar que se obtengan los datos esperados.
- Se prueba la función process_values con un conjunto de valores para verificar que se procesen correctamente.
- Se prueba la función plot_data con un conjunto de años, valores y valores procesados para verificar que se grafiquen correctamente.
'''
class TestSystem(unittest.TestCase):
    @patch("requests.get")
    def test_get_data_from_url(self, mock_get):
        data = [
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2020",
                "value": 42.7,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2019",
                "value": 43.3,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2018",
                "value": 41.7,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2017",
                "value": 41.4,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2016",
                "value": 42.3,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2015",
                "value": None,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2014",
                "value": 41.8,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2013",
                "value": 41.1,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2012",
                "value": 41.4,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2011",
                "value": 42.7,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
        ]
        expected_value = {
            entry["date"]: {
                "indicator": entry["indicator"],
                "country": entry["country"],
                "countryiso3code": entry["countryiso3code"],
                "value": entry["value"],
                "unit": entry["unit"],
                "obs_status": entry["obs_status"],
                "decimal": entry["decimal"],
            }
            for entry in data
        }
        mock_get.return_value.json.return_value = [None, expected_value]
        result = get_data_from_url(
            "https://api.worldbank.org/v2/en/country/ARG/indicator/SI.POV.GINI?format=json&date=2011:2020&per_page=32500&page=1"
        )
        self.assertEqual(result, expected_value)

    def test_process_values(self):
        test_values = [123.2, 22.6, 5.8]
        expected_result = [124, 23, 6]
        result = process_values(test_values)
        self.assertEqual(result, expected_result)

    def test_plot_data(self):
        test_years = [
            "2011",
            "2012",
            "2013",
            "2014",
            "2016",
            "2017",
            "2018",
            "2019",
            "2020",
        ]
        test_values = [42.7, 41.4, 41.1, 41.8, 42.3, 41.4, 41.7, 43.3, 42.7]
        test_processed_values = [43, 42, 42, 42, 43, 42, 42, 44, 43]
        test_country = "ARG"
        expected_result = (test_years, test_values, test_processed_values)
        result, fig, ax = plot_data(
            test_years, test_values, test_processed_values, test_country
        )
        self.assertEqual(result, expected_result)
        self.assertEqual(ax.get_title(), f"Gini Index for {test_country}")
        self.assertEqual(ax.get_xlabel(), "Year")
        self.assertEqual(ax.get_ylabel(), "Gini Index")
        lines = ax.get_lines()
        self.assertEqual(lines[0].get_ydata().tolist(), test_values)
        self.assertEqual(lines[1].get_ydata().tolist(), test_processed_values)


'''Pruebas de integracion:
Se busca probar que el sistema funcione correctamente en su totalidad, es decir, que las funciones se comuniquen correctamente entre si y que el sistema en forma global funcione correctamente.
- Se prueba la función get_gini_index con un mock de requests.get para verificar que se obtengan los datos esperados y que se procesen correctamente.
- Se prueba la función print_countries con un mock de get_data_from_url para verificar que se obtengan los datos esperados.
- Se prueba la función get_gini_index con un mock de get_data_from_url para verificar que se obtengan los datos esperados y que se procesen correctamente.
'''
class TestIntegration(unittest.TestCase):
    @patch("TP2_CLI.requests.get")
    @patch("TP2_CLI.lib.process_data")
    @patch("TP2_CLI.plt.subplots")
    @patch('matplotlib.pyplot.subplots')
    def test_get_gini_index(self, mock_matplotlib_subplots, mock_subplots, mock_process_data, mock_get):
        mock_fig = MagicMock()
        mock_ax = MagicMock()
        mock_subplots.return_value = (mock_fig, mock_ax)
        data = [
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2020",
                "value": 42.7,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2019",
                "value": 43.3,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2018",
                "value": 41.7,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2017",
                "value": 41.4,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2016",
                "value": 42.3,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2015",
                "value": None,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2014",
                "value": 41.8,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2013",
                "value": 41.1,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2012",
                "value": 41.4,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
            {
                "indicator": {"id": "SI.POV.GINI", "value": "Gini index"},
                "country": {"id": "AR", "value": "Argentina"},
                "countryiso3code": "ARG",
                "date": "2011",
                "value": 42.7,
                "unit": "",
                "obs_status": "",
                "decimal": 1,
            },
        ]
        expected_data = [{"date": entry["date"], "value": entry["value"]} for entry in data]
        mock_response = MagicMock()
        mock_response.json.return_value = [None, expected_data]
        mock_get.return_value = mock_response
        mock_process_data.return_value = [43, 42, 42, 42, 43, 42, 42, 44, 43]
        get_gini_index("AR")
        mock_get.assert_called_once()
        mock_process_data.assert_called()
        mock_subplots.assert_called_once()


'''Pruebas de validacion de Usuario:
Se pretende probar como el usuario ingresa un codigo iso3 valido y uno invalido.
- Se prueba la función get_gini_index con un codigo iso3 invalido para verificar que se obtenga una excepcion.
- Se prueba la función get_gini_index con un codigo iso3 valido para verificar que no se obtenga una excepcion.
'''
class TestUserValidation(unittest.TestCase):
    @patch("TP2_CLI.get_data_from_url")
    def test_get_gini_index(self, mock_get_data_from_url):
        def side_effect(url):
            if "invalid_country_code" in url:
                raise Exception("API error")
            else:
                return [{"date": "2020", "value": 42.0}]
        mock_get_data_from_url.side_effect = side_effect
        with self.assertRaises(Exception) as context:
            get_gini_index("invalid_country_code")
        self.assertTrue('El pais no existe o no se pudo obtener el Gini Index, intente nuevamente' in str(context.exception))

        try:
            get_gini_index("ARG")
        except Exception:
            self.fail("get_gini_index() raised Exception unexpectedly!")

if __name__ == "__main__":
    unittest.main()
