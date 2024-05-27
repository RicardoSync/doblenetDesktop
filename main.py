from customtkinter import *
from tkinter import ttk
from PIL import Image
import mysql.connector
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import Menu
from PIL import Image, ImageDraw, ImageFont
from mysql.connector import Error
import tkinter as tk
from tkinter import ttk
from customtkinter import CTk, CTkFrame, CTkToplevel
from datetime import datetime, timedelta
from customtkinter import CTk, CTkToplevel, CTkFrame, CTkLabel, CTkEntry, CTkButton, CTkTextbox
import json
import datetime
import webbrowser

app = CTk()
app.title("DoblenetDesktop - v0.2")
app.geometry("1500x768")

set_appearance_mode("dark")

subtitulo = CTkFont("Arial", 15)

# DEFINICION DE LOS COLORES
color_azul = "#5dade2"
color_medio_guero = "#DAF7A6"
color_azul = "#2874a6"
color_medio_guero = "#DAF7A6"
color_amarillo = "#FFC300"
color_verde = "#138d75"
color_blanco = "#FDFEFE"
color_azul_contra = "#2471a3"
color_negro = "#17202A"


# DEFINIMOS LOS FRAMES A USAR EN LA APP
banner = CTkFrame(master=app, corner_radius=0, fg_color=color_azul)
centro = CTkFrame(master=app, corner_radius=0, fg_color=color_medio_guero)

def load_images():
    images = {
        "crear_usuario": CTkImage(dark_image=Image.open("icons/agregar-usuario.png"), size=(50, 50)),
        "agua": CTkImage(dark_image=Image.open("icons/agua.png"), size=(70, 70)),
        "metodo_de_pago": CTkImage(dark_image=Image.open("icons/metodo-de-pago.png"), size=(50, 50)),
        "ver_pagos": CTkImage(dark_image=Image.open("icons/buscar.png"), size=(50, 50)),
        "recibo": CTkImage(dark_image=Image.open("icons/recibo.png"), size=(50, 50)),
        "configuraciones": CTkImage(dark_image=Image.open("icons/configuraciones.png"), size=(50, 50)),
        "fondo" : CTkImage(dark_image=Image.open("icons/fondo.png"), size=(350,350)),
        "usuario" : CTkImage(dark_image=Image.open("icons/usuario.png"), size=(150,150)),
        "pago" : CTkImage(dark_image=Image.open("icons/pago.png"), size=(150,150)),
        "lupa" : CTkImage(dark_image=Image.open("icons/validando-billete.png"), size=(100,100)),
        "antena" : CTkImage(dark_image=Image.open("icons/antena-parabolica.png"), size=(50,50)),
        "editar" : CTkImage(dark_image=Image.open("icons/editar-informacion.png"), size=(150,150)),
        "herramientas" : CTkImage(dark_image=Image.open("icons/herramienta_red.png"), size=(50,50)),
        "configuracion-red" : CTkImage(dark_image=Image.open("icons/configuracion-red.png"), size=(150,150)),
        "radar-de-velocidad" : CTkImage(dark_image=Image.open("icons/radar-de-velocidad.png"), size=(50,50)),
        "desbloqueado" : CTkImage(dark_image=Image.open("icons/desbloqueado.png"), size=(50,50)),
        "reiniciar" : CTkImage(dark_image=Image.open("icons/reiniciar.png"), size=(50,50))

    }
    return images

# Ruta al archivo JSON
config_file = 'config.json'

# Abrir y cargar el archivo JSON
with open(config_file, 'r') as file:
    db_config = json.load(file)


images = load_images()

# DEFINIMOS LAS ETIQUETAS CON IMAGEN
agua_logo_lb = CTkLabel(master=banner, text="", image=images["agua"])



#================================================FUNCIONES==================================


# Configura la conexión a la base de datos
def connect_db():
    # Abrir y cargar el archivo JSON
    with open(config_file, 'r') as file:
        db_config = json.load(file)
    
    # Establecer la conexión usando los datos del archivo JSON
    return mysql.connector.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database']
    )

