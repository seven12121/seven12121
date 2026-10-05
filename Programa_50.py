import customtkinter

# Configuración inicial
customtkinter.set_appearance_mode("Light")   # "Light", "Dark" o "System"
customtkinter.set_default_color_theme("blue")

# Crear ventana principal
app = customtkinter.CTk()
app.geometry("400x300")
app.title("Programa_50.py")

# --- Función de conversión ---
def convertir():
    try:
        pesos = float(entry_pesos.get())
        dolares = float(entry_dolares.get())

       
        tasa_dolar = 18.0   # 1 dólar = 18 pesos
        tasa_libra = 22.0   # 1 libra = 22 pesos
        tasa_colombiano = 0.0045  # 1 peso colombiano = 0.0045 pesos mexicanos

        
        if pesos > 0:
            entry_dolares.delete(0, "end")
            entry_dolares.insert(0, round(pesos / tasa_dolar, 2))

        
        if dolares > 0:
            entry_pesos.delete(0, "end")
            entry_pesos.insert(0, round(dolares * tasa_dolar, 2))

        
        label_libra.configure(text=f"Libra esterlina: {round(pesos/tasa_libra, 2)}")
        label_colombiano.configure(text=f"Peso colombiano: {round(pesos/tasa_colombiano, 2)}")

    except ValueError:
        label_libra.configure(text="Libra esterlina: Error")
        label_colombiano.configure(text="Peso colombiano: Error")

entry_pesos = customtkinter.CTkEntry(app, placeholder_text="Pesos")
entry_pesos.grid(row=0, column=0, padx=10, pady=10)

entry_dolares = customtkinter.CTkEntry(app, placeholder_text="Dólares")
entry_dolares.grid(row=0, column=1, padx=10, pady=10)

btn_convertir = customtkinter.CTkButton(app, text="Convertir", command=convertir)
btn_convertir.grid(row=1, column=0, columnspan=2, pady=10)

label_libra = customtkinter.CTkLabel(app, text="Libra esterlina: 0.0")
label_libra.grid(row=2, column=0, columnspan=2, pady=5)

label_colombiano = customtkinter.CTkLabel(app, text="Peso colombiano: 0.0")
label_colombiano.grid(row=3, column=0, columnspan=2, pady=5)

app.mainloop()
