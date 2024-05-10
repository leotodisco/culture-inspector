import numpy as np
import json
from service import data_retriever
import json
from service import data_retriever

def standard_deviation(json_data):
    data = json.loads(json_data)
    # Creare una matrice vuota
    matrix = []

    # Per ogni elemento nel file JSON
    for item in data:
        # Ottenere i dati dal file CSV
        country_data = data_retriever.retrieve_country_from_csv(item['nationality'])
        print(country_data.dispersion_metrics.pdi,"cioa")
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

    std_devs = np.std(matrix, axis=0)

    print(std_devs)
    return std_devs

