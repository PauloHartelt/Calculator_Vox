import customtkinter

from main import main

app = customtkinter.CTk()
app.title("Calculadora")
app.geometry("300x150")

botao = customtkinter.CTkButton(app, text="Iniciar", width= 70, height= 70, corner_radius= 20,command=main, anchor="center")
botao.pack(padx=20, pady=20)

app.mainloop()