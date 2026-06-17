from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox 
import connection 
import view
import Addtrain
from tkinter import Toplevel
import booktrain
from datetime import datetime

def dashboardfn(): 
    dashboard = Tk()
    dashboard.geometry("1200x700")
    dashboard.resizable(False, False)
    dashboard.title("Train Management System")
    dashboard.configure(bg="#f2f6ff")
    

    sidebar = Frame(dashboard, bg="#091b3e", width=320, height=700)
    sidebar.pack(side=LEFT,fill=Y)
  
    
    title = Label(sidebar, text="Train Management\n System", bg="#091b3e", fg="white")
    title.config(font=("Arial", 18, "bold"))
    title.place(x=40, y=30)

   

    main = Frame(dashboard, width=880, height=700,bg="white")
    main.place(x=320, y=0)

    Label(
    main,
    text=datetime.now().strftime("%d-%m-%Y"),
    font=("Arial",12,"bold"),
    bg="white").place(x=760,y=20)
     
    card1 = Frame(main, bg="#091b3e", width=120, height=70,relief="ridge")
    card1.place(x=40, y=120)

    Label(card1, text="Total Trains",
      bg="#091b3e", fg="white",
      font=("Arial", 12, "bold")).pack(pady=3)

    Label(card1, text="20",
      bg="#091b3e", fg="white",
      font=("Arial", 22, "bold")).pack()


    card2 = Frame(main, bg="#091b3e", width=120, height=70,relief="ridge")
    card2.place(x=250, y=120)
 
    Label(card2, text="Bookings",
      bg="#091b3e", fg="white",
      font=("Arial", 12, "bold")).pack(pady=3)

    Label(card2, text="20",
      bg="#091b3e", fg="white",
      font=("Arial", 22, "bold")).pack()


    card3 = Frame(main, bg="#091b3e", width=120, height=70,relief="ridge")
    card3.place(x=460, y=120)

    Label(card3, text="Available",
      bg="#091b3e", fg="white",
      font=("Arial", 12, "bold")).pack(pady=3)

    Label(card3, text="20",
      bg="#091b3e", fg="white",
      font=("Arial", 22, "bold")).pack()
    
    
    

    welcome = Label(main, text=" 🚆Railway Management Dashboard", fg="#091b3e",borderwidth=0,highlightthickness=0,bg="white")
    welcome.config(font=("Arial", 28, "bold"))
    welcome.place(x=40, y=20)
    img = Image.open("21.jpg")   # your image file
    img = img.resize((800, 420))         # adjust size as needed
    img_photo = ImageTk.PhotoImage(img)

    img_label = Label(main, image=img_photo, bg="white", bd=3,relief="groove")
    img_label.image = img_photo
    img_label.place(x=40, y=225)

    desc = Label(main, text="Manage trains, bookings and schedules easily", fg="#091b3e",borderwidth=0,highlightthickness=0,bg="white")
    desc.config(font=("Arial", 12))
    desc.place(x=50, y=80)
    

    

    def logout():
        dashboard.destroy()
        import login
        login.loginfn()
        

    def create_btn(text, y, cmd):
        print("Creating:", text)
        Button(sidebar,
               text=text,
               width=24,
               font=("Arial", 13, "bold"),
               bg="#091b3e",
               fg="white",
               cursor="hand2",
              
               command=cmd).place(x=35, y=y)
    print("Reached button section")
    create_btn("🚆Add Train", 140, Addtrain.Add_train)
    create_btn("📋View Train", 200, view.viewfn)
    create_btn("🎫Book Train", 260, booktrain.book_train)

    create_btn("🗑Delete Train", 320, Addtrain.Add_train)
    create_btn("🔄Update Train", 380, Addtrain.Add_train)

    
    create_btn("🚪Logout",580 , logout)
    

    

                 


                    
                    

    