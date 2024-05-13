import pandas as pd
from entities import country


def retrieve_country_from_csv(country_name: str) -> country:
    """
    Retrieves a country's cultural dimensions from a CSV file.

    Parameters:
    country (str): The name of the country.

    Returns:
    country (country.Country): A Country object containing the country's cultural dimensions.
    """
    data = pd.read_csv("data/data.csv", sep=';')

    country_data = data[data['country'] == country_name]
    country_name = country_data['country'].values[0]
    country_code = country_data['ctr'].values[0]
    country_pdi = country_data['pdi'].values[0]
    country_idv = country_data['idv'].values[0]
    country_mas = country_data['mas'].values[0]
    country_uai = country_data['uai'].values[0]
    country_lto = country_data['lto'].values[0]
    country_ind = country_data['ind'].values[0]
    
    #se qualcuno di questi valori è NaN, il valore sarà None
    if pd.isna(country_pdi):
        country_pdi = None
    if pd.isna(country_idv):
        country_idv = None
    if pd.isna(country_mas):
        country_mas = None
    if pd.isna(country_uai):
        country_uai = None
    if pd.isna(country_lto):
        country_lto = None
    if pd.isna(country_ind):
        country_ind = None


    culture_data = {'name': country_name, 'code': country_code, 'pdi': country_pdi, 'idv': country_idv,
                    'mas': country_mas, 'uai': country_uai, 'lto': country_lto, 'ind': country_ind}
    dispersion_metrics = country.metrics.DispersionMetrics(culture_data)
    country_obj = country.Country(country_name, country_code)

    country_obj.add_metrics(dispersion_metrics)

    return country_obj
