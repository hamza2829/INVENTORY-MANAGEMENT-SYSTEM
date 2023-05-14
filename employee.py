from tkinter import*
from PIL import ImageTk,Image
import customtkinter 
from tkinter import ttk
from tkinter import ttk,messagebox
import sqlite3
customtkinter.set_appearance_mode("dark")
#customtkinter.set_default_color_theme("#17c0e9")
class emp_class:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1600x740+300+220")
        self.root.title("Inventory Managment System|Made by HRM ") 
        self.root.focus_force()
        self.root.config(bg="#282424")
        #*************variable**********
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()
       
        self.var_emp_id=StringVar()
        self.var_gender=StringVar()
        self.var_contact=StringVar()
        self.var_name=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_email=StringVar()
        self.var_pass=StringVar()
        self.var_utype=StringVar()
        #self.var_addresse=StringVar()
        self.var_salary=StringVar()
       #**************search_frame********
        SearchFrame=LabelFrame(self.root,text="Search Employe",font=("Small caps Font",12,"bold"),bg="white",bd=2,relief=RIDGE)
        SearchFrame.place(x=250,y=20,width=650,height=90)
       
        #*************options**************
        #cmb_search=customtkinter.CTkComboBox(self.root,values=("Select","email","name","contact"),state='readonly',justify=CENTER,font=("Small caps Font",15))
        #cmb_search.place(x=12,y=18,width=550)
        
 
        combobox=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,state='readonly',justify=CENTER,values=["Select", "email","name","contact"],font=("Small caps Font",15),foreground="#1F1C1C")
        combobox.place(x=2,y=15,width=180)
        combobox.current(0)

        txt_search=customtkinter.CTkEntry(SearchFrame,textvariable=self.var_searchtxt,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=150,y=10)
        btn_search = customtkinter.CTkButton(SearchFrame,text="Search",command=self.search,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=300,y=10,width=122,height=40)
        title_emp=customtkinter.CTkLabel(self.root,text="Employee",font=("Small caps Font",16),text_color="#282424",corner_radius=14,fg_color="#00c1e4").place(x=50,y=100,width=1500 )
       
#**********content********
        #txtf_gender=customtkinter.CTkEntry(self.root,textvariable=self.var_gender,font=("Small caps Font",16),text_color="#282424",corner_radius=14,fg_color="#00c1e4").place(x=500,y=150 )
#**********row_1**********
        labl_emp_id=customtkinter.CTkLabel(self.root,text="Emp ID",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=50,y=150 )
        labl_gender=customtkinter.CTkLabel(self.root,text="Gender",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=350,y=150 )
        labl_contact=customtkinter.CTkLabel(self.root,text="Contact",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=750,y=150 )

        txtf_emp_id=customtkinter.CTkEntry(self.root,textvariable=self.var_emp_id,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=150,y=150,width=180 )
        combobox_gender=ttk.Combobox(self.root,textvariable=self.var_gender,state='readonly',justify=CENTER,values=["Select", "Male","Female","Others"],font=("Small caps Font",15),foreground="#1F1C1C")
        combobox_gender.place(x=750,y=230,width=180 )
        combobox_gender.current(0)
        txtf_contact=customtkinter.CTkEntry(self.root,textvariable=self.var_contact,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=900,y=150,width=180 )
#**********r0w_2*********       
        labl_name=customtkinter.CTkLabel(self.root,text="Name",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=50,y=190)
        labl_D_O_B=customtkinter.CTkLabel(self.root,text="D.O.B",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=350,y=190)
        labl_D_O_J=customtkinter.CTkLabel(self.root,text="D.O.J",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=750,y=190 )

        txtf_name=customtkinter.CTkEntry(self.root,textvariable=self.var_name,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=150,y=190,width=180 )
        txtf_D_O_B=customtkinter.CTkEntry(self.root,textvariable=self.var_dob,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=500,y=190,width=180 )
        txtf_D_O_J=customtkinter.CTkEntry(self.root,textvariable=self.var_doj,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=900,y=190 ,width=180)
