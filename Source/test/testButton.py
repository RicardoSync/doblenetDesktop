import customtkinter as ctk

# Función para mostrar/ocultar el frame con opciones adicionales
def toggle_options():
    if opciones_frame.winfo_viewable():
        opciones_frame.grid_remove()
    else:
        opciones_frame.grid()

# Crear la ventana principal
root = ctk.CTk()

# Crear el banner (puedes ajustar esto según tu diseño)
banner = ctk.CTkFrame(root)
banner.pack(pady=20)

# Definir las imágenes (asegúrate de que las imágenes estén cargadas correctamente)
images = {"herramientas": ctk.CTkImage(file="path_to_your_image.png")}  # Actualiza el path a la imagen correcta

# Crear el botón
crear_recibo_btn = ctk.CTkButton(
    master=banner,
    text="Herramientas Red",
    image=images["herramientas"],
    command=toggle_options  # Asigna la función toggle_options al comando del botón
)
crear_recibo_btn.pack(pady=10)

# Crear el frame que contendrá las opciones adicionales
opciones_frame = ctk.CTkFrame(root)
opciones_frame.pack(pady=20)

# Agregar opciones al frame
opcion1_btn = ctk.CTkButton(opciones_frame, text="Opción 1", command=lambda: print("Opción 1 seleccionada"))
opcion1_btn.pack(pady=5)

opcion2_btn = ctk.CTkButton(opciones_frame, text="Opción 2", command=lambda: print("Opción 2 seleccionada"))
opcion2_btn.pack(pady=5)

opcion3_btn = ctk.CTkButton(opciones_frame, text="Opción 3", command=lambda: print("Opción 3 seleccionada"))
opcion3_btn.pack(pady=5)

# Inicialmente ocultar el frame de opciones adicionales
opciones_frame.grid_remove()

# Iniciar el loop principal de la aplicación
root.mainloop()
