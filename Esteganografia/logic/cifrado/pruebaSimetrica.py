from cryptography.fernet import Fernet


clave = Fernet.generate_key()

print(clave)

f = Fernet(clave)

token = f.encrypt(b'Juan Pablo')

print(token)

#des = f.decrypt(token)
#print(str(des))
