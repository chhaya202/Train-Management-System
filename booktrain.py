from tkinter import *
from PIL import Image, ImageTk

from tkinter import messagebox
import connection
def book_train():
    book=Toplevel()
    book.title("book train")
    book.geometry("1200x700")
    book.resizable(False, False)
    book.config(bg="#091b3e")
    Title=Label(book, text="Book train", fg="#091b3e",bg="white")
    Title.config(font=('arial',20))
    Title.place(x=400,y=30)

    def submitfn():
        Train_Name=Train_name_entry.get()
        Train_no=Train_no_entry.get()
        Source=Source_entry.get()
        Destination=Destination_entry.get()
        Class=Class_entry.get()
        Date=Date_entry.get()
        passanger_no=passanger_no_entry.get()
        Mobile_No=Mobile_No_entry.get()
        Coustomer_name=Coustomer_name_entry.get()
        Gender=gendervar.get()
        if not all([Train_no, Train_Name, Source, Destination, Class, Date, passanger_no, Coustomer_name, Mobile_No, Gender]):
         messagebox.showwarning("Missing Data", "All fields are required!")
         return
        #else:
        data=(Train_no,Train_Name,Source,Destination,Class,Date,passanger_no,Coustomer_name,Mobile_No,Gender)
        
        try:
            query="insert into booking(trainno,trainname,source,destination,class,date,passengerno,coudtomername,mobileno,gender) values(?,?,?,?,?,?,?,?,?,?)"
            connection.cur.execute(query,data)
            connection.con.commit()
            messagebox.showinfo("succes","Train booked")
            
        except Exception as e:
            
            messagebox.showerror("error",str(e)) 
            print(e)
                    
    def Searchfn():
        tno=Train_no_entry.get()
        try:
                query="Select * from train where trainNo=?"
                res=connection.cur.execute(query,(tno,))
                row=res.fetchone()
                if row:
                 trainname_var.set(row[2])
                 source_var.set(row[3])
                 Destination_var.set(row[4])
                else: 
                     messagebox.showwarning("Not Found", "Train not found", parent=book)

        except Exception as e:
                print(e)
                messagebox.showerror("error","unable to Search",parent=book)  
              
    def clear_fields():
        Train_name_entry.delete(0, END)
        Train_no_entry.delete(0, END)
        Source_entry.delete(0, END)
        Destination_entry.delete(0, END)
        Class_entry.delete(0, END)
        Date_entry.delete(0, END)
        passanger_no_entry.delete(0, END)
        Mobile_No_entry.delete(0, END)
        Coustomer_name_entry.delete(0, END)
        gendervar.set("")  
        
        #clear_fields() 

        
                
                
    train_frame=LabelFrame(book,height=600,width=940,bg='white',bd=3)
    train_frame.place(x=60,y=30)
    Train_details=Label(train_frame, text="Train Details", fg="#091b3e",bg="white")
    Train_details.config(font=('arial',20))
    Train_details.place(x=200,y=10)
    Train_no=Label(train_frame, text="Train No.", fg="#091b3e", bg="white")
    Train_no.config(font=('arial',10))
    Train_no.place(x=70, y=60)
    Train_no_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e")
    Train_no_entry.place(x=70,y=90)
    Search=Button(train_frame,text='Search',fg="white",bg="#091b3e",width='10',cursor='arrow',relief='flat',command=Searchfn)
    Search.config(font=('arial',10,'bold'))
    Search.place(x=330,y=90)



    Train_Name=Label(train_frame, text="Train Name", fg="#091b3e", bg="white")
    Train_Name.config(font=('arial',10))
    Train_Name.place(x=480, y=60)

    trainname_var=StringVar()
    Train_name_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e", textvariable=trainname_var)
    Train_name_entry.place(x=480,y=90)
    Source=Label(train_frame, text="Source", fg="#091b3e", bg="white")
    Source.config(font=('arial',10))
    Source.place(x=70, y=130)

    source_var=StringVar()
    Source_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e", textvariable=source_var)
    Source_entry.place(x=70,y=160)

    Destination_var=StringVar()
    Destination=Label(train_frame, text="Destination", fg="#091b3e", bg="white")
    Destination.config(font=('arial',10))
    Destination.place(x=480, y=130)
    Destination_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e",textvariable=Destination_var)
    Destination_entry.place(x=480,y=160)

    Class=Label(train_frame, text="Class", fg="#091b3e", bg="white")
    Class.config(font=('arial',10))
    Class.place(x=70, y=200)
    Class_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e")
    Class_entry.place(x=70,y=230)

    Date=Label(train_frame, text="Date", fg="#091b3e", bg="white")
    Date.config(font=('arial',10))
    Date.place(x=480, y=200)
    Date_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e")
    Date_entry.place(x=480,y=230)

    #coustomer details

    Passanger_details=Label(train_frame, text="Passanger Details", fg="#091b3e",bg="white")
    Passanger_details.config(font=('arial',20))
    Passanger_details.place(x=200,y=290)

    passanger_no=Label(train_frame, text="Number Of Passangers", fg="#091b3e", bg="white")
    passanger_no.config(font=('arial',10))
    passanger_no.place(x=70, y=360)
    passanger_no_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e")
    passanger_no_entry.place(x=70,y=390)

    Coustomer_name=Label(train_frame, text="Coustomer Name", fg="#091b3e", bg="white")
    Coustomer_name.config(font=('arial',10))
    Coustomer_name.place(x=70, y=430)
    Coustomer_name_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e")
    Coustomer_name_entry.place(x=70,y=460)

    Mobile_No=Label(train_frame, text="Mobile No", fg="#091b3e", bg="white")
    Mobile_No.config(font=('arial',10))
    Mobile_No.place(x=500, y=360)
    Mobile_No_entry=Entry(train_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e")
    Mobile_No_entry.place(x=500,y=390)
    Gender=Label(train_frame, text="Gender", fg="#091b3e", bg="white")
    Gender.config(font=('arial',10))
    Gender.place(x=500, y=430)

    gendervar=StringVar()
    R1 = Radiobutton(train_frame ,text="Male",bg='white',fg='#091b3e', variable=gendervar, height='1',width='6',font=("arial",10),value="Male")
    R1.place(x=500,y=460)
    R2 = Radiobutton( train_frame,text="Female",bg='white',fg='#091b3e', variable=gendervar,height='1',width='6',font=("arial",10),value="Female")
    R2.place(x=580,y=460)

    Book_buton=Button(train_frame,text='Submit',fg="white",bg="#091b3e",width='10',height='1',cursor='arrow',command=submitfn)
    Book_buton.config(font=('arial',10,'bold'))
    Book_buton.place(x=270,y=530)

    Clr_buton=Button(train_frame,text='Clear',fg="white",bg="#091b3e",width='10',height='1',cursor='arrow',command=clear_fields)
    Clr_buton.config(font=('arial',10,'bold'))
    Clr_buton.place(x=390,y=530)
    
    Exit=Button(train_frame,text='Back',fg='white',bg="#091b3e",height='1',width='10',cursor='arrow', command=book.destroy)
    Exit.config(font=('arial',10,'bold'))
    Exit.place(x=500,y=530)


    