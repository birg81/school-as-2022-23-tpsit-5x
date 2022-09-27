"""
importa dal file person.py tutto
tale file contiene solo la classe persona
"""
from person import *

# creo una lista di persone - ogni fireimento a persone è puramente causale
people = [
	Person('Antonio', 'Zito', 17),
	Person('Barbara', 'Vuolo', 18),
	Person('Carlo', 'Tramparulo', 16),
	Person('Daniela', 'Simeone', 19),
	Person('Enrico', 'Ruggiero', 21),
	Person('Francesca', 'Uliano', 15),
	Person('Gianni', 'Nappi', 20)
]

# stampo tutte le persone attraverso un ciclo for
for p in people:
	print(p)

'''
attraverso la list comprehension creo un arrai di interi i cui valori
rappresentano le età dei minorenni contenuti nella lista
'''
under_ages = [p.get_age() for p in people if p.get_age() < 18]

# se ci sono dei minoerenni stampa un messaggio
if len(under_ages) > 0:
	print(f'''in questo elenco, ci sono {len(under_ages)} minorenni,
che hanno rispettivamente {under_ages} anni
''')