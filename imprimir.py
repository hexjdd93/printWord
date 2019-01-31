import time
from letters import *


maximo = []

palabra = input()

palabra = palabra.upper()

print(palabra)



for letra in palabra:
	if letra not in dicLetras:
		maximo.append(diccionario[len(diccionario)-1])
		continue
	for x in range(0, len(dicLetras)):
		if letra == dicLetras[x]:
			maximo.append(diccionario[x])
			
if len(maximo) == 0:
	exit()


for otro in range(0,8):
	imp = ""
	for ii in range(0, len(maximo)):
		
		for x in range(0,10):
			# print(maximo[ii][otro])
			# print(otro)
			if maximo[ii][otro][x] == 1:
				imp += "8"
			else:
				imp += " "
			if x == 9:
				imp +="  "
	print(imp)
	time.sleep(0.1)
