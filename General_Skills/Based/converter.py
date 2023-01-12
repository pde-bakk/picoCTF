
def convert_binary():
	binary = input('Gimme the space seperated binary: ')
	result = ''
	for s in binary.split():
		value = int(s, 2)
		result += chr(value)
	print(result)


def convert_octal_values():
	asciis = input('Gimme the space seperate octal values: ')
	result = ''
	for s in asciis.split():
		val = int(s, 8)
		result += chr(val)
	print(result)


def convert_hex_value():
	hex_value = input('Gimme the hex value: ')
	result = ''
	for i in range(0, len(hex_value), 2):
		val = hex_value[i:i+2]
		result += chr(int(val, 16))
	print(result)

if __name__ == '__main__':
	convert_binary()
	convert_octal_values()
	convert_hex_value()
