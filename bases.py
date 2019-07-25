from tkinter import*
from tkinter import ttk
import pymysql


db = pymysql.connect( host='localhost',port=3306, user='root',passwd='',db='proyecto_bases')
cursor=db.cursor()


def autprof():
    entradaU=StringVar()
    entradaP=StringVar()
    p1=Label(ventana,text="Por favor ingrese el usuario: ",font =("Agency FB",15)).place(x=65, y=90)
    txtprof=Entry(ventana,textvariable=entradaU,font=("Agency FB",15))
    txtprof.place(x=65,y=125)
    p2=Label(ventana,text="Por favor ingrese la clave: ",font=("Agency FB",15)).place(x=65, y=160)
    txtprofpasswd=Entry(ventana,textvariable=entradaP,font=("Agency FB",15))
    txtprofpasswd.place(x=65,y=195)
    nprof= txtprof.get()
    pprof= txtprofpasswd.get()
    def login1():
        sql1="SELECT COUNT(Id_prof) FROM profesores WHERE Nom_prof='" + nprof + "'"
        sql2="SELECT COUNT(Id_prof) FROM profesores WHERE Id_prof='" + pprof + "'"
        if((cursor.execute(sql1))==1 and (cursor.execute(sql2))==1):
            db.commit()
            print ("Usuario Correcto")
            ventanaProfesores()        
        else:
            print("El usuario no existe o esta incorrecto")



    aceptarautprof=Button(ventana,text="Aceptar", command= login1,font=("Agency FB",15)).place(x=265, y=145, width=100, height=30)

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
    def login2():
        esql1="SELECT COUNT(Id_est) FROM estudiantes WHERE Nom_est='" + usre + "'"
        esql2="SELECT COUNT(Id_est) FROM estudiantes WHERE Id_est='" + pssw + "'"
        if((cursor.execute(esql1))==1 and (cursor.execute(esql2))==1):
            db.commit()
            print ("Usuario Correcto")
            ventanaestudiante()        
        else:
            print("El usuario no existe o esta incorrecto")    

    Button(ventana,text="Comprobacion", command=ventanaestudiante,font =("Agency FB",15)).place(x=265, y=145, width=100, height=30)



def ventanaestudiante():
    ventana.withdraw()
    win=Toplevel()
    win.geometry("450x300+200+200")
    win.title("Sistema Estudiantes")
    elegir=Label(win,text="Por favor escoja una materia: ",font=("Agency FB",15)).place(x=60, y=20)
    listaMat=ttk.Combobox(win,state ="readonly",font=("Agency FB",15))
    listaMat.place(x=160, y=60,width=200,height=30)
    listaMat['values']=['Programacion','Sistemas','Algoritmos']

def ventanaprog():
    ventana.withdraw()
    win=Toplevel()
    win.geometry("450x300+200+200")
    win.title("Nota Programacion")

def ventanaProfesores():
    entradaPM1=StringVar()
    entradaPM2=StringVar()
    ventana.withdraw()
    winPro=Toplevel()
    winPro.geometry("450x300+200+200")
    winPro.title("Validacion Profesores")
    elegir=Label(winPro,text="Por favor escoja su materia: ",font=("Agency FB",15)).place(x=60, y=20)
    clavemat=Label(winPro,text="Por favor ingrese la clave de la materia: ",font=("Agency FB",15)).place(x=60, y=120)
    passwdMat=Entry(winPro,textvariable=entradaPM1,font=("Helvetica",15))
    passwdMat.place(x=65,y=150)
    claveid=Label(winPro,text="Por favor ingrese su id de profesor: ",font=("Agency FB",15)).place(x=60, y=180)
    passwdid=Entry(winPro,textvariable=entradaPM2,font=("Helvetica",15))
    passwdid.place(x=65,y=210)

    def comprobarmateria():
        pmat=passwdMat.get()
        pid=passwdid.get()
        if (pmat=='201901' and pid=='33301'):
            EditProf1()

        if(pmat=='201902' and pid=='33302'):
            EditProf2()
        
        if(pmat=='201903' and pid=='33303'):
            EditProf3()
        
        else:
            print("Los valores ingresados no corresponden")
        
    botonmateria=Button(winPro,text="Validar", command=comprobarmateria, font=("Agency FB",15)).place(x=300,y=195,width=100)    
        

