'''
Creare una funzione che:
- in ingresso prende una stringa
- in uscita fornisca un dizionario che ha
	- per chiavi le diverse lettere della stringa
	- per valori il conteggio delle diverse occorrenze delle lettere
Esempio
INPUT:
	"CIAO ANNA"
OUTPUT:
	{'C': 1, 'I': 1, 'A': 3, 'O': 1, ' ': 1, 'N':2}
'''

# funzione che effettua il conteggio
def lettersCounter(world = ''):
	#dizionario che contiene le lettere e le loro occorrenze
	counting = {}
'''
si scorre la stringa lettera per lettera, memorizzandole in l
se l è già presente nel dizionario, il valore viene incrementato
altrimenti si crea una nuova chiave con valore 1
'''
	for l in world:
		if l in counting:
			counting[l] += 1
		else:
			counting[l] = 1
	return counting

print(lettersCounter('Forza Napoli'))
