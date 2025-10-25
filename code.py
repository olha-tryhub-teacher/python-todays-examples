from customtkinter import *
from PIL import Image


window = CTk()
window.geometry("400x400")
window.title("Моє перше зображення в вікні")


img = Image.open("img1111.png")
img_ctk = CTkImage(light_image=img, size=(350, 450))


label = CTkLabel(window, text="", image=img_ctk)
label.pack(pady=10)


window.mainloop()
