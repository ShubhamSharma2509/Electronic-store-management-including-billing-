from tkinter import*
from PIL import Image,ImageTk
from employee import employeeClass
from supplier import supplierClass
from category import categoryClass
from product import productClass
from sales import salesClass
import sqlite3
from tkinter import messagebox
import os
import time

class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1537x830+-8+-2")
        self.root.title("Electronic Store Management")
        self.root.config(bg="white")

        #===Title===
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Electronic Store Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #===button_logout===
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("times new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1350,y=10,height=50,width=150)

        #===clock===
        self.lbl_clock=Label(self.root,text="Welcome to Electronic Store Management System\t\t Date: 12/12/12 \t\t Time:HH:MM:SS",font=("times new roman",15),bg="#4d636d",fg="white",padx=20)
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)

        #===List menu===
        self.menulogo=Image.open("images/menu_im.png")
        self.menulogo=self.menulogo.resize((200,200),Image.ANTIALIAS)
        self.menulogo=ImageTk.PhotoImage(self.menulogo)

        leftmenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        leftmenu.place(x=0,y=102,width=200, height=565)

        lbl_menulogo=Label(leftmenu,image=self.menulogo)
        lbl_menulogo.pack(side=TOP,fill=X)

        self.icon_side=PhotoImage(file="images/side.png")
        lbl_menu=Label(leftmenu,text="Menu",font=("times new roman",20,),bg="#003688").pack(side=TOP,fill=X)
        
        btn_employee=Button(leftmenu,text="Employee",command=self.employee ,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)

        btn_supplier=Button(leftmenu,text="Supplire", command=self.supplier ,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)

        btn_category=Button(leftmenu,text="Category", command=self.category,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)

        btn_product=Button(leftmenu,text="Product", command=self.product ,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)

        btn_sales=Button(leftmenu,text="Sales", command=self.sales ,image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)

        btn_exit=Button(leftmenu,text="Exit",image=self.icon_side,compound=LEFT,padx=5,anchor="w",font=("times new roman",20,),bg="white",bd=3, cursor="hand2").pack(side=TOP,fill=X)

        #===Content===

        self.lbl_employee=Label(self.root,text="total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white" ,font=("goudy old style",20,"bold"))
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_suplier=Label(self.root,text="total Suplier\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_suplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category=Label(self.root,text="total Category\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product=Label(self.root,text="total Product\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales=Label(self.root,text="total Sales\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("goudy old style",20,"bold"))
        self.lbl_sales.place(x=650,y=300,height=150,width=300)

        #===Footer===
        lbl_footer=Label(self.root,text="IMS - Electronic Store Management System",font=("times new roman",12),bg="#4d636d",fg="white",padx=20).pack(side=BOTTOM,fill=X)

        self.update_content()

    #=========================================================================================================================================

    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_win)
    
    def supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_win)
    
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            cur.execute("select* from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f"Total Products\n[{str(len(product))}]")

            cur.execute("select* from supplier")
            supplier=cur.fetchall()
            self.lbl_suplier.config(text=f"Total Suppliers\n[{str(len(supplier))}]")

            cur.execute("select* from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f"Total Category\n[{str(len(category))}]")

            cur.execute("select* from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f"Total Employee\n[{str(len(employee))}]")

            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n[{str(bill)}]')


            time_=time.strftime("%I:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Electronic Store Management System\t\t Date: {str(date_)} \t\t Time:{str(time_)}")
            self.lbl_clock.after(200,self.update_content) 

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)
    
    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__=="__main__":
    root=Tk()
    OBJ=IMS(root)
    root.mainloop()
