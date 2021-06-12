from Crypto.Cipher import AES
from Crypto import Random
import base64
import binascii
from datetime import datetime
from itertools import product
import codecs


Plain_text = binascii.unhexlify("686f6c61000000000000000000000000")
IV = binascii.unhexlify('00000000000000000000000000000000')
texto_cifrado = binascii.unhexlify("597c41c4b672e343ca95a7f8d6117607")
count = 1
start = datetime.now()

POSSCAR = ['e7','c6','a5','84','63','42','21','00']
iteracion = 0

contador = 1




for item in product(POSSCAR,repeat=12):
	valorHexa = ''.join(item)+'00000000'
	key = binascii.unhexlify(valorHexa)
	Cipher = AES.new(key, AES.MODE_CBC, IV)
	Encrypting = Cipher.encrypt(Plain_text)
	if(binascii.hexlify(texto_cifrado) == binascii.hexlify(Encrypting)):
		print(str(count)+") La clave es: "+str(binascii.hexlify(Encrypting)))
		print("Hora final: "+str(final))
		break
	if(contador==10000000):
			print(str(count)+") - "+str(start)+" // probando la clave: "+str(binascii.hexlify(Encrypting)))
			contador = 0
		
	count = count + 1
	contador = contador + 1