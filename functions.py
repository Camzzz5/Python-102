def myfunction():
    #print("xd")
    return "esto se devuelve?"

myfunction()

print(myfunction())

suma = lambda a, b : a + b

print(suma(4,5))

def function_1(x):
    return x+1

def function_2(x,ejemplo):
    return x+ejemplo(x)

result = function_2(2,function_1)
print(result)

ejemplo1 = lambda x:x+ 1
ejemplo2 = lambda x , ej: x + ej(x)
result = ejemplo2(2, ejemplo1)
print(result)
