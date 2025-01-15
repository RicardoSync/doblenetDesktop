from customtkinter import CTkEntry, CTkButton, CTkFrame, CTkTabview, CTkToplevel, CTkLabel
from insert import insertarCliente
from tkinter import messagebox

def agregarCliente():
    nuevoCliente  = CTkToplevel()
    nuevoCliente.title("Nuevo cliente")
    nuevoCliente.geometry("700x600")
    nuevoCliente.resizable(False, False)
    nuevoCliente._set_appearance_mode("dark")

    #funcion de insertar
    def obtenerDatos():
        nombre = nombreEntry.get()
        apellido = apellidoEntry.get()
        direccion = direccionEntry.get()
        telefono = telefonoEntry.get()
        email = emailEntry.get()

        if len(nombre)>0:
            insertarCliente(nombre, apellido, direccion, telefono, email)
        else:
            messagebox.showerror("DOBLENET", "No podemos almacenar un cliente con el nombre vacio.")
    
    def cancelar():
        nuevoCliente.destroy()
    

    #banner titulo
    banner = CTkFrame(nuevoCliente, border_width=2, corner_radius=10)
    titulo = CTkLabel(banner, text="Registro nuevo cliente", font=("Monospace", 22, "bold"))
    btnGuardar = CTkButton(banner, text="Guardar", border_width=2, corner_radius=10, command=obtenerDatos)
    btnCancelar = CTkButton(banner, text="Cancelar", border_width=2, corner_radius=10, command=cancelar)

    #contenedor de elementos
    contenedorElementos = CTkFrame(nuevoCliente, border_width=2, corner_radius=10)
    nombreEntry = CTkEntry(contenedorElementos, placeholder_text="Nombre del cliente", border_width=2, corner_radius=10, width=320)
    apellidoEntry = CTkEntry(contenedorElementos, placeholder_text="Apellido del cliente", border_width=2, corner_radius=10, width=320)
    direccionEntry = CTkEntry(contenedorElementos, placeholder_text="Direccion del cliente", border_width=2, corner_radius=10,width=320 )
    telefonoEntry = CTkEntry(contenedorElementos, placeholder_text="Telefono del cliente", border_width=2, corner_radius=10, width=320)
    emailEntry = CTkEntry(contenedorElementos, placeholder_text="Email del cliente", border_width=2, corner_radius=10, width=320)

    #etiquetas
    nombreLabel = CTkLabel(contenedorElementos, text="Nombre Cliente", font=("Arial", 15, "bold"))
    apellidoLabel = CTkLabel(contenedorElementos, text="Apellido Cliente", font=("Arial", 15, "bold"))
    direccionLabel = CTkLabel(contenedorElementos, text="Direccion Cliente", font=("Arial", 15, "bold"))
    telefonoLabel = CTkLabel(contenedorElementos, text="Telefono Cliente", font=("Arial", 15, "bold"))
    emailLabel = CTkLabel(contenedorElementos, text="Email Cliente", font=("Arial", 15, "bold"))


    #posicion de los elementos
    banner.place(relx=0.0, rely=0.0, relwidth=1.0, relheight=0.1)
    titulo.grid(column=0, row=0, padx=10, pady=15)
    btnGuardar.grid(column=1, row=0, padx=10, pady=15)
    btnCancelar.grid(column=2, row=0, padx=10, pady=15)
    
    contenedorElementos.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)
    nombreLabel.grid(column=0, row=0, padx=10, pady=10)
    nombreEntry.grid(column=1, row=0, padx=10, pady=10)

    apellidoLabel.grid(column=0, row=1, padx=10, pady=10)
    apellidoEntry.grid(column=1, row=1, padx=10, pady=10)

    direccionLabel.grid(column=0, row=2, padx=10, pady=10)
    direccionEntry.grid(column=1, row=2, padx=10, pady=10)

    telefonoLabel.grid(column=0, row=3, padx=10, pady=10)
    telefonoEntry.grid(column=1, row=3, padx=10, pady=10)

    emailLabel.grid(column=0, row=4, padx=10, pady=10)
    emailEntry.grid(column=1, row=4, padx=10, pady=10)

    nuevoCliente.mainloop()