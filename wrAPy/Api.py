from abc import ABCMeta, abstractmethod
import json
import pycurl
try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

class Api(object):
	__metaclass__ = ABCMeta

        def __getattr__(self, name):
            def get(self, path, options, json):
                buffer = BytesIO()
                c = pycurl.Curl()
                c.setopt(c.URL, path)
                c.setopt(c.WRITEDATA, buffer)
                c.perform()
                c.close()
                return json.load(buffer)
            def post(self, path, options, json):

