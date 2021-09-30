import string
import pickle

minusculas = string.ascii_lowercase   # O si prefieres pones "abcde...z" que es lo mismo

def letra_a_codigo(letra):
       #if letra in minusculas:
    return minusculas.index(letra) + 97

def getNode(key): 
	keyVerification = letra_a_codigo(key[0])
	if (keyVerification >= 97 and keyVerification <= 102):
    		return "localhost", 1000
	elif (keyVerification >= 103 and keyVerification <= 108):
    		return "localhost", 2000
	elif (keyVerification >= 109 and keyVerification <= 115):
    		return "localhost", 3000
	elif (keyVerification >= 116 and keyVerification <= 122):
		return "localhost", 4000
	else:
    		return "Valor incorrecto ingresado"


#Here's an example dict
grades = { 'Alice': 89, 'Bob': 72, 'Charles': 87 }

#Use dumps to convert the object to a serialized string
serial_grades = pickle.dumps( grades )

#Use loads to de-serialize an object
received_grades = pickle.loads( serial_grades )

host, port = getNode("amarillo")
print(host, port)
print(serial_grades)