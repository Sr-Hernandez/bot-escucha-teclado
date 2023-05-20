import keyboard




archivo = open("archivo.txt", "w")
def on_key(event):
    print('Tecla presionada:', event.name)
    archivo.write(event.name)
    if event.name == '}': 
         archivo.close()


keyboard.on_press(on_key)

keyboard.wait('esc')  # Espera hasta que se presione la tecla 'esc'
# 