"""Moduel for metrics of country data"""

class DispersionMetrics:
    """
    A class to represent a country's cultural dimensions.
    """
    pdi: int
    idv : int
    mas : int
    uai : int
    lto: int
    ind: int

    def __init__(self, culture_data: dict):
        """
        Constructs all the necessary attributes for the country object.

        Parameters:
        culture_data (dict): A dictionary containing the country's name, code, and cultural dimensions.
                            dict keys: 'name (str)', 'code (str)', 'pdi (int)', 'idv (int)', 'mas (int)', 'uai (int)', 'lto (int)', 'ind (int)'
        """
        self.pdi = culture_data['pdi']
        self.idv = culture_data['idv']
        self.mas = culture_data['mas']
        self.uai = culture_data['uai']
        self.lto = culture_data['lto']
        self.ind = culture_data['ind']
    
    def __str__(self):
        return f'PDI: {self.pdi}, IDV: {self.idv}, MAS: {self.mas}, UAI: {self.uai}, LTO: {self.lto}, IND: {self.ind}'