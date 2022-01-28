import os
from tkinter import *

def rename_file(folderpath,fileprefix,extension):
    print("File renaming process started")
    counter = 1
    for filename in os.listdir(folderpath):
        dst = '{}_{}.{}'.format(fileprefix, counter,extension)
        src = os.path.join(folderpath, filename)
        dst = os.path.join(folderpath, dst)
        print(src,dst)
        os.rename(src, dst)
        counter += 1
    print("File renaming process ended")
    pathentry.delete(0, END)
    prefixentry.delete(0, END)
    extensionentry.delete(0, END)


root = Tk()
root.geometry("600x300")
root.title('Bulk File Rename')

w = Label(root, text="Bulk File Rename",font=("Verdana", 25),bg="yellow")
w.grid(row=0, column=0, columnspan=2,pady=5)

path  = StringVar()
Label(root, text='FILE PATH').grid(row=1,column=0)
pathentry = Entry(root,textvariable= path,width=40,font=("Verdana", 15))
pathentry.grid(row=1,column=1,pady=5)

word = StringVar()
Label(root, text='PREFIX').grid(row=2,column=0)
prefixentry = Entry(root,textvariable= word,width=40,font=("Verdana", 15))
prefixentry.grid(row=2,column=1,pady=5)

extension = StringVar()
Label(root, text='EXTENSION').grid(row=3,column=0)
extensionentry = Entry(root,textvariable= extension,width=40,font=("Verdana", 15))
extensionentry.grid(row=3,column=1,pady=5)

button =Button(root, text='RENAME', command=lambda: rename_file(path.get(),word.get(),extension.get()),font=("Verdana", 15),width=40)
button.grid(row=4,column=1,columnspan=2,pady=5)


root.mainloop()