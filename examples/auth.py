from wrAPy.Apis.Google import Auth

api = Auth()

result = api.get('/token', {'foo':'bar'})

print result
