def encrypt(plaintext):
	binary_plain = str_2_binary(plaintext)
	binary_random = str_2_binary(bytes_2_str(get_random_bytes(len(plaintext))))
	out = []

	for i in range(len(binary_plain)):
		if ord(get_random_bytes(1))/255 > 0.1:
			out.append(str(int(binary_random[i]) ^ int(binary_plain[i]))) # 0 or 1
		else:
			out.append(str(int(binary_plain[i]))) # 0 or 1
	
	out = binary_2_str(''.join(out))
	return out