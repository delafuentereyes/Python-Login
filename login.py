from tkinter import *
from tkinter import messagebox


def ventanaPrincipal(): #ventana para elegir entre login o registrarse 
    global root
    root = Tk()
    root.geometry("300x300")
    root.title("Login")
    Label(root, text="Escoja una opcion", width="300",height="2", font=("calibri",12),bg="Lightgreen").pack()
    Label(root,text="").pack()
    Button(root,text="Login",width="30",height="2", command=login,bg="Lightblue").pack()
    Label(root,text="").pack()
    Button(root,text="Registro",width="30",height="2", command=registro,bg="Lightblue").pack()
    Label(root,text="").pack()
    Button(root,text="Administrador",width="30",height="2",command=admin,bg="Lightblue").pack
    root.mainloop()


def login(): #ventana para iniciar sesion
    global ventana_login
    ventana_login = Toplevel(root)
    ventana_login.title("Ventana Login")
    ventana_login.geometry("400x400")
    Label(ventana_login, text="Digite los datos para el login").pack()
    Label(ventana_login,text="").pack()
    global verifica_usuario
    global verifica_clave
    verifica_usuario = StringVar()
    verifica_clave = StringVar()
    global entrada_login_usuario
    global entrada_login_clave
    Label(ventana_login, text="Nombre usaurio (requerido)").pack()
    entrada_login_usuario = Entry(ventana_login,textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_login,text="").pack()

    Label(ventana_login, text="Contraseña").pack()
    entrada_login_clave = Entry(ventana_login,textvariable=verifica_clave,show="*")
    #entrada_login_clave.config(show="*")
    entrada_login_clave.pack()
    Label(ventana_login,text="").pack()

    global cambio_contrasenna
    cambio_contrasenna = StringVar()
    Button(ventana_login, text="Acceder",width="10",height="2",command=verifique_login).pack()
    Label(ventana_login,text="").pack()
    Button(ventana_login, text="Contraseña",width="10",height="2",command=cambio_contrasenna).pack()

    global ver_usuarios
    ver_usuarios = []
    Button(ventana_login, text="Usuarios",width="10",height="2",command=ver_usuarios).pack()
    Label(ventana_login,text="").pack()


usuarios = {}

def registro(): #ventana de registro
    global ventana_registro
    ventana_registro = Toplevel(root)
    ventana_registro.geometry("300x300")
    Label(ventana_registro, text="Complete los campos para el registro").pack()
    Label(ventana_registro,text="").pack()
    global nombre_usuario
    global clave
    global entrada_usuario
    global entrada_clave

    nombre_usuario = StringVar()
    clave = StringVar()

    Label(ventana_registro, text="Nombre usaurio (requerido)").pack()
    entrada_usuario = Entry(ventana_registro,textvariable=nombre_usuario)
    entrada_usuario.pack()
    Label(ventana_registro,text="").pack()

    Label(ventana_registro, text="Digite la contraseña").pack()
    entrada_clave = Entry(ventana_registro,textvariable=clave, show="*")
    entrada_clave.pack()
    Label(ventana_registro,text="").pack()

    Label(ventana_registro,text="").pack()
    Button(ventana_registro, text="Acceder",width="10",height="2",command=registro_usuario).pack()



    
def verifique_login():
    if entrada_login_usuario.get() in usuarios and entrada_login_clave.get() in usuarios.values():
        messagebox.showinfo(message="Acceso correcto", title="Mensaje")
    else:
        messagebox.showwarning(message="Acceso incorrecto", title="Mensaje")
        

def registro_usuario():
    usuarios[entrada_usuario.get()] = entrada_clave.get()
    ventana_registro.destroy()


def lista_usuarios():
    global ventana_usuarios
    ventana_usuarios = Toplevel()
    ventana_usuarios.geometry("300x300")
    ventana_usuarios.title("Lista de usuarios registrados")
    Label(ventana_usuarios,text="Usuarios").pack()
    usuarios = {}
    ventana_usuarios.mainloop()

def contrasenna():
    global ventana_contrasenna
    ventana_contrasenna = Toplevel()
    ventana_contrasenna.geometry("300x300")
    ventana_contrasenna.tittle("Cambio de contraseña") 
    Label(ventana_contrasenna, text="Digite los datos").pack()
    Label(ventana_contrasenna, text="").pack()
    
    verifica_usuario = StringVar()
    Label(ventana_contrasenna,text="Nombre de usuario").pack()
    entrada_login_usuario = Entry(ventana_contrasenna,textvariable=verifica_usuario)
    entrada_login_usuario.pack()
    Label(ventana_contrasenna,text="").pack()
    ventana_contrasenna.mainloop()

def admin():
    if entrada_usuario.get() in usuarios and entrada_login_clave.get() in usuarios.values():
        ventana_admin = Tk()
        ventana_admin.geometry("300x300")
        ventana_admin.title("Administrador")
        Button(ventana_admin, text="Salir",width="10",height="2",command=registro_usuario).pack()
        ventana_admin.destroy()



    ventana.config(menu=menuprincipal)
    archivo = Menu(menuprincipal, tearoff=0)
    menuprincipal.add_cascade(label="Archivo",menu=archivo)
    archivo.add_command(label="Salir")



ventanaPrincipal()