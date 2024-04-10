from tkinter import *
from random import *
from itertools import *
#def play_again():
#    main()
def play():
    user=compress(["rock","paper","scissor"],[bool(var1.get()),bool(var2.get()),bool(var3.get())])
    user=[i for i in user]
    comp=choice(["rock","paper","scissor"])
    res=Toplevel(game)
    if user[0]==comp:
        label=Label(res,text="TIE \n COMPUTER CHOICE:{}\nUSER CHOICE:{}".format(comp.upper(),user[0].upper()))
        label.pack()
    elif (user[0]=="rock" and comp=="scissor") or (user[0]=="paper" and comp=="rock") or (user[0]=="scissor" and comp=="paper"):
        label=Label(res,text="YOU WIN\nCOMPUTER CHOICE:{}\nUSER CHOICE:{}".format(comp.upper(),user[0].upper()))
        label.pack()
    else:
        label=Label(res,text="YOU LOOSE\nCOMPUTER CHOICE:{}\nUSER CHOICE:{}".format(comp.upper(),user[0].upper()))
        label.pack()
    button=Button(res,text="QUIT",command=quit)
    button.pack()
   #button1.pack()
game=Tk()
var1=IntVar()
var2=IntVar()
var3=IntVar()
label=Label(game,text="ROCK PAPER SCISSOR")
label.pack()
check1=Checkbutton(game,text="ROCK",variable=var1)
check1.pack()
check2=Checkbutton(game,text="PAPER",variable=var2)
check2.pack()
check3=Checkbutton(game,text="SCISSOR",variable=var3)
check3.pack()
button=Button(game,text="OK",command=play)
button.pack()
game.mainloop()
