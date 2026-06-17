from tkinter import *
from PIL import Image, ImageTk


win=Tk()

win.geometry("2000x1500")
win.title("First window")
win.config(bg="slate gray")

bgimg1=Image.open("3.jpg")
bgimg1=bgimg1.resize((1200,800))
bgimg1=ImageTk.PhotoImage(bgimg1)
lbgimg=Label(win, image=bgimg1)
lbgimg.place(x=0, y=0)




lframe=LabelFrame(win, text="Register Now", height=430, width=550, bg="gold2")
lframe.place(x=400, y=50)

img1=Image.open("4.png")
img1=img1.resize((300,300))
img1=ImageTk.PhotoImage(img1)
limg=Label(win, image=img1)
limg.place(x=10, y=50)


#label
la1=Label(lframe, text="User id", fg="black", bg="slate grey",font=('Arial',15),bd=5)
#la1.pack(pady=10, side="bottom")
la1.place(x=50, y=50)

#entry
E1=Entry(lframe,bd=10,font=('arial',15),justify='center')
E1.place(x=200,y=50)
#la1.grid(row=1, column=1)

la1=Label(lframe, text="Password",fg="black",bg="slate grey",font=('Arial',15),bd=4)
# la1.pack(side="left")
la1.place(x=50, y=100)
E2=Entry(lframe,bd=10,show="*",font=(15),justify='center')
E2.place(x=200,y=100,)
#la1.grid(row=2, column=1)

#button
b=Button(lframe,text='Submit',fg='white',bg="steel blue",height='3',width='20',font=('arial',10),bd=4,activebackground='light sky blue',cursor='arrow')
b.place(x=300,y=350)

#radio button
la1=Label(lframe, text="Gender",fg='black',bg="slate grey",height='2',width='8',font=("arial",15),bd='5')
la1.place(x=50,y=200)

gendervar=StringVar()
R1 = Radiobutton(lframe ,text="Male", variable=gendervar, height='2',width='6',font=("arial",10),value="Male")
R1.place(x=200,y=200)
R2 = Radiobutton( lframe,text="Female",variable=gendervar,height='2',width='6',font=("arial",10),value="Female")
R2.place(x=300,y=200)

# la1=Label(win,text="Select the programming languages:",fg='black',bg='slate grey',height='2',width='30',font=('arial',15),bd='5')
# la1.place(x=50,y=380)

# # checkbutton
# c1 = Checkbutton(win, text='Python',variable='var1', onvalue=1, offvalue=0, command='print_selection',bg='slate grey')
# c1.place(x=50,y=440)
# c2 = Checkbutton(win, text='C++',variable='var2', onvalue=1, offvalue=0, command='print_selection',bg='slate grey')
# c2.place(x=50,y=470)
# c3 = Checkbutton(win, text='C',variable='var3', onvalue=1, offvalue=0, command='print_selection',bg='slate grey')
# c3.place(x=50,y=500)
# c4 = Checkbutton(win, text='java',variable='var4', onvalue=1, offvalue=0, command='print_selection',bg='slate grey')
# c4.place(x=50,y=530)
# c5 = Checkbutton(win, text='html',variable='var5', onvalue=1, offvalue=0, command='print_selection',bg='slate grey')
# c5.place(x=50,y=560)

la1=Label(lframe,text="Age",fg='black',bg='slate grey',height='1',width='4',font=('arial',15),bd='5')
la1.place(x=50,y=290)

#spinbox
w = Spinbox(lframe  , from_=0, to=100,width='35')
w.place(x=200,y=290)

# la1=Label(win,text="Temperature",fg='black',bg='slate grey',height='1',width='10',font=('arial',15),bd='5')
# la1.place(x=600,y=150)

# #scale
w=Scale(win,variable=vars)
w.place(x=750,y=150)
la1=Label(win,text="Feedback",fg='black',bg='slate grey',height='1',width='10',font=('arial',15),bd='5')
la1.place(x=540,y=400)

# #text
w=Text(win,height='7',width='35')
w.insert(INSERT,"Give your feedback.......")
w.place(x=670,y=400)

# w = Label(win, text ='Python', height='1',width='7',pady='7',font=('arial',30),bg='slate grey') 
 w.place(x=420,y=10)

# #message  
msg = Message( win, text = " A message widget of python tikinter",bg='slate grey',font=('arial',20))  
msg.place(x=400,y=500)  

win.mainloop()

# Entry
# Button
# Radiobutton
# Checkbutton
# Spinbox
# Scale
# Text
# Message