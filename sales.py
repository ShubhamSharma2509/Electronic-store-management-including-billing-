from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
import os
class salesClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1537x830+-8+-2")
        self.root.title("Electronic Store Management")
        self.root.config(bg="white")
        self.root.focus_force()

        self.bill_list=[]
        self.var_invoice=StringVar()

        #=======title========

        lbl_title=Label(self.root,text="View Customer bills", font=("goudy old style",30),bg="#184a45",fg="white",bd=3,relief=RIDGE).pack(side=TOP,fill=X,padx=10,pady=20)
        
        lbl_invoice=Label(self.root,text="Invoice No.",font=("times new roman",18),bg="white").place(x=40,y=100)
        txt_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="lightyellow").place(x=160,y=100,width=220,height=33)

        btn_search=Button(self.root,text="Search", command=self.search,font=("times new roman",15,"bold"),bg="#2196f3",fg="white",cursor="hand2").place(x=400,y=100,width=220,height=33)

        btn_clear=Button(self.root,text="Clear", command=self.clear ,font=("times new roman",15,"bold"),bg="lightgray",cursor="hand2").place(x=630,y=100,width=220,height=33)

        
        #======bill list=====

        sales_frame=Frame(self.root,bd=3,relief=RIDGE)
        sales_frame.place(x=40,y=160,width=312,height=600)

        Scrolly=Scrollbar(sales_frame,orient=VERTICAL)
        self.Sales_list=Listbox(sales_frame,font=("goudy old style",15),bg="white",yscrollcommand=Scrolly.set)
        Scrolly.pack(side=RIGHT,fill=Y)
        Scrolly.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)

        #======bill area=====

        bill_frame=Frame(self.root,bd=3,relief=RIDGE)
        bill_frame.place(x=375,y=160,width=625,height=600)

        lbl_title2=Label(bill_frame,text="Customer bill Area", font=("goudy old style",20),bg="orange").pack(side=TOP,fill=X)
        

        Scrolly2=Scrollbar(bill_frame,orient=VERTICAL)
        self.bill_area=Text(bill_frame,bg="lightyellow",yscrollcommand=Scrolly2.set)
        Scrolly2.pack(side=RIGHT,fill=Y)
        Scrolly2.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)

        #=======images=======

        self.bill_photo=Image.open("images/cat2.jpg")
        self.bill_photo=self.bill_photo.resize((550,400),Image.ANTIALIAS)
        self.bill_photo=ImageTk.PhotoImage(self.bill_photo)

        lbl_image=Label(self.root,image=self.bill_photo,bd=0)
        lbl_image.place(x=1000,y=200)

        self.show()


#================================Footer================================

        footer=Label(self.root,text="ESM",font=("times new roman",15),bg="#4d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)

#=========================================================================
    
    def show(self):
        del self.bill_list[:]
        self.Sales_list.delete(0,END)
        #print(os.listdir('bill'))
        for i in os.listdir('bill'):
            if i.split('.')[-1]=='txt':
                self.Sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])

    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_)
        #print(file_name)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice no. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                    self.bill_area.insert(END,i)
                fp.close()
            else:
                messagebox.showerror("Error","Invalid Invoice No.",parent=self.root)

    def clear(self):
        self.show()
        self.bill_area.delete('1.0',END)


if __name__=="__main__":
    root=Tk()
    OBJ=salesClass(root)
    root.mainloop()