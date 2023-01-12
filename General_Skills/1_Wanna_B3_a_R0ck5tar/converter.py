
def convert_ascii():
	with open('rockstar_output.txt', 'r') as f:
		asciis = map(int, f.read().splitlines())
	print(''.join(map(chr, asciis)))


if __name__ == '__main__':
	convert_ascii()
