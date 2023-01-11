import hashlib
import sys
username_trial = "FREEMAN"
bUsername_trial = b"FREEMAN"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial


def check_key(key, username_trial):

	global key_full_template_trial

	if len(key) != len(key_full_template_trial):
		print(f'{len(key)=} is not {len(key_full_template_trial)=}')
		return False
	else:
		# Check static base key part --v
		i = 0
		for c in key_part_static1_trial:
			if key[i] != c:
				return False
			i += 1

		print(f'hexdigest =', hashlib.sha256(username_trial).hexdigest())
		for i2 in [4, 5, 3, 6, 2, 7, 1, 8]:
			print(hashlib.sha256(username_trial).hexdigest()[i2])
		if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:
			return False
		else:
			i += 1

		if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:
			return False
		else:
			i += 1

		if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:
			return False
		else:
			i += 1

		if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:
			return False
		else:
			i += 1

		if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:
			return False
		else:
			i += 1
		if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:
			return False
		else:
			i += 1
		if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:
			return False
		else:
			i += 1
		if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:
			return False
	return True

if __name__ == '__main__':
	print(len(sys.argv))
	if len(sys.argv) != 2:
		exit()
	check_key(sys.argv[1], bUsername_trial)
