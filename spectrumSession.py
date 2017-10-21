from requests_oauthlib import OAuth1Session

client_key = 'l7xx66025f7d4f4646b0b1cdf24a846ce1a8'
client_secret = 'cbb3e04b32b74691b738181fdc9444e6'
request_token_url = 'https://api.spectrum.net/auth/oauth/request'
base_authorization_url = 'https://api.spectrum.net/auth/oauth/device/authorize'
access_token_url = 'https://api.spectrum.net/auth/oauth/token'


def get_session(username, password):
	## Get Token for Auth
    oauth = OAuth1Session(client_key, client_secret=client_secret)
    token_response = oauth.fetch_request_token(request_token_url)
    resource_owner_key = token_response.get('oauth_token')
    resource_owner_secret = token_response.get('oauth_token_secret')

    ## Authorize Credentials
    authorization_url = oauth.authorization_url(base_authorization_url, username=username, password=password)
    r = oauth.get(url=authorization_url)
    auth_response = oauth.parse_authorization_response(authorization_url + "&" + r.text)
    token_verifier = auth_response.get('oauth_verifier')

    ## Get Access Token
    oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret,
                          verifier=token_verifier)

    oauth_tokens = oauth.fetch_access_token(access_token_url)
    resource_owner_key = oauth_tokens.get('oauth_token')
    resource_owner_secret = oauth_tokens.get('oauth_token_secret')

    ## Generate OAuth Object with Access Token
    oauth = OAuth1Session(client_key,
                   client_secret=client_secret,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=token_verifier)

    return oauth