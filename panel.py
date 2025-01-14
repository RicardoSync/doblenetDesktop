from customtkinter import CTkEntry, CTkButton, CTkFrame, CTkTabview, CTk, CTkLabel
from tkinter import ttk
from consultas import consultarClientes

# Función para cargar los datos en el Treeview
def cargar_clientes(tablaClientes):
    # Eliminar elementos existentes en la tabla
    for item in tablaClientes.get_children():
        tablaClientes.delete(item)
    # Obtener clientes desde la base de datos
    clientes = consultarClientes()
    # Insertar datos en la tabla
    for datos in clientes:
        tablaClientes.insert("", "end", values=datos)

def panelControl(user):
    windows = CTk()
    windows.title(f"Panel de Control - DOBLENET")
    windows.geometry("1280x800")
    windows.resizable(False, False)
    windows._set_appearance_mode("dark")


    #banner de bienvenidaa
    banner = CTkFrame(windows, border_width=2, corner_radius=10)
    welcomeLabel = CTkLabel(banner, text=f"Bienvenido de nuevo {user}", font=("Monospace", 25, "bold"))


    #tab view con los elementos clientes, pagos, equipos, planes
    navegacionTab = CTkTabview(windows, border_width=2, corner_radius=10)
    navegacionTab.add("Home")
    navegacionTab.add("Clientes")
    navegacionTab.add("Pagos")
    navegacionTab.add("Equipos")
    navegacionTab.add("Planes")


    #elementos de UIX cleintes
    def clientesNavegacion():
        bannerNabegacion = CTkFrame(navegacionTab.tab("Clientes"), border_width=2, corner_radius=10)
        idEntry = CTkEntry(bannerNabegacion, placeholder_text="Nombre del cliente", border_width=2, corner_radius=10, width=340)
        btnBuscar = CTkButton(bannerNabegacion, text="Buscar cliente", border_width=2, corner_radius=10)
        btnAgregar = CTkButton(bannerNabegacion, text="Agregar cliente", border_width=2, corner_radius=10)

        # Configuración de la tabla de clientes
        tablaClientes = ttk.Treeview(
            master=navegacionTab.tab("Clientes"),
            columns=("Nombre", "Apellido", "Direccion", "Telefono", "Email"),
            show="headings"
        )

        # Configurar encabezados
        for col in ("Nombre", "Apellido", "Direccion", "Telefono", "Email"):
            tablaClientes.heading(col, text=col)


        def refrescarTabla():
            cargar_clientes(tablaClientes)
        
        bannerNabegacion.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
        idEntry.grid(column=0, row=0, padx=10, pady=20)
        btnBuscar.grid(column=1, row=0, padx=10, pady=20)
        btnAgregar.grid(column=2, row=0, padx=10, pady=20)
        tablaClientes.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
        refrescarTabla()
        btnActualizar = CTkButton(bannerNabegacion, text="Refrescar", border_width=2, corner_radius=10, command=refrescarTabla)
        btnActualizar.grid(column=3, row=0, padx=10, pady=10)

        
    #posicion de los elementos
    banner.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    welcomeLabel.pack(padx=10, pady=10)
    navegacionTab.place(relx=0.0, rely=0.1, relwidth=1.0, relheight=0.9)
    clientesNavegacion()
    windows.mainloop()