def registrarPago():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Crear Pago")
    crearUsuarioWindow.geometry("1000x600")
    crearUsuarioWindow.resizable(False, False)
    
    imagenes = load_images()

    # Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

    def salir():
        crearUsuarioWindow.destroy()

    def buscarCliente():
        cliente_id = entId.get()
        conn = connect_db()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT Nombre, FechaInstalacion, Mensualidad FROM clientes WHERE id = %s", (cliente_id,))
        cliente = cursor.fetchone()
        if cliente:
            entNombre.delete(0, 'end')
            entNombre.insert(0, cliente['Nombre'])
            entMonto.insert(0, cliente['Mensualidad'])
            
        else:
            lbAutomatico.config(text="Cliente no encontrado")
        cursor.close()
        conn.close()

    def guardarPago():
        cliente_id = entId.get()
        monto = entMonto.get()
        fecha_pago = datetime.date.today()

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pagos (NombreCliente, Mensualidad, FechaPago) VALUES (%s, %s, %s)", (cliente_id, monto, fecha_pago))
        fecha_proximo_pago = fecha_pago + timedelta(days=31)

        sql_update = "UPDATE clientes SET ProximoPago = %s WHERE id = %s"
        cursor.execute(sql_update, (fecha_proximo_pago, cliente_id))
        conn.commit()
        cursor.close()
        conn.close()
        archivo_salida = "recibo.png"



        dna = cliente_id
        nombre = cliente_id
        fecha = fecha_pago
        no_recibo = fecha_pago + timedelta(days=31)
        concepto = "Servicio de internet"
        folio = "000-0000-0909"
        id_transaccion = "ASX12-PLO0908"
        archivo = dna + "." + monto + ".png"
        archivo_salida = archivo

        crear_recibo_imagen(dna, nombre, fecha, monto, no_recibo, concepto, folio, id_transaccion, archivo_salida)
        messagebox.showinfo("Pago Registrado", "Cliente registrado con exito")

    recibo = CTkLabel(master=frame2, text="", image=imagenes["pago"])
    recibo.pack()
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.5,
        rely=0.5
    )

    lbNombre = CTkLabel(
        master=frame1,
        text="Nombre",
        text_color=color_blanco,
        font=subtitulo,
    )
    entNombre = CTkEntry(
        master=frame1,
        placeholder_text="Martin Antonio",
        width=240,
        height=20,
    )

    lbId = CTkLabel(
        master=frame1,
        text="ID",
        text_color=color_blanco,
        font=subtitulo
    )
    entId = CTkEntry(
        master=frame1,
        placeholder_text="5",
        width=240,
        height=20
    )
    lbMonto = CTkLabel(
        master=frame1,
        text="Monto $",
        text_color=color_blanco,
        font=subtitulo
    )
    entMonto = CTkEntry(
        master=frame1,
        placeholder_text="300.45",
        width=240,
        height=20
    )
    lbFecha = CTkLabel(
        master=frame1,
        text="Fecha",
        text_color=color_blanco,
        font=subtitulo
    )
    lbAutomatico = CTkLabel(
        master=frame1,
        text="Generado Automaticamente",
        text_color=color_blanco,
        font=subtitulo
    )

    lbNota = CTkLabel(
        master=frame2,
        text="Notas",
        font=("Arial", 15)
    )
    nota = CTkTextbox(
        master=frame2,
        font=subtitulo,
        width=240,
        height=290
    )
    
    btnGuardar = CTkButton(
        master=frame1,
        text="Guardar",
        width=100,
        height=30,
        command=guardarPago
    )
    btnBuscar = CTkButton(
        master=frame1,
        text="Buscar",
        width=100,
        height=30,
        command=buscarCliente
    )
    btnSalir = CTkButton(
        master=frame1,
        text="Salir",
        width=100,
        height=30,
        command=salir
    )

    lbNombre.grid(
        row=0,
        column=0,
        pady=10,
        padx=10
    )
    entNombre.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )
    lbId.grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )
    entId.grid(
        row=0,
        column=3,
        padx=10,
        pady=10
    )
    btnBuscar.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )
    lbMonto.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    entMonto.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )
    lbFecha.grid(
        row=1,
        column=2,
        padx=10,
        pady=10
    )
    lbAutomatico.grid(
        row=1,
        column=3,
        padx=10,
        pady=10
    )
    lbNota.place(
        relx=0.1,
        rely=0.4
    )
    nota.place(
        relx=0.1,
        rely=0.5
    )
    btnGuardar.place(
        relx=0.1,
        rely=0.9
    )
    btnBuscar.place(
        relx=0.4,
        rely=0.9
    )
    btnSalir.place(
        relx=0.7,
        rely=0.9
    )

    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
    relx=0.7,
    rely=0.0,
    relwidth=0.3,
    relheight=1.0
    )

