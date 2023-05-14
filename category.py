from tkinter import*
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import sqlite3
import customtkinter 
import os
class categoryclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x740+300+220")
        self.root.title("Inventory Management System  |  Developed by RAFI")
        self.root.config(bg="#282424")
        self.root.focus_force() 
        
       #=====variables====
        self.var_cat_id=StringVar()
        self.var_name=StringVar()
        self.var_sup_invoice=StringVar()
        
        
        
        #=======title====
        # lbl_title=Label(self.root,text="Manage product category",font=("times new roman",30,),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=10) 
        lbl_title=customtkinter.CTkLabel(self.root,text="\t\t\tManage product category",font=("Small caps Font",25,"bold"),text_color="#00c1e4",fg_color="#414141",anchor="w",padx=20,corner_radius=14).place(x=0,y=2,width=1600,height=50)
        lbl_name=customtkinter.CTkLabel(self.root,text="Enter category name",font=("Small caps Font",30),bg_color="white",text_color="#00c1e4",fg_color="#282424").place(x=30,y=50) 
        txt_name=customtkinter.CTkEntry(self.root,textvariable=self.var_name,font=("Small caps Font",16),text_color="#282424",corner_radius=14).place(x=40,y=110,width=300,height=35) 
               
        #Entry(self.root,textvariable=self.var_name,font=("times new roman",18),bg="lightyellow").place(x=50,y=170,width=300) 
        btn_add=customtkinter.CTkButton(self.root,text="ADD", command=self.add,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=250,y=110,width=150,height=35) 
        btn_del=customtkinter.CTkButton(self.root,text="Delete",command=self.delete,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=360,y=110,width=150,height=35) 

        #====Category Details===
        
        cat_frame=Frame(self.root,bd=3,relief=RIDGE)
        cat_frame.place(x=50,y=220,width=600,height=500)
        
        scrolly=Scrollbar(cat_frame,orient=VERTICAL)
        scrollx=Scrollbar(cat_frame,orient=HORIZONTAL)
        
        
        self.categoryTable=ttk.Treeview(cat_frame,columns=("cid","name"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.categoryTable.xview)
        scrolly.config(command=self.categoryTable.yview)
        
        
        self.categoryTable.heading("cid",text="C ID")
        self.categoryTable.heading("name",text="Name")
        self.categoryTable["show"]="headings"
        self.categoryTable.column("cid",width=90)
        self.categoryTable.column("name",width=100)
        self.categoryTable.pack(fill=BOTH,expand=1)
        self.categoryTable.bind("<ButtonRelease-1>",self.get_data)
        
        
        
        #===Images====



        self.im2=Image.open("images/category.png")
        self.im2=self.im2.resize((900,650),Image.ANTIALIAS)
        self.im2=ImageTk.PhotoImage(self.im2)
               
        self.lbl_im2=Label(self.root,image=self.im2)
        self.lbl_im2.place(x=700,y=220,width=850,height=500)
        
        
        
        self.show()
        
 #=============Functions=================
        
    def add(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cursor_1=con.cursor()
        try:
            if  self.var_name.get()=="":
                messagebox.showerror("Error","Category should be required",parent=self.root)
            else:
                cursor_1.execute("select * from category where name=?",(self.var_name.get(),))
                row=cursor_1.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Category already generated Try another one!!" )
                else:
                    cursor_1.execute("Insert into category (name) values(?)",(self.var_name.get(),))
                    con.commit()
                    messagebox.showinfo("Success","Category Added supplier",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            




    def show(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cursor_1=con.cursor()
        try:
            cursor_1.execute("select * from category")
            rows=cursor_1.fetchall()
            self.categoryTable.delete(*self.categoryTable.get_children())
            for row in rows:
                self.categoryTable.insert('',END,values=row)       
            
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")   
            
    def get_data(self,ev):
        f=self.categoryTable.focus()
        content=(self.categoryTable.item(f))
        row=content['values']
        self.var_cat_id.set(row[0]),
        self.var_name.set(row[1]),




        
    def delete(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                if self.var_cat_id.get()=="":
                        messagebox.showerror("Error","Please select category from the list ",parent=self.root)
                else:
                        cur.execute("Select * from category where cid=?",(self.var_cat_id.get(),))
                        row=cur.fetchone()
                        if row==None:
                                messagebox.showerror("Error","Error, please try again",parent=self.root)
                        else:   
                                op=messagebox.askyesno("Confrim","Do you rally want to delete?",parent=self.root)
                                if op==True:

                                        cur.execute("delete from category where cid=?",(self.var_cat_id.get(),))
                                        con.commit()
                                        messagebox.showinfo("Delete","Categort Deleted Succesfully",parent=self.root)
                                    
                                        self.show()
                                        self.var_cat_id.set("")
                                        self.var_name.set("")
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                
                        


if __name__=="__main__":
        root=customtkinter.CTk()
        obj=categoryclass(root)
        root.mainloop()