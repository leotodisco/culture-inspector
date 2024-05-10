import json

from service import data_retriever
from service.standard_deviation import standard_deviation

json_data =json.dumps( [
    {"number": 2, "nationality": "Italy"},
    {"number": 5, "nationality": "France"},
    {"number": 3, "nationality": "Germany"},
    {"number": 4, "nationality": "Spain"}
])
standard_deviation(
    json_data
)