def crearUsuario():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Crear Persona")
    crearUsuarioWindow.geometry("1000x600")
    crearUsuarioWindow.resizable(False, False)
    
    imagenes = load_images()

    #Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

    def getDatos():
        nombre = entName.get()
        direccion = entDireccion.get()
        telefono = entTelefono.get()
        equipos = equiposOpctions.get()
        Ip = entIpMicrotik.get()
        Velocidad = entVelocidad.get()
        FechaInstalacion =  datetime.date.today()
        ProximoPago = FechaInstalacion + timedelta(days=31)
        Mensualidad = entMensualidad.get()
        crear_usuario_db(nombre, direccion, telefono, equipos, Ip, Velocidad, FechaInstalacion, ProximoPago, Mensualidad)

    def salir():
        crearUsuarioWindow.destroy()

    def buscarCliente():
            cliente_id = entIP.get()
            conn = connect_db()
            cursor = conn.cursor(dictionary=True)
            cursor.execute("SELECT Nombre, Direccion, Telefono, Equipos, Ip, Velocidad, Mensualidad FROM clientes WHERE id = %s", (cliente_id,))
            cliente = cursor.fetchone()
            if cliente:
                #entName.delete(0, 'end')
                entName.insert(0, cliente['Nombre'])
                entDireccion.insert(0, cliente['Direccion'])
                entTelefono.insert(0, cliente['Telefono'])
                entVelocidad.insert(0, cliente['Velocidad'])
                entIpMicrotik.insert(0, cliente['Ip'])
                equiposOpctions.insert(0, cliente['Equipos'])
                entMensualidad.insert(0, cliente['Mensualidad'])
                
            else:
                messagebox.showerror("Error", "Cliente no encontrado")
            cursor.close()
            conn.close()
            conn.close()
    def actualizar():
        conn = connect_db()
        cursor = conn.cursor()
        cliente_id = entIP.get()  # Asegúrate de obtener el ID del cliente correctamente
        Nombre = entName.get()
        Direccion = entDireccion.get()
        Telefono = entTelefono.get()
        Equipos = equiposOpctions.get()
        Ip = entIpMicrotik.get()
        Velocidad = entVelocidad.get()
        Mensualidad = entMensualidad.get()

        sql_update = """
            UPDATE clientes 
            SET Nombre = %s, Direccion = %s, Telefono = %s, Equipos = %s, Ip = %s, Velocidad = %s, Mensualidad = %s 
            WHERE id = %s
        """
        cursor.execute(sql_update, (Nombre, Direccion, Telefono, Equipos, Ip, Velocidad, Mensualidad, cliente_id))
        conn.commit()
        cursor.close()
        conn.close()
        messagebox.showinfo("Listo", "Cliente Actualizado")


    usuario = CTkLabel(master=frame2, text="", image=imagenes["usuario"])
    usuario.place(
        relx=0.3,
        rely=0.0
    )
    btnActualizar = CTkButton(
        master=frame2,
        text="Actualizar",
        width=200,
        height=20,
        command=actualizar
    )
    btnActualizar.place(
        relx=0.2,
        rely=0.3
    )
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.5,
        rely=0.4
    )

    lbName = CTkLabel(
        master=frame1,
        text="Nombre",
        text_color=color_blanco,
        font=subtitulo,
    )
    entName = CTkEntry(
        master=frame1,
        placeholder_text="Martin Antonio",
        width=240,
        height=20,
    )

    lbDireccion = CTkLabel(
        master=frame1,
        text="Direccion",
        text_color=color_blanco,
        font=subtitulo
    )
    entDireccion = CTkEntry(
        master=frame1,
        placeholder_text="Francisco #12",
        width=200,
        height=20
    )
    lbTelefono = CTkLabel(
        master=frame1,
        text="Celular",
        text_color=color_blanco,
        font=subtitulo
    )
    entTelefono = CTkEntry(
        master=frame1,
        placeholder_text="0909129856",
        width=240,
        height=20
    )
    lbPaquete = CTkLabel(
        master=frame1,
        text="Velocidad",
        text_color=color_blanco,
        font=subtitulo
        )
    entVelocidad = CTkEntry(
        master=frame1,
        placeholder_text="100M/15M",
        width=200,
        height=20
    )
    lbComunidad = CTkLabel(
        master=frame1,
        text="Comunidad",
        text_color=color_blanco,
        font=subtitulo
    )
    entComunidad = CTkEntry(
        master=frame1,
        placeholder_text="Loreto",
        width=240,
        height=20
    )
    lbMicrotikIp = CTkLabel(
        master=frame1,
        text="Ip Cliente",
        font=subtitulo
    )
    entIpMicrotik = CTkEntry(
        master=frame1,
        placeholder_text="122.122.126.98",
        width=200,
        height=20
    )
    lbEquipos = CTkLabel(
        master=frame1,
        text="Equipos",
        font=subtitulo
    )
    equiposOpctions = CTkEntry(
        master=frame1,
        placeholder_text="2",
        width=240,
        height=20
    )
    lbMensualidad = CTkLabel(
        master=frame1,
        text="Mensualidad",
        font=subtitulo
    )
    entMensualidad = CTkEntry(
        master=frame1,
        placeholder_text="400.00",
        width=200,
        height=20
    )
    lbIP = CTkLabel(
        master=frame1,
        text="ID Search",
        text_color=color_blanco,
        font=subtitulo
    )
    entIP = CTkEntry(
        master=frame1,
        placeholder_text="2",
        width=220,
        height=20
    )

    lbNota = CTkLabel(
        master=frame2,
        text="Notas",
        font=("Arial", 15)
    )
    nota = CTkTextbox(
        master=frame2,
        font=subtitulo,
        width=240,
        height=290
        )
    btnGuardar = CTkButton(
        master=frame1,
        text="Guardar",
        width=200,
        height=30,
        command=getDatos
    )
    btnSalir = CTkButton(
        master=frame1,
        text="Salir",
        width=200,
        height=30,
        command=salir
    )
    btnBuscar = CTkButton(
        master=frame1,
        text="Buscar",
        width=200,
        height=30,
        command=buscarCliente
    )
    entIP.grid(
        row=4,
        column=1,
        padx=10,
        pady=10
    )
    lbIP.grid(
        row=4,
        column=0,
        padx=10,
        pady=10
    )

    lbName.grid(
        row=0,
        column=0,
        pady=10,
        padx=10
    )
    entName.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )
    lbDireccion.grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )
    entDireccion.grid(
        row=0,
        column=3,
        padx=10,
        pady=10
    )
    lbTelefono.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    entTelefono.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )
    lbPaquete.grid(
        row=1,
        column=2,
        padx=10,
        pady=10
    )
    entVelocidad.grid(
        row=1,
        column=3,
        padx=10,
        pady=10
    )
    lbComunidad.grid(
        row=2,
        column=0,
        pady=10,
        padx=10
    )
    entComunidad.grid(
        row=2,
        column=1,
        padx=10,
        pady=10
    )
    lbMicrotikIp.grid(
        row=2,
        column=2,
        padx=10,
        pady=10
    )
    entIpMicrotik.grid(
        row=2,
        column=3,
        padx=10,
        pady=10
    )
    lbEquipos.grid(
        row=3,
        column=0,
        padx=10,
        pady=10
    )
    equiposOpctions.grid(
        row=3,
        column=1,
        padx=10,
        pady=10
    )
    lbMensualidad.grid(
        row=3,
        column=2,
        padx=10,
        pady=10
    )
    entMensualidad.grid(
        row=3,
        column=3,
        padx=10,
        pady=10
    )
    lbNota.place(
        relx=0.1,
        rely=0.4
    )
    nota.place(
        relx=0.1,
        rely=0.5
    )
    btnGuardar.place(
        relx=0.1,
        rely=0.9
    )
    btnBuscar.place(
        relx=0.4,
        rely=0.9
    )
    btnSalir.place(
        relx=0.7,
        rely=0.9
    )
    

    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
    relx=0.7,
    rely=0.0,
    relwidth=0.3,
    relheight=1.0
    )


