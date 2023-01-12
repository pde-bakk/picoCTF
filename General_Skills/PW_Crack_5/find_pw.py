import hashlib

with open('dictionary.txt', 'r') as f:
	possible_passwords = f.read().splitlines()
valid_hash = "1236 50dd 0560 5879 18b3 d771 cf0c 0171".replace(' ', '')

if __name__ == '__main__':
	for pw in possible_passwords:
		encoded = pw.encode("utf-8")
		hashed = hashlib.md5(encoded).hexdigest()
		if hashed == valid_hash:
			print(f's= {pw}, md5sum= {hashed}')
			break
