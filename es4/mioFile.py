class Person:
	'Classe Persona'
	def __init__(self, firstname = 'Anna', lastname = 'Russo', age = 27):
		self._firstname = firstname
		self._lastname = lastname
		self._age = age
	def __str__(self):
		return f'I\'m {self._firstname} {self._lastname}, I\'m  {self._age}'

class Student(Person):
	'studente'
	def __init__(
		self,
		firstname = 'Biagio',
		lastname = 'Greco',
		age = 14,
		school = 'ITI Renato Elia'
	):
		super().__init__(firstname, lastname, age)
		self.__school = school
	def __str__(self):
		return f'{super().__str__()}. I\'m study at {self.__school}'

anna = Student('Maria', 'Zurolo', 19)
print(anna)