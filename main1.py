from tkinter import *
import pyqrcode
from PIL import ImageTk, Image
import os

root = Tk()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"

    # Gera o QR Code
    url = pyqrcode.create(link)
    url.png(file_name, scale=8)

    # Carrega a imagem gerada e exibe no canvas
    if os.path.exists(file_name):
        image = Image.open(file_name)
        image = image.resize((200, 200))  # Ajusta o tamanho se quiser
        photo = ImageTk.PhotoImage(image)

        image_label = Label(root, image=photo)
        image_label.image = photo  # Mantém referência da imagem
        canvas.create_window(200, 450, window=image_label)

canvas = Canvas(root, width=400, height=600)
canvas.pack()

app_Label = Label(root, text="QR Code Generator", fg="blue", font=("Arial", 20))
canvas.create_window(200, 50, window=app_Label)

name_label = Label(root, text="Nome do arquivo (sem .png):")
link_label = Label(root, text="Link para gerar o QR Code:")

canvas.create_window(200, 100, window=name_label)
canvas.create_window(200, 160, window=link_label)

name_entry = Entry(root)
link_entry = Entry(root)

canvas.create_window(200, 130, window=name_entry)
canvas.create_window(200, 180, window=link_entry)

# Botão para gerar o QR Code
generate_button = Button(root, text="Gerar QR Code", command=generate)
canvas.create_window(200, 220, window=generate_button)

root.mainloop()
