def cesare(word = '', key = 3):
	# numero di simboli da codificare (26: lettere dell'alfabeto)
	M = ord('Z') - ord('A') + 1
	# per traslazioni di lunghezza maggiore di M le riporta nel range 0, M-1
	key = key % M
	# parola criptata
	word_enc = word.strip().upper()
	# se key % M = 0 ovvero se key = 0, 26, 52 ecc non fa nulla
	if key > 0:
		word_enc = ''
		for l in word.strip().upper():
			# controlla se l è compresa nel mio alfabeto
			if ord(l) >= ord('A') and ord(l) <= ord('Z'):
				# in tal caso codifica il carattere
				word_enc += chr( ord('A') + ((ord(l) -ord('A') +key) %M) )
			else:
				# altrimenti lo prende invariato
				word_enc += l
	return word_enc

def encode(message):
	return cesare(message)

def decode(message):
	return cesare(message, -3)
