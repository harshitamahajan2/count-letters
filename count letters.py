from tkinter import *
root=Tk()
root.geometry('500x500')
root.maxsize(600,600)
def f1():
    a=txt.get()
    l=0
    u=0
    w=0
    r=0
    q=0
    t=0
    v=0
    j=0  
    for i in a:
        if i.islower():
            l=l+1
            
        elif i.isupper():
            u=u+1
    
        elif i.isdigit():
            q=q+1

        elif i.isspace():
            r=r+1
        
        else:
            w=w+1
    k=a.split(' ')
    t=len(k)
    for i in a:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            v=v+1
        else:
            j=j+1

    
            
            
    x=f''
total no of upper:  {u}        
total no of lower:  {l}        
total no of digit:  {q}
total no of space:  {r}        
total no of sp char:{w}
total no of words:  {t}
total no of vowels: {v}
total no of consonants:{j}
''
    s.config(text=x)

    
txt=StringVar()

Label(root,text='characters count',font='algerian 12').place(x=200, y=0)
Label(root,text='enter your text',font='aerial 12').place(x=2, y=20)
Entry(root,textvariable=txt,font='arial 11').place(x=2, y=40)
Button(root,text='count',command=f1).place(x=20, y=60)
Label(root,text=' your text',font='aerial 12').place(x=2, y=200)
s=Label()
s.place(x=2,y=220)
root.mainloop()
