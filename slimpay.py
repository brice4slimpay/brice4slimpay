# coding: utf-8

# Imports needed by the application
import requests
import json
from requests.auth import HTTPBasicAuth
from requests_oauthlib import OAuth2Session
from oauthlib.oauth2 import BackendApplicationClient


class User:
    def __init__(self):
        self.id = 'democreditor01'
        self.secret = 'demosecret01'
        self.creditor = 'democreditor'

user = User()


# Authentication function using a combination between BasicAuthentication & OAuth2
# Get the bearer token, essential for each of those requests
def get_bearer():
    auth = HTTPBasicAuth(user.id, user.secret)
    client = BackendApplicationClient(client_id=user.id)
    oauth = OAuth2Session(client=client)
    token = oauth.fetch_token(token_url='https://api-sandbox.slimpay.net/oauth/token', auth=auth)
    bearer = token['access_token']
    return bearer


# Used each time a GET request is call by the application
def get_header():
    bearer = get_bearer()
    header = {'Authorization': 'Bearer %s' % bearer, 'Accept': 'application/hal+json;',
              'profile': 'https://api.slimpay.net/alps/v1'}
    return header


# Used each time a POST request is call by the application
def post_header():
    bearer = get_bearer()
    header = {'Authorization': 'Bearer %s' % bearer, 'Accept': 'application/hal+json;',
              'profile': 'https://api.slimpay.net/alps/v1', 'Content-Type': 'application/json'}
    return header


# Basic Authentication + Oauth2.0 Authentication
# Used in order to authenticate yourself with the API
def slimpay_authentication():
    client = OAuth2Session(client_id=user.id, token=get_bearer(), redirect_uri='https://api.slimpay.net/alps/v1')
    response = requests.get('https://api-sandbox.slimpay.net/',
                            headers=get_header())
    print("content:"+str(response.text))
    return response.status_code


# GET Request used to get one order, defined by the reference
def get_orders():
    parameters = {'creditorReference': user.creditor, 'reference': '1'}
    orders = requests.get('https://api-sandbox.slimpay.net/orders',
                          headers=get_header(), params=parameters)
    return orders.text


# GET Request used to get one card transaction, defined by the id
def get_card_transactions():
    parameters = {'id': '2a29ede7-2c68-11e5-930b-e7ebba4086f3'}
    response = requests.get('https://api-sandbox.slimpay.net/card-transactions',
                            headers=get_header(), params=parameters)
    return response.text


# GET Request used to get one card alias by id, defined by the id
def get_card_aliases():
    parameters = {'id': 'bb78f52e-5881-11e5-949f-bbda0eef6d56'}
    response = requests.get('https://api-sandbox.slimpay.net/card-aliases',
                            headers=get_header(), params=parameters)
    return response.text


# POST Request used in order to create one order. All the parameters (even the optional) are used for this request
def create_orders():
    data = {
    'creditor': {
        "reference": "democreditor"
    },
    'subscriber': {
        "reference": "subscriber01"
    },
    'items': [
        {
            "type": "signMandate",
            "mandate": {
                "signatory": {
                    "honorificPrefix": "Mr",
                    "familyName": "Doe",
                    "givenName": "John",
                    "telephone": "+33612345678",
                    "email": "change.me@slimpay.com",
                    "billingAddress": {
                        "street1": "27 rue des fleurs",
                        "street2": "Bat 2",
                        "postalCode": "75008",
                        "city": "Paris",
                        "country": "FR"
                    }
                }
            }
        },
        {
            "type": "payment",
            "payin": {
                "scheme": "SEPA.CREDIT_TRANSFER",
                "amount": 10000000,
                "label": "TEST Brice4SlimPay",
                "reference": "Credit transfer by Sofort or iDeal"
            }
        }
    ],
    "started": 'true'
}
    data_json = json.dumps(data)
    response = requests.post('https://api-sandbox.slimpay.net/orders',
                             headers=post_header(), data=data_json)
    return response.text


slimpay_authentication()
