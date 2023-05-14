from tkinter import*
from PIL import ImageTk,Image
import os
import customtkinter 
from employee import emp_class
from supplier import supplierclass
from category import categoryclass
from product import productclass
from sales import salesclass
import sqlite3
from tkinter import messagebox
import os
import time
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
class hrm:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Managment System|Made by HRM")
        
#******TITLE********
        self.icon_title=PhotoImage(file="images/cart1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Small caps Font",40,"bold"),bg="#1F1C1C",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=90)
#******button*******
        button_logout = customtkinter.CTkButton(self.root,text="Logout",command=self.logout,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button_logout.place(x=1150,y=15,height=50,width=150)

#*****clock*********
        self.labl_clock=Label(self.root,text="Welcome To Inventory Management System \t\t Date:DD-MM-YYYY \t\t Time:HH-MM-SS",font=("Small caps Font",20),bg="#1F1C1C",fg="white")
        self.labl_clock.place(x=0,y=100,relwidth=1,height=70)
#*****left_menu*****
        self.MenuLogo=Image.open("images/menu.png")
        self.MenuLogo=self.MenuLogo.resize((290,280),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)
        left_menu=Frame(self.root,bd=2,relief=RIDGE,bg="#1F1C1C")
        left_menu.place(x=0,y=180,width=300,height=780)

        labl_menu_logo=Label(left_menu,image=self.MenuLogo)
        labl_menu_logo.pack(side=TOP,fill=X)

        labl_menu = customtkinter.CTkLabel(master=left_menu,text="Menu",width=120,height=25,font=("Small caps Font",23,"bold"),fg_color=("white", "#00c1e4"),text_color="#282424")
        labl_menu.place(x=0,y=192,width=300,height=50)
        button_emp = customtkinter.CTkButton(master=left_menu,text="Employee",command=self.employee,font=("Small caps Font",20),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button_emp.place(x=0,y=228,width=300,height=50)
        button_supp = customtkinter.CTkButton(master=left_menu,text="Supplier",command=self.supplier,font=("Small caps Font",20),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button_supp.place(x=0,y=264,width=300,height=50)
        button_cat = customtkinter.CTkButton(master=left_menu,text="Category",command=self.category,font=("Small caps Font",20),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button_cat.place(x=0,y=300,width=300,height=50)
        button_pro = customtkinter.CTkButton(master=left_menu,text="Product",command=self.product,font=("Small caps Font",20),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button_pro.place(x=0,y=336,width=300,height=50)
        button_sale = customtkinter.CTkButton(master=left_menu,text="Sale",command=self.sales,font=("Small caps Font",20),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button_sale.place(x=0,y=372,width=300,height=50)
        button_ext = customtkinter.CTkButton(master=left_menu,text="Exit",font=("Small caps Font",20),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button_ext.place(x=0,y=408,width=300,height=50)
#*****content******
        self.lbl_employee=customtkinter.CTkLabel(master=self.root,text="Total Employee\n [ 0 ]",font=("Small caps Font",20),fg_color=("white", "#00c1e4"),text_color="#282424",corner_radius=8)        
        self.lbl_employee.place(x=300,y=140,height=150,width=300)

        self.lbl_Supplier=customtkinter.CTkLabel(master=self.root,text="Total Supplier\n [ 0 ]",font=("Small caps Font",20),fg_color=("white", "#00c1e4"),text_color="#282424",corner_radius=8)        
        self.lbl_Supplier.place(x=650,y=140,height=150,width=300)

        self.lbl_category=customtkinter.CTkLabel(master=self.root,text="Total Category\n [ 0 ]",font=("Small caps Font",20),fg_color=("white", "#00c1e4"),text_color="#282424",corner_radius=8)        
        self.lbl_category.place(x=1000,y=140,height=150,width=300)

        self.lbl_product=customtkinter.CTkLabel(master=self.root,text="Total Product\n [ 0 ]",font=("Small caps Font",20),fg_color=("white", "#00c1e4"),text_color="#282424",corner_radius=8)        
        self.lbl_product.place(x=300,y=320,height=150,width=300)

        self.lbl_sale=customtkinter.CTkLabel(master=self.root,text="Total Sale\n [ 0 ]",font=("Small caps Font",20),fg_color=("white", "#00c1e4"),text_color="#282424",corner_radius=8)        
        self.lbl_sale.place(x=650,y=320,height=150,width=300)
        self.update_content()
#******************************************************************************************************************************************************************************************************
     def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=emp_class(self.new_win)
     def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierclass(self.new_win)
     def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryclass(self.new_win)
     def logout(self):
        self.root.destroy()
        os.system("python login1.py")
     def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productclass(self.new_win)

     def sales(self):
         self.new_win=Toplevel(self.root)
         self.new_obj=salesclass(self.new_win)
        
     def update_content(self):
         con=sqlite3.connect(database=r'inventory_management_sys.db')
         cur=con.cursor()
         try:
                cur.execute("select * from product")
                product=cur.fetchall()
                self.lbl_product.configure(text=f"Total Products\n [ {str(len(product))}]")

                cur.execute("select * from supplier")
                supplier=cur.fetchall()
                self.lbl_Supplier.configure(text=f"Total Suppliers\n [ {str(len(supplier))}]")

                cur.execute("select * from category")
                category=cur.fetchall()
                self.lbl_category.configure(text=f"Total Category\n [ {str(len(category))}]")

                cur.execute("select * from employee")
                employee=cur.fetchall()
                self.lbl_employee.configure(text=f"Total Employess\n [ {str(len(employee))}]")
                bill=len(os.listdir('bill'))

                time_=time.strftime("%I:%M:%S")
                date_=time.strftime("%d:%m:%Y")

                self.labl_clock.config(text=f"Welcome To Inventory Management System \t\t Date:{str(date_)} \t\t Time:{str(time_)}")
                self.labl_clock.after(200,self.update_content)


               # self.lbl_sales.configure(trxt=f"Total Sales{[str('bill') ]}")
         except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
        
            


if __name__=="__main__":

        root=customtkinter.CTk()
        obj=hrm(root)
        root.mainloop()