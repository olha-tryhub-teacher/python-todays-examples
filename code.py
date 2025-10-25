from customtkinter import *
from PIL import Image

set_default_color_theme("theme.json")


class AuthWindow(CTk):
   def __init__(self):
       super().__init__()
       self.geometry("700x400")
       self.title("Вхід")
       self.resizable(True, False)

       # --- ліва частина --
       self.left_frame  = CTkFrame(self)
       self.left_frame.pack(side="left", fill="both")

       img_ctk = CTkImage(light_image=Image.open("img/bg.png"), size=(450, 400))
       self.img_label = CTkLabel(self.left_frame, text="Welcome", image=img_ctk, font=("Helvetica", 50, "bold"))
       self.img_label.pack()

       # -- ПРАВА ЧАСТИНА----
       self.right_frame = CTkFrame(self)
       self.right_frame.pack_propagate(False)
       self.right_frame.pack(side="right", fill="both", expand="True")

       CTkLabel(self.right_frame, text="LogiTalk").pack(pady=60)

       self.name_entry = CTkEntry(self.right_frame, placeholder_text="☻ ім`я")
       self.name_entry.pack(fill="x", padx=10, pady=10)
       img_ctk = CTkImage(light_image=Image.open("img/setting.png"), size=(20, 20))
       self.settings_button = CTkButton(self.right_frame, text="Налаштування", image=img_ctk, compound="left")
       self.settings_button.pack(fill="x", padx=10, pady=10)

       self.connect_button = CTkButton(self.right_frame, text="УВІЙТИ")
       self.connect_button.pack(fill="x", padx=10, pady=5)


window = AuthWindow()
window.mainloop()
