from tkinter import *
from tkinter import ttk


#Funciones botones

def Inicio():
    def Sali2():
        ventanaInicio.destroy()
        ventana.destroy()
        
    ventanaInicio = Tk()
    #ventanaInicio.geometry('1024x720')
    ventanaInicio.fullScreenState = True
    ventanaInicio.attributes("-fullscreen", True)
    ventanaInicio.title("Partículas")
    ventanaInicio.config(bg="skyblue")
    btn3 = Button(ventanaInicio, text="Salir", bg="black", fg="white", command = Sali2)
    btn3.place(relx=0.5, rely=0.68, relwidth=0.06, relheight=0.05)
    btn2 = Button(ventanaInicio, text="Gráficar", bg="black", fg="white", command = Sali2)
    btn2.place(relx=0.5, rely=0.6, relwidth=0.06, relheight=0.05)
    combo = ttk.Combobox(ventanaInicio, state="readonly")
    combo['values']= (1, 2, 3, 4, 5, "Text")
    combo.place(relx=0.4, rely=0.6, relwidth=0.06, relheight=0.05)
    lbl = Label(ventanaInicio, text="TRAYECTORIA DE LA PARTICULA", font =("Arial Bond",30), bg="skyblue", fg="white")
    lbl.place(relx=0.3, rely=0.15)
    ventana.iconify()
    ventanaInicio.mainloop()
    
    
def Salir():
    ventana.destroy()
    

   
    
    
ventana = Tk()
#ventana.geometry('1024x720')
ventana.fullScreenState = True
ventana.attributes("-fullscreen", True)
ventana.bind("<Escape>", False)
ventana.title("Inicio")
ventana.config(bg="black")
lbl = Label(ventana, text="TRAYECTORIA DE DISTINTAS PARTICULAS EN UN CAMPO ELECTRICO", font =("Arial Bond",30), bg="black", fg="yellow")
lbl.place(relx=0.07, rely=0.15)
btn = Button(ventana, text="Iniciar", bg="white", fg="black", command=Inicio)
btn.place(relx=0.5, rely=0.6, relwidth=0.06, relheight=0.05)
btn2 = Button(ventana, text="Salir", bg="white", fg="black", command=Salir)
btn2.place(relx=0.5, rely=0.68, relwidth=0.06, relheight=0.05)

ventana.mainloop()


