import customtkinter as ctk

ventanita = ctk.CTk()
ventanita.geometry ("400 x 200 + 200 + 200")
ventanita.title("Python")
ventanita.configure(fg_color = "#1F2937") #-> codigo hexaedecimal del color, # "blue"
ventanita.resizable (True, False)
ventanita.iconbitmap ("c:\Users\moira\Downloads\20260520_191052.ico")

ventanita.mainloop()