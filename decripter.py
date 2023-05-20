from cryptography.fernet import Fernet

# Leer la clave utilizada para encriptar
clave = b'y7TFYDCcI4I5NFf4uprpfQE1L_YfN47BTppwZumylxY='  # Reemplaza con la clave utilizada en la encriptación

# Crear un objeto Fernet con la clave
cipher_suite = Fernet(clave)

# Abrir el archivo encriptado
with open("archivo_encriptado.txt", "rb") as archivo_encriptado:
    contenido_encriptado = archivo_encriptado.read()

# Desencriptar el contenido del archivo
print('# Desencriptando el contenido del archivo')
contenido_desencriptado = cipher_suite.decrypt(contenido_encriptado)

# Escribir el contenido desencriptado en un nuevo archivo
with open("archivo_desencriptado.txt", "wb") as archivo_desencriptado:
    archivo_desencriptado.write(contenido_desencriptado)
