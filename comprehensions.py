import random
countries = ["COLOMBIA", "ARGENTINA", "BOLIVIA","BRASIL"]
dictprueba = { x:random.randint(1,100) for x in countries}
print(dictprueba)

nombres = ["cam","may","san", "hen"]
edades = [14,15,50,28]
match = {x:y for (x,y) in zip(nombres,edades)}
print(match)

prueba = {x:y if y>20 else "no_cumple" for (x,y) in dictprueba.items()} 
print(prueba)

