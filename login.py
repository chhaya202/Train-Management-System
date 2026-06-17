from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import connection
import signup
from tkinter import Toplevel
import Dashboard



def loginfn():
    loginwin=Tk()
    loginwin.geometry("1200x700")

    loginwin.resizable(False, False)
    loginwin.title("Train maanagement -Login Window")

    bg_img = Image.open("12.jpg")   
    bg_img = bg_img.resize((1200, 700))
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = Label(loginwin, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    bg_label.image = bg_photo
    frame2 = Frame(loginwin, bg="white", bd=0)
    frame2.place(x=140, y=120, width=450, height=470)

    LForm = Label(frame2, text="LOGIN", fg="#091b3e", bg="white")
    LForm.config(font=('Arial', 22, 'bold'))
    LForm.place(x=170, y=20)

    Wlc = Label(frame2, text="Welcome back!", fg="#091b3e", bg="white")
    Wlc.config(font=('Arial', 12, 'bold'))
    Wlc.place(x=150, y=60)
   
    def showpassword():
        if(E12.cget('show')=='*'):
            E12.config(show="")
           
        else:
            E12.config(show='*')   

    def checklogin():
      print("button clicked")
      username = E11.get().strip()
      password = E12.get().strip()
      if not username or not password:
        messagebox.showwarning(
        "Missing Data",
        "Please enter username and password"
    )
        return
      
      print("Username:", username)
      print("Password:", password)

      query = """
      SELECT * FROM users
      WHERE name=? AND password=?
       """

      connection.cur.execute(query,(username, password) )

      user = connection.cur.fetchone()

     
      print("Result:", user)

      if user:
        messagebox.showinfo(
            "Success",
            "Login Successful"
        )

        loginwin.destroy()
        Dashboard.dashboardfn()

      else:
        messagebox.showerror(
            "Login Failed",
            "Invalid username or password"
        )
    
    
    """frame2=LabelFrame(loginwin,height=460,width=900,bg='white')
    frame2.place(x=150,y=120)
    
    LForm=Label(frame2, text="Login Form", fg="blue4", bg="white")
    LForm.config(font=('arial',20,'bold'))
    LForm.place(x=120, y=20)
    Wlc=Label(frame2, text="Welcome back!", fg="blue4", bg="white",bd=5)
    Wlc.config(font=('arial',15,'bold'))
    Wlc.place(x=40, y=70)
    img1=Image.open("user.jpeg")
    img1=img1.resize((70,20))
    img1=ImageTk.PhotoImage(img1)
    limg=Label(frame2,image=img1)
    limg.place(x=145,y=75)"""

    """Username=Label(frame2, text="*Username", fg="blue4", bg="white",font=('Arial',10))
    Username.place(x=40, y=130)
    E11=Entry(frame2,font=('arial',13),justify='center',width=40,fg='blue4',highlightthickness=2, 
    highlightbackground="blue4", 
    highlightcolor="blue4")
    E11.place(x=40,y=155)
    password=Label(frame2, text="*Password", fg="blue4", bg="white",font=('Arial',10))
    password.place(x=40, y=195)
    E12=Entry(frame2,show='*',font=(13),justify='center',width=40,fg='blue4',highlightthickness=2, 
    highlightbackground="blue4", 
    highlightcolor="blue4")
    E12.place(x=40,y=220)
    chkb = Checkbutton(frame2, text='Show password',variable='var1', onvalue=1, offvalue=0, command=showpassword,bg='white',fg='blue4')
    chkb.place(x=40,y=260)
    btn3=Button(frame2,text='Login',fg='white',bg="blue4",height='1',width='20',font=('arial',10),bd=4,activebackground='blue4',cursor='arrow',command=checklogin)
    btn3.place(x=120,y=320)

    btn4=Button(frame2,text='New User? Signup',fg='blue4',bg="white",relief="flat", command=loginwin.destroy)
    btn4.config(font=('arial',10,'underline'))
    btn4.place(x=150,y=360)

    loginwin.mainloop()"""
    Username = Label(frame2, text="Username", fg="#091b3e", bg="white",font=("segoe",12,"bold"))
    Username.place(x=60, y=120)

    E11 = Entry(frame2, font=('Arial', 12), width=30,
                justify='center', bd=2, relief="groove",fg="blue4")
    E11.place(x=60, y=145)

    # ================= PASSWORD =================
    password = Label(frame2, text="Password", fg="#091b3e", bg="white",font=("segoe",12,"bold"))
    password.place(x=60, y=190)

    E12 = Entry(frame2, font=('Arial', 12), width=30,
                justify='center', show='*', bd=2, relief="groove",fg="blue4")
    E12.place(x=60, y=215)

    # ================= SHOW PASSWORD CHECKBOX =================
    var1 = IntVar()

    chkb = Checkbutton(
        frame2,
        text='Show password',
        variable=var1,
        onvalue=1,
        offvalue=0,
        command=showpassword,
        bg='white',
        fg='#0B3D91'
    )
    chkb.place(x=60, y=250)

    # ================= LOGIN BUTTON =================
    btn3 = Button(
        frame2,
        text='LOGIN',
        fg='white',
        bg="#091b3e",
        height=1,
        width=20,
        font=('Arial', 11, 'bold'),
        bd=0,
        cursor='hand2',
        command=checklogin
    )
    btn3.place(x=120, y=300)

    # ================= SIGNUP BUTTON =================
    def open_signup():
        loginwin.destroy()
        signup.signup()

    btn4 = Button(
        frame2,
        text='New User? Signup',
        fg='#0B3D91',
        bg="white",
        relief="flat",
        command=open_signup,
        font=('Arial', 10, 'underline'),
        cursor='hand2',
        activebackground="blue4"
    )
    btn4.place(x=160, y=350)

if __name__ == "__main__":
    loginfn()  

