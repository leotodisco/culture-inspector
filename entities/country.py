"""Module for the Country class."""

from entities import metrics

class Country:
    """
    A class to represent a country and its cultural dimensions.
    """
    name : str
    code : str

    dispersion_metrics : metrics.DispersionMetrics

    def __init__(self, country_name: str, country_code:str):
        """
        Constructs all the necessary attributes for the country object.

        Parameters:
        country_name (str): The name of the country.
        country_code (str): The code of the country.
        """
        self.name = country_name
        self.code = country_code

    def add_metrics(self, dispersion_metrics: metrics.DispersionMetrics):
        """
        Adds cultural dimensions to the country object.

        Parameters:
        dispersion_metrics (metrics.DispersionMetrics): A DispersionMetrics object containing the country's cultural dimensions.
        """
        self.dispersion_metrics = dispersion_metrics

    def __str__(self):
        return f'{self.name} ({self.code}) ({self.dispersion_metrics})'