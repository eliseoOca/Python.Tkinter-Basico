from tkinter import *

ventana = Tk()
ventana.title("Mi primera ventana")
ventana.resizable(True, True)
ventana.iconbitmap('icono.png')
ventana.geometry("640x360")
ventana.config(bg="red")
frame = Frame()
frame.pack(side="right", anchor="s")
frame.config(bg="yellow")
frame.config(width="640", height="350")
ventana.mainloop()