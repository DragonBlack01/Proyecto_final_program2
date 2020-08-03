from tkinter import * 
from tkinter import font
from tkinter import messagebox as msg
from tkinter import ttk 

from tksheet import Sheet # para instalarlo -> pip3 install tksheet

from tkcalendar import Calendar, DateEntry # para instalarlo -> pip3 install tkcalendar

#Incluye el objeto de persona
from modelo import Persona

#Incluye el objeto de logica de negocio
from modelo import PersonoBO

#incluye las otras pantallas
import mant_telefonos



class Aplicacion:
    

    def __init__(self):
        #*************************************************************************
        #Crea un objeto TK
        #*************************************************************************
        self.raiz = Tk()
        self.raiz.title ("Mantenimiento de Personas")
        self.raiz.geometry('900x600') 

        #*************************************************************************
        #crea el menu de la pantalla
        #*************************************************************************
        menubar = Menu(self.raiz)
        self.raiz.config(menu=menubar)

        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Acerca de..")
        filemenu.add_separator()
        filemenu.add_command(label="Salir", command=self.raiz.quit)

        mantmenu = Menu(menubar, tearoff=0)
        mantmenu.add_command(label="Teléfonos", command=self.mostrar_mant_telefonos)
       

        menubar.add_cascade(label="Archivo", menu=filemenu)
        menubar.add_cascade(label="Mantenimiento", menu=mantmenu)

        #*************************************************************************
        #crea un objeto tipo fuenta
        #*************************************************************************
        self.fuente = font.Font(weight="bold")

        #*************************************************************************
        #se crean atributos de la clase
        #*************************************************************************
        self.persona = Persona.Persona() #se crea el objeto de dominio para guardar la información
        self.insertando = True
        
        #*************************************************************************
        #se crean los campos de la pantalla
        #*************************************************************************

        #Se coloca un label del titulo
        self.lb_tituloPantalla = Label(self.raiz, text = "MANTENIMIENTO DE PERSONAS", font = self.fuente)
        self.lb_tituloPantalla.place(x = 320, y = 20) #colocar por medio de espacion en pixeles de la parte superior de la pantalla considerando un eje x y un eje y
        
        #coloca en el formulario el campo y el label de cedula
        self.lb_cedula = Label(self.raiz, text = "Cedula:")
        self.lb_cedula.place(x = 240, y = 60)
        self.txt_cedula = Entry(self.raiz, textvariable=self.persona.cedula, justify="right")
        self.txt_cedula.place(x = 370, y = 60)

        #coloca en el formulario el campo y el label de nombre
        self.lb_nombre = Label(self.raiz, text = "Nombre:")
        self.lb_nombre.place(x = 240, y = 90)
        self.txt_nombre = Entry(self.raiz, textvariable=self.persona.nombre, justify="right", width=30)
        self.txt_nombre.place(x = 370, y = 90)

        #coloca en el formulario el campo y el label de apellido1
        self.lb_apellido1 = Label(self.raiz, text = "Primer apellido:")
        self.lb_apellido1.place(x = 240, y = 120)
        self.txt_apellido1 = Entry(self.raiz, textvariable=self.persona.apellido1, justify="right", width=30)
        self.txt_apellido1.place(x = 370, y = 120)


        #coloca en el formulario el campo y el label de apellido2
        self.lb_apellido2 = Label(self.raiz, text = "Segundo apellido:")
        self.lb_apellido2.place(x = 240, y = 150)
        self.txt_apellido2 = Entry(self.raiz, textvariable=self.persona.apellido2, justify="right", width=30)
        self.txt_apellido2.place(x = 370, y = 150)

        #coloca en el formulario el campo y el label de fecha nacimiento
        self.lb_fecNacimiento = Label(self.raiz, text = "Fecha nacimiento:")
        self.lb_fecNacimiento.place(x = 240, y = 180)
        self.txt_fecNacimiento = Entry(self.raiz, textvariable=self.persona.fecNacimiento, justify="right", width=30, state="readonly")
        self.txt_fecNacimiento.place(x = 370, y = 180)
        self.bt_mostrarCalendario = Button(self.raiz, text="...", width=3, command = self.mostrarDatePicker)
        self.bt_mostrarCalendario.place(x = 650, y = 180)

        #coloca en el formulario el campo y el label de sexo
        self.lb_sexo = Label(self.raiz, text = "Sexo:")
        self.lb_sexo.place(x = 240, y = 210)
        self.radio_sexoM = Radiobutton(self.raiz, text="Masculino", variable=self.persona.sexo,   value=1)
        self.radio_sexoF = Radiobutton(self.raiz, text="Femenino", variable=self.persona.sexo,   value=2)
        self.radio_sexoM.place(x = 370, y = 210)
        self.radio_sexoF.place(x = 490, y = 210)
        self.persona.sexo.set(1) #setea el sexo al inicio como masculino

        #coloca en el formulario el campo y el label de Direccion
        self.lb_Direccion = Label(self.raiz, text = "Direccion:")
        self.lb_Direccion.place(x = 240, y = 250)
        self.txt_Direccion = Entry(self.raiz, textvariable=self.persona.Direccion, justify="right", width=30)
        self.txt_Direccion.place(x = 370, y = 250)

        #coloca en el formulario el campo y el label de observaciones
        self.lb_observaciones = Label(self.raiz, text = "Observaciones:")
        self.lb_observaciones.place(x = 240, y = 290)
        self.txt_observaciones = Entry(self.raiz, textvariable=self.persona.observaciones, justify="right", width=30)
        self.txt_observaciones.place(x = 370, y = 290)

        #coloca los botones enviar y borrar
        self.bt_borrar = Button(self.raiz, text="Limpiar", width=15, command = self.limpiarInformacion)
        self.bt_borrar.place(x = 370, y = 310)

        self.bt_enviar = Button(self.raiz, text="Enviar", width=15, command = self.enviarInformacion)
        self.bt_enviar.place(x = 510, y = 310)

        self.bt_modificar = Button(self.raiz, text="Modificar", width=15, command = self.enviarInformacion)
        self.bt_modificar.place(x = 650, y = 310)


        #Se coloca un label del informacion
        self.lb_tituloPantalla = Label(self.raiz, text = "INFORMACIÓN INCLUIDA", font = self.fuente)
        self.lb_tituloPantalla.place(x = 350, y = 355) #colocar por medio de espacion en pixeles de la parte superior de la pantalla considerando un eje x y un eje y

        #*************************************************************************
        #tabla con informacion
        #*************************************************************************
        
        self.sheet = Sheet(self.raiz,
                            page_up_down_select_row = True,
                            column_width = 120,
                            startup_select = (0,1,"rows"),
                            headers = ['Cédula', 'Nombre', 'Primer Ape.', 'Segundo Ape.', 'Fec. Nacimiento', 'Sexo','Direccion'],
                            height = 195, #height and width arguments are optional
                            width = 720 #For full startup arguments see DOCUMENTATION.md
                            )
        
        self.sheet.enable_bindings(("single_select", 
                                    "column_select",
                                    "row_select",
                                    "column_width_resize",
                                    "double_click_column_resize",
                                    #"row_width_resize",
                                    #"column_height_resize",
                                    "arrowkeys",
                                    "row_height_resize",
                                    "double_click_row_resize",
                                    "right_click_popup_menu",
                                    "rc_select",
                                    "rc_insert_column",
                                    "rc_delete_column",
                                    "rc_insert_row",
                                    "rc_delete_row"))
        self.sheet.place(x = 20, y = 390)
        
        #coloca los botones cargar y eliminar
        self.bt_cargar = Button(self.raiz, text="Cargar", width=15, command = self.cargarInformacion)
        self.bt_cargar.place(x = 750, y = 385)

        self.bt_eliminar = Button(self.raiz, text="Eliminar", width=15, command = self.eliminarInformacion)
        self.bt_eliminar.place(x = 750, y = 425)
        
        self.cargarTodaInformacion()


        #*************************************************************************
        #se inicial el main loop de la pantalla
        #*************************************************************************
        self.raiz.mainloop()
    #*************************************************************************
        #         #Llamadas a otras pantallas
   #*************************************************************************
    def mostrar_mant_telefonos(self):
        mant_telefonos.MantTelefonos(self.raiz)
    


    #*************************************************************************
    #Metodo para consultar la información de la base de datos para 
    #cargarla en la tabla
    #*************************************************************************
    def cargarTodaInformacion(self):
        try:
            self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
            resultado = self.personaBo.consultar()

            self.sheet.set_sheet_data(resultado)
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para cargar informacion
    #*************************************************************************
    def cargarInformacion(self):
        try:
            datoSeleccionado = self.sheet.get_currently_selected()
            cedula = (self.sheet.get_cell_data(datoSeleccionado[0],0))
            self.persona.cedula.set(cedula)
            self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
            self.personaBo.consultarPersona(self.persona) #se envia a consultar
            self.insertando = False
            msg.showinfo("Acción: Consultar persona", "La información de la persona ha sido consultada correctamente") # Se muestra el mensaje de que todo esta correcto
            
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para cargar eliminar la informacion
    #*************************************************************************
    def eliminarInformacion(self):
        try:
            datoSeleccionado = self.sheet.get_currently_selected()
            cedula = (self.sheet.get_cell_data(datoSeleccionado[0],0))
            nombre = (self.sheet.get_cell_data(datoSeleccionado[0],1))

            resultado = msg.askquestion("Eliminar",  "¿Desear eliminar a "+nombre+" de la base de datos?")
            if resultado == "yes":
                self.persona.cedula.set(cedula)
                self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
                self.personaBo.eliminar(self.persona) #se envia a consultar
                self.cargarTodaInformacion()
                self.persona.limpiar()
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    
    def printTxt(self, texto):
        print(texto)

    #*************************************************************************
    #Metodo para enviar la información a la base de datos
    #*************************************************************************
    def enviarInformacion(self):
        try:
            self.personaBo = PersonoBO.PersonaBO() #se crea un objeto de logica de negocio
            if(self.insertando == True):
                self.personaBo.guardar(self.persona)
            else:
                self.personaBo.modificar(self.persona)
            
            self.cargarTodaInformacion()
            self.persona.limpiar() #se limpia el formulario

            if(self.insertando == True):
                msg.showinfo("Acción: Agregar persona", "La información de la persona ha sido incluida correctamente") # Se muestra el mensaje de que todo esta correcto
            else:
                msg.showinfo("Acción: Agregar modificar", "La información de la persona ha sido modificada correctamente") # Se muestra el mensaje de que todo esta correcto
        except Exception as e: 
            msg.showerror("Error",  str(e)) #si se genera algun tipo de error muestra un mensache con dicho error

    #*************************************************************************
    #Metodo para limpiar el formulario
    #*************************************************************************
    def limpiarInformacion(self):
        self.persona.limpiar() #llama al metodo de la clase persona para limpiar los atritudos de la clase
        self.insertando = True
        msg.showinfo("Acción del sistema", "La información del formulario ha sido eliminada correctamente") # muestra un mensaje indicando que se limpio el formulario


    #*************************************************************************
    #Metodo para mostrar un contro tipo datepicker
    #*************************************************************************
    def mostrarDatePicker(self):
        self.top = Toplevel(self.raiz)
        self.cal = Calendar(self.top, font="Arial 14", selectmode='day', locale='en_US',
                   cursor="hand1", year=2019, month=6, day=16)
        self.cal.pack(fill="both", expand=True)
        ttk.Button(self.top, text="Seleccionar", command = self.seleccionarFecha).pack()

    #*************************************************************************
    #Evento para obtener la fecha del datepicker
    #*************************************************************************
    def seleccionarFecha(self):
        self.persona.fecNacimiento.set(self.cal.selection_get())

    
def main():
    Aplicacion()
    return 0

if __name__ == "__main__":
    main()