from tkinter import*

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                value = "Error"
        
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

root = Tk()
root.geometry("300x450")
root.configure(bg='black')
root.resizable(0,0)
root.title("Calculator")
root.wm_iconbitmap("3.ico")

scvalue = StringVar()
scvalue.set("")

screen = Entry(root, textvar = scvalue, font = "lucida 20 bold")
screen.pack(fill= X, padx = 4, pady = 5)

f = Frame(root, bg="grey")
b = Button(f, text= "9", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "8", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "7", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "6", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "5", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "4", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "3", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "2", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "1", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "0", font = "lucida 20 bold",  padx = 16, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "-", font = "lucida 20 bold",  padx = 16, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "*", font = "lucida 20 bold",  padx = 16, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "/", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "%", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "=", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text= "C", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= "+", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
b = Button(f, text= ".", font = "lucida 20 bold",  padx = 15, bg = "red")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>", click)
f.pack()





root.mainloop()