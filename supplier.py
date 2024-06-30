from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class supplierClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1537x830+-8+-2")
        self.root.title("Electronic Store Management")
        self.root.config(bg="white")
        self.root.focus_force()
        #=================================================================
        #All verialbles=======
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_sup_invoice=StringVar()
        self.var_name=StringVar()
        self.var_contact=StringVar()
        
        #===Title===
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Electronic Store Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)

        #======searchframe===========
        searchframe=LabelFrame(self.root,text="Search Invoice",font=("goudy old style", 15, "bold"), bd=2, relief=RIDGE ,bg="white")
        searchframe.place(x=40,y=75,width=1450,height=77)

        #======option================

        lbl_search=Label(searchframe,text="Search by Invoice no",font=("goudy old style",15),bg="white")
        lbl_search.place(x=445,y=10,width=180) 
        

        txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=645,y=10)

        btn_search=Button(searchframe, text="Search", command=self.search ,font=("goudy old style",15),bg="#4caf50" ,fg="white", cursor="hand2").place(x=875,y=9,width=150,height=30)

        #======title=================
        title=Label(self.root,text="Supplier Detail",font=("goudy old style",15),bg="#0f4d7d" ,fg="white").place(x=50,y=170,width=1000)

        #========Content==============

        #=========row1================

        lbl_supplier_invoice=Label(self.root,text="Invoice Number",font=("goudy old style",15),bg="white" ,).place(x=50,y=210)
        txt_supplier_invoice=Entry(self.root,textvariable=self.var_sup_invoice,font=("goudy old style",15),bg="lightyellow").place(x=210,y=210,width=180)

       #=========row2================

        lbl_name=Label(self.root,text="Name",font=("goudy old style",15),bg="white" ,).place(x=50,y=260)
        
        txt_name=Entry(self.root,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=210,y=260,width=180)
        
        #=========row3================

        lbl_contact=Label(self.root,text="contact",font=("goudy old style",15),bg="white" ,).place(x=50,y=310)
        
        txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="lightyellow").place(x=210,y=310,width=180)
        
        #=========row4================

        lbl_desc=Label(self.root,text="Description",font=("goudy old style",15),bg="white" ,).place(x=50,y=360)
        
        self.txt_desc=Text(self.root,font=("goudy old style",15),bg="lightyellow")
        self.txt_desc.place(x=210,y=360,height=60 ,width=300)
        #=========buttons================

        btn_add=Button(self.root, text="Save", command=self.add ,font=("goudy old style",15),bg="#2196f3" ,fg="white", cursor="hand2").place(x=530,y=385,width=180,height=35)
        btn_update=Button(self.root, text="Update", command=self.update ,font=("goudy old style",15),bg="#4caf50" ,fg="white", cursor="hand2").place(x=740,y=385,width=180,height=35)
        btn_delete=Button(self.root, text="Delete", command=self.delete ,font=("goudy old style",15),bg="#f44336" ,fg="white", cursor="hand2").place(x=950,y=385,width=180,height=35)
        btn_clear=Button(self.root, text="Clear", command=self.clear ,font=("goudy old style",15),bg="#607d8b",fg="white", cursor="hand2").place(x=1160,y=385,width=180,height=35)

        #=========Employee details================

        emp_frame=Frame(self.root,bd=3,relief=RIDGE)
        emp_frame.place(x=0,y=450,relwidth=1,height=300)

        scrolly=Scrollbar(emp_frame,orient=VERTICAL)
        scrollx=Scrollbar(emp_frame,orient=HORIZONTAL)

        self.supplierTable=ttk.Treeview(emp_frame,columns=("invoice","name","Contact","desc"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.supplierTable.xview)
        scrolly.config(command=self.supplierTable.yview)

        self.supplierTable.heading("invoice",text="Invoice")
        self.supplierTable.heading("name",text="Name")
        self.supplierTable.heading("Contact",text="Contact")
        self.supplierTable.heading("desc",text="Description")
       
        self.supplierTable["show"]="headings"

        self.supplierTable.column("invoice",width=90)
        self.supplierTable.column("name",width=100)
        self.supplierTable.column("Contact",width=100)
        self.supplierTable.column("desc",width=100)
        
        self.supplierTable.pack(fill=BOTH,expand=1)
        self.supplierTable.bind("<ButtonRelease-1>",self.get_data)

        self.show()

        
#================================Footer================================

        footer=Label(self.root,text="ESM",font=("times new roman",15),bg="#4d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)

#==========================================================================

    def add(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:        
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice must be required", parent=self.root)
            else: 
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Invoice no. is already assigned, Try different id",parent=self.root)
                    
                else:
                    cur.execute("Insert into supplier (invoice,name,contact,desc) values(?,?,?,?)",(
                                        self.var_sup_invoice.get(),
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                    ))
                    con.commit()
                    messagebox.showwarning("Sucess","supplier Added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from supplier")
            row=cur.fetchall()
            self.supplierTable.delete(*self.supplierTable.get_children())
            for row in row:
                self.supplierTable.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root )


    def get_data(self,ev):
        f=self.supplierTable.focus()
        content=(self.supplierTable.item(f))
        row=content['values']
        #print(row)
        self.var_sup_invoice.set(row[0])
        self.var_name.set(row[1])
        self.var_contact.set(row[2])
        self.txt_desc.delete('1.0',END)
        self.txt_desc.insert(END,row[3])


    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:        
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","Invoice no. Must be required", parent=self.root)
            else: 
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","INVALID invoice no",parent=self.root)
                    
                else:
                    cur.execute("Update supplier set name=?,contact=?,desc=?  where invoice=?",(
                                        
                                        self.var_name.get(),
                                        self.var_contact.get(),
                                        self.txt_desc.get('1.0',END),
                                        self.var_sup_invoice.get(),
                    ))
                    con.commit()
                    messagebox.showwarning("Sucess","Supplier Updateed Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try: 
            if self.var_sup_invoice.get()=="":
                messagebox.showerror("Error","invoice no Must be required", parent=self.root)
            else: 
                cur.execute("Select * from supplier where invoice=?",(self.var_sup_invoice.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error","INVALID invoice no",parent=self.root)
                    
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from supplier where invoice=?",(self.var_sup_invoice.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","supplier Deleted Sucessfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        
    def clear(self):
        self.var_sup_invoice.set("")
        self.var_name.set("")
        self.var_contact.set("")
        self.txt_desc.delete('1.0',END)
        self.var_searchtxt.set("")
        self.show()

    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Invoice no should shoult be required ",parent=self.root)
            else:
                cur.execute("Select * from supplier where invoice=?",(+self.var_searchtxt.get(),))
                row=cur.fetchone()
                if row!=None:
                    self.supplierTable.delete(*self.supplierTable.get_children())
                    self.supplierTable.insert('',END,values=row)
                else:
                        messagebox.showerror("Error","No record found",parent=self.root)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root )

if __name__=="__main__":
    root=Tk()
    OBJ=supplierClass(root)
    root.mainloop()
 