def verPagos():
        
    
    def obtener_datos(filtro_reciente=False, filtro_mensualidad=False):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor(dictionary=True)
            if filtro_reciente:
                query = "SELECT * FROM pagos ORDER BY FechaPago DESC"
            elif filtro_mensualidad:
                query = "SELECT * FROM pagos ORDER BY Mensualidad DESC"
            else:
                query = "SELECT * FROM pagos"
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            conn.close()
            return rows
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []

    def actualizar_treeview(filtro_reciente=False, filtro_mensualidad=False):
        for item in tree.get_children():
            tree.delete(item)
        rows = obtener_datos(filtro_reciente, filtro_mensualidad)
        for row in rows:
            tree.insert("", "end", values=(row["id"], row["NombreCliente"], row["Mensualidad"], row["FechaPago"]))

    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Ver Pago")
    crearUsuarioWindow.geometry("1000x600")
    crearUsuarioWindow.resizable(False, False)

    imagenes = load_images()

    # Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

    recibo = CTkLabel(master=frame2, text="", image=imagenes["pago"])
    recibo.place(relx=0.2, rely=0.1)

    frame1.place(relx=0.0, rely=0.0, relwidth=0.7, relheight=1.0)
    frame2.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)

    # Crear el Treeview en frame1
    tree = ttk.Treeview(frame1, columns=("id", "NombreCliente", "Mensualidad", "FechaPago"), show='headings')
    tree.heading("id", text="No Recibo")
    tree.heading("NombreCliente", text="DNA")
    tree.heading("Mensualidad", text="Mensualidad")
    tree.heading("FechaPago", text="FechaPago")

    # Ajustar el ancho de las columnas
    tree.column("id", width=100)
    tree.column("NombreCliente", width=100)
    tree.column("Mensualidad", width=100)
    tree.column("FechaPago", width=100)

    tree.pack(fill=tk.BOTH, expand=True)

    # Crear un botón para filtrar los pagos más recientes
    btn_filtrar_recientes = CTkButton(master=frame2, text="Mostrar más recientes", command=lambda: actualizar_treeview(filtro_reciente=True))
    btn_filtrar_recientes.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    # Crear un botón para filtrar por mensualidad más alta
    btn_filtrar_mensualidad = CTkButton(master=frame2, text="Mensualidad más alta", command=lambda: actualizar_treeview(filtro_mensualidad=True))
    btn_filtrar_mensualidad.place(relx=0.5, rely=0.9, anchor=tk.CENTER)

    # Llenar el Treeview con los datos iniciales
    actualizar_treeview()

    crearUsuarioWindow.mainloop()


