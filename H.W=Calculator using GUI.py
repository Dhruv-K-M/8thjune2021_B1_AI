import tkinter as t

ap = t.Tk()
ap.title('calculator')
ap.geometry('500x600')
ap.configure(bg='dark green')

result = t.Variable(ap)
result.set('Result')
t.Label(ap,textvariable = result,bg='olive',height='5',width='42',font=('calibre',15,'bold')).place(x=0,y=0)


p=''

def string(h):
    global p
    p+=h
    
    result.set(p)

def ans():
    global p
    result.set(eval(p))
    
def clear():
    global p
    p=''
    result.set(p)

def back():
    global p
    p=p[:-1]
    result.set(p)


# 1st row
t.Button(ap,text='1',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('1')).place(x=30,y=150)
t.Button(ap,text='2',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('2')).place(x=150,y=150)
t.Button(ap,text='3',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('3')).place(x=270,y=150)
t.Button(ap,text='+',bg='yellow',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('+')).place(x=390,y=150)   

#2nd row    
t.Button(ap,text='4',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('4')).place(x=30,y=250)
t.Button(ap,text='5',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('5')).place(x=150,y=250)
t.Button(ap,text='6',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('6')).place(x=270,y=250)
t.Button(ap,text='-',bg='yellow',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('-')).place(x=390,y=250)

#3rd row
t.Button(ap,text='7',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('7')).place(x=30,y=350)
t.Button(ap,text='8',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('8')).place(x=150,y=350)
t.Button(ap,text='9',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('9')).place(x=270,y=350)
t.Button(ap,text='*',bg='yellow',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('*')).place(x=390,y=350)

#4th row
t.Button(ap,text='.',bg='yellow',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('.')).place(x=30,y=450)
t.Button(ap,text='0',bg='cyan',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('0')).place(x=150,y=450)
t.Button(ap,text='/',bg='yellow',height='3',width='10',font=('calibre',10,'bold'),command= lambda:string('/')).place(x=270,y=450)
t.Button(ap,text='=',bg='yellow',height='3',width='10',font=('calibre',10,'bold'),command= lambda:ans()).place(x=390,y=450)
#clear and back button
t.Button(ap,text='Clear',bg='orange',height='3',width='10',font=('calibre',10,'bold'),command= lambda:clear()).place(x=0,y=0)
t.Button(ap,text='Back',bg='orange',height='3',width='10',font=('calibre',10,'bold'),command= lambda:back()).place(x=410,y=0)


ap.mainloop()
