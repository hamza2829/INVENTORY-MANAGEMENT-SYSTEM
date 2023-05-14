from tkinter import*
from tkinter import ttk,messagebox
from PIL import ImageTk,Image
import sqlite3
import customtkinter 
import os
customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("#17c0e9")
class supplierclass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x740+300+220")
        self.root.config(bg="#282424")
        #self.root.resizable(width=False, height=False)
        self.root.title("Inventory Managment System|Made by HRM")
        self.root.focus_force()
        
         #********************variables*********************************
        
        self.var_invoiceno=StringVar()
        self.var_suppliername=StringVar()
        self.var_contact=StringVar()
        self.var_description=StringVar()
        self.var_invoicenotxt=StringVar()
        

    
        title_label=customtkinter.CTkLabel(self.root,text="\t\t\tManage Supplier Details",font=("Small caps Font",25,"bold"),text_color="#00c1e4",fg_color="#414141",anchor="w",padx=20,corner_radius=14).place(x=0,y=2,width=1600,height=50)
        
        #********************contents*********************************
        #********************labels*********************************
        invoice_label=customtkinter.CTkLabel(self.root,text="Invoice No.",font=("Small caps Font",17,"bold"),text_color="#00c1e4",anchor="w",padx=20,corner_radius=14).place(x=25,y=65,width=1100,height=35)
        supname_label=customtkinter.CTkLabel(self.root,text="Supplier Name",font=("Small caps Font",17,"bold"),text_color="#00c1e4",anchor="w",padx=20,corner_radius=14).place(x=25,y=125,width=1100,height=35)
        contact_label=customtkinter.CTkLabel(self.root,text="Contact",font=("Small caps Font",17,"bold"),text_color="#00c1e4",anchor="w",padx=20,corner_radius=14).place(x=25,y=185,width=1100,height=35)
        Descryption_label=customtkinter.CTkLabel(self.root,text="Description",font=("Small caps Font",17,"bold"),text_color="#00c1e4",anchor="w",padx=20,corner_radius=14).place(x=25,y=245,width=1100,height=35)
        invoice2_label=customtkinter.CTkLabel(self.root,text="Invoice No.",font=("Small caps Font",17,"bold"),text_color="#00c1e4",anchor="w",padx=20,corner_radius=14).place(x=650,y=65,width=1100,height=35)
        
        #********************text fields*********************************
        invoice_txt=customtkinter.CTkEntry(self.root,textvariable=self.var_invoiceno,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=180,y=62,width=250)
        supname_txt=customtkinter.CTkEntry(self.root,textvariable=self.var_suppliername,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=180,y=122,width=250)
        contact_txt=customtkinter.CTkEntry(self.root,textvariable=self.var_contact,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=180,y=182,width=250)
        Descryption_txt=customtkinter.CTkEntry(self.root,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14,textvariable=self.var_description)
        Descryption_txt.place(x=180,y=242,width=350,height=185)
        invoice2_txt=customtkinter.CTkEntry(self.root,textvariable=self.var_invoicenotxt,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=775,y=62,width=190)
        
        #********************buttons*********************************
        btn_search = customtkinter.CTkButton(self.root,text="Search",font=("Small caps Font",15,"bold"),command=self.search,text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=972,y=60,width=122,height=40)
        btn_save = customtkinter.CTkButton(self.root,text="Save",font=("Small caps Font",15,"bold"),command=self.add,text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=180,y=440,width=122,height=40)
        btn_update = customtkinter.CTkButton(self.root,text="Update",font=("Small caps Font",15,"bold"),command=self.update_1,text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=290,y=440,width=122,height=40)
        btn_delete = customtkinter.CTkButton(self.root,text="Delete",font=("Small caps Font",15,"bold"),command=self.delete,text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=400,y=440,width=122,height=40)
        btn_clear = customtkinter.CTkButton(self.root,text="Clear",font=("Small caps Font",15,"bold"),command=self.clear,text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=510,y=440,width=122,height=40)

        #********************frame*********************************
        
        sup_frame=Frame(self.root,bd=3,relief=RIDGE)
        sup_frame.place(x=1020,y=180,width=400,height=370)
        scrollx=Scrollbar(sup_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(sup_frame,orient=VERTICAL)
        self.supplier_table=ttk.Treeview(sup_frame,columns=("invoice","name","contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplier_table.xview)
        scrolly.config(command=self.supplier_table.yview)
        self.supplier_table.heading("invoice",text="Invoice No")
        self.supplier_table.heading("name",text="Name")
        self.supplier_table.heading("contact",text="Contact")
        self.supplier_table.heading("desc",text="Description")
        
        self.supplier_table["show"]="headings"
        self.supplier_table.column("invoice",width=80)
        self.supplier_table.column("name",width=110)
        self.supplier_table.column("contact",width=110)
        self.supplier_table.column("desc",width=140)
        self.supplier_table.pack(side=TOP,fill=BOTH,expand=1)
        self.show()
        self.supplier_table.bind("<ButtonRelease-1>",self.get_data)
        

        
        
#*********************************database work*******************************************************        
    def add(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cursor_1=con.cursor()
        try:
            if  self.var_invoiceno.get()=="" or self.var_suppliername.get()=="" or self.var_contact.get()=="" or self.var_description.get()==""  :
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cursor_1.execute("select * from supplier where invoice=?",(self.var_invoiceno.get(),))
                row=cursor_1.fetchone()
                if row!=None:
                    messagebox.showerror("Error","This Invoice Nomber is already generated Try another one!!" )
                else:
                    cursor_1.execute("insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                            
                            self.var_invoiceno.get(),
                            self.var_suppliername.get(),
                            self.var_contact.get(),
                            self.var_description.get(),  
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Supplier","Supplier Added supplier",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            
    
    
    
    def show(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cursor_1=con.cursor()
        try:
            cursor_1.execute("select * from supplier ")
            rows=cursor_1.fetchall()
            self.supplier_table.delete(*self.supplier_table.get_children())
            for row in rows:
                self.supplier_table.insert('',END,values=row)       
            
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")   
            
    def get_data(self,ev):
        f=self.supplier_table.focus()
        content=(self.supplier_table.item(f))
        row=content['values']
        #print(row)
        self.var_invoiceno.set(row[0]),
        self.var_suppliername.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_description.set(row[3]),  
                        
    
    
    #
    def update_1(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cursor_1=con.cursor()
        try:
            if  self.var_invoiceno.get()=="" or self.var_suppliername.get()=="" or self.var_contact.get()=="" or self.var_description.get()==""  :
                messagebox.showerror("Error","All fields are required",parent=self.root)
            else:
                cursor_1.execute("select * from supplier where invoice=?",(self.var_invoiceno.get(),))
                row=cursor_1.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid Invoice Nomber!!" )
                else:
                    cursor_1.execute("update supplier set name=?,contact=?,desc=? where invoice=?",(
                            
                           
                            self.var_suppliername.get(),
                            self.var_contact.get(),
                            self.var_description.get(),
                            self.var_invoiceno.get(),  
                        
                    ))
                    con.commit()
                    messagebox.showinfo("Supplier","Supplier Updated Successfully",parent=self.root)
                    self.show()
            
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")
            
    
        
    def delete(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                if self.var_invoiceno.get()=="":
                        messagebox.showerror("Error","invoice nomber must be required ",parent=self.root)
                else:
                        cur.execute("Select * from supplier where invoice=?",(self.var_invoiceno.get(),))
                        row=cur.fetchone()
                        if row==None:
                                messagebox.showerror("Error","Invalid Invoice Nomber,Try different",parent=self.root)
                        else:   
                                op=messagebox.askyesno("Confrim","Do you rally want to delete?",parent=self.root)
                                if op==True:

                                        cur.execute("delete from supplier where invoice=?",(self.var_invoiceno.get(),))
                                        con.commit()
                                        messagebox.showinfo("Delete","Supplier Deleted Succesfully",parent=self.root)
                                    
                                        self.clear()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
                
                
                
        
    
    def clear(self):
        self.var_invoiceno.set(""),
        self.var_suppliername.set(""),
        self.var_contact.set(""),
        self.var_description.set(""),  
        self.var_invoicenotxt.set(""),
        self.show()
        
        
    
        
        
    def search(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cursor_1=con.cursor()
        try:
            if self.var_invoicenotxt.get()=="":
                messagebox.showerror("Error","Search Invoice Nomber Should be required!!",parent=self.root)
            else:
                cursor_1.execute("select * from supplier where invoice=?",(self.var_invoicenotxt.get(),))
                row=cursor_1.fetchone()
                if row!=None:
                    self.supplier_table.delete(*self.supplier_table.get_children())
                    self.supplier_table.insert('',END,values=row)
                                
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to: {str(ex)}")       
        
                    
if __name__=="__main__" :
        root=customtkinter.CTk()
        obj=supplierclass(root)
        root.mainloop() 
        
       
   #or self.var_suppliername.get()=="" or self.var_contact.get()=="" or self.var_description.get()=="" or self.var_invoiceno2.get()==""