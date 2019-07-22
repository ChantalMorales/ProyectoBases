from tkinter import*
from tkinter import ttk
import pymysql


conn = pymysql.connect( host='localhost',port=3306, user='root',passwd='',db='proyecto_bases')
cur=conn.cursor()


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
"""    if listaMat['Programacion']:
        mostrar=Button(win,text="Mostrar",font=("Agency FB",15)).place(x=100, y=160,width=100)
        mostrarTo=Button(win,text="Mostrar Todo",font=("Agency FB",15)).place(x=300,y=160)
        ira=Button(win,text="IRA",font=("Agency FB",15)).place(x=230,y=200,width=50)
"""
def ventanaprog():
    ventana.withdraw()
    win=Toplevel()
    win.geometry("450x300+200+200")
    win.title("Nota Programacion")

def ventanaProfesores():
    entradaPM=StringVar()
    ventana.withdraw()
    winPro=Toplevel()
    winPro.geometry("450x300+200+200")
    winPro.title("Validacion Profesores")
    elegir=Label(winPro,text="Por favor escoja su materia: ",font=("Agency FB",15)).place(x=60, y=20)
    #listaMat=ttk.Combobox(winPro,state ="readonly",font=("Agency FB",15))
    #listaMat.place(x=160, y=60,width=200,height=30)
    #listaMat['values']=['Programacion','Sistemas','Algoritmos']
    #clave=Label(winPro,text="Por favor ingrese la clave de la materia: ",font=("Agency FB",15)).place(x=60, y=120)
    #passwdMat=Entry(winPro,textvariable=entradaPM,font=("Helvetica",15))
    #passwdMat.place(x=65,y=150)
    prog=Button(winPro,text="PROGRAMACION",command= EditProf1,font=("Agency FB",15)).place(x=160,y=60,width=100)
    sis=Button(winPro,text="SISTEMAS",command= EditProf2,font=("Agency FB",15)).place(x=160,y=120,width=100)
    alg=Button(winPro,text="ALGORITMOS",command= EditProf3,font=("Agency FB",15)).place(x=160,y=180,width=100)



