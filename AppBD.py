import tkinter as tk
from tkinter import ttk
from Seleccion_productos.Select_product1 import Select_product

# Ventana principal
root = tk.Tk()
root.title("Sistema de Ventas")
root.geometry("800x600")

# Funciones para cambiar contenido dinámico
def mostrar_usuario():
    limpiar_contenido()
    label = tk.Label(frame_contenido, text="Gestión de Usuario", font=("Arial", 16))
    label.pack(pady=20)

def mostrar_producto():
    limpiar_contenido()
    label = tk.Label(frame_contenido, text="Selección de Productos", font=("Arial", 16))
    label.pack(pady=20)
    Select_product(frame_contenido)  


def mostrar_cliente():
    limpiar_contenido()
    label = tk.Label(frame_contenido, text="Gestión de Clientes", font=("Arial", 16))
    label.pack(pady=20)

def limpiar_contenido():
    for widget in frame_contenido.winfo_children():
        widget.destroy()



# Marco donde cambiará el contenido
frame_contenido = tk.Frame(root, bg="lightgray", width=800, height=600)
frame_contenido.pack(fill="both", expand=True)

# Barra de menú superior
barra_menu = tk.Menu(root)
barra_menu.add_command(label="Usuario", command=mostrar_usuario)
barra_menu.add_command(label="Producto", command=mostrar_producto)  # CORREGIDO
barra_menu.add_command(label="Cliente", command=mostrar_cliente)
barra_menu.add_command(label="Cerrar Sesión", command=root.quit)
root.config(menu=barra_menu)

root.mainloop()
