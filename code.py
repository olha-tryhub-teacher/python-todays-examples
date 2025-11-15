# УВАГА! ТЕМИ ШУКАЄМО ЗА ПОСИЛАННЯМ:
# https://github.com/a13xe/CTkThemesPack/tree/main/themes

from customtkinter import *
from PIL import Image


class AuthWindow(CTk):
    def __init__(self):
        super().__init__()
        self.geometry("700x400")
        self.title("Вхід")
        self.resizable(True, False)
        self.name = ""

        # --- ліва частина --
        self.left_frame = CTkFrame(self)
        self.left_frame.pack(side="left", fill="both")

        # ТУТ ЗМІНЮЄМО КАРТІНКУ ДЛЯ ФОНУ
        img_ctk = CTkImage(light_image=Image.open("bg.png"), size=(450, 400))
        self.img_label = CTkLabel(self.left_frame, text="Welcome", image=img_ctk, font=("Helvetica", 50, "bold"))
        self.img_label.pack()

        # -- ПРАВА ЧАСТИНА----
        self.right_frame = CTkFrame(self)
        self.right_frame.pack_propagate(False)
        self.right_frame.pack(side="right", fill="both", expand="True")

        CTkLabel(self.right_frame, text="LogiTalk").pack(pady=60)

        self.name_entry = CTkEntry(self.right_frame, placeholder_text="☻ ім`я")
        self.name_entry.pack(fill="x", padx=10, pady=10)

        self.connect_button = CTkButton(self.right_frame, text="УВІЙТИ", command=self.open_messenger)
        self.connect_button.pack(fill="x", padx=10, pady=5)

    def open_messenger(self):
        self.name = self.name_entry.get()
        self.destroy()