def funcion():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Crear Pago")
    crearUsuarioWindow.geometry("1000x600")
    crearUsuarioWindow.resizable(False, False)
    
    imagenes = load_images()

    #Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)

      

    def salir():
        crearUsuarioWindow.destroy()

    recibo = CTkLabel(master=frame2, text="", image=imagenes["pago"])
    recibo.pack()
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.5,
        rely=0.5
    )

    lbNombre = CTkLabel(
        master=frame1,
        text="Nombre",
        text_color=color_blanco,
        font=subtitulo,
    )
    entNombre = CTkEntry(
        master=frame1,
        placeholder_text="Martin Antonio",
        width=240,
        height=20,
    )

    lbId = CTkLabel(
        master=frame1,
        text="ID",
        text_color=color_blanco,
        font=subtitulo
    )
    entId = CTkEntry(
        master=frame1,
        placeholder_text="5",
        width=240,
        height=20
    )
    lbMonto = CTkLabel(
        master=frame1,
        text="Monto $",
        text_color=color_blanco,
        font=subtitulo
    )
    entMonto = CTkEntry(
        master=frame1,
        placeholder_text="300.45",
        width=240,
        height=20
    )
    lbFecha = CTkLabel(
        master=frame1,
        text="Fecha",
        text_color=color_blanco,
        font=subtitulo
        )
    lbAutomatico = CTkLabel(
        master=frame1,
        text="Generado Automaticamente",
        text_color=color_blanco,
        font=subtitulo
    )

    lbNota = CTkLabel(
        master=frame2,
        text="Notas",
        font=("Arial", 15)
    )
    nota = CTkTextbox(
        master=frame2,
        font=subtitulo,
        width=240,
        height=290
        )
    
    btnGuardar = CTkButton(
        master=frame1,
        text="Guardar",
        width=200,
        height=30
    )
    btnSalir = CTkButton(
        master=frame1,
        text="Salir",
        width=200,
        height=30,
        command=salir
    )

    lbNombre.grid(
        row=0,
        column=0,
        pady=10,
        padx=10
    )
    entNombre.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )
    lbId.grid(
        row=0,
        column=2,
        padx=10,
        pady=10
    )
    entId.grid(
        row=0,
        column=3,
        padx=10,
        pady=10
    )
    lbMonto.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    entMonto.grid(
        row=1,
        column=1,
        padx=10,
        pady=10
    )
    lbFecha.grid(
        row=1,
        column=2,
        padx=10,
        pady=10
    )
    lbAutomatico.grid(
        row=1,
        column=3,
        padx=10,
        pady=10
    )
    lbNota.place(
        relx=0.1,
        rely=0.4
    )
    nota.place(
        relx=0.1,
        rely=0.5
    )
    btnGuardar.place(
        relx=0.1,
        rely=0.9
    )
    btnSalir.place(
        relx=0.6,
        rely=0.9
    )

    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
    relx=0.7,
    rely=0.0,
    relwidth=0.3,
    relheight=1.0
    )


