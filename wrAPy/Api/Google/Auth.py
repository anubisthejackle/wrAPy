from wrAPy import Api

class Auth(Api):
    def __getattr__(self, name, path, options):
        return Api.call(self, name, 'https://accounts.google.com/o/oauth2' + path, options)
