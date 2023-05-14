from tkinter import*
import tkinter
import qrcode
from PIL import Image,ImageTk
import customtkinter 

class QR_Generator:
    def __init__(self,root):
        self.root=root 
        self.root.geometry("900x500+200+50")
        self.root.title("QR GENERATOR")
        self.root.resizable(False,False)

        title=Label(self.root,text="QR CODE GENERATOR",font=("times new roman",40),bg='#2596be').place(x=0,y=0,relwidth=1)


        ###employee window details#####
        ###Variables#####
        self.var_emp_code=StringVar()
        self.var_name=StringVar()
        self.var_designation=StringVar()
        self.var_department=StringVar()
        emp_Frame=Frame(self.root,bd=3,relief=RIDGE,bg='white')
        emp_Frame.place(x=50,y=100,width=500,height=380)

        emp_title=Label(emp_Frame,text="EMPLOYEE DETAILS",font=("goudy old style",20),bg='#2596be').place(x=0,y=0,relwidth=1)

        lble_emp_code=Label(emp_Frame,text="EMPLOYEE ID",font=("times new roman",15,'bold'),bg='white').place(x=20,y=60)
        lble_name=Label(emp_Frame,text="NAME ID",font=("times new roman",15,'bold'),bg='white').place(x=20,y=100)
        lble_department=Label(emp_Frame,text="DEPARTMENT",font=("times new roman",15,'bold'),bg='white').place(x=20,y=140)
        lble_designation=Label(emp_Frame,text="DESIGNATION",font=("times new roman",15,'bold'),bg='white').place(x=20,y=180)

        txt_emp_code=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_emp_code,bg='lightyellow').place(x=200,y=60)
        txt_name=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_name,bg='lightyellow').place(x=200,y=100)
        txt_department=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_designation,bg='lightyellow').place(x=200,y=140)
        txt_designation=Entry(emp_Frame,font=("times new roman",15),textvariable=self.var_department,bg='lightyellow').place(x=200,y=180)

        btn_generate=Button(emp_Frame,text='QR GENERATE',command=self.generate,font=('times new roman',18,'bold'),bg='#2596be',fg='white').place(x=90,y=250,width=180,height=30)
        btn_Clear=Button(emp_Frame,text='CLEAR',command=self.clear,font=('times new roman',18,'bold'),bg='#607d8b',fg='white').place(x=282,y=250,width=120,height=30)
        
        self.msg=''
        self.lble_msg=Label(emp_Frame,text=self.msg,font=("times new roman",15,'bold'),bg='white',fg='green')
        self.lble_msg.place(x=0,y=310,relwidth=1)

        ###employee QR CODE details#####
        qr_Frame=Frame(self.root,bd=2,relief=RIDGE,bg='white')
        qr_Frame.place(x=600,y=100,width=280,height=380)

        emp_title=Label(qr_Frame,text="EMPLOYEE QR CODE",font=("goudy old style",20),bg='#2596be').place(x=0,y=0,relwidth=1)
        self.qr_code=Label(qr_Frame,text="QR Not Avaialabe",font=("goudy old style",15),bg='#2596be',fg='white',bd=1,relief=RIDGE )
        self.qr_code.place(x=35,y=100,width=180,height=180)

    def clear(self):
        self.var_emp_code.set('')
        self.var_name.set('')
        self.var_designation.set('')
        self.var_department.set('')
        self.msg=''
        self.lble_msg.config(text=self.msg)
    def generate(self):
        if self.var_emp_code.get()=='' or self.var_name.get()=='' or self.var_department.get()=='' or self.var_designation.get()=='':
            self.msg='All feilds are required!!!'
            self.lble_msg.config(text=self.msg,fg='red')
        else:
            qr_data=(f"Employee ID: {self.var_emp_code.get()}\nEmployee Name:{self.var_name.get()}\nDepartment: {self.var_department.get()}\nDesignation: {self.var_designation.get()}")
            qr_code=qrcode.make(qr_data)
            print(qr_code)

            #### QR code Image#####
            self.im=ImageTk.PhotoImage(qr_code)
            self.qr_code.config(image=self.im)

            #### updating notification#####
            self.msg='QR GENERATED SUCCESSFULLY!!!!'   
            self.lble_msg.config(text=self.msg,fg='green')

if __name__=="__main__":

    
        
        root=customtkinter.CTk()
        obj=QR_Generator(root)
        root.mainloop()