def insertar_pago(id_factura, fecha_pago, monto, metodo_pago):
    try:

        cursor = connect_db()
        sql = "INSERT INTO pagos (id_factura, fecha_pago, monto, metodo_pago) VALUES (%s, %s, %s, %s)"
        val = (id_factura, fecha_pago, monto, metodo_pago)
        cursor.execute(sql, val)
        connect_db.commit()
        cursor.close()
        connect_db.close()
        messagebox.showinfo("Éxito", "Datos guardados exitosamente")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al guardar los datos: {err}")


def crear_usuario_db(nombre, direccion, telefono, equipos, Ip, Velocidad, FechaInstalacion, ProximoPago, Mensualidad):
    try:
        db = connect_db()
        cursor = db.cursor()
        sql = "INSERT INTO clientes (Nombre, Direccion, Telefono, Equipos, Ip, Velocidad, FechaInstalacion, ProximoPago, Mensualidad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (nombre, direccion, telefono, equipos, Ip, Velocidad, FechaInstalacion, ProximoPago, Mensualidad)
        cursor.execute(sql, val)
        db.commit()
        cursor.close()
        db.close()
        messagebox.showinfo("Éxito", "Datos guardados exitosamente")
    except mysql.connector.Error as err:
        messagebox.showerror("Error", f"Error al guardar los datos: {err}")


def fetch_data():

    db = connect_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clientes")
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return data

def display_data(frame):
    # Create Treeview
    tree = ttk.Treeview(frame, columns=("ID", "Nombre", "Dirección", "Teléfono", "Equipos", "Ip", "Velocidad", "Fecha Instalacion", "Proximo Pago", "Mensualidad"), show='headings')
    tree.heading("ID", text="ID")
    tree.heading("Nombre", text="Nombre")
    tree.heading("Dirección", text="Dirección")
    tree.heading("Teléfono", text="Telefono")
    tree.heading("Equipos", text="Equipos")
    tree.heading("Ip", text="Ip")
    tree.heading("Velocidad", text="Velocidad")
    tree.heading("Fecha Instalacion", text="Fecha Instalacion")
    tree.heading("Proximo Pago", text="Proximo Pago")
    tree.heading("Mensualidad", text="Mensualidad")

    # Insert data into Treeview
    def refresh_data():
        for i in tree.get_children():
            tree.delete(i)
        data = fetch_data()
        for row in data:
            tree.insert("", "end", values=row)
    
    refresh_data()

    # Add right-click menu
    def do_popup(event):
        try:
            popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            popup.grab_release()
    
    popup = Menu(tree, tearoff=0)
    popup.add_command(label="Actualizar", command=refresh_data)
    
    tree.bind("<Button-3>", do_popup)
    
    # Configure Treeview layout
    tree.pack(expand=True, fill='both')


def buscarClienteEditar():
    crearUsuarioWindow = CTkToplevel(app)
    crearUsuarioWindow.title("Crear Recibo")
    crearUsuarioWindow.geometry("700x300")
    crearUsuarioWindow.resizable(False, False)

    imagenes = load_images()

    #Definimos los frames
    frame1 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_negro)
    frame2 = CTkFrame(master=crearUsuarioWindow, corner_radius=0, fg_color=color_azul)


    usuario = CTkLabel(master=frame2, text="", image=imagenes["editar"])
    fondo = CTkLabel(master=frame1, text="", image=imagenes["fondo"])
    fondo.place(
        relx=0.3,
        rely=0.3
    )

    btnGenerarPago = CTkButton(
        master=frame1,
        text="Crear Pago",
        width=200,
        height=20
    )

    lbIdFactura = CTkLabel(
        master=frame1,
        text="ID Factura",
        text_color=color_blanco,
        font=subtitulo
    )
    entFactura = CTkEntry(
        master=frame1,
        placeholder_text="9010294",
        width=340,
        height=20
    )
    lbIdFactura.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )
    entFactura.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    btnGenerarPago.place(
        relx=0.1,
        rely=0.9
    )


    usuario.pack()

    frame1.place(
        relx=0.0,
        rely=0.0,
        relwidth=0.7,
        relheight=1.0
    )
    frame2.place(
    relx=0.7,
    rely=0.0,
    relwidth=0.3,
    relheight=1.0
    )
    crearUsuarioWindow.mainloop() 


