'''
Creare una funzione che
- in ingresso prende come argomento una stringa
- in uscita fornisca un dizionario
	- che ha per chiavi le lettere contenute nella stringa di ingresso
	- per valori i numeri di occorrenza di tali lettere
------------------------------------------------------------------
PREREQUISITI TEORICI:
- Stringhe, indexing, funzioni built-in sulle stringhe
- Dizionari
- Definizione di una funzione
- Iterazioni
- Strutture decisionali
------------------------------------------------------------------
ESEMIO
INPUT:
	"CIAO ANNA"
OUTPUT:
	{'C': 1, 'I': 1, 'A': 3, 'O': 1, 'N':2}
'''

# funzione che effettua il conteggio
def lettersCounter(word = ''):
	# dizionario che contiene le lettere e le loro occorrenze
	counting = {}
	# questa funzione sostituisce i caratteri. Usata per eliminare gli spazi
	word = word.replace(" ", "")
'''
si scorre la stringa lettera per lettera, memorizzandole in l
se l è già presente nel dizionario, il valore viene incrementato
altrimenti si crea una nuova chiave con valore 1
'''
	for l in word:
		if l in counting:
			counting[l] += 1
		else:
			counting[l] = 1
	return counting

print(lettersCounter('Forza Napoli'))
