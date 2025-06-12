import tkinter as tk
from tkinter import ttk

def Select_product(parent):
    # Frame para gestionar productos
    frame_productos = tk.Frame(parent)
    frame_productos.pack(pady=20)

    # --- Tabla de productos (Treeview) ---
    tree = ttk.Treeview(frame_productos, columns=("nombre", "cantidad", "precio", "descripcion", "iva", "categoria"), show="headings")
    tree.heading("nombre", text="Nombre")
    tree.heading("cantidad", text="Cantidad")
    tree.heading("precio", text="Precio")
    tree.heading("descripcion", text="Descripción")
    tree.heading("iva", text="IVA")
    tree.heading("categoria", text="Categoría")
    tree.pack()

    # Datos de ejemplo
    tree.insert("", tk.END, values=("Coca Cola", 20, 1.5, "2 litros", 0.18, "bebidas"))
    tree.insert("", tk.END, values=("Pepsi", 10, 1.3, "1 litro", 0.16, "bebidas"))

    # --- Campos de entrada ---
    campos_frame = tk.Frame(parent)
    campos_frame.pack(pady=10)

    tk.Label(campos_frame, text="Nombre").grid(row=0, column=0)
    entry_nombre = tk.Entry(campos_frame)
    entry_nombre.grid(row=0, column=1)

    tk.Label(campos_frame, text="Cantidad").grid(row=0, column=2)
    entry_cantidad = tk.Entry(campos_frame)
    entry_cantidad.grid(row=0, column=3)

    tk.Label(campos_frame, text="Precio").grid(row=1, column=0)
    entry_precio = tk.Entry(campos_frame)
    entry_precio.grid(row=1, column=1)

    tk.Label(campos_frame, text="Descripción").grid(row=1, column=2)
    entry_descripcion = tk.Entry(campos_frame)
    entry_descripcion.grid(row=1, column=3)

    tk.Label(campos_frame, text="IVA").grid(row=2, column=0)
    combo_iva = ttk.Combobox(campos_frame, values=["0.00", "0.10", "0.16", "0.18"])
    combo_iva.grid(row=2, column=1)

    tk.Label(campos_frame, text="Categoría").grid(row=2, column=2)
    combo_categoria = ttk.Combobox(campos_frame, values=["bebidas", "zapatos", "vestimenta", "equipos de computo", "frutas", "verduras"])
    combo_categoria.grid(row=2, column=3)

    # --- Botones de acción ---
    boton_frame = tk.Frame(parent)
    boton_frame.pack(pady=10)

    tk.Button(boton_frame, text="Actualizar", bg="lightgreen").pack(side=tk.LEFT, padx=5)
    tk.Button(boton_frame, text="Eliminar", bg="red").pack(side=tk.LEFT, padx=5)
