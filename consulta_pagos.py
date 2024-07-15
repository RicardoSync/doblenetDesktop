import customtkinter as ctk
import mysql.connector
from tkinter import ttk
import json

def mostrar_tabla_pagos():
    # Leer configuración desde el archivo JSON
    with open('config.json', 'r') as f:
        config = json.load(f)

    # Conexión a la base de datos MySQL
    conn = mysql.connector.connect(
        host=config["host"],
        user=config["user"],
        password=config["password"],
        database=config["database"]
    )
    cursor = conn.cursor()

    # Consulta a la tabla pagos
    cursor.execute("SELECT * FROM pagos")
    rows = cursor.fetchall()

    # Configuración de la ventana principal de customtkinter
    ctk.set_appearance_mode("dark")  # Puedes cambiar a "light" si prefieres
    ctk.set_default_color_theme("blue")

    root = ctk.CTk()
    root.title("Tabla de Pagos")
    root.geometry("800x400")

    # Crear un frame para el Treeview
    frame = ctk.CTkFrame(root)
    frame.pack(expand=True, fill="both", padx=10, pady=10)

    # Creación del widget Treeview para mostrar los datos
    tree = ttk.Treeview(frame, columns=("id", "NombreCliente", "Mensualidad", "FechaPago"), show="headings")
    tree.heading("id", text="ID")
    tree.heading("NombreCliente", text="Nombre del Cliente")
    tree.heading("Mensualidad", text="Mensualidad")
    tree.heading("FechaPago", text="Fecha de Pago")

    # Estilo para el Treeview
    style = ttk.Style()
    style.configure("Treeview", 
                    background="#2e2e2e", 
                    foreground="white", 
                    rowheight=25, 
                    fieldbackground="#2e2e2e")
    style.configure("Treeview.Heading", 
                    background="#565656", 
                    foreground="white")
    style.map('Treeview', background=[('selected', '#4a6984')])

    # Inserción de los datos en el Treeview
    for row in rows:
        tree.insert("", "end", values=row)

    tree.pack(expand=True, fill="both")

    # Agregar opciones de scrollbar
    scrollbar_x = ctk.CTkScrollbar(frame, orientation="horizontal", command=tree.xview)
    scrollbar_x.pack(side="bottom", fill="x")
    tree.configure(xscrollcommand=scrollbar_x.set)

    scrollbar_y = ctk.CTkScrollbar(frame, orientation="vertical", command=tree.yview)
    scrollbar_y.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar_y.set)

    # Iniciar la aplicación
    root.mainloop()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conn.close()

# Llamada a la función para mostrar la tabla de pagos
