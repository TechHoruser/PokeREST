import urllib2
import json

#inicializamos lista de pokemon
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://localhost:5000/Todos', data='')
request.get_method = lambda: 'PUT'
url = opener.open(request)

print "Comenzamos con nuestra lista vacia"
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://localhost:5000/MiListaGen/1', data='')
request.get_method = lambda: 'GET'
url = opener.open(request)
print url.read()

print "Incluimos la primera generacion de pokemon"
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://localhost:5000/MiListaGen/1', data='')
#request = urllib2.Request('http://localhost:5000/MiListaGen/1', data=json.dumps({'gen':[1,2,3]}))
#request.add_header('Content-Type', 'application/json')
request.get_method = lambda: 'POST'
url = opener.open(request)

opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://localhost:5000/MiListaGen/1', data='')
request.get_method = lambda: 'GET'
url = opener.open(request)
print url.read()

print "La volvemos a vaciar"
opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://localhost:5000/MiListaGen/1', data='')
request.get_method = lambda: 'DELETE'
url = opener.open(request)

opener = urllib2.build_opener(urllib2.HTTPHandler)
request = urllib2.Request('http://localhost:5000/MiListaGen/1', data='')
request.get_method = lambda: 'GET'
url = opener.open(request)
print url.read()
