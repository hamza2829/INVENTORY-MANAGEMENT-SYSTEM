import smtplib
import email_pass
import tkinter
import customtkinter
from PIL import ImageTk,Image
from tkinter import*
from PIL import ImageTk,Image
import customtkinter 
from tkinter import ttk
from tkinter import ttk,messagebox
import os
import sqlite3
import time
customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green
class login_sys:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title('Login')
        self.root.config(bg='#242424')
        self.root.title('Login')

        
 



    

        self.otp=''

        self.img1=ImageTk.PhotoImage(Image.open("pattern.png"))
        l1=customtkinter.CTkLabel(self.root,image=self.img1)
        l1.pack()
        
#creating custom frame
        self.employee_id=StringVar()
        self.password=StringVar()
        frame=customtkinter.CTkFrame(self.root, width=320, height=360, corner_radius=15)
        frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
 
        l2=customtkinter.CTkLabel(master=frame, text="Log into your Account",font=('Century Gothic',20))
        l2.place(x=50, y=45)
        entry1=customtkinter.CTkEntry(master=frame, width=220,textvariable=self.employee_id ,placeholder_text='Employee id')
        entry1.place(x=50, y=110)
        

        entry2=customtkinter.CTkEntry(master=frame, width=220,textvariable=self.password, placeholder_text='Password', show="*")
        entry2.place(x=50, y=165)

        # l3=customtkinter.CTkLabel(master=frame, text="Forget password?",font=('Century Gothic',12))
        # l3.place(x=155,y=195)

        button1_forget = customtkinter.CTkButton(master=frame, command=self.forget_pass,width=220, text="Forget password?", corner_radius=6,border_width=0,fg_color="transparent",hover_color="#2c2c2c")
        button1_forget.place(x=100,y=195)

        l2=customtkinter.CTkLabel(master=frame, text="OR",font=('Century Gothic',14),fg_color="transparent",text_color="Lightgrey")
        l2.place(x=145, y=270)

