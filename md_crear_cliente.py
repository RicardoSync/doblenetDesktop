from customtkinter import CTkEntry, CTkButton, CTkFrame, CTkTabview, CTkToplevel, CTkLabel



def agregarCliente():
    nuevoCliente  = CTkToplevel()
    nuevoCliente.title("Nuevo cliente")
    nuevoCliente.geometry("1280x500")
    nuevoCliente.resizable(False, False)
    nuevoCliente._set_appearance_mode("dark")


    nuevoCliente.mainloop()