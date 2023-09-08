from tkinter import *
ventana = Tk()
ventana.title("Banda")
ventana.geometry("920x496")
imagenI = PhotoImage (file="Imagenes/Guitarra_i.png")
imagenI1 = PhotoImage (file="Imagenes/Bajo_i.png")
lblImegen=Label(ventana,image=imagenI).place(x=0,y=0)
lblImegen1=Label(ventana,image=imagenI1).place(x=400,y=0)
ventana.mainloop()