#Create custom button
        button_login = customtkinter.CTkButton(master=frame,command=self.login,width=220, text="Login",bg_color="#2c2c2c",corner_radius=6)
        button_login.place(x=50, y=240)

        button_signup = customtkinter.CTkButton(master=frame, width=110, text="Sign Up", corner_radius=6,bg_color="#2c2c2c")
        button_signup.place(x=100, y=300)

        

    def forget_pass(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:    
                if self.employee_id.get()=="":
                    messagebox.showerror("Error","Employee id is required",parent=self.root)
                else:
                    cur.execute("select email from employee where eid=? ",(self.employee_id.get(),))
                    email=cur.fetchone()
                    if email==None:
                        messagebox.showerror("Error","Invalid Employee Id",parent=self.root)
                    else:
                    #    call send_email_function()
                         self.var_otp=StringVar()
                         self.var_newpass=StringVar()
                         self.var_con_newpass=StringVar()
                         chk=self.send_email(email[0])
                         if chk=='f':
                                messagebox.showerror("Error","Connection error ,Try again")
                         else:
                            self.forget_pass_win=Toplevel(self.root)
                            self.forget_pass_win.title=('Reset password')
                            self.forget_pass_win.geometry('480x550+730+270')
                            self.forget_pass_win.focus_force()
                            self.forget_pass_win.config(bg='#242424')
                            title=customtkinter.CTkLabel(self.forget_pass_win,text="Reset Password",font=("Century Gothic",20),fg_color="transparent").pack(side=TOP,fill=X)
                            
                            l2_forget=customtkinter.CTkLabel(master=self.forget_pass_win, text="Enter The OTP Sent To Your Email",font=('Century Gothic',16))
                            l2_forget.place(x=35, y=55)
                            l2_OTP=customtkinter.CTkLabel(master=self.forget_pass_win, text="O.T.P",font=('Century Gothic',14))
                            l2_OTP.place(x=10, y=120)
                            entry1_OTP=customtkinter.CTkEntry(master=self.forget_pass_win,textvariable=self.var_otp ,width=220,placeholder_text='Enter O.T.P')
                            entry1_OTP.place(x=80, y=120,width=210,height=40)
                            self.VERIFY = customtkinter.CTkButton(master=self.forget_pass_win,command=self.validate_otp,width=220, text="Verify",bg_color="#2c2c2c",corner_radius=6)
                            self.VERIFY.place(x=235,y=120,width=100,height=40)
                            entry1_pass=customtkinter.CTkEntry(master=self.forget_pass_win, textvariable=self.var_newpass,width=220,placeholder_text='Enter Password')
                            entry1_pass.place(x=80, y=170,width=330,height=40)   
                            l2_pass=customtkinter.CTkLabel(master=self.forget_pass_win,text="Password",font=('Century Gothic',14))
                            l2_pass.place(x=10, y=170)
                            entry1_repass=customtkinter.CTkEntry(master=self.forget_pass_win,textvariable=self.var_con_newpass ,width=220 ,placeholder_text='Re-Enter Password')
                            entry1_repass.place(x=80, y=220,width=330,height=40)   
                            l2_repass=customtkinter.CTkLabel(master=self.forget_pass_win, text="Confrim",font=('Century Gothic',14))
                            l2_repass.place(x=10, y=220)
                            self.button_submit = customtkinter.CTkButton(master=self.forget_pass_win, width=110,command=self.update_pass,state=DISABLED,text="Submit", corner_radius=6,bg_color="#2c2c2c")
                            self.button_submit.place(x=100, y=270)

                        
        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def update_pass(self):
        if self.var_newpass.get()=="" or self.var_con_newpass.get()=="":
            messagebox.showerror("Error","password is required",parent=self.forget_pass_win) 
        elif self.var_newpass.get()!=self.var_con_newpass.get():
            messagebox.showerror("Error","Password mismatch",parent=self.forget_pass_win) 
        else:
            con=sqlite3.connect(database=r'inventory_management_sys.db')
            cur=con.cursor()
            try:         
                cur.execute("Update employee SET pass=? where eid=?",(self.var_newpass.get(),self.employee_id.get()))
                con.commit()
                messagebox.showinfo("Succes","Password Updated succesfully",parent=self.forget_pass_win)
                self.forget_pass_win.destroy()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def validate_otp(self):
        
        if int(self.otp)==int(float(self.var_otp.get())):
            self.button_submit.configure(state=NORMAL)
            self.VERIFY.configure(state=DISABLED)
        else:
            messagebox.showerror("Error","Invalid Otp,Try again",parent=self.forget_pass_win)    
    def login(self):
        con=sqlite3.connect(database=r'inventory_management_sys.db')
        cur=con.cursor()
        try:
                if self.employee_id.get()=="" or self.password.get()=="":
                    messagebox.showerror("Error","employee_id and Password is required",parent=self.root)
                else:
                    cur.execute("select utype from employee where eid=? AND pass=? ",(self.employee_id.get(),self.password.get()))
                    user=cur.fetchone()
                    if user==None:
                        messagebox.showerror("Error","employee_id or Password is invalid",parent=self.root)
                    else:
                        if user[0]=="Admin":
                            self.root.destroy()
                            os.system("python dashboard.py")
                        else:
                            self.root.destroy()
                            os.system("python newbilling.py")

        except Exception as ex:
                messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    def send_email(self,to_):
        s=smtplib.SMTP('smtp.gmail.com',587)
        s.starttls()
        email_=email_pass.email_
        pass_=email_pass.pass_

        s.login(email_,pass_)

        self.otp=int(time.strftime("%H%M%S"))+int(time.strftime("%H"))
        print(self.otp)

        subject='Inventory Management System Restore Password'
        msg=f'Dear Sir/Madam,\n\n Your Reset OTP is {str(self.otp)}.\n\nWith Regards ,\nHRM Team'
        msg="Subject:{}\n\n{}".format(subject,msg)
        s.sendmail(email_,to_,msg)
        chk=s.ehlo()
        if chk[0]==250:
            return 's'
        else:
            return 'f'


# You can easily integrate authentication system 

if __name__=="__main__":
    
        root=customtkinter.CTk()
        obj=login_sys(root)
        root.mainloop()