import string

LOWERCASE_OFFSET = ord('a')
ALPHABET = string.ascii_lowercase[:16]
encrypted_flag = 'lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil'


def b16_decode(cipher: str):
	dec = ''
	for c in range(0, len(cipher), 2):
		# Reverse the encoding
		tmp = '{0:b}'.format(ALPHABET.index(cipher[c])).zfill(4)
		tmp += '{0:b}'.format(ALPHABET.index(cipher[c + 1])).zfill(4)
		value = int(tmp, 2)
		dec += chr(value)
	return dec


def unshift(c: str, k: str):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 - t2) % len(ALPHABET)]


if __name__ == '__main__':
	for alpha in ALPHABET:
		s = ''
		for i, char in enumerate(encrypted_flag):
			s += unshift(char, alpha)
		print(b16_decode(s))
