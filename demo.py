from tkinter import *


def rename(path,prefix,extension):
    



window = Tk()

window.title("Bulk File Renamer")
window.geometry('600x400')

heading = Label(window, text="Bulk File Renamer",font=("Arial Bold",20))
heading.grid(column=0, row=0,columnspan=2)

path  = StringVar()
Label(window, text='FILE PATH').grid(row=1,column=0)
pathentry = Entry(window,textvariable= path,width=40,font=("Verdana", 15))
pathentry.grid(row=1,column=1,pady=5)

prefix  = StringVar()
Label(window, text='Prefix').grid(row=2,column=0)
prefixentry = Entry(window,textvariable= prefix,width=40,font=("Verdana", 15))
prefixentry.grid(row=2,column=1,pady=5)

extension  = StringVar()
Label(window, text='Extension').grid(row=3,column=0)
entensionentry = Entry(window,textvariable= extension,width=40,font=("Verdana", 15))
entensionentry.grid(row=3,column=1,pady=5)


submitButton = Button(window, text="Submit",width=10,command=lambda: rename(pathentry.get(),prefixentry.get(),entensionentry.get()))


window.mainloop()









