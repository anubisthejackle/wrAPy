from abc import ABCMeta, abstractmethod
import json
import pycurl
import urllib

try:
    from io import BytesIO
except ImportError:
    from StringIO import StringIO as BytesIO

class Api(object):
	__metaclass__ = ABCMeta

        def __init__(self):
            self.customHeaders = []

        def call(self, name, path, options=None):
            buffer = BytesIO()
            c = pycurl.Curl()

            def get(path, options):
                if options is None:
                    return path
                return path + '?' + urllib.urlencode(options)

            def post(options):
                c.setopt(c.POST,True)
                if options is None:
                    return
                setOptions(options)

            def deletePut(name,options):
                c.setopt(c.CUSTOMREQUEST, name.upper())
                if options is None:
                    return
                setOptions(options)

            def setOptions(options):
                c.setopt(c.POSTFIELDS, options)

            if name.lower() == "get":
                path = get(path, options)
        
            elif name.lower() == "post":
                post(options)

            elif name.lower() == "put" or name.lower() == "delete":
                deletePut(name, options)

            c.setopt(c.URL, path)
            c.setopt(c.WRITEDATA, buffer)

            for i in range(len(self.customHeaders)):
                c.setopt(c.HTTPHEADER,self.customHeaders[i])

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
