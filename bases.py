from tkinter import*
def autprof():
    entradaU=StringVar()
    entradaP=StringVar()
    txtprof=Entry(ventana,textvariable=entradaU).place(x=65,y=125)
    txtprofpasswd=Entry(ventana,textvariable=entradaP).place(x=65,y=175)
    aceptar=Button(ventana,text="Aceptar").place(x=265, y=145, width=100, height=30)
    
def autest():
    entradaE=StringVar()
    entradaPE=StringVar()
    txtest=Entry(ventana,textvariable=entradaE).place(x=65,y=125)
    txtestpasswd=Entry(ventana,textvariable=entradaPE).place(x=65,y=175)
    aceptar2=Button(ventana,text="Aceptar").place(x=265, y=145, width=100, height=30)



ventana=Tk()
ventana.geometry("500x400")
ventana.title("Repaso")

bienvenida=Label(ventana,text="Por favor seleccione el usuario: ")
bienvenida.place(x=60, y=20)
boton1=Button(ventana,text="Profesor",command=autprof)
boton1.place(x=60, y=40, width=100, height=30)
##boton1.grid(row=3,column=3)
boton2=Button(ventana,text="alumnos",command=autest)
boton2.place(x=160, y=40, width=100, height=30)
ventana.mainloop() #ventana permanezca abierta
