from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
from PIL import Image, ImageTk
import connection

def viewfn():
    view=Toplevel()
    view.title("View Train")
    view.geometry("1200x700")
    view.resizable(False,False)
    view.config(bg="#091D46")
    tree_frame1=LabelFrame(view,height=620,width=1150,bg="#EAF1FF",bd=2,relief="groove")
    tree_frame1.place(x=25,y=35)
    Train_details=Label(tree_frame1, text="🚆Train Details", fg="#081b41",bg="#EAF1FF")
    Train_details.config(font=('arial',20))
    Train_details.place(x=450,y=20)

     ###################################
    Label(tree_frame1,
    text="Search Train No:",
    bg="#EAF1FF",
    fg="#091b3e",
    font=("Arial",11,"bold")).place(x=40,y=50)

    search_entry = Entry(tree_frame1, width=25)
    search_entry.place(x=170,y=52)

    def search_train():
     print("serach button is clicked")
     trainno = search_entry.get()

     tree.delete(*tree.get_children())

     q = "select * from train where trainno=?"
     connection.cur.execute(q, (trainno,))

     result = connection.cur.fetchall()

     if len(result) == 0:
        messagebox.showinfo("Search", "Train not found")
        populate_table()
        return

     for row in result:
        tree.insert('', END,
                    values=(row[1], row[2], row[3], row[4], row[5]))

    search=Button(tree_frame1,
       text="Search",
       bg="#091b3e",
       fg="white",command=search_train)
    search.place(x=350,y=48)

    columns=("Train No","Train name","Source","Destinamtion","Time")
    scroll_y = Scrollbar(tree_frame1, orient=VERTICAL)
    scroll_y.place(x=940, y=80, height=425)

    

    style = ttk.Style()
    style.theme_use("default")

    style.configure(
    "Treeview",
    rowheight=22,
    background="white",
    foreground="#0B3D91",
    font=("Arial", 11)
)

    style.configure(
    "Treeview.Heading",
    background="#081b41",
    foreground="white",
    font=("Arial", 12, "bold")
)

    tree=ttk.Treeview(tree_frame1,columns=columns,show="headings",height=20,yscrollcommand=scroll_y.set)
    scroll_y.config(command=tree.yview)
    for col in columns:
        tree.column(col,anchor=CENTER)
        tree.heading(col,text=col)
        
        tree.column(col,width=180)
    tree.place(x=40,y=80)
    
        
        


    def populate_table():
            tree.delete(* tree.get_children())
            q="select * from train"
            #connection.cur.execute(q)
            result=connection.cur.execute(q)
            print("result=",result)
            for row in result:
                print("row=",row)
                tree.insert('',END,iid=row[0],values=(row[1],row[2],row[3],row[4],row[5]))   
    populate_table()
                  
    Back=Button(tree_frame1,text='⬅Back',fg='white',bg="#091b3e",height='1',width='10',bd=4,activebackground='#091b3e',cursor='arrow',command=view.destroy)
    Back.config(font=('arial',10,'bold'))
    Back.place(x=500,y=550)

    