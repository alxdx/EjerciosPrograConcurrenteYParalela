class Archivo:
	def __init__(self,nombre):
		try:
			self.f=open(nombre,'r')
			self.nombre=nombre
		except:
			print("no se puede abrir el Archivo",nombre)
			exit()
	def muestra(self):
		i=1
		for linea in self.f:
			print("{}:{}".format(i,linea))
			i+=1
		self.f.seek(0)
	def cuentaVocales(self):
		def vocales(s):
			contador=0
			for i in range(len(s)):
				if s[i] in set('aeiouáéíóúAEIOUÁÉÉÍÓÚ'):
					contador+=1
			return contador
		contador=0
		for linea in self.f:
			contador+=vocales(linea)
		self.f.seek(0)
		return contador
	def cuentaConsonantes(self):
		def consonantes(s):
			contador=0
			for i in range(len(s)):
				if s[i] in set('qwrtypsdfghjklñzxcvbnmQWRTYPSDFGHJKLÑZXCVBNM'):
					contador+=1
			return contador
		contador=0
		for linea in self.f:
			contador+=consonantes(linea)
		self.f.seek(0)
		return contador
	def cuentaSignos(self):
		def signos(s):
			contador=0
			for i in range(len(s)):
				if s[i] in set(',;.:-_{^´¨*[]}¿!¡?'):
					contador+=1
			return contador
		contador=0
		for linea in self.f:
			contador+=signos(linea)
		self.f.seek(0)
		return contador
	def cuentaPalabras(self):
		contador=self.f.read().split()
		self.f.seek(0)
		return len(contador)
	def cuentaLineas(self):
		i=0
		for linea in self.f:
			i+=1
		self.f.seek(0)
		return i;
	def cuentaMayusculas(self):
		def mayusculas(s):
			contador=0
			for i in range(len(s)):
				if s[i] in set('QWERTYUIOPÑLKJHGFDSAZXCVBNM'):
					contador+=1
			return contador
		contador=0
		for linea in self.f:
			contador+=mayusculas(linea)
		self.f.seek(0)
		return contador
	def cuentaMinusculas(self):
		def mayusculas(s):
			contador=0
			for i in range(len(s)):
				if s[i] in set('qwertyuiopñlkjhgfdsazxcvbnm'):
					contador+=1
			return contador
		contador=0
		for linea in self.f:
			contador+=mayusculas(linea)
		self.f.seek(0)
		return contador
	def copia(self):
		nombreSinExtension=self.nombre.split(sep=".")
		nuevacopia=open(nombreSinExtension[0]+"COPIA.txt","w+")
		for linea in self.f:
			nuevacopia.write(linea)
		self.f.seek(0)
		nuevacopia.close()
	def copiaMayusculas(self):
		nombreSinExtension=self.nombre.split(sep=".")
		nuevacopia=open(nombreSinExtension[0]+"Mayusculas.txt","w+")
		for linea in self.f:
			nuevacopia.write(linea.upper())
		self.f.seek(0)
		nuevacopia.close()
	def copiaMinusculas(self):
		nombreSinExtension=self.nombre.split(sep=".")
		nuevacopia=open(nombreSinExtension[0]+"Minusculas.txt","w+")
		for linea in self.f:
			nuevacopia.write(linea.lower())
		self.f.seek(0)
		nuevacopia.close()
	def muestraHex(self):
		i=1
		for linea in self.f:
			print("{}:{}".format(i,linea.encode('utf-8').hex()))
			i+=1
		self.f.seek(0)