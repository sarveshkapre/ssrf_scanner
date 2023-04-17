import requests
from requests_oauthlib import OAuth1, OAuth2

def handle_authentication(auth_type, credentials):
    """
    Handles authentication for the specified authentication type and credentials.
    """
    if auth_type == 'basic':
        auth = requests.auth.HTTPBasicAuth(credentials['username'], credentials['password'])
    elif auth_type == 'oauth1':
        auth = OAuth1(credentials['client_key'], credentials['client_secret'],
                      credentials['resource_owner_key'], credentials['resource_owner_secret'])
    elif auth_type == 'oauth2':
        auth = OAuth2(credentials['client_id'], credentials['client_secret'],
                      token=credentials['access_token'], token_type='Bearer')
    else:
        auth = None
        
    return auth
