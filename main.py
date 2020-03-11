from http.client import HTTPSConnection
import json
from models import transform_data


def get_api_data():
    conn = HTTPSConnection('api.tfl.gov.uk')
    conn.request('GET', '/Line/Mode/tube,dlr,tflrail,overground/Status')
    response = conn.getresponse()
    return json.loads(response.read())


def slack_response(attachments):
    return (json.dumps({
        'response_type': 'in_channel',
        'attachments': attachments,
    }), 200, {
        'Content-Type': 'application/json',
    })


def request_handler(request):
    api_data = get_api_data()
    slack_data = transform_data(api_data)
    return slack_response(slack_data)
