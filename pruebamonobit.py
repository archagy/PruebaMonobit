import random,math,time,string,Gnuplot
from math import sqrt,erfc

def keychar(cantidad):   
	key= ''.join(random.choice(string.letters) for i in range(cantidad))    
	return key
	

def keychar_tobit(key):
	return "".join([bin(ord(letra))[2:].zfill(8) for letra in key])
	
	
def monobit(bits):
	ceros=	bits.count("0")
	unos =  bits.count("1")
	frequencia = len(bits)
	SN = ceros-unos
	test = abs(SN)/sqrt(frequencia)
	return erfc(test/sqrt(2))
	

def main():
	cantidad = int(raw_input("Cantidad de numeros a generar:"))
	cantidad_pruebas= int(raw_input("Cuantas veces se repetira la prueba:"))
	f=open("archivo.txt","w+")
	for i in range(cantidad_pruebas):
		binfile=keychar_tobit(keychar(cantidad))
		f.write(str(binfile))
		valor_p =monobit(binfile)
		if (valor_p < 0.01):
			print "Test de frecuencia extiosa ",valor_p
		else:
			print "Test de frecuencia no exitosa ",valor_p
		
	
main()