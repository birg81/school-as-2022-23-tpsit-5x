def cesare(word = '', key = 3):
	M = ord('Z') - ord('A') + 1
	word_enc = word.strip().upper()
	if (M + key) % M > 0:
		word_enc = ''
		for l in word.strip().upper():
			if ord(l) >= ord('A') and ord(l) <= ord('Z'):
				word_enc += chr(
					ord('A') +
					((ord(l) - ord('A') + key + M) % M)
				)
			else:
				word_enc += l
	return word_enc

def encode(message):
	return cesare(message)

def decode(message):
	return cesare(message, -3)