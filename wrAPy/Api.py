from abc import ABCMeta, abstractmethod
import json
import pycurl

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

class Api(object):
	__metaclass__ = ABCMeta

        def call(self, name, path, options=None):
            def get(self, path, options=None):
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, path)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                c.close()
                try:
                    result = json.load(buffer)
                except ValueError:
                    try:
                        result = json.loads(buffer.getvalue())
                    except ValueError:
                        result = None
                return result
        
            def post(self, path, options=None):
                return False;

            if name == "get":
                return get(self, path, options)
