import hashlib


if __name__ == '__main__':
	for i in ["f09e", "4dcf", "87ab", "dba8", "752e", "3961", "f159"]:
		print(f's= {i}, md5sum= {hashlib.md5(i.encode("utf-8")).hexdigest()}')
