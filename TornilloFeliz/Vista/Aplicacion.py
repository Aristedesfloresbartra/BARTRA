from tkinter import ttk
from tkinter import *
import pyperclip as seleccionar
from tkinter import messagebox as msg
from Controlador.controlUsuarios import *
from Controlador.controlProductos import *
from Controlador.controlVentas import *

class aplicacion(ttk.Frame):
    
    def __init__(self,ventana):
        self.ventana = ventana
        self.ventana.geometry("900x560")
        self.ventana.config(bg=("#34495E"))
        self.ventana.title("Ferreteria el tornillo feliz")
        self.ventana.resizable(False,False)
        self.propiedadesLoginAndRegister()
        self.comprarAtributos()

        self.Frames()
        self.EtiquetasLogin()
        self.EtiquetasRegistro()

#-----------FRAMES PRINCIPAL------------------------

    def Frames(self):
        self.frameLogin = Frame(self.ventana,highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameLogin.config(relief=RAISED,bd=1,bg=("#34495E"),borde=1)
        self.frameLogin.pack(expand=True,side=LEFT,fill=BOTH,padx=0,pady=0)

        self.frameRegistro = Frame(self.ventana, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameRegistro.config(relief=RAISED,bd=1,bg=("#34495E"),borde=1)
        self.frameRegistro.pack(expand=True,side=RIGHT,fill=BOTH,padx=0,pady=0)

    def EtiquetasLogin(self):
        self.Login = Label(self.frameLogin,text="Login")
        self.Login.config(bg=("#34495E"),fg="white",font=("arial black",30))
        self.Login.pack(padx=0,pady=15)

        self.Linea1 = Label(self.frameLogin,text="--------------------------------------------------------------")
        self.Linea1.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea1.pack(padx=0,pady=0)

        self.lblUsuario = Label(self.frameLogin,text="Usuario")
        self.lblUsuario.config(bg=("#34495E"),fg="white",font=("arial black",13))
        self.lblUsuario.pack(padx=0,pady=10)

        self.txtUsuarioLogin = Entry(self.frameLogin,textvariable=self.usuarioLo)
        self.txtUsuarioLogin.config(relief=FLAT,font=("arial",13),justify=CENTER,bg="#E8EEF5")
        self.txtUsuarioLogin.pack(padx=0,pady=0,ipadx=25,ipady=4)

        self.lblClave = Label(self.frameLogin,text="Contraseña")
        self.lblClave.config(bg=("#34495E"),fg="white",font=("arial black",13))
        self.lblClave.pack(padx=0,pady=10)

        self.txtClaveLogin = Entry(self.frameLogin,textvariable=self.claveLo)
        self.txtClaveLogin.config(show="●",relief=FLAT,font=("arial",13),justify=CENTER,bg="#E8EEF5")
        self.txtClaveLogin.pack(padx=0,pady=0,ipadx=25,ipady=4)


        self.btnIniciar = Button(self.frameLogin,text="Iniciar session",command=self.iniciarSesion)
        self.btnIniciar.config(relief=FLAT,font=("arial black",11),bg=("#546F8A"),fg="black")
        self.btnIniciar.config(activebackground="#A1ACB7",bd=0)
        self.btnIniciar.pack(padx=0,pady=40,ipadx=50,ipady=4)

        self.space1 = Label(self.frameLogin,text="")
        self.space1.config(bg=("#34495E"),fg="white",font=("arial black",10))
        self.space1.pack(padx=0,pady=20)

        self.git = Label(self.frameLogin,text="""Codigo:                                               
             https://github.com/Aristedesfloresbartra/BARTRA""")
        self.git.config(bg=("#34495E"),fg="#D8E3EE",font=("arial",10))
        self.git.pack(padx=0,pady=0)

        self.btnCopiar = Button(self.frameLogin,text="Copiar link",command=self.CopiarLink)
        self.btnCopiar.config(relief=FLAT,font=("arial",9),bg=("#34495E"),fg="#E53A2C")
        self.btnCopiar.config(activebackground="#85929E",bd=0)
        self.btnCopiar.pack(side=LEFT,padx=130,pady=0)

    def EtiquetasRegistro(self):
        self.Registro = Label(self.frameRegistro,text="Register")
        self.Registro.config(bg=("#34495E"),fg="white",font=("arial black",27))
        self.Registro.pack(padx=0,pady=15)

        self.Linea2 = Label(self.frameRegistro,text="--------------------------------------------------------------")
        self.Linea2.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea2.pack(padx=0,pady=0)

        self.lblUsuarioRegsiter = Label(self.frameRegistro,text="Usuario")
        self.lblUsuarioRegsiter.config(bg=("#34495E"),fg="white",font=("arial black",11))
        self.lblUsuarioRegsiter.pack(padx=0,pady=10)

        self.txtUsuarioRegis = Entry(self.frameRegistro,textvariable=self.usuarioRe)
        self.txtUsuarioRegis.config(relief=FLAT,font=("arial",13),justify=CENTER,bg="#E8EEF5")
        self.txtUsuarioRegis.pack(padx=0,pady=0,ipadx=30,ipady=4)

        self.lblEmail = Label(self.frameRegistro,text="Correo electronico")
        self.lblEmail.config(bg=("#34495E"),fg="white",font=("arial black",11))
        self.lblEmail.pack(padx=0,pady=10)

        self.txtEmail = Entry(self.frameRegistro,textvariable=self.emailRe)
        self.txtEmail.config(relief=FLAT,font=("arial",13),justify=CENTER,bg="#E8EEF5")
        self.txtEmail.pack(padx=0,pady=0,ipadx=30,ipady=4)

        self.lblClaveRe = Label(self.frameRegistro,text="Contraseña")
        self.lblClaveRe.config(bg=("#34495E"),fg="white",font=("arial black",11))
        self.lblClaveRe.pack(padx=0,pady=10)

        self.txtClaveRegistro = Entry(self.frameRegistro,textvariable=self.claveRe)
        self.txtClaveRegistro.config(show="●",relief=FLAT,font=("arial",13),justify=CENTER,bg="#E8EEF5")
        self.txtClaveRegistro.pack(padx=0,pady=0,ipadx=30,ipady=4)

        self.lblClaveReConfirmar = Label(self.frameRegistro,text="Confirmar contraseña")
        self.lblClaveReConfirmar.config(bg=("#34495E"),fg="white",font=("arial black",11))
        self.lblClaveReConfirmar.pack(padx=0,pady=10)

        self.txtClaveRegistroConfirmar = Entry(self.frameRegistro,textvariable=self.claveConfirmar)
        self.txtClaveRegistroConfirmar.config(show="●",relief=FLAT,font=("arial",13),justify=CENTER,bg="#E8EEF5")
        self.txtClaveRegistroConfirmar.pack(padx=0,pady=0,ipadx=30,ipady=4)

        self.btnRegistrar = Button(self.frameRegistro,text="Registrarse",command=self.registrarse)
        self.btnRegistrar.config(relief=FLAT,font=("arial black",12),bg=("#546F8A"),fg="black")
        self.btnRegistrar.config(activebackground="#A1ACB7",bd=0)
        self.btnRegistrar.pack(padx=0,pady=30,ipadx=64,ipady=8)
#---------------------------------------------------


#--------------WIDGETS-----------------------------
    def toplabel(self):
        self.ventana.withdraw()#Ocultar ventana de login

        self.ventana_inicio = Toplevel()
        self.ventana_inicio.geometry("1050x400")
        self.ventana_inicio.config(bg="#34495E")
        self.ventana_inicio.resizable(False,False)
        self.propiedades()

        self.framesTop()
        self.cajaBuscar()
        self.treeview()
        self.labelFrame()
        self.btnAcciones()



        #---------------Frame-------------------------

    def framesTop(self):

        self.frame1 = Frame(self.ventana_inicio,highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frame1.config(relief=RAISED,bd=1,bg=("#34495E"),borde=0)
        self.frame1.pack(expand=True,side=LEFT,fill=BOTH,padx=5,pady=5)

        self.frame2 = Frame(self.ventana_inicio, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frame2.config(relief=RAISED,bd=1,bg=("#34495E"),borde=0)
        self.frame2.pack(expand=True,side=RIGHT,fill=BOTH,padx=5,pady=5)

        #------------FRAMES DENTRO DEL FRAME 1 --------------------------
        self.frameBuscar = Frame(self.frame1, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameBuscar.config(relief=RAISED,bd=1,bg=("#34495E"),borde=0)
        self.frameBuscar.pack(expand=True,fill=BOTH,padx=5,pady=5,ipadx=0,ipady=10)

        #------------------------------------------------------------------
        #------------Frame englobado--------------------------------------
        self.frameEnglob = Frame(self.frameBuscar, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameEnglob.config(relief=RAISED,bd=1,bg=("#34495E"),borde=0)
        self.frameEnglob.pack(expand=True,fill=BOTH,padx=5,pady=5,ipadx=0,ipady=0)
    
        self.frameAcciones1 = Frame(self.frame2, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameAcciones1.config(relief=RAISED,bd=1,bg=("green"),borde=0)
        self.frameAcciones1.pack(expand=True,fill=BOTH,padx=5,pady=5,ipadx=0,ipady=0)

        self.frameAcciones2 = Frame(self.frame2, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameAcciones2.config(relief=RAISED,bd=1,bg=("red"),borde=0)
        self.frameAcciones2.pack(expand=True,fill=BOTH,padx=5,pady=5,ipadx=0,ipady=0)

        self.frameAcciones3 = Frame(self.frameAcciones1, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameAcciones3.config(relief=RAISED,bd=1,bg=("red"),borde=0)
        self.frameAcciones3.pack(side=LEFT,fill=BOTH,expand=True)

        self.frameAcciones4 = Frame(self.frameAcciones1, highlightbackground = "black", highlightcolor= "black", highlightthickness=0)
        self.frameAcciones4.config(relief=RAISED,bd=1,bg=("#34495E"),borde=0)
        self.frameAcciones4.pack(side=RIGHT,fill=BOTH,expand=True)

        def cerrarVentana():
            salir = msg.askquestion("Salir","Quieres cerrar el programa?")
            if salir == "yes":
                self.ventana.destroy()
            else:
                pass  
        self.ventana_inicio.protocol("WM_DELETE_WINDOW",cerrarVentana)

    def labelFrame(self):
        self.text = Text(self.frameAcciones2,height=13,width=63)
        self.text.place(x=0,y=0)

        self.textFrame = LabelFrame(self.frameAcciones3,text="Acciones")
        self.textFrame.config(bg="#34495E",fg=("white"),font=("arial",12))
        self.textFrame.pack(fill=BOTH, expand=True)

    def TopAccionesRegistrar(self):
        
        self.btnRegistrar.config(state=DISABLED)
        self.ventanaAcion = Toplevel()
        self.ventanaAcion.geometry("400x600")
        self.ventanaAcion.config(bg="#34495E")
        self.ventanaAcion.resizable(False,False)

        self.lblRegistro= Label(self.ventanaAcion,text="Register")
        self.lblRegistro.config(bg=("#34495E"),fg="white",font=("arial black",23))
        self.lblRegistro.pack(padx=0,pady=15)


        self.Linea2 = Label(self.ventanaAcion,text="--------------------------------------------------------------")
        self.Linea2.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea2.pack(padx=0,pady=0)


        self.lblCodigo = Label(self.ventanaAcion,text="Codigo")
        self.lblCodigo.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblCodigo.pack(padx=0,pady=10)

        self.txtCodigo = Entry(self.ventanaAcion,textvariable=self.codigo)
        self.txtCodigo.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtCodigo.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblNombre = Label(self.ventanaAcion,text="Nombre")
        self.lblNombre.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblNombre.pack(padx=0,pady=10)

        self.txtNombre = Entry(self.ventanaAcion,textvariable=self.nombres)
        self.txtNombre.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtNombre.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblPrecio = Label(self.ventanaAcion,text="Precio")
        self.lblPrecio.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblPrecio.pack(padx=0,pady=10)

        self.txtPrecio = Entry(self.ventanaAcion,textvariable=self.precio)
        self.txtPrecio.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtPrecio.pack(padx=0,pady=0,ipadx=30,ipady=2)

        
        self.lblCate = Label(self.ventanaAcion,text="Categoria")
        self.lblCate.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblCate.pack(padx=0,pady=10)

        self.txtCate = Entry(self.ventanaAcion,textvariable=self.categoria)
        self.txtCate.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtCate.pack(padx=0,pady=0,ipadx=30,ipady=2)


        self.lblMarca= Label(self.ventanaAcion,text="Marca")
        self.lblMarca.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblMarca.pack(padx=0,pady=10)

        self.txtMarca = Entry(self.ventanaAcion,textvariable=self.Marca)
        self.txtMarca.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtMarca.pack(padx=0,pady=0,ipadx=30,ipady=2)


        self.registrar = Button(self.ventanaAcion,text="Registrar",command=self.insertarProducto)
        self.registrar.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="white")
        self.registrar.config(activebackground="#A1ACB7",bd=0)
        self.registrar.pack(padx=0,pady=25,ipadx=40,ipady=5)


        def close():
            self.ventanaAcion.destroy()
            self.btnRegistrar.config(state=NORMAL)
        self.ventanaAcion.protocol("WM_DELETE_WINDOW",close)

    def TopAccionEditar(self):
   
        self.btnEditar.config(state=DISABLED)
        self.ventanaAcionE = Toplevel()
        self.ventanaAcionE.geometry("400x650")
        self.ventanaAcionE.config(bg="#34495E")
        self.ventanaAcionE.resizable(False,False)

        self.lblEditar= Label(self.ventanaAcionE,text="Editar")
        self.lblEditar.config(bg=("#34495E"),fg="white",font=("arial black",20))
        self.lblEditar.pack(padx=0,pady=15)


        self.Linea = Label(self.ventanaAcionE,text="--------------------------------------------------------------")
        self.Linea.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea.pack(padx=0,pady=0)

        self.lblIdE = Label(self.ventanaAcionE,text="Id productos")
        self.lblIdE.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblIdE.pack(padx=0,pady=10)

        self.txtIdE = Entry(self.ventanaAcionE,textvariable=self.id_productoE)
        self.txtIdE.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="white")
        self.txtIdE.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblCodigoE = Label(self.ventanaAcionE,text="Codigo")
        self.lblCodigoE.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblCodigoE.pack(padx=0,pady=10)

        self.txtCodigoE = Entry(self.ventanaAcionE,textvariable=self.codigoE)
        self.txtCodigoE.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5",state=DISABLED)
        self.txtCodigoE.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblNombreE = Label(self.ventanaAcionE,text="Nombre")
        self.lblNombreE.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblNombreE.pack(padx=0,pady=10)

        self.txtNombreE = Entry(self.ventanaAcionE,textvariable=self.nombresE)
        self.txtNombreE.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5",state=DISABLED)
        self.txtNombreE.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblPrecioE = Label(self.ventanaAcionE,text="Precio")
        self.lblPrecioE.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblPrecioE.pack(padx=0,pady=10)

        self.txtPrecioE = Entry(self.ventanaAcionE,textvariable=self.precioE)
        self.txtPrecioE.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5",state=DISABLED)
        self.txtPrecioE.pack(padx=0,pady=0,ipadx=30,ipady=2)

        
        self.lblCateE = Label(self.ventanaAcionE,text="Categoria")
        self.lblCateE.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblCateE.pack(padx=0,pady=10)

        self.txtCateE = Entry(self.ventanaAcionE,textvariable=self.categoriaE)
        self.txtCateE.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5",state=DISABLED)
        self.txtCateE.pack(padx=0,pady=0,ipadx=30,ipady=2)


        self.lblMarcaE= Label(self.ventanaAcionE,text="Marca")
        self.lblMarcaE.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblMarcaE.pack(padx=0,pady=10)

        self.txtMarcaE = Entry(self.ventanaAcionE,textvariable=self.MarcaE)
        self.txtMarcaE.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5",state=DISABLED)
        self.txtMarcaE.pack(padx=0,pady=0,ipadx=30,ipady=2)


        self.accion = Button(self.ventanaAcionE,text="CONSULTA",command=self.consultaId)
        self.accion.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="white")
        self.accion.config(activebackground="#A1ACB7",bd=0)
        self.accion.pack(padx=0,pady=35,ipadx=50,ipady=5)


        def closeEditar():
            self.ventanaAcionE.destroy()
            self.btnEditar.config(state=NORMAL)
            self.limpiarEdicion()
        self.ventanaAcionE.protocol("WM_DELETE_WINDOW",closeEditar)
    
    def btnAcciones(self):
        self.btnRegistrar = Button(self.textFrame,text="Registrar",command=self.TopAccionesRegistrar)
        self.btnRegistrar.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="white")
        self.btnRegistrar.config(activebackground="#A1ACB7",bd=0)
        self.btnRegistrar.config(width=20,height=2)
        self.btnRegistrar.place(x=30,y=5)

        self.btnEditar = Button(self.textFrame,text="Editar",command=self.TopAccionEditar)
        self.btnEditar.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="white")
        self.btnEditar.config(activebackground="#A1ACB7",bd=0)
        self.btnEditar.config(width=20,height=2)
        self.btnEditar.place(x=30,y=57)

        self.btnEliminar = Button(self.textFrame,text="Eliminar",command=self.eliminarProductosFila)
        self.btnEliminar.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="white")
        self.btnEliminar.config(activebackground="#A1ACB7",bd=0)
        self.btnEliminar.config(width=20,height=2)
        self.btnEliminar.place(x=30,y=110)

        self.btnComprar = Button(self.frameAcciones4,text="Comprar",command=self.ventanaCompra)
        self.btnComprar.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="white")
        self.btnComprar.config(activebackground="#A1ACB7",bd=0)
        self.btnComprar.config(width=20,height=2)
        self.btnComprar.place(x=30,y=10)

        self.Linea3 = Label(self.frameAcciones4,text="-------------------------------------------------------------------------------------------")
        self.Linea3.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea3.place(x=30,y=80)

        self.Linea4 = Label(self.frameAcciones4,text="-------------------------------------------------------------------------------------------")
        self.Linea4.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea4.place(x=30,y=110)

        self.Linea5 = Label(self.frameAcciones4,text="-------------------------------------------------------------------------------------------")
        self.Linea5.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea5.place(x=30,y=140)

        self.Linea6 = Label(self.frameAcciones4,text="-------------------------------------------------------------------------------------------")
        self.Linea6.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.Linea6.place(x=30,y=170)

    def cajaBuscar(self):
        self.txtBuscar= Entry(self.frameEnglob,width=32,textvariable=self.buscar)
        self.txtBuscar.config(relief=FLAT,font=("arial",16),justify=CENTER,bg="#E8EEF5")
        self.txtBuscar.place(x=20,y=5)

        self.btnBuscar = Button(self.frameEnglob,text="Buscar",command=self.buscarProductos)
        self.btnBuscar.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="black")
        self.btnBuscar.config(activebackground="#A1ACB7",bd=0)
        self.btnBuscar.place(x=415,y=5)

    def treeview(self):
        
        self.style = ttk.Style(self.frameEnglob)
        self.style.configure("Treeview", rowheight=30)

        self.treev = ttk.Treeview(self.frameEnglob,selectmode='browse') 
        self.treev.place(x=20,y=60)

        self.scrollbar_vertical = ttk.Scrollbar(self.frameEnglob, orient='vertical', command = self.treev.yview)
        self.scrollbar_horizontal = ttk.Scrollbar(self.frameEnglob, orient='horizontal', command = self.treev.xview)
        self.scrollbar_horizontal.place(x=21,y=353,width=451) 
        self.scrollbar_vertical.place(x=471,y=61,height=310) 
        self.treev.configure(xscrollcommand=self.scrollbar_horizontal.set,yscrollcommand=self.scrollbar_vertical.set)

        self.treev["columns"] = ("1", "2", "3","4","5","6") 
        self.treev['show'] = 'headings'

        self.treev.column("1", width = 50, anchor ='c') 
        self.treev.column("2", width = 80, anchor ='c') 
        self.treev.column("3", width = 80, anchor ='c')
        self.treev.column("4", width = 80, anchor ='c') 
        self.treev.column("5", width = 80, anchor ='c') 
        self.treev.column("6", width = 80, anchor ='c') 
      
        self.treev.heading("1", text ="Id") 
        self.treev.heading("2", text ="Codigo") 
        self.treev.heading("3", text ="Nombres") 
        self.treev.heading("4", text ="Precio") 
        self.treev.heading("5", text ="Categoria") 
        self.treev.heading("6", text ="Marca") 

        self.tablaProductos()

    def ventanaAcciones(self):
        self.accion.config(state=DISABLED)
        self.ventanaAciones = Toplevel()
        self.ventanaAciones.geometry("450x150")
        self.ventanaAciones.config(bg="#34495E")
        self.ventanaAciones.resizable(False,False)

        self.B_editar = Button(self.ventanaAciones,text="EDITAR",command=self.editarProductos)
        self.B_editar.config(relief=FLAT,font=("arial black",12),bg=("#546F8A"),fg="white")
        self.B_editar.config(activebackground="#A1ACB7",bd=0)
        self.B_editar.pack(side=LEFT,padx=15,pady=10,ipadx=60,ipady=8)

        self.B_eliminar = Button(self.ventanaAciones,text="ELIMINAR",command=self.eliminarProductos)
        self.B_eliminar.config(relief=FLAT,font=("arial black",12),bg=("#EE3131"),fg="white")
        self.B_eliminar.config(activebackground="#A1ACB7",bd=0)
        self.B_eliminar.pack(side=RIGHT,padx=15,pady=10,ipadx=50,ipady=8)


        def closeVentanaA():
            self.ventanaAciones.destroy()
            self.accion.config(state=NORMAL)
            self.limpiarEdicion()

        self.ventanaAciones.protocol("WM_DELETE_WINDOW",closeVentanaA)

    def ventanaCompra(self):

        msg.showwarning("Advertencia","Para realizar la compra sin errores\nNO INGRESE VALORES DE TEXTOS\nEL CODIGO Y PRECIO DEBEN SER IGUAL AL (CODIGO,PRECIO) DE LA TABLA PRODUCTO")

        self.btnComprar.config(state=DISABLED)
        self.ventanaComprar = Toplevel()
        self.ventanaComprar.geometry("400x600")
        self.ventanaComprar.config(bg="#34495E")
        self.ventanaComprar.resizable(False,False)

        self.lblcomprar= Label(self.ventanaComprar,text="Comprar")
        self.lblcomprar.config(bg=("#34495E"),fg="white",font=("arial black",23))
        self.lblcomprar.pack(padx=0,pady=15)


        self.LineaC = Label(self.ventanaComprar,text="--------------------------------------------------------------")
        self.LineaC.config(bg=("#34495E"),fg="white",font=("arial black",5))
        self.LineaC.pack(padx=0,pady=0)


        self.lblCodigoC = Label(self.ventanaComprar,text="Codigo del producto")
        self.lblCodigoC.config(bg=("#34495E"),fg="red",font=("arial black",11))
        self.lblCodigoC.pack(padx=0,pady=10)

        self.txtCodigoC = Entry(self.ventanaComprar,textvariable=self.codigoCompra)
        self.txtCodigoC.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtCodigoC.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblNventas = Label(self.ventanaComprar,text="Numero de venta")
        self.lblNventas.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblNventas.pack(padx=0,pady=10)

        self.txtNventa = Entry(self.ventanaComprar,textvariable=self.Nventas)
        self.txtNventa.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtNventa.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblCantidad= Label(self.ventanaComprar,text="Cantidad de productos")
        self.lblCantidad.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblCantidad.pack(padx=0,pady=10)

        self.txtCantidad = Entry(self.ventanaComprar,textvariable=self.cantidad)
        self.txtCantidad.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtCantidad.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblPrecioC = Label(self.ventanaComprar,text="Precio del productp")
        self.lblPrecioC.config(bg=("#34495E"),fg="red",font=("arial black",12))
        self.lblPrecioC.pack(padx=0,pady=10)

        self.txtPrecioC = Entry(self.ventanaComprar,textvariable=self.precioCompra)
        self.txtPrecioC.config(relief=FLAT,font=("arial",12),justify=CENTER,bg="#E8EEF5")
        self.txtPrecioC.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.lblTOATL = Label(self.ventanaComprar,text="TOTAL - ")
        self.lblTOATL.config(bg=("#34495E"),fg="white",font=("arial black",12))
        self.lblTOATL.pack(padx=0,pady=10)

        self.txtTotal= Entry(self.ventanaComprar,textvariable=self.total)
        self.txtTotal.config(state=DISABLED,relief=FLAT,font=("arial",12),justify=CENTER,bg="#646161")
        self.txtTotal.pack(padx=0,pady=0,ipadx=30,ipady=2)

        self.comprar = Button(self.ventanaComprar,text="COMPRAR",command=self.comprar)
        self.comprar.config(relief=FLAT,font=("arial",12),bg=("#546F8A"),fg="white")
        self.comprar.config(activebackground="#A1ACB7",bd=0)
        self.comprar.pack(padx=0,pady=25,ipadx=40,ipady=5)

    
        def close():
            self.ventanaComprar.destroy()
            self.btnComprar.config(state=NORMAL)
        
        self.ventanaComprar.protocol("WM_DELETE_WINDOW",close)
#----------------------------------------------------


#--------------CRUD DE LOS PRODUCTOS------------------

    def insertarProducto(self):

        try:
            lista = [self.id_producto.get(),self.codigo.get(),self.nombres.get(),self.precio.get(),self.categoria.get(),self.Marca.get()]
            if len(self.codigo.get() and self.nombres.get() and self.precio.get()and self.categoria.get()and self.Marca.get())>0:
                codigo = self.codigo.get()
                precio = self.precio.get()
                precioFloat = float(precio)
                if codigo.isdigit()==True:
                    if precio.isdigit()==True or precioFloat:
                        enlace = controlProductos()
                        validar = enlace.validarCodigo(self.codigo.get())
                        if validar:
                            msg.showwarning("Registro","Es posible que el codigo ingresado ya exista")
                        else:
                            enlace.insertarProductos(lista)
                            msg.showinfo("Registro","Registro creado correcatmente")  
                            self.tablaProductos()     
                else:
                    msg.showwarning("Registro","Debes ingresar solo numeros en el campo codigo")
            else:
                msg.showwarning("Registro","Debes llenar todos los campos")     
        except Exception as e:
            msg.showerror("Registrar","¡Ha ocurrido un error al intentar registrar. verifique los campos!") 
    
    def tablaProductos(self):
        registro = self.treev.get_children()

        for registros in registro:
            self.treev.delete(registros)

        enlace = controlProductos()
        consulta = enlace.tablaProductos()

        for datos in consulta:
            self.treev.insert('',1,text='datos',value=(datos))

    def buscarProductos(self):
        buscar = self.buscar.get()
        enlace = controlProductos()
        valor = enlace.buscarProductos(buscar)
        if valor:
            registros = self.treev.get_children()
            for registro in registros:
                self.treev.delete(registro)
            
            for datos in valor:
                self.treev.insert('',1,text='datos',value=(datos))

        else:
            msg.showerror("Buscar","No se encontro el registro")

    def consultaId(self):
        try:
            id_producto = self.id_productoE.get()
            enlace = controlProductos()
            valor=enlace.consultaId(id_producto)
            if valor:
                for producto in valor:
                    self.codigoE.set(producto[1])
                    self.nombresE.set(producto[2])
                    self.precioE.set(producto[3])
                    self.categoriaE.set(producto[4])
                    self.MarcaE.set(producto[5])

                self.activarCasillas()
                self.ventanaAcciones()
            else:
                msg.showwarning("Edicion","Es posible que el producto relacionado con el id no exista")

        except Exception as e:
            msg.showerror("Edicion","¡Ha ocurrido un error al intentar editar!")

    def editarProductos(self):
        try:
            if len(self.id_productoE.get())>0 or self.id_productoE.get()=="":
                lista = [self.id_productoE.get(),self.codigoE.get(),self.nombresE.get(),self.precioE.get(),self.categoriaE.get(),self.MarcaE.get()]
                enlace = controlProductos()
                precio = self.precioE.get()
                precioFloat = float(precio)
                if(precio.isdigit()==True or precioFloat):
                    enlace.editarProductos(lista)
                    msg.showinfo("Edicion","La edicion se realizo con exito")
                    self.tablaProductos()
                else:
                    print("Edicion","Ingrese valores numericos o flotantes en el campo precio")
            else:
                msg.showwarning("Edicion","Debes ingresar un codigo existente para editar")
        except Exception as e:
            msg.showerror("Edicion","Ha ocirrido un error al intentar editar. verifique los campos")

    def eliminarProductos(self):
        try:
            enlace = controlProductos()
            id_productos = enlace.consultaId(self.id_productoE.get())
            if id_productos:
                confirmar = msg.askquestion("Eliminar","¿Seguro que deseas eliminar el registro?")
                if confirmar == "yes":
                    lista = [self.id_productoE.get(),self.codigoE.get(),self.nombresE.get(),self.precioE.get(),self.categoriaE.get(),self.MarcaE.get()]
                    enlace.eliminarProductos(lista)
                    msg.showinfo("Eliminar","El registro se elimino correctamente")
                    self.ventanaAciones.destroy()
                    self.accion.config(state=NORMAL)
                    self.limpiarEdicion()
                    self.tablaProductos()
                else:
                    pass
            else:
                msg.showwarning("Eliminar","El id ingresado no existe")

        except Exception as e:
            msg.showerror("Eliminar","Ha ocurrido un error al intentar eliminar")

    def eliminarProductosFila(self):

        try:
            seleccion = self.treev.selection()[0]
            values = self.treev.item(seleccion)['values']
            if seleccion:
                mensaje = msg.askquestion("Eliminar","¿Seguro que deseas eliminar el registro?")
                if mensaje =="yes":        
                    enlace = controlProductos()
                    enlace.eliminarProductosFila(value=(values))
                    self.treev.delete(seleccion) 
                else:
                    pass
            else:
                pass
        except:
            msg.showwarning("Eliminar","Debe seleccionar un producto para eliminar")
# ----------------------------------------------------   
  
#--------------Aciones de compra---------------------
    def comprar(self):
        try:
            id_venta = self.id_venta.get()
            codigo = self.codigoCompra.get()
            n_ventas = self.Nventas.get()
            cantidad = self.cantidad.get()
            precio = self.precioCompra.get()

            i_precio = float(precio)

            if len(codigo and n_ventas and cantidad and precio)>0:
                if(codigo.isdigit()==True and n_ventas.isdigit()==True and cantidad.isdigit()==True):
                    if precio.isdigit()==True or i_precio:
                        enlace = controlProductos()
                        validar = enlace.consultaPrecioP(codigo,precio)
                        if validar:
                            cant = int(cantidad)*float(precio)
                            total = str(cant)
                            lista = [id_venta,codigo,n_ventas,cantidad,precio,total]
                            registra = controlventas()
                            registra.registrarVentas(lista)
                            msg.showinfo("Compra","La venta se ha realizado con exito")

                            self.text.delete("1.0","end")

                            self.text.insert(END, '\n')
                            self.text.insert(END, 'DETALLES DE VENTA\n')
                            self.text.insert(END, '------------------\n')
                            self.text.insert(END, 'CODIGO DEL PRODUCTO ' + codigo+ '\n')
                            self.text.insert(END, 'NUMERO DE VENTA '+ n_ventas+'\n')
                            self.text.insert(END, 'CANTIDAD DE PRODUCTOS ' + cantidad + '\n')
                            self.text.insert(END, 'PRECIO TOTAL DEL PRODUCTO ' + precio + ' $' + '\n')
                            self.text.insert(END, 'TOTAL A PAGAR ' + total + ' $' + '\n')
                            self.text.insert(END, '------------------\n')
                            self.text.insert(END, 'TOTAL ' + total + ' $' + '\n')

                        else:
                            msg.showerror("Compra","Es posible que no exista el codigo. o el precio ingresado no coinciden con el precio registrado en la DB productos")
                    else:
                        msg.showwarning("Compra","El campo precio solo acepta numeros enteros o flotantes")   
                else:
                    msg.showwarning("Compra","Solo debes introducir valores numericos")
            else:
                msg.showwarning("Compra","Debes introducir valores en los campos")
        except Exception as e:
            msg.showerror("Error","Ha ocurrido un error verifique si NO ingresaste valores de texto")

#----------------------------------------------------


#--------------Funciones del sistema ---------------
    
    def registrarse(self):

        try:
            if len(self.usuarioRe.get() and self.emailRe.get() and self.claveRe.get() and self.claveConfirmar.get())>4:
                if self.claveRe.get() == self.claveConfirmar.get():
                    lista = [self.id_usuarios.get(),self.usuarioRe.get(),self.emailRe.get(),self.claveRe.get()]
                    enlace = controlUsuario()
                    enlace.insertarUsuarios(lista)
                    msg.showinfo("Registro","Registro creado correctamente")
                    self.Limpiar()
                else:
                    msg.showwarning("Registro","Las contraseñas deben coincidir")
                    self.Limpiar()
            else:
                msg.showwarning("Registro","Todos los compos deben ser mayor a 4 didgitos")
                self.Limpiar()
        except Exception as e:
            msg.showerror("Registro","Ha ocurriodo un error al intentar registrar")

    def iniciarSesion(self):
        if len(self.usuarioLo.get() and self.claveLo.get())>0:
            enlace = controlUsuario()
            validar=enlace.iniciarSession(self.usuarioLo.get(),self.claveLo.get())
            if validar:
                self.toplabel()
            else:
                msg.showerror("Iniciar session","Usuario y contraseñas incorrectos")
        else:
            msg.showwarning("Iniciar","Ingrese datos en los campos")


#--------------Funciones secundarias-------------------
    def comprarAtributos(self):
        self.id_venta = StringVar()
        self.codigoCompra = StringVar()
        self.Nventas = StringVar()
        self.cantidad = StringVar()
        self.precioCompra = StringVar()
        self.total = StringVar()
    
    def activarCasillas(self):
        self.txtCodigoE.config(state=DISABLED)
        self.txtCodigoE.config(bg="#504747")

        self.txtNombreE.config(state=NORMAL)
        self.txtPrecioE.config(state=NORMAL)
        self.txtCateE.config(state=NORMAL)
        self.txtMarcaE.config(state=NORMAL)

    def CopiarLink(self):
        link = "https://github.com/Aristedesfloresbartra/BARTRA"
        seleccionar.copy(link)
        msg._show("Copy","Link copiado con exito")

    def propiedadesLoginAndRegister(self):
        
        self.usuarioLo = StringVar()
        self.claveLo = StringVar()

        self.usuarioRe = StringVar()
        self.emailRe = StringVar()
        self.claveRe = StringVar()
        self.claveConfirmar = StringVar()

        self.id_usuarios = StringVar()

    def propiedades(self):
        self.buscar = StringVar()

        self.id_producto = StringVar()
        self.codigo = StringVar()
        self.nombres = StringVar()
        self.precio = StringVar()
        self.categoria = StringVar()
        self.Marca = StringVar()

        self.id_productoE = StringVar()
        self.codigoE = StringVar()
        self.nombresE = StringVar()
        self.precioE = StringVar()
        self.categoriaE = StringVar()
        self.MarcaE = StringVar()

    def Limpiar(self):
        self.usuarioLo.set("")
        self.claveLo.set("")

        self.usuarioRe.set("")
        self.emailRe.set("")
        self.claveRe.set("")
        self.claveConfirmar.set("")
    
    def limpiarEdicion(self):

        self.id_productoE.set("") 
        self.codigoE.set("") 
        self.nombresE.set("") 
        self.precioE.set("") 
        self.categoriaE.set("") 
        self.MarcaE.set("") 