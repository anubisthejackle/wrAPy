from wrAPy import Api

class Jaundies(Api):
    def __getattr__(self, name):
        return Api.call(self, name, 'http://api.jaundies.com/', {'foo':'bar'})

j = Jaundies()
tlds = j.get

print '\n'.join(tlds)
