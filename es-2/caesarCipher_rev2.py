'''
Codifico e decodifico un messaggio secondo il cifrario di cesare
'''

# importo le funzioni per la cifratura e decodidica del messaggio
from encDecMsg import encode, decode
# importo la libreria per prelevare parametri da command line
import sys

# se sono presenti parametri da riga di comando li utilizzo
if len(sys.argv) > 1:
	# .join() unisce gli elementi di un array in una stringa
	# il primo argomento del cmd line è il file stesso
	# il primo argomento non mi serve, quindi lo filtro
	msg = ' '.join(sys.argv[1:])
else:
	# se non ho inserito parametri chiedo il messaggio in input
	msg = input('Insert your message: ').strip()

# stampo dunque sia il messaggio originale
# sia il messaggio codificato
# sia la decodifica del messaggio codificato
print(
f'''
* msg:	{msg}
* enc:	{encode(msg)}
* dec:	{decode(encode(msg))}
'''
)
