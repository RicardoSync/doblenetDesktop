from customtkinter import CTk, CTkEntry, CTkFrame, CTkButton, CTkTabview, CTkLabel
from CTkTable import *
from tkinter import ttk


from db_consultas import consultaPaquetes, consultarPagos, consultarClientes, consultarEquipos


def panelControl(user, database):
    windows = CTk()
    windows.title(f"Panel de control {user}")
    windows.geometry("1280x800")
    windows._set_appearance_mode("dark")

    #creamos el banner principal
    banner = CTkFrame(windows, border_width=2, corner_radius=10)
    saludoLabel = CTkLabel(banner, text=f"Bienvenido de nuevo {user}", font=("Monospace", 25, "bold"))
    btnUsuarios = CTkButton(banner, text="Usuarios", border_width=2, corner_radius=10)
    btnServidor = CTkButton(banner, text="Servidor", border_width=2, corner_radius=10)
    btnInformacion = CTkButton(banner, text="Informacion", border_width=2, corner_radius=10)



    #creamos las pestanias
    navegacionPestanias = CTkTabview(windows, border_width=2, corner_radius=10)
    navegacionPestanias.add("Paquetes")
    navegacionPestanias.add("Equipos")
    navegacionPestanias.add("Pagos")
    navegacionPestanias.add("Clientes")

    def paquetesNavegacion():
        bannerPaquetes = CTkFrame(navegacionPestanias.tab("Paquetes"), border_width=2, corner_radius=10)
        paqueteID = CTkEntry(navegacionPestanias.tab("Paquetes"), border_width=2, corner_radius=10,placeholder_text="Nombre del paquete", width=400)
        btnBuscar = CTkButton(navegacionPestanias.tab("Paquetes"), border_width=2, corner_radius=10, text="Buscar Paquete", width=100)
        btnAgregar = CTkButton(navegacionPestanias.tab("Paquetes"), border_width=2, corner_radius=10, text="Agregar Paquete", width=100)

        contenedorTabla = CTkFrame(navegacionPestanias.tab("Paquetes"), border_width=2, corner_radius=25)

        #cargamos los datos
        datosPaquetes = consultaPaquetes()

        #creacion de la tabla
        encabezado = ["Nombre", "Velocidad", "Precio"]
        encabezado_datos = [encabezado] + list(datosPaquetes)


        num_filas = len(encabezado_datos)
        num_column = len(encabezado)

        tablaPaquetes = CTkTable(
            master=contenedorTabla,
            row=num_filas,
            column=num_column,
            values=encabezado_datos
        )

        #posicion de los submenus
        bannerPaquetes.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
        paqueteID.grid(column=0, row=0, padx=10, pady=20)
        btnBuscar.grid(column=1, row=0, padx=10, pady=20)
        btnAgregar.grid(column=2, row=0, padx=10, pady=20)

        contenedorTabla.place(relx=0.0, rely=0.2, relwidth=1.0, relheight=0.7)
        tablaPaquetes.pack(expand=True, fill="both")

    def pagosNavegacion():
        bannerPagos = CTkFrame(navegacionPestanias.tab("Pagos"), border_width=2, corner_radius=10)
        pagosID = CTkEntry(navegacionPestanias.tab("Pagos"), border_width=2, corner_radius=10,placeholder_text="Nombre del cliente", width=400)
        btnBuscarPago = CTkButton(navegacionPestanias.tab("Pagos"), border_width=2, corner_radius=10, text="Buscar Pagos", width=100)
        btnAgregarPago = CTkButton(navegacionPestanias.tab("Pagos"), border_width=2, corner_radius=10, text="Agregar Pago", width=100)
        busquedaFiltro = CTkEntry(navegacionPestanias.tab("Pagos"), placeholder_text="17-12-2024", border_width=2, corner_radius=10, width=400)
        btnFiltro = CTkButton(navegacionPestanias.tab("Pagos"), border_width=2, corner_radius=10, text="Busqueda Filtrada")

        contenedorTabla = CTkFrame(navegacionPestanias.tab("Pagos"), border_width=2, corner_radius=25)

        #cargamos los datos
        datosPaquetes = consultarPagos()

        #creacion de la tabla
        encabezado = ["Nombre", "Plan", "Mensualidad", "Ultimo Pago", "Proximo Pago", "Cambio"]
        encabezado_datos = [encabezado] + list(datosPaquetes)


        num_filas = len(encabezado_datos)
        num_column = len(encabezado)

        tablaPagos = CTkTable(
            master=contenedorTabla,
            row=num_filas,
            column=num_column,
            values=encabezado_datos
        )

        #posicion de los submenus
        bannerPagos.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
        pagosID.grid(column=0, row=0, padx=10, pady=20)
        btnBuscarPago.grid(column=1, row=0, padx=10, pady=20)
        btnAgregarPago.grid(column=2, row=0, padx=10, pady=20)
        busquedaFiltro.grid(column=3, row=0, padx=10, pady=20)
        btnFiltro.grid(column=4, row=0, padx=10, pady=20)
        contenedorTabla.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
        tablaPagos.pack(expand=True, fill="both")

    def clientesNavegacion():
        bannerClientes = CTkFrame(navegacionPestanias.tab("Clientes"), border_width=2, corner_radius=10)
        nombreID = CTkEntry(navegacionPestanias.tab("Clientes"), border_width=2, corner_radius=10,placeholder_text="Nombre del cliente", width=400)
        btnBuscarCliente = CTkButton(navegacionPestanias.tab("Clientes"), border_width=2, corner_radius=10, text="Buscar Cliente", width=100)
        btnAgregarCliente = CTkButton(navegacionPestanias.tab("Clientes"), border_width=2, corner_radius=10, text="Agregar Cliente", width=100)

        contenedorTabla = CTkFrame(navegacionPestanias.tab("Clientes"), border_width=2, corner_radius=25)

        #cargamos los datos
        datosClientes = consultarClientes()

        #creacion de la tabla
        encabezado = ["Nombre", "Direccion", "Telefono", "Paquete", "Proximo Pago", "Estado"]
        encabezado_datos = [encabezado] + list(datosClientes)


        num_filas = len(encabezado_datos)
        num_column = len(encabezado)

        tablaPagos = CTkTable(
            master=contenedorTabla,
            row=num_filas,
            column=num_column,
            values=encabezado_datos
        )

        #posicion de los submenus
        bannerClientes.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
        nombreID.grid(column=0, row=0, padx=10, pady=20)
        btnBuscarCliente.grid(column=1, row=0, padx=10, pady=20)
        btnAgregarCliente.grid(column=2, row=0, padx=10, pady=20)

        contenedorTabla.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
        tablaPagos.pack(expand=True, fill="both")

    def equiposNavegacion():
        bannerEquipos = CTkFrame(navegacionPestanias.tab("Equipos"), border_width=2, corner_radius=10)
        nombreEquipoID = CTkEntry(navegacionPestanias.tab("Equipos"), border_width=2, corner_radius=10,placeholder_text="Nombre del equipo", width=400)
        btnBuscarEquipo = CTkButton(navegacionPestanias.tab("Equipos"), border_width=2, corner_radius=10, text="Buscar Equipo", width=100)
        btnAgregarEquipo = CTkButton(navegacionPestanias.tab("Equipos"), border_width=2, corner_radius=10, text="Agregar Equipo", width=100)

        contenedorTabla = CTkFrame(navegacionPestanias.tab("Equipos"), border_width=2, corner_radius=25)

        #cargamos los datos
        datosEquipos = consultarEquipos()

        #creacion de la tabla
        encabezado = ["Nombre", "Modelo", "Descripcion"]
        encabezado_datos = [encabezado] + list(datosEquipos)


        num_filas = len(encabezado_datos)
        num_column = len(encabezado)

        tablaPagos = CTkTable(
            master=contenedorTabla,
            row=num_filas,
            column=num_column,
            values=encabezado_datos
        )

        #posicion de los submenus
        bannerEquipos.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
        nombreEquipoID.grid(column=0, row=0, padx=10, pady=20)
        btnBuscarEquipo.grid(column=1, row=0, padx=10, pady=20)
        btnAgregarEquipo.grid(column=2, row=0, padx=10, pady=20)

        contenedorTabla.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
        tablaPagos.pack(expand=True, fill="both")



    #posicion de los elementos
    banner.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    saludoLabel.grid(column=0, row=0, padx=10, pady=20)
    btnUsuarios.grid(column=1, row=0, padx=10, pady=20)
    btnServidor.grid(column=2, row=0, padx=10, pady=20)
    btnInformacion.grid(column=3, row=0, padx=10, pady=20)

    #posicion de la navegaciosn
    navegacionPestanias.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)

    #llamamos las funciones de las pestanias
    paquetesNavegacion()
    pagosNavegacion()
    clientesNavegacion()
    equiposNavegacion()
    windows.mainloop()


panelControl(user="doblenet", database="doblenet")