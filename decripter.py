from cryptography.fernet import Fernet

# Leer la clave utilizada para encriptar

# Abre el archivo en modo lectura
with open("key.txt", "r") as archivo:
    contenido = archivo.read()

# Imprime el contenido del archivo
# print(contenido)


clave = contenido  # Reemplaza con la clave utilizada en la encriptación

# Crear un objeto Fernet con la clave


# Abrir el archivo encriptado
with open("archivo_encriptado.txt", "rb") as archivo_encriptado:
    contenido_encriptado = archivo_encriptado.read()
    partes = contenido_encriptado.decode('utf-8').split('=')
    key = partes[0]
    msj=partes[1]
    contenido_str = ''.join(key)

key=key+'='
msj=msj+'=='
cipher_suite = Fernet(key)
print('# Desencriptando el contenido del archivo')
# Desencriptar el contenido del archivo
contenido_desencriptado = cipher_suite.decrypt(msj)

# Escribir el contenido desencriptado en un nuevo archivo
with open("archivo_desencriptado.txt", "wb") as archivo_desencriptado:
    archivo_desencriptado.write(contenido_desencriptado)