def IngnotP():
    entradaNP=StringVar()
    entradaID=StringVar()
    ventana.withdraw()
    wining1=Toplevel()
    wining1.geometry("450x300+200+200")
    wining1.title("NOTA PROGRAMACION")
    lnotap=Label(wining1,text="Por favor ingrese la nota de la materia: ",font=("Agency FB",15)).place(x=60, y=120)
    txtnotap=Entry(wining1,textvariable=entradaNP,font=("Helvetica",15))
    txtnotap.place(x=65,y=150)
    lid_est=Label(wining1,text="Por favor ingrese el id del estudiante: ",font=("Agency FB",15)).place(x=60, y=180)
    txtid_est=Entry(wining1,textvariable=entradaID,font=("Helvetica",15))
    txtid_est.place(x=65,y=210)    
    def obtenernota1():
        id_est_in=txtid_est.get()
        notap = txtnotap.get()       
        in_notap="INSERT INTO notas (Id_materiaFK, Id_estFK, Nota) VALUES (201901,'"+id_est_in+"','"+notap+"')"        
        cursor.execute(in_notap)
        db.commit()
        print("Ingreso Correcto")
        txtnotap.delete(0,'end')
        txtid_est.delete(0,'end')
        
    mostrar_reg1=Button(wining1,text="Registrar",command=obtenernota1,font=("Agency FB",15)).place(x=300, y=190,width=100)


