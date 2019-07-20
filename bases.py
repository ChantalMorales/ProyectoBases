from tkinter import*
from tkinter import ttk


def autprof():
    entradaU=StringVar()
    entradaP=StringVar()
    p1=Label(ventana,text="Por favor ingrese el usuario: ",font =("Agency FB",15)).place(x=65, y=90)
    txtprof=Entry(ventana,textvariable=entradaU,font=("Agency FB",15)).place(x=65,y=125)
    p2=Label(ventana,text="Por favor ingrese la clave: ",font=("Agency FB",15)).place(x=65, y=160)
    txtprofpasswd=Entry(ventana,textvariable=entradaP,font=("Agency FB",15)).place(x=65,y=195)
    aceptar=Button(ventana,text="Aceptar", command= ventanaProfesores,font=("Agency FB",15)).place(x=265, y=145, width=100, height=30)

def ventanaestudiante():
    ventana.withdraw()
    win=Toplevel()
    win.geometry("450x300+200+200")
    win.title("Sistema Estudiantes")
    elegir=Label(win,text="Por favor escoja una materia: ",font=("Agency FB",15)).place(x=60, y=20)
    listaMat=ttk.Combobox(win,state ="readonly",font=("Agency FB",15))
    listaMat.place(x=160, y=60,width=200,height=30)
    listaMat['values']=['Programacion','Sistemas','Algoritmos']
    mostrar=Button(win,text="Mostrar",font=("Agency FB",15)).place(x=100, y=160,width=100)
    mostrarTo=Button(win,text="Mostrar Todo",font=("Agency FB",15)).place(x=300,y=160)
    ira=Button(win,text="IRA",font=("Agency FB",15)).place(x=230,y=200,width=50)


def ventanaProfesores():
    entradaPM=StringVar()
    ventana.withdraw()
    winPro=Toplevel()
    winPro.geometry("450x300+200+200")
    winPro.title("Validacion Profesores")
    elegir=Label(winPro,text="Por favor escoja su materia: ",font=("Agency FB",15)).place(x=60, y=20)
    listaMat=ttk.Combobox(winPro,state ="readonly",font=("Agency FB",15))
    listaMat.place(x=160, y=60,width=200,height=30)
    listaMat['values']=['Programacion','Sistemas','Algoritmos']
    clave=Label(winPro,text="Por favor ingrese la clave de la materia: ",font=("Agency FB",15)).place(x=60, y=120)
    passwdMat=Entry(winPro,textvariable=entradaPM,font=("Helvetica",15)).place(x=65,y=150)
    ingresar=Button(winPro,text="Ingresar",command= EditProf,font=("Agency FB",15)).place(x=300,y=230,width=100)

def EditProf():
    entradaPM=StringVar()
    #winPro.withdraw()
    edit=Toplevel()
    edit.geometry("600x200")
    edit.title("Sistema Profesores")
    seleccionar=Label(edit,text="Por favor escoja una opcion: ",font=("Agency FB",15)).place(x=60, y=20)
    ingNot=Button(edit,text="Ingresar Notas",font =("Agency FB",15)).place(x=100, y=60,width=100)
    edNot=Button(edit,text="Editar Notas",font =("Agency FB",15)).place(x=220, y=60,width=100)
    ElimNot=Button(edit,text="Eliminar Notas",font =("Agency FB",15)).place(x=340, y=60,width=100)
    prom=Button(edit,text="Promedio Materia",font =("Agency FB",15)).place(x=100, y=120,width=110)
    MaxMin=Button(edit,text="Nota Maxima y Nota Minima",font =("Agency FB",15)).place(x=220, y=120,width=180)
    mosTod=Button(edit,text="Mostrar todo",font =("Agency FB",15)).place(x=420, y=120,width=100)
    

    
def autest():
    entradaE=StringVar()
    entradaPE=StringVar()
    p1=Label(ventana,text="Por favor ingrese el usuario: ",font =("Agency FB",15)).place(x=65, y=90)
    txtest=Entry(ventana,textvariable=entradaE,font =("Agency FB",15)).place(x=65,y=125)
    p2=Label(ventana,text="Por favor ingrese la clave: ",font=("Agency FB",15)).place(x=65, y=160)
    txtestpasswd=Entry(ventana,textvariable=entradaPE,font =("Agency FB",15)).place(x=65,y=195)
    aceptar2=Button(ventana,text="Aceptar", command=ventanaestudiante,font =("Agency FB",15)).place(x=265, y=145, width=100, height=30)



ventana=Tk()
ventana.geometry("500x400")
ventana.title("Repaso")

bienvenida=Label(ventana,text="Por favor seleccione el usuario: ",font =("Agency FB",15))
bienvenida.place(x=60, y=20)
boton1=Button(ventana,text="Profesor",command=autprof,font =("Agency FB",15))
boton1.place(x=60, y=50, width=100, height=30)
##boton1.grid(row=3,column=3)
boton2=Button(ventana,text="Alumnos",command=autest,font =("Agency FB",15))
boton2.place(x=160, y=50, width=100, height=30)
ventana.mainloop() #ventana permanezca abierta

