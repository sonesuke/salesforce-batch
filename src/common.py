import json
import os
import requests
import pandas as pd
from simple_salesforce import Salesforce


def login():
    client_id     = os.environ['SF_CLIENT_ID'] # Consumer Key
    client_secret = os.environ['SF_CLIENT_SECRET'] # Consumer Secret
    username      = os.environ['SF_USERNAME'] # login id
    password      = os.environ['SF_PASSWORD'] # password
    security_token = os.environ['SF_SECURITY_TOKEN'] # security token
    sandbox       = False
    access_token_url = 'https://login.salesforce.com/services/oauth2/token'

    data = {
             'grant_type': 'password',
             'client_id' : client_id,
             'client_secret' : client_secret,
             'username'  : username,
             'password'  : password + security_token
           }

    headers = { 'content-type': 'application/x-www-form-urlencoded' }
    response = requests.post(access_token_url,data=data,headers=headers)
    response = response.json()
    if response.get('error'):
        print(response)
        raise Exception(response.get('error_description'))

    session = requests.Session()
    return Salesforce(instance_url = response['instance_url'],
                    session_id=response['access_token'],
                    sandbox=False,
                    session=session)


def sf_to_df(sf):
    records = sf['records']
    if len(records) == 0:
        return
    [r.pop('attributes') for r in records]
    return pd.read_json(json.dumps(records), orient='records')


def df_to_sf(df):
    data = df.to_dict(orient='records')
    return data