def ednotP():
    entradaidest=StringVar()
    entradane1=StringVar()
    entradane2=StringVar()
    ventana.withdraw()
    wineditp=Toplevel()
    wineditp.geometry("450x300")
    wineditp.title("EDITAR NOTA PROGRAMACION")
    lid_est1=Label(wineditp,text="Por favor ingrese el id del estudiante: ",font =("Agency FB",15)).place(x=65, y=20)    
    txtidest_1=Entry(wineditp,textvariable=entradaidest,font=("Agency FB",15))
    txtidest_1.place(x=65,y=55)
    lnotae1=Label(wineditp,text="Por favor ingrese la nota a editar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtep=Entry(wineditp,textvariable=entradane1,font=("Agency FB",15))
    txtep.place(x=65,y=125)
    lnotae2=Label(wineditp,text="Por favor ingrese la nueva nota: ",font =("Agency FB",15)).place(x=65, y=160)    
    txtnp=Entry(wineditp,textvariable=entradane2,font=("Agency FB",15))
    txtnp.place(x=65,y=195)    
    def editarnota1():
        id_est_ed=txtidest_1.get()
        notae1 = txtep.get()
        notae2 = txtnp.get()
        int_id_est_ed=int(id_est_ed)
        #int_notae1=int(notae1)
        int_notae2=int(notae2)       
        editp="UPDATE notas SET Id_materiaFK=201901 , Id_estFK=%s , Nota=%s WHERE Nota='"+notae1+"' "
        val=(int_id_est_ed,int_notae2)
        cursor.execute(editp,val)
        db.commit()
        print("Las notas fueron actualizadas correctamente")
        txtidest_1.delete(0,'end')
        txtep.delete(0,'end')
        txtnp.delete(0,'end')

    mostrar_edit1=Button(wineditp,text="Registrar",command=editarnota1,font=("Agency FB",15)).place(x=300, y=190,width=100)   
        

def elimnotP():
    entradanelim1=StringVar()
    ventana.withdraw()
    winelimp=Toplevel()
    winelimp.geometry("450x300")
    winelimp.title("ELIMINAR NOTA PROGRAMACION")
    lnotelm1=Label(winelimp,text="Por favor ingrese la nota a eliminar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtelip=Entry(winelimp,textvariable=entradanelim1,font=("Agency FB",15))
    txtelip.place(x=65,y=125)
    def eliminarnota1():

        notaelim1 = txtelip.get()     
        elimnota1="DELETE FROM notas WHERE nota = '"+notaelim1+"'"
        cursor.execute(elimnota1)
        db.commit()
        print("La nota fue eliminada correctamente")
        txtelip.delete(0,'end')
         
    mostrar_elim1=Button(winelimp,text="Eliminar",command=eliminarnota1,font=("Agency FB",15)).place(x=300, y=140,width=100)

def PromnotP():
    entradaprom1=StringVar()
    salidaprom1=StringVar()
    ventana.withdraw()
    winprom_p=Toplevel()
    winprom_p.geometry("450x300")
    winprom_p.title("PROMEDIO DE ESTUDIANTES PROGRAMACION")
    lprom1=Label(winprom_p,text="Por favor ingrese el ID del estudiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txtprom_p=Entry(winprom_p,textvariable=entradaprom1,font=("Agency FB",15))
    txtprom_p.place(x=65,y=125)
    lprom2=Label(winprom_p,text="El promedio del estudiante es: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultp=Label(winprom_p,textvariable=salidaprom1,font=("Agency FB",15))
    lresultp.place(x=65,y=195)
    def promedionota1():
        id_est_prom=txtprom_p.get()
        promnota1="SELECT AVG(Nota) FROM notas WHERE Id_estFK='"+id_est_prom+"' "
        salidaprom1.set(cursor.execute(promnota1))        
        db.commit()

        print("El promedio fue mostrado correctamente")

    mostrar_prom1=Button(winprom_p,text="Mostrar",command=promedionota1,font=("Agency FB",15)).place(x=300, y=140,width=100)    


def MaxMinP():
    entradamax1=StringVar()
    salidamax1=StringVar()
    salidamax2=StringVar()
    ventana.withdraw()
    winmax_p=Toplevel()
    winmax_p.geometry("450x300")
    winmax_p.title("NOTAS MAXIMAS Y MINIMAS PROGRAMACION")
    lmax1=Label(winmax_p,text="Por favor ingrese el ID del estidiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txtmax_p=Entry(winmax_p,textvariable=entradamax1,font=("Agency FB",15))
    txtmax_p.place(x=65,y=125)
    lmax2=Label(winmax_p,text="La nota Maxima del estudiante es: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultmaxp=Label(winmax_p,textvariable=salidamax1,font=("Agency FB",15))
    lresultmaxp.place(x=65,y=195)
    lmax3=Label(winmax_p,text="La nota Minima del estudiante es: ",font =("Agency FB",15)).place(x=65, y=230)
    lresultminp=Label(winmax_p,textvariable=salidamax2,font=("Agency FB",15))
    lresultminp.place(x=65,y=265)    
    def maxnota1():
        id_est_max=txtmax_p.get()
        maxnota1="SELECT MAX(Nota) FROM notas WHERE Id_estFK='"+id_est_max+"' "
        minnota1="SELECT MIN(Nota) FROM notas WHERE Id_estFK='"+id_est_max+"' "
        salidamax1.set(cursor.execute(maxnota1)) 
        salidamax2.set(cursor.execute(minnota1))       
        db.commit()

        print("Las notas maximas y minimas fueron mostradas correctamente")

    mostrar_max1=Button(winmax_p,text="Mostrar",command=maxnota1,font=("Agency FB",15)).place(x=300, y=140,width=100)     


def TotalnotP():
    entradatot1=StringVar()
    salidatot1=StringVar()
    ventana.withdraw()
    wintot_p=Toplevel()
    wintot_p.geometry("450x300")
    wintot_p.title("TOTAL DE NOTAS PROGRAMACION")
    ltot1=Label(wintot_p,text="Por favor ingrese el ID del estudiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txttot_p=Entry(wintot_p,textvariable=entradatot1,font=("Agency FB",15))
    txttot_p.place(x=65,y=125)
    ltot2=Label(wintot_p,text="Las notas del Estudiante son: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultotp=Label(wintot_p,textvariable=salidatot1,font=("Agency FB",15))
    lresultotp.place(x=65,y=195)
    def total1():
        id_est_tot=txttot_p.get()
        totnota1="SELECT * FROM notas WHERE Id_estFK='"+id_est_tot+"' "
        salidatot1.set(cursor.execute(totnota1))        
        db.commit()

        print("El total de notas fue mostrado correctamente")

    mostrar_tot1=Button(wintot_p,text="Mostrar",command=total1,font=("Agency FB",15)).place(x=300, y=140,width=100) 





def EditProf1():

    edit1=Toplevel()
    edit1.geometry("600x200")
    edit1.title("Sistema Profesores Programacion")
    seleccionar=Label(edit1,text="Por favor escoja una opcion: ",font=("Agency FB",15)).place(x=60, y=20)
    ingNot1=Button(edit1,text="Ingresar Notas",command= IngnotP,font =("Agency FB",15)).place(x=100, y=60,width=100)
    edNot1=Button(edit1,text="Editar Notas",command= ednotP,font =("Agency FB",15)).place(x=220, y=60,width=100)
    ElimNot1=Button(edit1,text="Eliminar Notas",command= elimnotP,font =("Agency FB",15)).place(x=340, y=60,width=100)
    prom=Button(edit1,text="Promedio Materia",command=PromnotP,font =("Agency FB",15)).place(x=100, y=120,width=110)
    MaxMin=Button(edit1,text="Nota Maxima y Nota Minima",command=MaxMinP,font =("Agency FB",15)).place(x=220, y=120,width=180)
    mosTod=Button(edit1,text="Mostrar todo",command=TotalnotP,font =("Agency FB",15)).place(x=420, y=120,width=100)


def IngnotS():
    entradaNS=StringVar()
    entradaID=StringVar()
    ventana.withdraw()
    wining2=Toplevel()
    wining2.geometry("450x300+200+200")
    wining2.title("NOTA SISTEMAS")
    lnotas=Label(wining2,text="Por favor ingrese la nota de la materia: ",font=("Agency FB",15)).place(x=60, y=120)
    txtnotas=Entry(wining2,textvariable=entradaNS,font=("Helvetica",15))
    txtnotas.place(x=65,y=150)
    lid_ests=Label(wining2,text="Por favor ingrese el id del estudiante: ",font=("Agency FB",15)).place(x=60, y=180)
    txtid_ests=Entry(wining2,textvariable=entradaID,font=("Helvetica",15))
    txtid_ests.place(x=65,y=210)    
    def obtenernota2():
        id_est_in=txtid_ests.get()
        nota_so = txtnotas.get()       
        in_notas="INSERT INTO notas (Id_materiaFK, Id_estFK, Nota) VALUES (201902,'"+id_est_in+"','"+nota_so+"')"        
        cursor.execute(in_notas)
        db.commit()
        print("Ingreso Correcto")
        txtnotas.delete(0,'end')
        txtid_ests.delete(0,'end')
        
    mostrar_reg2=Button(wining2,text="Registrar",command=obtenernota2,font=("Agency FB",15)).place(x=300, y=190,width=100)

def ednotS():
    entradaidest_s=StringVar()
    entradane_s1=StringVar()
    entradane_s2=StringVar()
    ventana.withdraw()
    winedits=Toplevel()
    winedits.geometry("450x300")
    winedits.title("EDITAR NOTA SISTEMAS")
    lid_est2=Label(winedits,text="Por favor ingrese el id del estudiante: ",font =("Agency FB",15)).place(x=65, y=20)    
    txtidest_2=Entry(winedits,textvariable=entradaidest_s,font=("Agency FB",15))
    txtidest_2.place(x=65,y=55)
    lnotaes1=Label(winedits,text="Por favor ingrese la nota a editar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtes=Entry(winedits,textvariable=entradane_s1,font=("Agency FB",15))
    txtes.place(x=65,y=125)
    lnotaes2=Label(winedits,text="Por favor ingrese la nueva nota: ",font =("Agency FB",15)).place(x=65, y=160)    
    txtns=Entry(winedits,textvariable=entradane_s2,font=("Agency FB",15))
    txtns.place(x=65,y=195)    
    def editarnota2():
        id_est_eds=txtidest_2.get()
        notaes1 = txtes.get()
        notaes2 = txtns.get()
        int_id_est_eds=int(id_est_eds)
        #int_notae1=int(notae1)
        int_notaes2=int(notaes2)       
        edits="UPDATE notas SET Id_materiaFK=201902 , Id_estFK=%s , Nota=%s WHERE Nota='"+notaes1+"' "
        vals=(int_id_est_eds,int_notaes2)
        cursor.execute(edits,vals)
        db.commit()
        print("Las notas fueron actualizadas correctamente")
        txtidest_2.delete(0,'end')
        txtes.delete(0,'end')
        txtns.delete(0,'end')

    mostrar_edit2=Button(winedits,text="Registrar",command=editarnota2,font=("Agency FB",15)).place(x=300, y=190,width=100)     

def elimnotS():
    entradanelim2=StringVar()
    ventana.withdraw()
    winelims=Toplevel()
    winelims.geometry("450x300")
    winelims.title("ELIMINAR NOTA SISTEMAS")
    lnotelm2=Label(winelims,text="Por favor ingrese la nota a eliminar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txtelis=Entry(winelims,textvariable=entradanelim2,font=("Agency FB",15))
    txtelis.place(x=65,y=125)
    def eliminarnota2():

        notaelim2 = txtelis.get()     
        elimnota2="DELETE FROM notas WHERE nota = '"+notaelim2+"'"
        cursor.execute(elimnota2)
        db.commit()
        print("La nota fue eliminada correctamente")
        txtelis.delete(0,'end')
         
    mostrar_elim2=Button(winelims,text="Eliminar",command=eliminarnota2,font=("Agency FB",15)).place(x=300, y=140,width=100)


def PromnotS():
    entradaprom2=StringVar()
    salidaprom2=StringVar()
    ventana.withdraw()
    winprom_s=Toplevel()
    winprom_s.geometry("450x300")
    winprom_s.title("PROMEDIO DE ESTUDIANTES SISTEMAS")
    lprom_s1=Label(winprom_s,text="Por favor ingrese el ID del estudiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txtprom_s=Entry(winprom_s,textvariable=entradaprom2,font=("Agency FB",15))
    txtprom_p.place(x=65,y=125)
    lprom2=Label(winprom_s,text="El promedio del estudiante es: ",font =("Agency FB",15)).place(x=65, y=160)
    lresults=Label(winprom_s,textvariable=salidaprom2,font=("Agency FB",15))
    lresults.place(x=65,y=195)
    def promedionota2():
        id_est_proms=txtprom_s.get()
        promnota2="SELECT AVG(Nota) FROM notas WHERE Id_estFK='"+id_est_proms+"' "
        salidaprom2.set(cursor.execute(promnota2))        
        db.commit()

        print("El promedio fue mostrado correctamente")

    mostrar_prom2=Button(winprom_s,text="Mostrar",command=promedionota2,font=("Agency FB",15)).place(x=300, y=140,width=100)    


def MaxMinS():
    entradamax2=StringVar()
    salidamax1_s=StringVar()
    salidamax2_s=StringVar()
    ventana.withdraw()
    winmax_s=Toplevel()
    winmax_s.geometry("450x300")
    winmax_s.title("NOTAS MAXIMAS Y MINIMAS SISTEMAS")
    lmax1_s=Label(winmax_s,text="Por favor ingrese el ID del estidiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txtmax_s=Entry(winmax_s,textvariable=entradamax2,font=("Agency FB",15))
    txtmax_s.place(x=65,y=125)
    lmax2_s=Label(winmax_s,text="La nota Maxima del estudiante es: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultmaxs=Label(winmax_s,textvariable=salidamax1_s,font=("Agency FB",15))
    lresultmaxs.place(x=65,y=195)
    lmax3_s=Label(winmax_s,text="La nota Minima del estudiante es: ",font =("Agency FB",15)).place(x=65, y=230)
    lresultmins=Label(winmax_s,textvariable=salidamax2_s,font=("Agency FB",15))
    lresultmins.place(x=65,y=265)    
    def maxnota2():
        id_est_maxs=txtmax_s.get()
        maxnota1_s="SELECT MAX(Nota) FROM notas WHERE Id_estFK='"+id_est_maxs+"' "
        minnota1_s="SELECT MIN(Nota) FROM notas WHERE Id_estFK='"+id_est_maxs+"' "
        salidamax1_s.set(cursor.execute(maxnota1_s)) 
        salidamax2_s.set(cursor.execute(minnota1_s))       
        db.commit()

        print("Las notas maximas y minimas fueron mostradas correctamente")

    mostrar_max2=Button(winmax_s,text="Mostrar",command=maxnota2,font=("Agency FB",15)).place(x=300, y=140,width=100)     


def TotalnotS():
    entradatot2=StringVar()
    salidatot2=StringVar()
    ventana.withdraw()
    wintot_s=Toplevel()
    wintot_s.geometry("450x300")
    wintot_s.title("TOTAL DE NOTAS SISTEMAS")
    ltot1_s=Label(wintot_s,text="Por favor ingrese el ID del estudiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txttot_s=Entry(wintot_s,textvariable=entradatot2,font=("Agency FB",15))
    txttot_s.place(x=65,y=125)
    ltot2_s=Label(wintot_s,text="Las notas del Estudiante son: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultots=Label(wintot_s,textvariable=salidatot2,font=("Agency FB",15))
    lresultots.place(x=65,y=195)
    def total2():
        id_est_tots=txttot_s.get()
        totnota2="SELECT * FROM notas WHERE Id_estFK='"+id_est_tots+"' "
        salidatot2.set(cursor.execute(totnota2))        
        db.commit()

        print("El total de notas fue mostrado correctamente")

    mostrar_tot2=Button(wintot_s,text="Mostrar",command=total2,font=("Agency FB",15)).place(x=300, y=140,width=100) 

    
def EditProf2():
    #entradaPM=StringVar()
    #winPro.withdraw()
    edit_s=Toplevel()
    edit_s.geometry("600x200")
    edit_s.title("Sistema Profesores Sistemas Operativos")
    seleccionar_s=Label(edit_s,text="Por favor escoja una opcion: ",font=("Agency FB",15)).place(x=60, y=20)
    ingNot_s=Button(edit_s,text="Ingresar Notas",command= IngnotS,font =("Agency FB",15)).place(x=100, y=60,width=100)
    edNot_s=Button(edit_s,text="Editar Notas",command= ednotS,font =("Agency FB",15)).place(x=220, y=60,width=100)
    ElimNot_s=Button(edit_s,text="Eliminar Notas",command= elimnotS,font =("Agency FB",15)).place(x=340, y=60,width=100)
    prom_s=Button(edit_s,text="Promedio Materia",command=PromnotS,font =("Agency FB",15)).place(x=100, y=120,width=110)
    MaxMin_s=Button(edit_s,text="Nota Maxima y Nota Minima",command=MaxMinS,font =("Agency FB",15)).place(x=220, y=120,width=180)
    mosTod_s=Button(edit_s,text="Mostrar todo",command=TotalnotS,font =("Agency FB",15)).place(x=420, y=120,width=100)


def IngnotA():
    entradaNA=StringVar()
    entradaID=StringVar()
    ventana.withdraw()
    wining3=Toplevel()
    wining3.geometry("450x300+200+200")
    wining3.title("NOTA ALGORTIMOS")
    lnotas=Label(wining3,text="Por favor ingrese la nota de la materia: ",font=("Agency FB",15)).place(x=60, y=120)
    txtnotaA=Entry(wining3,textvariable=entradaNA,font=("Helvetica",15))
    txtnotaA.place(x=65,y=150)
    lid_estA=Label(wining3,text="Por favor ingrese el id del estudiante: ",font=("Agency FB",15)).place(x=60, y=180)
    txtid_estA=Entry(wining3,textvariable=entradaID,font=("Helvetica",15))
    txtid_estA.place(x=65,y=210)    
    def obtenernota3():
        id_est_in=txtid_estA.get()
        nota_A = txtnotaA.get()       
        in_notaA="INSERT INTO notas (Id_materiaFK, Id_estFK, Nota) VALUES (201903,'"+id_est_in+"','"+nota_A+"')"        
        cursor.execute(in_notaA)
        db.commit()
        print("Ingreso Correcto")
        txtnotaA.delete(0,'end')
        txtid_estA.delete(0,'end')
        
    mostrar_reg3=Button(wining3,text="Registrar",command=obtenernota3,font=("Agency FB",15)).place(x=300, y=190,width=100)

def ednotA():
    entradaidest_A=StringVar()
    entradane_A1=StringVar()
    entradane_A2=StringVar()
    ventana.withdraw()
    wineditA=Toplevel()
    wineditA.geometry("450x300")
    wineditA.title("EDITAR NOTA ALGORITMOS")
    lid_est3=Label(wineditA,text="Por favor ingrese el id del estudiante: ",font =("Agency FB",15)).place(x=65, y=20)    
    txtidest_3=Entry(wineditA,textvariable=entradaidest_A,font=("Agency FB",15))
    txtidest_3.place(x=65,y=55)
    lnotaeA1=Label(wineditA,text="Por favor ingrese la nota a editar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txteA=Entry(wineditA,textvariable=entradane_A1,font=("Agency FB",15))
    txteA.place(x=65,y=125)
    lnotaeA2=Label(wineditA,text="Por favor ingrese la nueva nota: ",font =("Agency FB",15)).place(x=65, y=160)    
    txtnA=Entry(wineditA,textvariable=entradane_A2,font=("Agency FB",15))
    txtnA.place(x=65,y=195)    
    def editarnota3():
        id_est_edA=txtidest_3.get()
        notaeA1 = txteA.get()
        notaeA2 = txtnA.get()
        int_id_est_edA=int(id_est_edA)
        #int_notae1=int(notae1)
        int_notaeA2=int(notaeA2)       
        editA="UPDATE notas SET Id_materiaFK=201903 , Id_estFK=%s , Nota=%s WHERE Nota='"+notaeA1+"' "
        valA=(int_id_est_edA,int_notaeA2)
        cursor.execute(editA,valA)
        db.commit()
        print("Las notas fueron actualizadas correctamente")
        txtidest_3.delete(0,'end')
        txteA.delete(0,'end')
        txtnA.delete(0,'end')

    mostrar_edit3=Button(wineditA,text="Registrar",command=editarnota3,font=("Agency FB",15)).place(x=300, y=190,width=100)    

def elimnotA():
    entradanelim3=StringVar()
    ventana.withdraw()
    winelimA=Toplevel()
    winelimA.geometry("450x300")
    winelimA.title("ELIMINAR NOTA ALGORITMOS")
    lnotelm3=Label(winelimA,text="Por favor ingrese la nota a eliminar: ",font =("Agency FB",15)).place(x=65, y=90)    
    txteliA=Entry(winelimA,textvariable=entradanelim3,font=("Agency FB",15))
    txteliA.place(x=65,y=125)
    def eliminarnota3():

        notaelim3 = txteliA.get()     
        elimnota3="DELETE FROM notas WHERE nota = '"+notaelim3+"'"
        cursor.execute(elimnota3)
        db.commit()
        print("La nota fue eliminada correctamente")
        txteliA.delete(0,'end')
         
    mostrar_elim3=Button(winelimA,text="Eliminar",command=eliminarnota3,font=("Agency FB",15)).place(x=300, y=140,width=100)


def PromnotA():
    entradaprom3=StringVar()
    salidaprom3=StringVar()
    ventana.withdraw()
    winprom_A=Toplevel()
    winprom_A.geometry("450x300")
    winprom_A.title("PROMEDIO DE ESTUDIANTES ALGORITMOS")
    lprom_A1=Label(winprom_A,text="Por favor ingrese el ID del estudiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txtprom_A=Entry(winprom_A,textvariable=entradaprom3,font=("Agency FB",15))
    txtprom_A.place(x=65,y=125)
    lprom3=Label(winprom_A,text="El promedio del estudiante es: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultA=Label(winprom_A,textvariable=salidaprom3,font=("Agency FB",15))
    lresultA.place(x=65,y=195)
    def promedionota3():
        id_est_promA=txtprom_A.get()
        promnota3="SELECT AVG(Nota) FROM notas WHERE Id_estFK='"+id_est_promA+"' "
        salidaprom3.set(cursor.execute(promnota3))        
        db.commit()

        print("El promedio fue mostrado correctamente")

    mostrar_prom3=Button(winprom_A,text="Mostrar",command=promedionota3,font=("Agency FB",15)).place(x=300, y=140,width=100)    


def MaxMinS():
    entradamax3=StringVar()
    salidamax1_A=StringVar()
    salidamax2_A=StringVar()
    ventana.withdraw()
    winmax_A=Toplevel()
    winmax_A.geometry("450x300")
    winmax_A.title("NOTAS MAXIMAS Y MINIMAS ALGORITMOS")
    lmax1_A=Label(winmax_A,text="Por favor ingrese el ID del estidiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txtmax_A=Entry(winmax_A,textvariable=entradamax3,font=("Agency FB",15))
    txtmax_A.place(x=65,y=125)
    lmax2_A=Label(winmax_A,text="La nota Maxima del estudiante es: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultmaxA=Label(winmax_A,textvariable=salidamax1_A,font=("Agency FB",15))
    lresultmaxA.place(x=65,y=195)
    lmax3_A=Label(winmax_A,text="La nota Minima del estudiante es: ",font =("Agency FB",15)).place(x=65, y=230)
    lresultminA=Label(winmax_A,textvariable=salidamax2_A,font=("Agency FB",15))
    lresultminA.place(x=65,y=265)    
    def maxnota3():
        id_est_maxA=txtmax_A.get()
        maxnota1_A="SELECT MAX(Nota) FROM notas WHERE Id_estFK='"+id_est_maxA+"' "
        minnota1_A="SELECT MIN(Nota) FROM notas WHERE Id_estFK='"+id_est_maxA+"' "
        salidamax1_A.set(cursor.execute(maxnota1_A)) 
        salidamax2_A.set(cursor.execute(minnota1_A))       
        db.commit()

        print("Las notas maximas y minimas fueron mostradas correctamente")

    mostrar_max3=Button(winmax_A,text="Mostrar",command=maxnota3,font=("Agency FB",15)).place(x=300, y=140,width=100)     


def TotalnotA():
    entradatot3=StringVar()
    salidatot3=StringVar()
    ventana.withdraw()
    wintot_A=Toplevel()
    wintot_A.geometry("450x300")
    wintot_A.title("TOTAL DE NOTAS ALGORTIMOS")
    ltot1_A=Label(wintot_A,text="Por favor ingrese el ID del estudiante a consultar: ",font =("Agency FB",15)).place(x=65, y=90)
    txttot_A=Entry(wintot_A,textvariable=entradatot3,font=("Agency FB",15))
    txttot_A.place(x=65,y=125)
    ltot2_A=Label(wintot_A,text="Las notas del Estudiante son: ",font =("Agency FB",15)).place(x=65, y=160)
    lresultotA=Label(wintot_A,textvariable=salidatot3,font=("Agency FB",15))
    lresultotA.place(x=65,y=195)
    def total3():
        id_est_totA=txttot_A.get()
        totnota3="SELECT * FROM notas WHERE Id_estFK='"+id_est_totA+"' "
        salidatot3.set(cursor.execute(totnota3))        
        db.commit()

        print("El total de notas fue mostrado correctamente")

    mostrar_tot3=Button(wintot_A,text="Mostrar",command=total3,font=("Agency FB",15)).place(x=300, y=140,width=100) 







def EditProf3():
    #entradaPM=StringVar()
    #winPro.withdraw()
    edit_A=Toplevel()
    edit_A.geometry("600x200")
    edit_A.title("Sistema Profesores Algoritmos")
    seleccionarA=Label(edit_A,text="Por favor escoja una opcion: ",font=("Agency FB",15)).place(x=60, y=20)
    ingNotA=Button(edit_A,text="Ingresar Notas",command= IngnotA,font =("Agency FB",15)).place(x=100, y=60,width=100)
    edNotA=Button(edit_A,text="Editar Notas",command= ednotA,font =("Agency FB",15)).place(x=220, y=60,width=100)
    ElimNotA=Button(edit_A,text="Eliminar Notas",command= elimnotA,font =("Agency FB",15)).place(x=340, y=60,width=100)
    promA=Button(edit_A,text="Promedio Materia",command=PromnotP,font =("Agency FB",15)).place(x=100, y=120,width=110)
    MaxMinA=Button(edit_A,text="Nota Maxima y Nota Minima",command=MaxMinA,font =("Agency FB",15)).place(x=220, y=120,width=180)
    mosTodA=Button(edit_A,text="Mostrar todo",command=TotalnotA,font =("Agency FB",15)).place(x=420, y=120,width=100)


    




  





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
db.close
ventana.mainloop() #ventana permanezca abierta