#*********ROW_3***********
        labl_EMAIL=customtkinter.CTkLabel(self.root,text="Email",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=50,y=230 )
        labl_PASSWORD=customtkinter.CTkLabel(self.root,text="Password",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=350,y=230 )
        labl_USER_TYPE=customtkinter.CTkLabel(self.root,text="User Type",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=750,y=230 )
        
        txtf_email=customtkinter.CTkEntry(self.root,textvariable=self.var_email,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=150,y=230,width=180 )
        txtf_password=customtkinter.CTkEntry(self.root,textvariable=self.var_pass,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=500,y=230,width=180 )
        #txtf_user_type=customtkinter.CTkEntry(self.root,textvariable=self.var_utype,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14,fg_color="#00c1e4").place(x=900,y=230,width=180 )
        
        combobox_USER_TYPE=ttk.Combobox(self.root,textvariable=self.var_utype,state='readonly',justify=CENTER,values=["Admin","Employee"],font=("Small caps Font",15),foreground="#1F1C1C")
        combobox_USER_TYPE.place(x=1350,y=350,width=180 )
        combobox_USER_TYPE.current(0)
#**********row_4************
        labl_Addresse=customtkinter.CTkLabel(self.root,text="Addresse",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=50,y=270 )
        labl_Salary=customtkinter.CTkLabel(self.root,text="Salary",font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=350,y=270 )        
        
        self.txtf_Addresse=Text(self.root,font=("Small caps Font",16))
        self.txtf_Addresse.place(x=230,y=405,width=250,height=100)
        txtf_Salary=customtkinter.CTkEntry(self.root,textvariable=self.var_salary,font=("Small caps Font",16),text_color="#00c1e4",corner_radius=14).place(x=500,y=270,width=180 )
#**********button*************
        btn_add = customtkinter.CTkButton(self.root,text="Add",command=self.add,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=500,y=305,width=120,height=40)
        btn_update = customtkinter.CTkButton(self.root,text="Update",command=self.update,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=620,y=305,width=120,height=40)
        btn_delete = customtkinter.CTkButton(self.root,text="Delete",command=self.delete,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=740,y=305,width=120,height=40)
        btn_clear = customtkinter.CTkButton(self.root,text="Clear",command=self.clear,font=("Small caps Font",15,"bold"),text_color="#282424",fg_color="#00c1e4",hover_color="#00d6fc",cursor="hand2").place(x=860,y=305,width=120,height=40)
#*********************frame**********************************
        EMP_frame=Frame(self.root,bd=3,relief=RIDGE)
        EMP_frame.place(x=0,y=530,relwidth=1,height=200)
        scrollx=Scrollbar(EMP_frame,orient=HORIZONTAL)
        scrolly=Scrollbar(EMP_frame,orient=VERTICAL)
        self.emp_table=ttk.Treeview(EMP_frame,columns=("eid","gender","contact","name","dob","doj","email","pass","utype","addresse","salary"),yscrollcommand=scrolly.set,xscrollcommand=scrollx)
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.emp_table.xview)
        scrolly.config(command=self.emp_table.yview)
        self.emp_table.pack(side=TOP,fill=BOTH,expand=1)
        self.emp_table.heading("eid",text="Emp Id")
        self.emp_table.heading("gender",text="Gender")
        self.emp_table.heading("contact",text="Contact")
        self.emp_table.heading("name",text="Name")
        self.emp_table.heading("dob",text="D_O_B")
        self.emp_table.heading("doj",text="D_O_J")
        self.emp_table.heading("email",text="Email")
        self.emp_table.heading("pass",text="Password")
        self.emp_table.heading("utype",text="User_type")
        self.emp_table.heading("addresse",text="Addresse")
        self.emp_table.heading("salary",text="Salary")
        self.emp_table["show"]="headings"

        self.emp_table.column("eid",width=90)
        self.emp_table.column("gender",width=90)
        self.emp_table.column("contact",width=90)
        self.emp_table.column("name",width=90)
        self.emp_table.column("dob",width=90)
        self.emp_table.column("doj",width=90)
        self.emp_table.column("email",width=90)
        self.emp_table.column("pass",width=90)
        self.emp_table.column("utype",width=90)
        self.emp_table.column("addresse",width=90)
        self.emp_table.column("salary",width=90)
        self.emp_table.pack(fill=BOTH,expand=1)
        self.emp_table.bind("<ButtonRelease-1>",self.get_data)
        self.show()
        #self.emp_table.place(x=680,y=100,width=410,height=380)
        #self.emp_table.column("sup_id",width=80)
        #self.emp_table.column("invoice_no",width=80)
        #self.emp_table.column("name",width=80)
        #self.emp_table.column("contact",width=80)
        #self.emp_table.column("detail",width=100)
