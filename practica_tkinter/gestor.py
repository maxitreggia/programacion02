import tkinter as tk


def agregar_contacto():
    nombre = campo_nombre.get()
    telefono = campo_telefono.get()
    if nombre and telefono:
        lista_contactos.insert(tk.END, f"{nombre} - {telefono}")
        campo_nombre.delete(0, tk.END)
        campo_telefono.delete(0, tk.END)


def eliminar_contacto_seleccionado():
    seleccion = lista_contactos.curselection()
    if seleccion:
        lista_contactos.delete(seleccion)


ventana = tk.Tk()
ventana.title("Administrador de Contactos")

tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
campo_nombre = tk.Entry(ventana)
campo_nombre.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Teléfono:").grid(row=1, column=0, padx=5, pady=5)
campo_telefono = tk.Entry(ventana)
campo_telefono.grid(row=1, column=1, padx=5, pady=5)

tk.Button(ventana, text="Añadir Contacto", command=agregar_contacto).grid(row=2, column=0, columnspan=2, pady=5)
tk.Button(ventana, text="Eliminar Contacto", command=eliminar_contacto_seleccionado).grid(row=3, column=0, columnspan=2, pady=5)

lista_contactos = tk.Listbox(ventana, width=40)
lista_contactos.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

ventana.mainloop()
