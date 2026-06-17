from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import connection

def Add_train():
#window creation
    Add=Toplevel()
    Add.title("Add train form")
    Add.geometry("1200x700")
    Add.resizable(False, False)
    Add.config(bg="#091b3e")

    #frame
    Ad_frame=LabelFrame(Add,bg='white',bd=3)
    Ad_frame.place(x=20,y=330,height=350,width=980)

    #image
    bgimg13=Image.open("10.png")
    bgimg13=bgimg13.resize((400,300))
    bgimg13=ImageTk.PhotoImage(bgimg13)
    lbgimg13=Label(Ad_frame, image=bgimg13)
    lbgimg13.image = bgimg13
    lbgimg13.place(x=430, y=30)

    #Add function
    def Addfn():
        Train_no=E11.get()
        Train_Name=E12.get()
        Source=E13.get()
        Destination=E14.get()
        Time=E15.get()
    
        if not all([Train_no, Train_Name, Source, Destination,Time]):
         messagebox.showwarning("Missing Data", "All fields are required!")
        else:
         data=(Train_no,Train_Name,Source,Destination,Time)
        
        try:
            query="insert into train(trainNo,trainName,Source,Destination,Time) values(?,?,?,?,?)"
            connection.cur.execute(query,data)
            connection.con.commit()
            messagebox.showinfo("succes","train Added")
            
        except Exception as e:
            print(e)
            messagebox.showerror("error","error")  
            
    #populate function         
    def populate_table():
            tree.delete(* tree.get_children())
            q="select * from train"
            result=connection.cur.execute(q)
            for row in result:
                print(row)
                tree.insert('',END,iid=row[0],values=(row[1],row[2],row[3],row[4],row[5]))     
                
    # delete Function                
    def deletefn():
            selected=tree.focus()
            if selected:
             try:
                query="delete from train where id=?"
                connection.cur.execute(query,(selected,))
                connection.con.commit()
                messagebox.showinfo("success","row deleted",parent=Add)
                populate_table()
             except Exception as e:
                print(e)
                messagebox.showerror("error","unable to delete",parent=Add)
            else:
                messagebox.showwarning("selection error","please select a train to delete.",parent=Add)          
                
                        
    #search Function   
    def searchfn():
        se=search_e.get()
        treeselect=[]
        for row in tree.get_children():
            if se in tree.item(row)['values']:
                treeselect.append(row)
        tree.selection_set(treeselect)
        
    #clear function    
    def clear_fields1():
    
        E11.delete(0, END)
        E12.delete(0, END)
        E13.delete(0, END)
        E14.delete(0, END)       
        E15.delete(0, END)
        #clear_fields1()  
    
    #edit function
    def Edittrain(e):
            selected=tree.focus()
            print(selected)
            q="select * from train where id=?"
            result=connection.cur.execute(q,(selected,))
            row=result.fetchone()
            E11_var.set(row[1])
            E12_var.set(row[2])
            E13_var.set(row[3])
            E14_var.set(row[4])
            E15_var.set(row[5])
            Update.config(command=lambda:update_train(selected))
            
    #update function      
    def update_train(id):
        Train_no=E11.get()
        Train_Name=E12.get()
        Source=E13.get()
        Destination=E14.get()
        Time=E15.get()  
        data=(Train_no,Train_Name,Source,Destination,Time,id)
        try:
            query="update train set trainNo=?,trainName=?,Source=?,Destination=?,Time=? where id=?"
            connection.cur.execute(query,data)
            connection.con.commit()
            populate_table()
            messagebox.showinfo("updated sucessfully","updated",parent=Add)
        except Exception as e:
            print(e)
            messagebox.showerror("error",e,parent=Add)    
            
            
            
        
                

    # labels
    Train_no=Label(Ad_frame, text="Train No.", fg="#091b3e", bg="white")
    Train_no.config(font=('arial',10))
    Train_no.place(x=70, y=10)
    E11_var=StringVar()
    E11=Entry(Ad_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e", textvariable=E11_var)
    E11.place(x=70,y=30)

    Train_Name=Label(Ad_frame, text="Train Name", fg="#091b3e", bg="white")
    Train_Name.config(font=('arial',10))
    Train_Name.place(x=70, y=60)
    E12_var=StringVar()
    E12=Entry(Ad_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e",textvariable=E12_var)
    E12.place(x=70,y=80)

    Source=Label(Ad_frame, text="Source", fg="#091b3e", bg="white")
    Source.config(font=('arial',10))
    Source.place(x=70, y=110)
    E13_var=StringVar()
    E13=Entry(Ad_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e",textvariable=E13_var)
    E13.place(x=70,y=130)

    Destination=Label(Ad_frame, text="Destination", fg="#091b3e", bg="white")
    Destination.config(font=('arial',10))
    Destination.place(x=70, y=160)
    E14_var=StringVar()
    E14=Entry(Ad_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e",textvariable=E14_var)
    E14.place(x=70,y=190)

    Time=Label(Ad_frame, text="Time", fg="#091b3e", bg="white")
    Time.config(font=('arial',10))
    Time.place(x=70, y=220)
    E15_var=StringVar()
    E15=Entry(Ad_frame,font=('arial',10),justify='center',width=35,fg='#091b3e',highlightthickness=2, 
    highlightbackground="#091b3e", 
    highlightcolor="#091b3e",textvariable=E15_var)
    E15.place(x=70,y=250)

    add=Button(Ad_frame,text='add',fg='white',bg="#091b3e",height='1',width='10',bd=4,activebackground='#091b3e',cursor='arrow',command=Addfn)
    add.config(font=('arial',10,'bold'))
    add.place(x=40,y=300)


    Clear=Button(Ad_frame,text='Clear',fg='white',bg="#091b3e",height='1',width='10',bd=4,activebackground='#091b3e',cursor='arrow',command=clear_fields1)
    Clear.config(font=('arial',10,'bold'))
    Clear.place(x=140,y=300)


    Exit=Button(Ad_frame,text='Back',fg='white',bg="#091b3e",height='1',width='10',bd=4,activebackground='#091b3e',cursor='arrow', command=Add.destroy)
    Exit.config(font=('arial',10,'bold'))
    Exit.place(x=240,y=300)

    #tree frame
    tree_frame=LabelFrame(Add,text="train Records",bg='white',bd=3)
    tree_frame.place(x=20,y=10,height=310,width=980)
    Delete=Button(tree_frame,text='Delete',fg='white',bg="#091b3e",height='1',width='10',bd=4,activebackground='#091b3e',cursor='arrow',command=deletefn)
    Delete.config(font=('arial',10,'bold'))
    Delete.place(x=380,y=250)

    #search Button
    search_e=Entry(tree_frame,font=('arial',10),justify='center',width=25,fg='black',highlightthickness=3,bd=3, 
    highlightbackground="black", 
    highlightcolor="#091b3e")
    search_e.place(x=310,y=5)
    Search=Button(tree_frame,text='Search',fg="white",bg="#091b3e",highlightbackground="#091b3e", width='10',bd=4,cursor='arrow',command=searchfn)
    Search.config(font=('arial',10,'bold'))
    Search.place(x=500,y=5)

    #update button
    Update=Button(tree_frame,text='Update',fg="white",bg="#091b3e",highlightbackground="#091b3e", width='10',bd=4,cursor='arrow')
    Update.config(font=('arial',10,'bold'))
    Update.place(x=600,y=5)

    Refresh=Button(tree_frame,text='Refresh',fg="white",bg="#091b3e",highlightbackground="#091b3e", width='10',bd=4,cursor='arrow',command=populate_table)
    Refresh.config(font=('arial',10,'bold'))
    Refresh.place(x=700,y=5)

    columns=("Train No","Train name","Source","Destinamtion","Time")
    tree=ttk.Treeview(tree_frame,columns=columns,show="headings")
    for col in columns:
        print("treeview created")
        tree.column(col,anchor=CENTER)
        tree.heading(col,text=col)
        tree.column(col,width=180)
    tree.place(x=40,y=40,width=900, height=200)
    tree.bind("<<TreeviewSelect>>",Edittrain)    
    populate_table()

if __name__ == "__main__":
    root = Tk()
    Add_train()
    root.mainloop()    
            
    
    
    