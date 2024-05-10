"""This module computes the standard deviation for each of the Halfstede 6 Dimensions"""

import numpy as np
from service import data_retriever


def compute_standard_deviation(data: list):
    """
    Builds a matrix where each column is one of the 6 Halfstede dimension
    and computes standard deviation for each column

    Parameters:
        data (list): list of dictionaries with keys "nationality" and "number"

    Returns:
        dict[str, Any]: a dictionary containing the standard deviation
                        for each of the Halfstede 6 Dimensions
        dict[str, list[str]]: a dictionary containing the countries with null values
                             for each of the Halfstede 6 Dimensions
    """
    # Creare una matrice vuota
    matrix = []

    # Creare una lista vuota per i paesi con valori nulli
    list_of_null_country = []

    # Creare un dizionario vuoto per i valori nulli
    null_values = {}

    # Per ogni elemento nel file JSON
    for item in data:
    # Ottenere i dati dal file CSV
        country_data = data_retriever.retrieve_country_from_csv(item['nationality'])

        # controlla se ci sono valori nulli per le dimensioni di Hofstede
        if country_data is not None:
            dispersions = country_data.dispersion_metrics

            create_list_of_null_country(list_of_null_country, item, dispersions)
            print(list_of_null_country)

            i = item['number']

            # Il ciclo si itera per un certo numero i di sviluppatori appartenenti a una certa nazionalità
            while i > 0:
                i -= 1
                # Aggiungere i dati alla matrice
                matrix.append([
                    int(dispersions.pdi) if dispersions.pdi is not None else np.nan,
                    int(dispersions.idv) if dispersions.idv is not None else np.nan,
                    int(dispersions.mas) if dispersions.mas is not None else np.nan,
                    int(dispersions.uai) if dispersions.uai is not None else np.nan,
                    int(dispersions.lto) if dispersions.lto is not None else np.nan,
                    int(dispersions.ind) if dispersions.ind is not None else np.nan
                ])

    # Aggiorna il dizionario delle metriche associate
    null_values = create_null_values_dict(list_of_null_country)

    # computa deviazione standard
    std_devs = list(np.nanstd(matrix, axis=0))

    result_dict = {
        "pdi": std_devs[0],
        "idv": std_devs[1],
        "mas": std_devs[2],
        "uai": std_devs[3],
        "lto": std_devs[4],
        "ind": std_devs[5]
    }

    return result_dict, null_values


#---------------Funzioni di supporto-------------------
def create_null_values_dict(list_of_null_country):
    """
    Crea un dizionario con i valori nulli per ogni paese
    """
    null_values = {}
    for country, metric in list_of_null_country:
        if country not in null_values:
            null_values[country] = []
        if metric not in null_values[country]:
            null_values[country].append(metric)

    return null_values

def create_list_of_null_country(list_of_null_country, item, dispersions):
    """
    Aggiunge i paesi con valori nulli a una lista
    """
    if dispersions.pdi is None:
        list_of_null_country.append((item['nationality'], 'pdi'))
    if dispersions.idv is None:
        list_of_null_country.append((item['nationality'], 'idv'))
    if dispersions.mas is None:
        list_of_null_country.append((item['nationality'], 'mas'))
    if dispersions.uai is None:
        list_of_null_country.append((item['nationality'], 'uai'))
    if dispersions.lto is None:
        list_of_null_country.append((item['nationality'], 'lto'))
    if dispersions.ind is None:
        list_of_null_country.append((item['nationality'], 'ind'))
    
    return list_of_null_country
