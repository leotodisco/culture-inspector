from typing import Any

import numpy as np
from service import data_retriever


def compute_standard_deviation(data: list) -> dict[str, Any]:
    """
    Builds a matrix where each column is one of the 6 Halfstede dimension and computes standard deviation for each column

    Parameters:
        data (list): list of dictionaries with keys "nationality" and "number"

    Returns:
        dict[str, Any]: a dictionary containing the standard deviation for each of the Halfstede 6 Dimensions
    """
    # Creare una matrice vuota
    matrix = []

    # Per ogni elemento nel file JSON
    for item in data:
        # Ottenere i dati dal file CSV
        country_data = data_retriever.retrieve_country_from_csv(item['nationality'])

        i = item['number']
        if country_data is not None:
            # Aggiungere i dati alla matrice
            for i in range(i):
                matrix.append([
                    int(country_data.dispersion_metrics.pdi),
                    int(country_data.dispersion_metrics.idv),
                    int(country_data.dispersion_metrics.mas),
                    int(country_data.dispersion_metrics.uai),
                    int(country_data.dispersion_metrics.lto),
                    int(country_data.dispersion_metrics.ind)
                ])

    # computa deviazione standard
    std_devs = list(np.std(matrix, axis=0))

    result_dict = {
        "pdi": std_devs[0],
        "idv": std_devs[1],
        "mas": std_devs[2],
        "uai": std_devs[3],
        "lto": std_devs[4],
        "ind": std_devs[5]
    }

    return result_dict
