"""
This module contains the route which implements the web service to compute the standard deviation of the Halstfede Dimensions.
"""
from flask import Flask, jsonify, request, make_response

from entities.metrics import GeographicalDispersion
from service.standard_deviation import compute_standard_deviation
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

app = Flask(__name__)


@app.route('/compute_std_dev', methods=['POST'])
@cross_origin()
def compute_standard_deviation_route():
    """
    Web Service to compute the standard deviation of all of the six Halstfede Dimensions.

    Parameters:
        request: The request must contain a list of JSON objects describing the community of developers.
        The request should have the following shape:
            [
                {"number": 3, "nationality": "Germany"},
                {"number": 4, "nationality": "Spain"}
                {"geographical_dispersion": 0.5}
            ]
        So number is the number of developers of a certain Nationality

    Returns:
        dictx: a dictionary containing the standard deviation of each of the 6 Halstfede Dimensions
    """
    try:
        data = request.get_json()
        print(data)
    except Exception as e:
        return make_response(jsonify({'error': 'Invalid input'}), 400)

    result, country_null_metrics = compute_standard_deviation(data)

    result['null_values'] = country_null_metrics

    for item in data:
        if 'nationality' not in item:
            geodisp = item['geographical_dispersion']
            result['geographical_dispersion'] = GeographicalDispersion(geodisp).toDict()
            break


    return jsonify(result), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
