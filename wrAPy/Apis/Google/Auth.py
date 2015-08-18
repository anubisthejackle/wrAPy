from wrAPy import Api
import urllib

class Auth(Api):
    def __getattr__(self, name):
        def wrapper(path, options):
            return Api.call(self, name, 'https://accounts.google.com/o/oauth2' + path, options)
        return wrapper
    # Returns the URL to redirect connect requests to
    def connect(self, params):
        return 'https://accounts.google.com/o/oauth2/auth?' + urllib.urlencode(options)

    def refresh(self, token, client_id, client_secret):
        data = { 
                "refresh_token":token,
                "client_id":client_id,
                "client_secret":client_secret,
                "grant_type":"refresh_token"
               }
        return Api.call(self, 'post', 'https://www.googleapis.com/oauth2/v3/token', urllib.urlencode(data))