def generar_recibo(id_factura):
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM pagos WHERE id_factura = %s"
        cursor.execute(query, (id_factura,))
        pago = cursor.fetchone()

        if pago:
            # Datos del pago
            id_pago = pago['id_pago']
            id_factura = pago['id_factura']
            fecha_pago = pago['fecha_pago'].strftime('%d-%m-%Y')
            monto = pago['monto']
            metodo_pago = pago['metodo_pago']

            # Crear imagen de recibo más grande
            img = Image.new('RGB', (600, 400), color='white')
            d = ImageDraw.Draw(img)
            font = ImageFont.truetype('arial.ttf', 24)
            font_small = ImageFont.truetype('arial.ttf', 18)

            # Logo (reemplaza 'logo.png' por el nombre de tu archivo de logo)
            logo = Image.open('icons/agua.png')
            logo = logo.resize((150, 150))  # Redimensionar el logo si es necesario
            img.paste(logo, (20, 20))

            # Texto del recibo
            y_text = 180  # Posición Y inicial para el texto
            d.text((20, y_text), f"Recibo de Pago", font=font, fill='black')
            y_text += 40
            d.text((20, y_text), f"ID Pago: {id_pago}", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"ID Factura: {id_factura}", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"Fecha de Pago: {fecha_pago}", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"Monto: {monto} MX", font=font_small, fill='black')
            y_text += 30
            d.text((20, y_text), f"Método de Pago: {metodo_pago}", font=font_small, fill='black')

            # Guardar la imagen como un archivo
            img.save(f"recibo_{id_factura}.png")
            print(f"Recibo generado: recibo_{id_factura}.png")

        else:
            print("No se encontró un pago con ese ID de factura.")

        cursor.close()
        conn.close()

    except Error as e:
        print(f"Error al conectar con MySQL: {e}")
    except IOError as e:
        print(f"Error al abrir el archivo de logo: {e}")

def enDesarrollo():
    pregunta = messagebox.askyesno("Desarrollo", "Funcion en desarrollo version 0.2. Corrobora si tenemos un nuevo lanzamiento. Presiona yes")
    if pregunta == True:
        webbrowser.open("https://github.com/ricardoescobedo2003/doblenetDesktop/releases")

def crear_recibo_imagen(dna, nombre, fecha, monto, no_recibo, concepto, folio, id_transaccion, archivo_salida):
    # Crear una nueva imagen en blanco
    width, height = 600, 700
    imagen = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(imagen)
    
    # Cargar fuentes
    font_path = "arial.ttf"  # Ruta a la fuente Arial, ajustar según el entorno
    font_title = ImageFont.truetype(font_path, 24)
    font_subtitle = ImageFont.truetype(font_path, 20)
    font_text = ImageFont.truetype(font_path, 16)
    font_mono = ImageFont.truetype(font_path, 18)
    font_bold = ImageFont.truetype(font_path, 20)
    
    # Título
    draw.text((width / 2 - 170, 30), "RatonApp Wisplus", font=font_title, fill="black")
    
    # Línea punteada
    draw.line((20, 110, width - 20, 110), fill="black", width=2)
    draw.line((20, 114, width - 20, 114), fill="black", width=2)
    
    # Información del recibo
    draw.text((20, 130), f"FECHA    1    {fecha}", font=font_text, fill="black")
    
    # Caja de cobro de EBANX
    draw.rectangle([150, 160, 450, 200], outline="blue", width=2)
    draw.text((200, 170), "Cobro RatonApp", font=font_text, fill="black")
    
    # Información de pago
    draw.text((20, 250), f"NOMBRE DE {nombre}", font=font_text, fill="black")
    draw.text((20, 280), f"DNA #{dna}", font=font_text, fill="black")
    draw.text((20, 310), f"PAGADA EL DÍA {fecha} A LAS {datetime.datetime.now().strftime('%H:%M')}", font=font_text, fill="black")

    
    # Valor
    draw.text((width / 2 - 60, 350), f"VALOR ${monto}", font=font_bold, fill="black")
    
    # Línea punteada
    draw.line((20, 390, width - 20, 390), fill="black", width=2)
    draw.line((20, 394, width - 20, 394), fill="black", width=2)
    
    # Folio e ID
    draw.text((20, 410), f"Conecepto: {concepto}", font=font_text, fill="black")
    draw.text((20, 440), f"Proximo Pago: {no_recibo}", font=font_text, fill="black")
    
    # Nota de conservación
    draw.text((width / 2 - 120, 470), "*Conserva el comprobante*", font=font_text, fill="black")
    draw.text((width / 2 - 120, 500), "Software por Ricardo Escobedo", font=font_text, fill="black")



    
    # Guardar la imagen
    imagen.save(archivo_salida)
    messagebox.showinfo("Recibo", f"Recibo de pago guardado como {archivo_salida}")

