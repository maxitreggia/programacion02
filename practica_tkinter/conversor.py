import tkinter as tk
from tkinter import messagebox

def convertir():
    try:
        km = float(entrada_km.get())
        millas = km * 0.621371
        resultado_millas.config(text=f'{millas:.2f} millas')
    except ValueError:
        messagebox.showerror("Error, ingresa un valor valido")

ventana = tk.Tk()
ventana.title("Conversor de Unidades")
ventana.configure(bg="#f0f0f0")

titulo = tk.Label(ventana, text="Conversor de km  a Millas", font=('Arial', 18, 'bold'), bg="#f0f0f0")
titulo.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(ventana, text="Kilómetros:", font=('Arial', 14), bg="#f0f0f0").grid(row=1, column=0, padx=10, pady=10)
entrada_km = tk.Entry(ventana, width=10, font=('Arial', 14))
entrada_km.grid(row=1, column=1, padx=10, pady=10)

tk.Button(ventana, text="Convertir", command=convertir, font=('Arial', 14), bg="#007acc", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

resultado_millas = tk.Label(ventana, text="0.00 millas", font=('Arial', 14), bg="#f0f0f0")
resultado_millas.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
