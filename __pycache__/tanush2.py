# Encryption Programme 
import string
import random
char=string.ascii_letters+string.punctuation+string.digits+" "
char=list(char)
key=char.copy()
random.shuffle(key)
s=input("Enter Your messege TO BE ENCRYPTED: ")
cipher_text=""
for x in s:
    index=char.index(x)
    cipher_text+=key[index]
print(f"The Encrypted Messge :  {cipher_text}")
k=input("Enter Your Encrypted messege: ")
h=""
for i in k:
    l=key.index(i)
    h+=char[l]
print(f"Your de-encrypeted Messege: {h}")
    