from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter as tk
#import customtkinter as ctk
import connection
import login
import Dashboard
#ctk.set_appearance_mode("light")
#ctk.set_default_color_theme("blue")


def signup():
 root=tk.Tk()
 root.geometry("1200x700")
 root.resizable(False, False)
 root.title("Railway Reservation System-Sign up")
 root.config(bg="#EAF1FF")
 def showpassword():
    if(E3.cget('show')=='*'):
        E3.config(show="")
        E4.config(show="")
    else:
        E3.config(show='*')
        E4.config(show='*')
        #background images\
        
 def open_login():
    root.destroy()      
    login.loginfn()       

 def signupfn():
    name=E1.get().strip()
    email=E2.get().strip()
    password=E3.get() .strip()    
    cpass=E4.get().strip()
    if not name or not email or not password or not cpass:
        messagebox.showwarning(
            "Missing Data",
            "Please fill all fields")
        return
    if password!=cpass:
        messagebox.showwarning("Password Error","Password do not match")
        return
        
    try:
            data=(name,email,password)
            query="insert into users(name,email, password) values(?,?,?)"
            connection.cur.execute(query, data)
            connection.con.commit()
            messagebox.showinfo("Success","Sign Up Successfully")
            root.destroy()   
            Dashboard.dashboardfn()
            
           
    except Exception as e:
            print(e)
            messagebox.showerror("Database Error",str(e))
           
   
   
   # else:
       # messagebox.showwarning("Password Error","Password do not match")
    

 frame1=LabelFrame(root,bd=2,bg="white",borderwidth=2,relief="flat")
 frame1.place(relx=0.5,rely=0.5,anchor=CENTER,width=1000,height=600)
 limg = Image.open("13.jpg")
 limg = limg.resize((480,550))

 photo = ImageTk.PhotoImage(limg)

 limg = Label(frame1, image=photo)
 limg.image = photo

 limg.place(x=500, y=20)
 """img1=Image.open("13.jpg")
 img1=img1.resize((480,550))
 photo = ImageTk.PhotoImage(img1)
 limg=ImageTk.PhotoImage(img1=photo)
 limg.image=photo
 limg.place(x=500, y=20)"""
 Signup=Label(frame1, text="Create Your Account", fg="#091b3e", bg="white")
 Signup.config(font=("Segoe UI",30,"bold"))
 Signup.place(x=50,y=20)

 Signup=Label(frame1, text="Join thousands of travelers and manage\nyour train bookings easily.",fg="#091b3e", bg="white")
 Signup.config(font=("Segoe UI",10))
 Signup.place(x=100,y=70)

 name=Label(frame1, text="Name", fg="#091b3e", bg="white")
 name.config(font=("Segoe",10))
 name.place(x=30, y=150)
 E1=Entry(frame1,font=("Segoe UI",12,),justify='center',width=35,fg='blue4',highlightthickness=2, 
 highlightbackground="blue4", 
 highlightcolor="blue4")
 E1.place(x=30,y=170)
 email=Label(frame1, text="Email", fg="#091b3e", bg="white",)
 email.config(font=("Segoe",10))
 email.place(x=30, y=230)
 E2=Entry(frame1,font=("Segoe UI",12,),justify='center',width=35,fg='blue4',highlightthickness=2, 
 highlightbackground="blue4", 
 highlightcolor="blue4")
 E2.place(x=30,y=250)
 password1=Label(frame1, text="*Password", fg="#091b3e", bg="white")
 password1.config(font=("Segoe UI",10))
 password1.place(x=30, y=300)
 E3=Entry(frame1,font=("Segoe UI",12,) ,show='*',justify='center',width=35,fg='blue4',highlightthickness=2, 
 highlightbackground="blue4", 
 highlightcolor="blue4")

 E3.place(x=30,y=320)
 Cpassword=Label(frame1, text="Confirm Password ", fg="#091b3e", bg="white")
 Cpassword.config(font=("Segoe UI",10))
 Cpassword.place(x=30, y=380)
 E4=Entry(frame1,font=("Segoe UI",12,) ,show='*',justify='center',width=35,fg='#091b3e',highlightthickness=2, 
 highlightbackground="blue4", 
 highlightcolor="blue4")
 E4.place(x=30,y=400)
 c1 = Checkbutton(frame1, text='Show password',variable='var1', onvalue=1, offvalue=0, command=showpassword,bg='white',fg='#091b3e')
 c1.place(x=30,y=450)
 Submit=Button(frame1,text='Submit',fg='white',bg="#091b3e",height='1',width='20',bd=4,cursor='arrow',command=signupfn)
 Submit.config(font=('arial',10))
 Submit.place(x=30,y=480)

 Ulogin=Button(frame1,text='Existing User? Login',fg="#091b3e",bg="white", relief="flat",command=open_login)
 Ulogin.config(font=("arial",10,'underline'))
 Ulogin.place(x=30,y=550)


 root.mainloop()

if __name__ == "__main__":
 signup() 