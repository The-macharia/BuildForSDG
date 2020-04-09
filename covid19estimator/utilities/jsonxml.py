import json
import xmltodict
def json_to_xml(data):
    data = {"root": data}
    return xmltodict.unparse(data, pretty=True)