from Archivo import Archivo
class Main:
	def main():
		nomb=input("Nombre del Archivo:")
		archivo=Archivo(nomb)
		archivo.muestra()
		print("Vocales: {}".format(archivo.cuentaVocales()))
		print("Consonantes: {}".format(archivo.cuentaConsonantes()))
		print("Signos:{}".format(archivo.cuentaSignos()))
		print("Palabras:{}".format(archivo.cuentaPalabras()))
		print("Lineas:{}".format(archivo.cuentaLineas()))
		print("Mayusculas:{}".format(archivo.cuentaMayusculas()))
		print("Minusculas:{}".format(archivo.cuentaMinusculas()))
		archivo.copia()
		archivo.copiaMayusculas()
		archivo.copiaMinusculas()
		archivo.muestraHex()


	
	if __name__ == '__main__':
		main()