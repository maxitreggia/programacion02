import tkinter as tk
from tkinter import messagebox


def realizar_conversion():
    try:
        kilometros = float(entrada_kilometros.get())
        millas_resultado = kilometros * 0.621371
        etiqueta_resultado.config(text=f'{millas_resultado:.2f} millas')
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido.")


ventana = tk.Tk()
ventana.title("Convertidor de Unidades")
ventana.configure(bg="#e6f2ff")

etiqueta_titulo = tk.Label(ventana, text="Convertidor de Km a Millas", font=('Arial', 18, 'bold'), bg="#e6f2ff")
etiqueta_titulo.grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(ventana, text="Kilómetros:", font=('Arial', 14), bg="#e6f2ff").grid(row=1, column=0, padx=10, pady=10)
entrada_kilometros = tk.Entry(ventana, width=10, font=('Arial', 14))
entrada_kilometros.grid(row=1, column=1, padx=10, pady=10)

tk.Button(ventana, text="Convertir", command=realizar_conversion, font=('Arial', 14), bg="#4CAF50", fg="white").grid(row=2, column=0, columnspan=2, pady=10)

etiqueta_resultado = tk.Label(ventana, text="Resultado: 0.00 millas", font=('Arial', 14), bg="#e6f2ff")
etiqueta_resultado.grid(row=3, column=0, columnspan=2, pady=10)

ventana.mainloop()
