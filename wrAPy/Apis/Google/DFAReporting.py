from wrAPy import Api

class DFAReporting(Api):
    def __getattr__(self, name):
        def wrapper(path, options):
            return Api.call(self, name, 'https://www.googleapis.com/dfareporting/v2.2' + path, options)
        return wrapper
