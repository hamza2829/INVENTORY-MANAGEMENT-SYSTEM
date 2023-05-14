from tkinter import*
from PIL import ImageTk,Image
import customtkinter 
import sqlite3
import time
from tkinter import ttk,messagebox
import os
import tempfile
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")
class BillClass:
     def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Managment System|Made by HRM")
        self.cart_list=[]
        self.chk_print=0
        
#***TITLE*****
        self.icon_title=PhotoImage(file="images/cart1.png")
        title=Label(self.root,text="Inventory Management System",image=self.icon_title,compound=LEFT,font=("Small caps Font",40,"bold"),bg="#1F1C1C",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=90)
#***button****
        button = customtkinter.CTkButton(self.root,text="Logout",command=self.logout,font=("Small caps Font",15,"bold"),text_color="white",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        button.place(x=1150,y=15,height=50,width=150)

#**clock******
        self.labl_clock=Label(self.root,text="Welcome To Inventory Management System \t\t Date:DD-MM-YYYY \t\t Time:HH-MM-SS",font=("Small caps Font",20),bg="#1F1C1C",fg="white")
        self.labl_clock.place(x=0,y=100,relwidth=1,height=70)
        ###product_frame###

        
        ProductFrame1=Frame(self.root,bd=4,relief=RIDGE,bg="#414141")
        ProductFrame1.place(x=6,y=180,width=600,height=700)

        pTitle=customtkinter.CTkLabel(ProductFrame1,text="All Products",font=("goudy old",27,"bold"),text_color="#0b9dcc",fg_color="#201c1c").pack(side=TOP,fill=X)


        ProductFrame2=Frame(ProductFrame1,bd=0,relief=RIDGE,bg="#414141")
        ProductFrame2.place(x=1,y=60,width=590,height=150)
        self.var_search=StringVar()
        lbl_search=customtkinter.CTkLabel(ProductFrame2,text="Search Product | By Name ",font=("Small caps Font",18,"bold"),text_color="#00c1e4").place(x=2,y=7)
        lbl_product=customtkinter.CTkLabel(ProductFrame2,text="Product Name",font=("Small caps Font",18,"bold"),text_color="#00c1e4").place(x=2,y=60)

        txt_search=customtkinter.CTkEntry(ProductFrame2,textvariable=self.var_search,font=("Small caps Font",17),text_color="#00c1e4",corner_radius=14).place(x=130,y=60,width=250,height=40)
        btn_search=customtkinter.CTkButton(ProductFrame2,text="Search",command=self.search,font=("Small caps Font",15,"bold"),text_color="white",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=302,y=55,width=125,height=50)
        btn_show_all=customtkinter.CTkButton(ProductFrame2,text="Show All",command=self.show,font=("Small caps Font",15,"bold"),text_color="white",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=302,y=5,width=125,height=50)


        ProductFrame3=Frame(ProductFrame1,bd=3,relief=RIDGE) 
        ProductFrame3.place(x=2,y=210,width=590,height=440)

        scrolly=Scrollbar(ProductFrame3,orient=VERTICAL)
        scrollx=Scrollbar(ProductFrame3,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)


        
        
        self.product_Table.heading("pid",text="PID")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="QTY")
        self.product_Table.heading("status",text="Status")
        
        self.product_Table["show"]="headings"
        
        self.product_Table.column("pid",width=50)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=50)
        self.product_Table.column("status",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)
        lbl_note=customtkinter.CTkLabel(ProductFrame1,text="Note: 'Enter 0 Quantity to remove product from the cart' ",font=("Small caps Font",13,"bold"),text_color="#00c1e4").pack(side=BOTTOM,fill=X)

