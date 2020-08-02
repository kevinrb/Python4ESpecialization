import urllib.request, urllib.parse, urllib.error
import oauth
import hidden

def augment(url,parameters):
    secrets = hidden.oauth()
    consumer = oauth.oauth.OAuthConsumer(secrets['consumer_key'],secrets['consumer_secret'])
    token = oauth.oauth.OAuthToken(secrets['token_key'], secrets['token_secret'])
    oauth_request = oauth.oauth.OAuthRequest.from_consumer_and_token(consumer, token=token, http_method='GET', http_url=url, parameters=parameters)
    oauth_request.sign_request(oauth.oauth.OAuthSignatureMethod_HMAC_SHA1(),consumer, token)
    return oauth_request.to_url()