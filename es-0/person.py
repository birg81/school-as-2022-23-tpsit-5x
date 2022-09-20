"""
modulo che contiene la classe persona
"""
class Person:
	''' CLASSE PERSONA '''
	# costruttore della classe
	def __init__(self, firstname, lastname, age = 18):
		self.__firstname = firstname
		self.__lastname = lastname
		self.__age = age

	# metodo toString()
	def __str__(self):
		return f'Sono {self.__firstname} {self.__lastname}, ho {self.__age} anni'

	# getters
	def get_firstname(self):
		return self.__firstname

	def get_lastname(self):
		return self.__lastname

	def get_age(self):
		return self.__age

	# getters
	def set_firstname(self, firstname):
		if len(strip(firstname)) >= 3:
			self.__firstname = strip(firstname)

	def set_lastname(self, lastname):
		if len(strip(lastname)) >= 3:
			self.__lastname = strip(lastname)

	def set_age(self, age):
		if age > 0:
			self.__age = age

'''
il main verrà richiamato solo se questo file verrà lanciato da linea di comando.
nel caso venga lanciato come uno script o un modulo non verrà invocato
'''
# main()
if __name__ == '__main__':
	teacher = Person('Biagio Rosario', 'Greco', 41)
	print(teacher)