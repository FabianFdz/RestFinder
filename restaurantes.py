from pyswip import *

p=Prolog()
p.consult("rest.pl") #El consult lo que hace es carga el archivo .pl con todas las reglas
def imprimirRest():
	p.consult("rest.pl")
	for i in p.query("restaurante(A,_,_,_,_)"): #hago una consulta e imprimo todos los que cumplen la consulta
		print i["A"]

def imprimirPlato():
	p.consult("rest.pl")
	for plato in p.query("platillo(_,A,_,_,_)"):
		print plato["A"]

def agregarRest(nombre,tipoComida,ubicacion,telefono,horario): #Agrega un nuevo saludo al archivo saludos.pl, carga el archivo, pero no se carga en la base de conocimientos
	arch = file("rest.pl","a")
	functor="\nrestaurante("
	functor=functor+nombre+","+tipoComida+","+ubicacion+","+telefono+","+horario+")."
	arch.write(functor)

def agregarPlatillo(rest,nombrePlat,sabor,PaisOrg,Ingredientes): #sabor puede ser picante, salado, dulce, agridulce, amargo
	arch = file("rest.pl","a")
	functor="\nplatillo("
	functor=functor+rest+","+nombrePlat+","+sabor+","+PaisOrg+","+Ingredientes+")." #Ingredientes por ahora lo agrego como si fuera una lista de python, creo que en prolog el manejo es algo similar
	arch.write(functor)