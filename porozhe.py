import tkinter
import json

def submit():
    lbl2.configure(text="")
    with open("e:/dms.json")as f:
        dct=json.load(f)
    u=txt.get()
    p=txt1.get()
    if (u in dct and dct[u]==p):
        lbl2.configure(text="username az ghabl vojod dard")
    else:
        dct={}
        dct[u]=p
        with open("e:/dms.json","w")as b:
            json.dump(dct,b)
        lbl2.configure(text="save anjam shod")
        
    
     
def login():
    lbl2.configure(text="")
    with open("E:/dms.json")as f:
        dct2=json.load(f)
    u1=txt.get()
    p1=txt1.get()
    if u1 in dct2 and dct2[u1]==p1:
        lbl2.configure(text='wellcome',fg='green')
    else:
        lbl2.configure(text='error')
def delete():
    lbl2.configure(text="")
    with open("e:/dms.json")as f:
        dct3=json.load(f)
    u3=txt.get()
    p3=txt1.get()
    if u3 in dct3 and dct3[u3]==p3:
        dct3.pop(u3)
    dct4={}
    with open("e:/dms.json","w")as b:
        json.dump(dct4,b)
    lbl2.configure(text='delete anjam shod',fg='red')
    
win=tkinter.Tk()
win.title("Diyaco")
win.geometry("500x200")

lbl=tkinter.Label(win,text="username")
lbl.grid(column=2,row=2)

 

txt=tkinter.Entry(win,width=80)
txt.grid(column=2,row=4)

lbl1=tkinter.Label(win,text="password")
lbl1.grid(column=2,row=6)

txt1=tkinter.Entry(win,width=80)
txt1.grid(column=2,row=8)

lbl2=tkinter.Label(win,text="")
lbl2.grid(column=2,row=30)




btn=tkinter.Button(win,text="submit",command=submit)
btn.grid(column=2,row=200)

btn2=tkinter.Button(win,text="login",command=login)
btn2.grid(column=2,row=150)

btn3=tkinter.Button(win,text="delete",command=delete)
btn3.grid(column=2,row=100)



win.mainloop()
