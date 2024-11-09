import tkinter as tk
import time


def actualizar_hora():
    hora_actual = time.strftime('%H:%M:%S')
    label_reloj.config(text=hora_actual)
    ventana_principal.after(1000, actualizar_hora)


ventana_principal = tk.Tk()
ventana_principal.title("Reloj en Tiempo Real")

label_reloj = tk.Label(ventana_principal, font=('Courier', 48), fg='blue', bg='lightgray')
label_reloj.pack(pady=30)

actualizar_hora()

ventana_principal.mainloop()
