import urllib
import re
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

def quitarsaltosdelinea(cadena):
    reemplazar_por = ""
    buscar = "\n"
    cadena = cadena.replace(buscar, reemplazar_por)
 
    return(cadena)

def listado_pokemon():
    # Web donde aparece los pokemons
    response = urllib.urlopen("http://pokemondb.net/pokedex/national")
    response.code
    html = response.read().decode("utf8")
    
    # Expresion que discrima la generacion, numero y nombre de los pokemons
    expresion = 'class="pkg.*?pkgG(.*?) .*?<small>#(.*?)<.*?class="ent-name".*?>(.*?)<'

    listadoPokemon = re.findall(expresion,html)
	
    if not listadoPokemon:
        print "No ha encontrado ningun pokemon"
    else:
        return(listadoPokemon)

app = Flask(__name__)
api = Api(app)

TODOS = []
MILISTA = []

parser = reqparse.RequestParser()
parser.add_argument('gen', type=int, choices=range(1,6), help='gen debe ser un entero comprendido entre 1 y 6')
parser.add_argument('num', type=int, help='num debe ser un entero')

class Lista(Resource):
	def get(self):
		return TODOS
		
	def put(self):
		global TODOS
		TODOS = listado_pokemon()
		
class MiListaGen(Resource):
	def get(self, gen):
		args = parser.parse_args()
		laux = []
		for e in MILISTA:
			if e[0]==gen:
				laux.append(e)
		return laux
		
	def post(self, gen):
		args = parser.parse_args()
		for e in TODOS:
			if e[0]==gen:
				MILISTA.append(e)
		
	def delete(self, gen):
		args = parser.parse_args()
		laux = []
		for e in MILISTA:
			if e[0]!=gen:
				laux.append(e)
		MILISTA = laux
		
class MiListaNum(Resource):
	def get(self, num):
		args = parser.parse_args()
		laux = []
		for e in MILISTA:
			if e[1]==num:
				laux.append(e)
		return laux
		
	def post(self, num):
		args = parser.parse_args()
		for e in TODOS:
			if e[1]==num:
				MILISTA.append(e)
		
	def delete(self, num):
		args = parser.parse_args()
		laux = []
		for e in MILISTA:
			if e[1]!=num:
				laux.append(e)
		MILISTA = laux
		
class MiLista(Resource):
	def get(self):
		return MILISTA
		
api.add_resource(Lista, '/Todos')

api.add_resource(MiListaGen, '/MiListaGen/<gen>')

api.add_resource(MiListaNum, '/MiListaNum/<num>')

api.add_resource(MiLista, '/MiLista')

#print listado_pokemon(3)

if __name__ == '__main__':
    app.run(debug=True)
