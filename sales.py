from tkinter import*
from PIL import Image,ImageTk 
from tkinter import ttk,messagebox
import sqlite3
import os
class salesclass:
    def __init__(self,root):
    
        self.root=root
        self.root.geometry("1600x740+300+220")
        self.root.title("Inventory Management System  |  Developed by HUZAIFA   ")
        self.root.config(bg="#282424")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()
        ###title###
        lbl_title=Label(self.root,text="View Customer Bill",font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        lbl_title=Label(self.root,text="Invoice No",font=("times new roman",15),bg="white").place(x=50,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="light yellow").place(x=160,y=100,width=180,height=28)

        btn_search=Button(self.root,text="Search",command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=360,y=100,width=120,height=28)
        btn_clear=Button(self.root,text="Clear",command=self.clear,font=("times new roman",15,"bold"),bg="#2196f3",cursor="hand2").place(x=490,y=100,width=120,height=28)
        ###bill list##
        sales_Frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_Frame.place(x=50,y=140,width=200,height=330)

        Scrolly=Scrollbar(sales_Frame,orient=VERTICAL)
        self.Sales_list=Listbox(sales_Frame,font=("goudy old style",15),bg="white",yscrollcommand=Scrolly.set)
        Scrolly.pack(side=RIGHT,fill=Y)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.bind

        ##bill area###
        bill_Frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_Frame.place(x=280,y=140,width=600,height=530)

        lbl_title2=Label(bill_Frame,text="Customer Bill Area",font=("goudy old style",30),bg="orange",fg="white").pack(side=TOP,fill=X)
        
        Scrolly2=Scrollbar(bill_Frame,orient=VERTICAL)
        self.bill_area=Text(bill_Frame,font=("goudy old style",15),bg="lightyellow",yscrollcommand=Scrolly.set)
        Scrolly2.pack(side=RIGHT,fill=Y)
        Scrolly2.config(command=self.Sales_list.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)

        ###image###
        self.bill_photo=Image.open("images/sales.png")
        self.bill_photo=self.bill_photo.resize((600,530),Image.ANTIALIAS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=900,y=140)

        self.show()
#==============================================================================#
    def show(self):
        del self.bill_list[:]
        self.Sales_list.delete(0,END)
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
    
    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_)
        print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()
    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                print("Yes find the invoice")
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No",parent=self.root)


    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)



if  __name__ =="__main__":
    root=Tk()
    obj=salesclass(root)
    root.mainloop()