from wrAPy.Apis.Google import Auth

print Auth().get('/token', {'foo':'bar'})

