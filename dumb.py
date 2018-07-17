import base64
strg=''
while(True):
	option=input('want to encode or decode\n')
	if option=='encode':
		str=input('enter to encode\n')
		En=base64.b64encode(str.encode('UTF-8')).decode('ascii')
		strg=En
		print(En)
		

	else:
		str1=input('enter to "decode" the earlier encode or enter a "new" decode input: \n')
		if str1=='decode':
			decoded=base64.b64decode(strg).decode('ascii')
			print(decoded)
			break
		else:
			str=input('enter new input to be decoded\n')
			str1=str.strip()
			decoded=base64.b64decode(str1).decode('ascii')
			print(decoded)
			break