#*****************************************************************
    def add(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                if self.var_emp_id.get()=="":
                        messagebox.showerror("Error","employe id is must be required",parent=self.root)
                else:
                        cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                        row=cur.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","This employee is already assigned,Try different",parent=self.root)
                        else:
                                cur.execute("Insert into employee(eid,gender,contact,name,dob,doj,email,pass,utype,addresse,salary) values(?,?,?,?,?,?,?,?,?,?,?)",(
                                                        self.var_emp_id.get(),
                                                        self.var_gender.get(),
                                                        self.var_contact.get(),
                                                        self.var_name.get(),
                                                        self.var_dob.get(),
                                                        self.var_doj.get(),
                                                        self.var_email.get(),
                                                        self.var_pass.get(),
                                                        self.var_utype.get(),
                                                        self.txtf_Addresse.get('1.0',END ),
                                                        self.var_salary.get(),


                                ))
                                con.commit()
                                messagebox.showinfo("Succes","Employee added succesfully",parent=self.root)
                                self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def show(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                cur.execute("select * from employee")
                rows=cur.fetchall()
                self.emp_table.delete(*self.emp_table.get_children())
                for row in rows:
                        self.emp_table.insert('',END,values=row)

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def get_data(self,ev):
        f=self.emp_table.focus()
        content=(self.emp_table.item(f))
        row=content['values']
        #print(row)
        self.var_emp_id.set(row[0]),
        self.var_gender.set(row[1]),
        self.var_contact.set(row[2]),
        self.var_name.set(row[3]),
        self.var_dob.set(row[4]),
        self.var_doj.set(row[5]),
        self.var_email.set(row[6]),
        self.var_pass.set(row[7]),                                                        
        self.var_utype.set(row[8]),
        self.var_salary.set(row[10]),
        self.txtf_Addresse.delete('1.0',END)
        self.txtf_Addresse.insert(END,row[9])
        self.txtf_Addresse.set(row[9]),
        
    def update(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                if self.var_emp_id.get()=="":
                        messagebox.showerror("Error","employe id is must be required",parent=self.root)
                else:
                        cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                        row=cur.fetchone()
                        if row==None:
                                messagebox.showerror("Error","This employee is already assigned,Try different",parent=self.root)
                        else:
                                cur.execute("Update employee set gender=?,contact=?,name=?,dob=?,doj=?,email=?,pass=?,utype=?,addresse=?,salary=? where eid=?",(
                                                        self.var_gender.get(),
                                                        self.var_contact.get(),
                                                        self.var_name.get(),
                                                        self.var_dob.get(),
                                                        self.var_doj.get(),
                                                        self.var_email.get(),
                                                        self.var_pass.get(),
                                                        self.var_utype.get(),
                                                        self.txtf_Addresse.get('1.0',END ),
                                                        self.var_salary.get(),
                                                        self.var_emp_id.get(),


                                ))
                                con.commit()
                                messagebox.showinfo("Succes","Employee Updated succesfully",parent=self.root)
                                self.show()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def delete(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                if self.var_emp_id.get()=="":
                        messagebox.showerror("Error","employe id is must be required",parent=self.root)
                else:
                        cur.execute("Select * from employee where eid=?",(self.var_emp_id.get(),))
                        row=cur.fetchone()
                        if row==None:
                                messagebox.showerror("Error","Invalid employee id,Try different",parent=self.root)
                        else:   
                                op=messagebox.askyesno("Confrim","Do you rally want to delete?",parent=self.root)
                                if op==True:

                                        cur.execute("delete from employee where eid=?",(self.var_emp_id.get(),))
                                        con.commit()
                                        messagebox.showinfo("Delete","Employee Deleted succesfully",parent=self.root)
                                        
                                        self.clear()
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def clear(self):
        self.var_emp_id.set(""),
        self.var_gender.set("Select"),
        self.var_contact.set(""),
        self.var_name.set(""),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_email.set(""),
        self.var_pass.set(""),                                                        
        self.var_utype.set("Admin"),
        self.var_salary.set(""),
        self.txtf_Addresse.delete('1.0',END)
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()
        #self.txtf_Addresse.set(""),
    def search(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                if self.var_searchby.get()=="Select":
                        messagebox.showerror("Error","Select Search by option",parent=self.root)
                elif self.var_searchtxt.get()=="":
                        messagebox.showerror("Error","Search input should be required",parent=self.root)
                else:
                        cur.execute("select * from employee where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                        rows=cur.fetchall()
                        if len(rows)!=0:
                                self.emp_table.delete(*self.emp_table.get_children())
                                for row in rows:
                                        self.emp_table.insert('',END,values=row)
                        else:
                                messagebox.showerror("Error","No record found",parent=self.root)
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

if __name__=="__main__":
        root=customtkinter.CTk()
        obj=emp_class(root)
        root.mainloop()        