def menuConfiguracionRed():
    menuConfiguracionRed = CTkToplevel(app)
    menuConfiguracionRed.title("Herramientas Red")
    menuConfiguracionRed.geometry("900x400")
    menuConfiguracionRed.resizable(False, False)

    images = load_images()


    frame2 = CTkFrame(master=menuConfiguracionRed, corner_radius=0, fg_color=color_azul)
    recibo = CTkLabel(master=frame2, text="", image=images["configuracion-red"])

    recibo.place(relx=0.2, rely=0.2)    
    frame2.place(relx=0.7, rely=0.0, relwidth=0.3, relheight=1.0)


    btnCambiarVelocidad = CTkButton(
        master=menuConfiguracionRed,
        text="Cambio de velocidad",
        width=150,
        height=20,
        image=images["radar-de-velocidad"],
        command=enDesarrollo
    )
    btnCambiarVelocidad.grid(
        row=0,
        column=0,
        padx=10,
        pady=10
    )
    btnDesbloquearCliente = CTkButton(
        master=menuConfiguracionRed,
        text="Desbloquear Cliente",
        width=150,
        height=20,
        image=images["desbloqueado"],
        command=enDesarrollo
    )
    btnDesbloquearCliente.grid(
        row=0,
        column=1,
        padx=10,
        pady=10
    )
    btnReiniciar = CTkButton(
        master=menuConfiguracionRed,
        text="Reiniciar Microtik",
        width=170,
        height=20,
        image=images["reiniciar"],
        command=enDesarrollo
    )
    btnReiniciar.grid(
        row=1,
        column=0,
        padx=10,
        pady=10
    )
    menuConfiguracionRed.mainloop()

# DEFINIMOS LOS BOTONES DE ACCION DENTRO DEL BANNER
crear_usuarioBtn = CTkButton(
    master=banner,
    text="Crear Persona",
    image=images["crear_usuario"],
    command=crearUsuario
)
crear_pago_btn = CTkButton(
    master=banner,
    text="Crear Pago",
    image=images["metodo_de_pago"],
    command=registrarPago
)

ver_pago_btn = CTkButton(
    master=banner,
    text="Ver Pagos",
    image=images["ver_pagos"],
    command=verPagos
)

crear_recibo_btn = CTkButton(
    master=banner,
    text="Herramientas Red",
    image=images["herramientas"],
    command=menuConfiguracionRed
)

configuracion = CTkButton(
    master=banner,
    text="Ajustes",
    image=images["configuraciones"],
    command=enDesarrollo
)

# DEFINIMOS LAS POSICIONES DE LOS WIDGETS
banner.place(
    relx=0.0,
    rely=0.0,
    relwidth=1.0,
    relheight=0.1
)
centro.place(
    relx=0.1,
    rely=0.2,
    relwidth=0.8,
    relheight=0.7
)

agua_logo_lb.place(
    relx=0.0,
    rely=0.0)

crear_usuarioBtn.place(
    relx=0.1,
    rely=0.1
)
crear_pago_btn.place(
    relx=0.3,
    rely=0.1
)
ver_pago_btn.place(
    relx=0.5,
    rely=0.1
)
crear_recibo_btn.place(
    relx=0.7,
    rely=0.1
)
configuracion.place(
    relx=0.9,
    rely=0.1
)

# Mostrar datos en el frame "centro"
display_data(centro)

app.mainloop()
