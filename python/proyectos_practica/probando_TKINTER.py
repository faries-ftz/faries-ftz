import random
import tkinter
#tkinter es una interfaz grafica que se dice viene instalada en windows, para linux se necesita intalarla 
def grafica():
    ven=tkinter.Tk()#qui asignas -ven- como ventana grafica
    ven.geometry("300x300") #por default tiene un tamaño pequeño, aqui especificamos sus dimenciones
    ven.mainloop()

x=int(input("put a number: "))
def guess(x):
    ran_num=random.randint(1,x)
    print(f"su numero es {x}")
guess(x)
grafica()