# 
#*********************** Billing Area************************ 
        billframe=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        billframe.place(x=1290,y=180,width=600,height=530)#x=1210
        bTitle=customtkinter.CTkLabel(billframe,text="Customer Billing Area",font=("goudy old",30,"bold"),text_color="#0b9dcc",fg_color="#10141c")
        bTitle.pack(side=TOP,fill=X)
        scrolly=Scrollbar(billframe,orient=VERTICAL)
        scrolly.pack(side=RIGHT, fill=Y)
        self.txt_bill_area=Text(billframe,yscrollcommand=scrolly.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scrolly.config(command=self.txt_bill_area.yview)
        
# #*********************** Billing menu Area************************ 
        billmenuframe=Frame(self.root,bd=2,relief=RIDGE,bg="#10141c")
        billmenuframe.place(x=1290,y=730,width=600,height=150)#x=1210 y=520
        
        self.lbl_amnt=Label(billmenuframe,text="Bill Amount\n[0]",font=("goudy old",15,"bold"),fg="white",background="#00c1e4")
        self.lbl_amnt.place(x=10,y=5,width=165,height=60)
        
        self.lbl_discount=Label(billmenuframe,text="Discount \n[5%]",font=("goudy old",15,"bold"),fg="white",background="#00c1e4")
        self.lbl_discount.place(x=210,y=5,width=165,height=60)
        
        self.lbl_net_pay=Label(billmenuframe,text="Net pay\n[0]",font=("goudy old",15,"bold"),fg="white",background="#00c1e4")
        self.lbl_net_pay.place(x=410,y=5,width=165,height=60)
        
        btn_print=customtkinter.CTkButton(billmenuframe,text="Print",command=self.print_bill,font=("Small caps Font",15,"bold"),text_color="white",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        btn_print.place(x=8,y=50,width=165,height=60)
        
        btn_clear_all=customtkinter.CTkButton(billmenuframe,text="Clear All",command=self.clear_all,font=("Small caps Font",15,"bold"),text_color="white",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        btn_clear_all.place(x=140,y=50,width=165,height=60)

        
        btn_generate=customtkinter.CTkButton(billmenuframe,text="Save Bill",command=self.generate_bill,font=("Small caps Font",15,"bold"),text_color="white",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2")
        btn_generate.place(x=273,y=50,width=165,height=60)#275
          

        ###customer frame###
        self.var_cname=StringVar()
        self.var_contact=StringVar()

        CustomerFrame=Frame(self.root,bd=4,relief=RIDGE,bg="white")
        CustomerFrame.place(x=650,y=180,width=600,height=700)#600

        cTitle=customtkinter.CTkLabel(CustomerFrame,text="Customer Details",font=("goudy old",27,"bold"),text_color="#0b9dcc",fg_color="#201c1c").pack(side=TOP,fill=X)
        lbl_name=Label(CustomerFrame,text="Name",font=("times new roman",15),bg="white",fg="green").place(x=5,y=60)
        txt_name=Entry(CustomerFrame,textvariable=self.var_cname,font=("times new roman",13),bg="lightblue").place(x=80,y=60,width=180)

        lbl_contact=Label(CustomerFrame,text="Contact No",font=("times new roman",15),bg="white",fg="green").place(x=270,y=60)
        txt_contact=Entry(CustomerFrame,textvariable=self.var_contact,font=("times new roman",13),bg="lightblue").place(x=380,y=60,width=180)

        ###cal cart farme ###
        Cal_Cart_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Cal_Cart_Frame.place(x=650,y=300,width=600,height=560)

#         ###calculator farme ###
        self.var_cal_input=StringVar()
        Cal_Frame=Frame(Cal_Cart_Frame,bd=2,relief=RIDGE,bg="white")
        Cal_Frame.place(x=5,y=30,width=280,height=360) #w260 h340
        
        
    
        txt_cal_input=Entry(Cal_Frame,textvariable=self.var_cal_input,font=('arial',15,'bold'),width=21,bd=10,relief=GROOVE,state='readonly',justify=RIGHT)
        txt_cal_input.grid(row=0,columnspan=4)
        
        
        btn_7=Button(Cal_Frame,text='7',font=('arial',15,'bold'),command=lambda:self.get_input(7),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=0)
        btn_8=Button(Cal_Frame,text='8',font=('arial',15,'bold'),command=lambda:self.get_input(8),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=1)
        btn_9=Button(Cal_Frame,text='9',font=('arial',15,'bold'),command=lambda:self.get_input(9),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=2)
        btn_sum=Button(Cal_Frame,text='+',font=('arial',15,'bold'),command=lambda:self.get_input('+'),bd=5,width=4,pady=10,cursor="hand2").grid(row=1,column=3)
   
    
        
        btn_4=Button(Cal_Frame,text='4',font=('arial',15,'bold'),command=lambda:self.get_input(4),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=0)
        btn_5=Button(Cal_Frame,text='5',font=('arial',15,'bold'),command=lambda:self.get_input(5),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=1)
        btn_6=Button(Cal_Frame,text='6',font=('arial',15,'bold'),command=lambda:self.get_input(6),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=2)
        btn_sub=Button(Cal_Frame,text='-',font=('arial',15,'bold'),command=lambda:self.get_input('-'),bd=5,width=4,pady=10,cursor="hand2").grid(row=2,column=3)
       
       
       
        btn_1=Button(Cal_Frame,text='1',font=('arial',15,'bold'),command=lambda:self.get_input(1),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=0)
        btn_2=Button(Cal_Frame,text='2',font=('arial',15,'bold'),command=lambda:self.get_input(2),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=1)
        btn_3=Button(Cal_Frame,text='3',font=('arial',15,'bold'),command=lambda:self.get_input(3),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=2)
        btn_mul=Button(Cal_Frame,text='*',font=('arial',15,'bold'),command=lambda:self.get_input('*'),bd=5,width=4,pady=10,cursor="hand2").grid(row=3,column=3)
       
       
        btn_0=Button(Cal_Frame,text='0',font=('arial',15,'bold'),command=lambda:self.get_input(0),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=0)
        btn_c=Button(Cal_Frame,text='c',font=('arial',15,'bold'),command=self.clear_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=1)
        btn_eq=Button(Cal_Frame,text='=',font=('arial',15,'bold'),command=self.perform_cal,bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=2)
        btn_div=Button(Cal_Frame,text='/',font=('arial',15,'bold'),command=lambda:self.get_input('/'),bd=5,width=4,pady=15,cursor="hand2").grid(row=4,column=3)
        
#         ###cart farme###
        
        cart_Frame=Frame(Cal_Cart_Frame,bd=3,relief=RIDGE) 
        cart_Frame.place(x=300,y=30,width=295,height=360)
        
        
        
        
        self.cartTitle=Label(cart_Frame,text="Cart \t Total Product: [0] ",font=("goudy old",12),bg="lightgray")
        self.cartTitle.pack(side=TOP,fill=X)


        scrolly=Scrollbar(cart_Frame,orient=VERTICAL)
        scrollx=Scrollbar(cart_Frame,orient=HORIZONTAL)

        self.CartTable=ttk.Treeview(cart_Frame,columns=("pid","name","price","qty"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.CartTable.xview)
        scrolly.config(command=self.CartTable.yview)


        

        self.CartTable.heading("pid",text="PID")
        self.CartTable.heading("name",text="Name")
        self.CartTable.heading("price",text="Price")
        self.CartTable.heading("qty",text="QTY")
        
        
        self.CartTable["show"]="headings"
        
        self.CartTable.column("pid",width=40)
        self.CartTable.column("name",width=90)
        self.CartTable.column("price",width=90)
        self.CartTable.column("qty",width=40)
        self.CartTable.pack(fill=BOTH,expand=1)
        self.CartTable.bind("<ButtonRelease-1>",self.get_data_cart)


# ###add cart bwidets frame###
        self.var_pid=StringVar()
        self.var_pname=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_stock=StringVar()

        Add_CartWidgetsFrame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        Add_CartWidgetsFrame.place(x=680,y=730,width=530,height=110)
        #y=730

        lbl_P_name=Label(Add_CartWidgetsFrame,text="Product Name",font=("times new roman",15),bg="white").place(x=5,y=5)
        txt_P_name=Entry(Add_CartWidgetsFrame,textvariable=self.var_pname,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=5,y=35,width=190,height=22)
        
        lbl_P_price=Label(Add_CartWidgetsFrame,text="Price Per Qty",font=("times new roman",15),bg="white").place(x=230,y=5)
        txt_P_price=Entry(Add_CartWidgetsFrame,textvariable=self.var_price,font=("times new roman",15),bg="lightyellow",state='readonly').place(x=230,y=35,width=150,height=22)
        
        lbl_P_qty=Label(Add_CartWidgetsFrame,text="Quantity",font=("times new roman",15),bg="white").place(x=390,y=5)
        txt_P_qty=Entry(Add_CartWidgetsFrame,textvariable=self.var_qty,font=("times new roman",15),bg="lightyellow").place(x=390,y=35,width=120,height=22)
        
        self.lbl_inStock=Label(Add_CartWidgetsFrame,text="In Stock ",font=("times new roman",15),bg="white")
        self.lbl_inStock.place(x=5,y=70)
        btn_clear_cart=Button(Add_CartWidgetsFrame,text="Clear",command=self.clear_cart,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=180,y=70,width=150,height=30)
        btn_add_cart=Button(Add_CartWidgetsFrame,command=self.add_update_cart,text="Add | Update Cart",font=("times new roman",15,"bold"),bg="orange",cursor="hand2").place(x=340,y=70,width=180,height=30)
        self.show()
        #self.bill_top()
        self.update_date_time()
# #==============All functions===================
     def get_input(self,num):
        xnum= self.var_cal_input.get() + str(num)
        self.var_cal_input.set(xnum)
        


     def clear_cal(self):
        self.var_cal_input.set('')    
        
 
 
        
     def perform_cal(self):
        result=self.var_cal_input.get()
        self.var_cal_input.set(eval(result))
     def logout(self):
        self.root.destroy()
        #os.system("python login1.py")  
        
     def show(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                # self.product_Table=ttk.Treeview(ProductFrame3,columns=("pid","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
                cur.execute("select pid,name,price,qty,status from product where status='Active'")
                rows=cur.fetchall()
                self.product_Table.delete(*self.product_Table.get_children())
                for row in rows:
                        self.product_Table.insert('',END,values=row)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


     def search(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                
                if self.var_search.get()=="":
                        messagebox.showerror("Error","Search input should be required",parent=self.root)
                else:
                        cur.execute("select pid,name,price,qty,status from product where name  LIKE '%"+self.var_search.get()+"%' and status='Active'")
                        rows=cur.fetchall()
                        if len(rows)!=0:
                                self.product_Table.delete(*self.product_Table.get_children())
                                for row in rows:
                                        self.product_Table.insert('',END,values=row)
                        else:
                                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)        
        
     def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']  
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.lbl_inStock.config(text=f"In Stock[{str(row[3])}]")
        self.var_stock.set(row[3])
        self.var_qty.set('1')



     def get_data_cart(self,ev):
        f=self.CartTable.focus()
        content=(self.CartTable.item(f))
        row=content['values']  
        self.var_pid.set(row[0])
        self.var_pname.set(row[1])
        self.var_price.set(row[2])
        self.var_qty.set(row[3])
        self.lbl_inStock.config(text=f"In Stock[{str(row[4])}]")
        self.var_stock.set(row[4])
            
        

        
     def add_update_cart(self):
             if self.var_pid.get()=="":
                messagebox.showerror("Error","Please select product from the list",parent=self.root)
             elif self.var_qty.get()=="":
                 messagebox.showerror("Error","Quantity is required",parent=self.root)
             elif int(self.var_qty.get())>int(self.var_stock.get()):
                 messagebox.showerror("Error","Quantity is Invalid!",parent=self.root)   
             else:
                # price_cal=int(self.var_qty.get())*float(self.var_price.get())
                # price_cal=float(price_cal)
                price_cal=self.var_price.get()
                cart_data=[self.var_pid.get(),self.var_pname.get(),price_cal,self.var_qty.get(),self.var_stock.get()] 
                 
                
                #************** update cart************#
                present='no'
                index_=0
                for row in self.cart_list:
                        if self.var_pid.get()==row[0]:
                                present='yes'
                                break
                        index_+=1
                if present=='yes':
                        op=messagebox.askyesno('Confirm', "Product already present \n Do you want to Update | Remove from the list",parent=self.root)
                        if op==True:
                                if self.var_qty.get()=="0":
                                        self.cart_list.pop(index_)
                                else:
                                        # pid,name,price,qty,status
                                        # self.cart_list[index_][2]=price_cal #price
                                        self.cart_list[index_][3]=self.var_qty.get()
                
                else:
                        self.cart_list.append(cart_data) 
                                                
              
                
                self.show_cart()
                self.bill_updates()
     
     
     
     def bill_updates(self):
                self.bill_amnt=0
                self.net_pay=0
                
                for row in self.cart_list:
                        # pid,name,price,qty,status 
                        self.bill_amnt=self.bill_amnt+(float(row[2])*int(row[3]))
                
                self.discount=(self.bill_amnt*5)/100
                self.net_pay=self.bill_amnt-self.discount
                self.lbl_amnt.config(text=f'Bill Amnt\n{str(self.bill_amnt)}')
                self.lbl_net_pay.config(text=f'Net Pay\n{str(self.net_pay)}')
                self.cartTitle.config(text=f"Cart \t Total Product: [{str(len(self.cart_list))}]")
                
                
                
                
     def show_cart(self):
        
        try:
                self.CartTable.delete(*self.CartTable.get_children())
                for row in self.cart_list:
                        self.CartTable.insert('',END,values=row)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)




     def generate_bill(self):
        if self.var_cname.get()=='' or self.var_contact.get()=='':
                messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len(self.cart_list)==0:
                messagebox.showerror("Error",f"Please add product in the cart!!",parent=self.root)

        else:
                #------bill top------
                self.bill_top()
                #------bill middle------
                self.bill_middle()
                #------bill bottom------
                self.bill_bottom()
                fp=open(f'bill/{str(self.invoice)}.txt','w')
                fp.write(self.txt_bill_area.get('1.0',END))
                fp.close()
                messagebox.showinfo('Saved',"Bill has been generated/ Saved in Backend",parent=self.root)
                self.chk_print=1
     def bill_top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        bill_top_temp=f'''
\t\tHRM-Inventory
\t Phone No. +9231567***** , Karachi-125001
{str("="*47)}
 Customer Name: {self.var_cname.get()}
 Ph no. :{self.var_contact.get()}
 Bill No. {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*47)}
 Product Name\t\t\tQTY\tPrice
{str("="*47)}
        '''
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',bill_top_temp)

     
     
     
     def bill_bottom(self):
        bill_bottom_temp=f'''
{str("="*47)}
 Bill Amount\t\t\t\tRs.{self.bill_amnt}
 Discount\t\t\t\tRs.{self.discount}
 Net Pay\t\t\t\tRs.{self.net_pay}
{str("="*47)}\n
        '''
        self.txt_bill_area.insert(END,bill_bottom_temp)                   

     def bill_middle(self):
            con=sqlite3.connect(database=r'inventory_management_sys.db')
            cur=con.cursor()
            
            try:
                

                for row in self.cart_list:
                        pid=row[0]
                        name=row[1]
                        qty=int(row[4])-int(row[3])
                        if int(row[3])==int(row[4]):
                                status='Inactive'
                        if int(row[3])!=int(row[4]):
                                status='Active'

                        price=float(row[2])*int(row[3])
                        price=str(price)
                        self.txt_bill_area.insert(END,"\n "+name+"\t\t\t"+row[3]+"\tRs."+price)
                        #+++++++ update qty in product table++++++++++++===
                        cur.execute('Update product set qty=?,status=? where pid=?',(
                                qty,
                                status,
                                pid
                        ))
                        con.commit()
                con.close()
                self.show()

            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
     def clear_cart(self):
        self.var_pid.set('')
        self.var_pname.set('')
        self.var_price.set('')
        self.var_qty.set('')
        self.lbl_inStock.config(text=f"In Stock")
        self.var_stock.set('')


     def clear_all(self):
        del self.cart_list[:]
        self.var_cname.set('')
        self.var_contact.set('')
        self.txt_bill_area.delete('1.0',END)
        self.cartTitle.config(text=f"Cart \t Total Product: [0]")
        self.var_search('')
        self.clear_cart()
        self.show()
        self.show_cart()   
        self.chk_print=0


     def update_date_time(self):
            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d:%m:%Y")

            self.labl_clock.config(text=f"Welcome To Inventory Management System \t\t Date:{str(date_)} \t\t Time:{str(time_)}")
            self.labl_clock.after(200,self.update_date_time)

     def print_bill(self):
        if self.chk_print==1:
                messagebox.showinfo('Print',"Please wait while printing",parent=self.root)
                new_file=tempfile.mktemp('.txt')
                open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
                os.startfile(new_file,'print')
        else:
                messagebox.showinfo('Print',"Please genertate bill to print receipt",parent=self.root)
     def logout(self):
        self.root.destroy()
        os.system("python login1.py")
if __name__=="__main__" :
        root=customtkinter.CTk()
        obj=BillClass(root)
        root.mainloop() 