import tkinter as tk


def iniciar_temporizador():
    try:
        segundos = int(campo_tiempo.get())
        cuenta_atras(segundos)
    except ValueError:
        etiqueta_mensaje.config(text="Por favor, ingresa un número válido")


def cuenta_atras(segundos):
    if segundos > 0:
        etiqueta_mensaje.config(text=f"{segundos} segundos restantes")
        ventana_principal.after(1000, cuenta_atras, segundos - 1)
    else:
        etiqueta_mensaje.config(text="¡Tiempo finalizado!")


ventana_principal = tk.Tk()
ventana_principal.title("Temporizador de Cuenta Regresiva")

tk.Label(ventana_principal, text="Tiempo en segundos:", font=('Arial', 14)).grid(row=0, column=0, padx=10, pady=10)
campo_tiempo = tk.Entry(ventana_principal, width=10, font=('Arial', 14))
campo_tiempo.grid(row=0, column=1, padx=10, pady=10)

tk.Button(ventana_principal, text="Empezar", command=iniciar_temporizador, font=('Arial', 14), bg="#28a745", fg="white").grid(row=1, column=0, columnspan=2, pady=10)

etiqueta_mensaje = tk.Label(ventana_principal, text="", font=('Arial', 18), fg="red")
etiqueta_mensaje.grid(row=2, column=0, columnspan=2, pady=10)

ventana_principal.mainloop()
