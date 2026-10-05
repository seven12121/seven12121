import tkinter as tk
from tkinter import messagebox

def calcular_conversion():
    try:
        
        monto_pesos = float(entry_pesos.get())
        
       
        TC_USD = 17  
        TC_EUR = 21
        
     
        dolares = monto_pesos / TC_USD
        euros = monto_pesos / TC_EUR
        
        
        lbl_resultado_usd.config(text=f"${dolares:,.2f} USD")
        lbl_resultado_eur.config(text=f"€{euros:,.2f} EUR")
        
    except ValueError:
        messagebox.showerror("Error de entrada", "Por favor ingresa una cantidad numérica válida.")


ventana = tk.Tk()
ventana.title("Conversor de Divisas")
ventana.geometry("380x280")
ventana.resizable(False, False)
ventana.config(bg="#f4f6f8")


lbl_titulo = tk.Label(
    ventana, 
    text="Conversor: Pesos a USD / EUR", 
    font=("Arial", 14, "bold"), 
    bg="#f4f6f8", 
    fg="#333333"
)
lbl_titulo.pack(pady=15)


frame_entrada = tk.Frame(ventana, bg="#f4f6f8")
frame_entrada.pack(pady=5)

lbl_pesos = tk.Label(frame_entrada, text="Monto en Pesos ($):", font=("Arial", 11), bg="#f4f6f8")
lbl_pesos.grid(row=0, column=0, padx=5, pady=5)

entry_pesos = tk.Entry(frame_entrada, font=("Arial", 11), width=15)
entry_pesos.grid(row=0, column=1, padx=5, pady=5)
entry_pesos.focus()


btn_convertir = tk.Button(
    ventana, 
    text="Convertir", 
    command=calcular_conversion, 
    font=("Arial", 11, "bold"), 
    bg="#007bff", 
    fg="white", 
    padx=10, 
    pady=3,
    relief="flat"
)
btn_convertir.pack(pady=12)


frame_resultados = tk.Frame(ventana, bg="#ffffff", bd=1, relief="solid")
frame_resultados.pack(fill="x", padx=30, pady=10)

lbl_usd_tag = tk.Label(frame_resultados, text="Dólares (USD):", font=("Arial", 11, "bold"), bg="#ffffff", fg="#555555")
lbl_usd_tag.grid(row=0, column=0, padx=15, pady=8, sticky="w")

lbl_resultado_usd = tk.Label(frame_resultados, text="$0.00 USD", font=("Arial", 11, "bold"), bg="#ffffff", fg="#28a745")
lbl_resultado_usd.grid(row=0, column=1, padx=15, pady=8, sticky="e")

lbl_eur_tag = tk.Label(frame_resultados, text="Euros (EUR):", font=("Arial", 11, "bold"), bg="#ffffff", fg="#555555")
lbl_eur_tag.grid(row=1, column=0, padx=15, pady=8, sticky="w")

lbl_resultado_eur = tk.Label(frame_resultados, text="€0.00 EUR", font=("Arial", 11, "bold"), bg="#ffffff", fg="#17a2b8")
lbl_resultado_eur.grid(row=1, column=1, padx=15, pady=8, sticky="e")


ventana.mainloop()