def IngnotP():
    entradan1=StringVar()
    ventana.withdraw()
    winIPro=Toplevel()
    winIPro.geometry("450x300")
    winIPro.title("NOTA PROGRAMACION")
    p1=Label(ventana,text="Por favor ingrese la nota: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtip=Entry(ventana,textvariable=entradan1,font=("Agency FB",15))
    txtip.place(x=65,y=125) 
    e = txtip.get()       
    sql="INSERT INTO notas(`PROGRAMACION`) Values ('%e') "
    cur.execute(sql)
    cur.close()

def ednotP():
    entradan1=StringVar()
    entradan12=StringVar()
    ventana.withdraw()
    winIPro=Toplevel()
    winIPro.geometry("450x300")
    winIPro.title("EDITAR NOTA PROGRAMACION")
    p1=Label(ventana,text="Por favor ingrese la nota a editar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtep=Entry(ventana,textvariable=entradan1,font=("Agency FB",15))
    txtep.place(x=65,y=125)
    p2=Label(ventana,text="Por favor ingrese la nueva nota: ",font =("Agency FB",15)).place(x=65, y=160)    
    txtnp=Entry(ventana,textvariable=entradan12,font=("Agency FB",15))
    txtnp.place(x=65,y=195)    

    e = txtep.get()
    f = txtnp.get()       
    sql="INSERT INTO notas(`PROGRAMACION`) Values ('%f') WHERE PROGRAMACION='%e'"
    cur.execute(sql)
    cur.close()    

def elimnotP():
    entradan1=StringVar()
    ventana.withdraw()
    winIPro=Toplevel()
    winIPro.geometry("450x300")
    winIPro.title("ELIMINAR NOTA PROGRAMACION")
    p1=Label(ventana,text="Por favor ingrese la nota a eliminar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtelip=Entry(ventana,textvariable=entradan1,font=("Agency FB",15))
    txtelip.place(x=65,y=125)
    e = txtelip.get()     
    sql="DELETE FROM notas WHERE PROGRAMACION = '%e'"
    cur.execute(sql)
    cur.close()     


def EditProf1():
    entradaPM=StringVar()
    #winPro.withdraw()
    edit=Toplevel()
    edit.geometry("600x200")
    edit.title("Sistema Profesores Programacion")
    seleccionar=Label(edit,text="Por favor escoja una opcion: ",font=("Agency FB",15)).place(x=60, y=20)
    ingNot=Button(edit,text="Ingresar Notas",command= IngnotP,font =("Agency FB",15)).place(x=100, y=60,width=100)
    edNot=Button(edit,text="Editar Notas",command= ednotP,font =("Agency FB",15)).place(x=220, y=60,width=100)
    ElimNot=Button(edit,text="Eliminar Notas",command= elimnotP,font =("Agency FB",15)).place(x=340, y=60,width=100)
    prom=Button(edit,text="Promedio Materia",font =("Agency FB",15)).place(x=100, y=120,width=110)
    MaxMin=Button(edit,text="Nota Maxima y Nota Minima",font =("Agency FB",15)).place(x=220, y=120,width=180)
    mosTod=Button(edit,text="Mostrar todo",font =("Agency FB",15)).place(x=420, y=120,width=100)


def IngnotS():
    entradan2=StringVar()
    ventana.withdraw()
    winISis=Toplevel()
    winISis.geometry("450x300")
    winISis.title("NOTA SISTEMAS")
    p1=Label(ventana,text="Por favor ingrese la nota: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtis=Entry(ventana,textvariable=entradan2,font=("Agency FB",15))
    txtis.place(x=65,y=125) 
    e = txtis.get()       
    sql="INSERT INTO notas(`SISTEMAS`) Values ('%e') "
    cur.execute(sql)
    cur.close()

def ednotS():
    entradan2=StringVar()
    entardan21=StringVar()
    ventana.withdraw()
    winISis=Toplevel()
    winISis.geometry("450x300")
    winISis.title("EDITAR NOTA SISTEMAS")
    p1=Label(ventana,text="Por favor ingrese la nota a editar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtes=Entry(ventana,textvariable=entradan2,font=("Agency FB",15))
    txtes.place(x=65,y=125)
    p2=Label(ventana,text="Por favor ingrese la nueva nota: ",font =("Agency FB",15)).place(x=65, y=160)    
    txtns=Entry(ventana,textvariable=entradan21,font=("Agency FB",15))
    txtns.place(x=65,y=195)    

    e = txtes.get()
    f = txtns.get()       
    sql="INSERT INTO notas(`SISTEMAS`) Values ('%f') WHERE SISTEMAS='%e'"
    cur.execute(sql)
    cur.close()    

def elimnotS():
    entradan2=StringVar()
    ventana.withdraw()
    winISis=Toplevel()
    winISis.geometry("450x300")
    winISis.title("ELIMINAR NOTA PROGRAMACION")
    p1=Label(ventana,text="Por favor ingrese la nota a eliminar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtelis=Entry(ventana,textvariable=entradan2,font=("Agency FB",15))
    txtelis.place(x=65,y=125)
    e = txtelis.get()     
    sql="DELETE FROM notas WHERE SISTEMAS = '%e'"
    cur.execute(sql)
    cur.close() 




    
def EditProf2():
    entradaPM=StringVar()
    #winPro.withdraw()
    edit=Toplevel()
    edit.geometry("600x200")
    edit.title("Sistema Profesores Sistemas Operativos")
    seleccionar=Label(edit,text="Por favor escoja una opcion: ",font=("Agency FB",15)).place(x=60, y=20)
    ingNot=Button(edit,text="Ingresar Notas",command= IngnotS,font =("Agency FB",15)).place(x=100, y=60,width=100)
    edNot=Button(edit,text="Editar Notas",command= ednotS,font =("Agency FB",15)).place(x=220, y=60,width=100)
    ElimNot=Button(edit,text="Eliminar Notas",command= elimnotS,font =("Agency FB",15)).place(x=340, y=60,width=100)
    prom=Button(edit,text="Promedio Materia",font =("Agency FB",15)).place(x=100, y=120,width=110)
    MaxMin=Button(edit,text="Nota Maxima y Nota Minima",font =("Agency FB",15)).place(x=220, y=120,width=180)
    mosTod=Button(edit,text="Mostrar todo",font =("Agency FB",15)).place(x=420, y=120,width=100)


def IngnotA():
    entradan3=StringVar()
    ventana.withdraw()
    winIAlg=Toplevel()
    winIAlg.geometry("450x300")
    winIAlg.title("NOTA ALGORITMOS")
    p1=Label(ventana,text="Por favor ingrese la nota: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtia=Entry(ventana,textvariable=entradan3,font=("Agency FB",15))
    txtia.place(x=65,y=125) 
    e = txtia.get()       
    sql="INSERT INTO notas(`ALGORITMOS`) Values ('%e') "
    cur.execute(sql)
    cur.close()

def ednotA():
    entradan3=StringVar()
    ventana.withdraw()
    winIAlg=Toplevel()
    winIAlg.geometry("450x300")
    winIAlg.title("EDITAR NOTA ALGORITMOS")
    p1=Label(ventana,text="Por favor ingrese la nota a editar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtea=Entry(ventana,textvariable=entradan3,font=("Agency FB",15))
    txtea.place(x=65,y=125)
    p2=Label(ventana,text="Por favor ingrese la nueva nota: ",font =("Agency FB",15)).place(x=65, y=160)    
    txtna=Entry(ventana,textvariable=entradan3,font=("Agency FB",15))
    txtna.place(x=65,y=195)    

    e = txtea.get()
    f = txtna.get()       
    sql="INSERT INTO notas(`ALGORITMOS`) Values ('%f') WHERE ALGORITMOS='%e'"
    cur.execute(sql)
    cur.close()    

def elimnotA():
    entradan3=StringVar()
    ventana.withdraw()
    winIAlg=Toplevel()
    winIAlg.geometry("450x300")
    winIAlg.title("EDITAR NOTA ALGORITMOS")
    p1=Label(ventana,text="Por favor ingrese la nota a eliminar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtelia=Entry(ventana,textvariable=entradan3,font=("Agency FB",15))
    txtelia.place(x=65,y=125)
    e = txtelia.get()     
    sql="DELETE FROM notas WHERE ALGORITMOS = '%e'"
    cur.execute(sql)
    cur.close() 


def EditProf3():
    entradaPM=StringVar()
    #winPro.withdraw()
    edit=Toplevel()
    edit.geometry("600x200")
    edit.title("Sistema Profesores Algoritmos")
    seleccionar=Label(edit,text="Por favor escoja una opcion: ",font=("Agency FB",15)).place(x=60, y=20)
    ingNot=Button(edit,text="Ingresar Notas",command= IngnotA,font =("Agency FB",15)).place(x=100, y=60,width=100)
    edNot=Button(edit,text="Editar Notas",command= ednotA,font =("Agency FB",15)).place(x=220, y=60,width=100)
    ElimNot=Button(edit,text="Eliminar Notas",command= elimnotA,font =("Agency FB",15)).place(x=340, y=60,width=100)
    prom=Button(edit,text="Promedio Materia",font =("Agency FB",15)).place(x=100, y=120,width=110)
    MaxMin=Button(edit,text="Nota Maxima y Nota Minima",font =("Agency FB",15)).place(x=220, y=120,width=180)
    mosTod=Button(edit,text="Mostrar todo",font =("Agency FB",15)).place(x=420, y=120,width=100)


    
def autest():
    entradaE=StringVar()
    entradaPE=StringVar()
    p1=Label(ventana,text="Por favor ingrese el usuario: ",font =("Agency FB",15)).place(x=65, y=90)
    txtest=Entry(ventana,textvariable=entradaE,font =("Agency FB",15))
    txtest.place(x=65,y=125)
    p2=Label(ventana,text="Por favor ingrese la clave: ",font=("Agency FB",15)).place(x=65, y=160)
    txtestpasswd=Entry(ventana,textvariable=entradaPE,font =("Agency FB",15))
    txtestpasswd.place(x=65,y=195)
    usre = txtest.get()    
    pssw = txtestpasswd.get()

    Button(ventana,text="Comprobacion", command=ventanaestudiante,font =("Agency FB",15)).place(x=265, y=145, width=100, height=30)



  





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
conn.close
ventana.mainloop() #ventana permanezca abierta


