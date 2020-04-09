import json
from flask import request, jsonify, Response
from covid19estimator.api import api_bp
from covid19estimator.utilities.jsonxml import json_to_xml
from src.estimator import estimator


@api_bp.route("/v1/on-covid-19/", defaults={"output_format": None}, methods=('POST',))
@api_bp.route("/v1/on-covid-19/<string:output_format>", methods=('POST',))
def estimate(output_format):
    output = estimator(request.get_json())
    if output_format and output_format == 'xml':
        return Response(json_to_xml(output), mimetype='application/xml')
    return jsonify(output)
