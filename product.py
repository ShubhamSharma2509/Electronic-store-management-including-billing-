from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk,messagebox
import sqlite3
class productClass:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1537x830+-8+-2")
        self.root.title("Electronic Store Management")
        self.root.config(bg="white")
        self.root.focus_force()
        #===============================================================
        
        self.var_searchby=StringVar()
        self.var_searchtxt=StringVar()

        self.var_pid=StringVar()
        self.var_cat=StringVar()

        self.var_cat=StringVar()
        self.var_sup=StringVar()
        self.cat_list=[]
        self.sup_list=[]
        self.fetch_cat_sup()
        self.var_name=StringVar()
        self.var_price=StringVar()
        self.var_qty=StringVar()
        self.var_status=StringVar()

        product_Frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        product_Frame.place(x=10,y=170,width=600,height=550)

        
        #===Title===
        self.icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Electronic Store Management System",image=self.icon_title,compound=LEFT,font=("times new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        

        #======title=================
        title=Label(product_Frame,text="Manage Products Detail",font=("goudy old style",18),bg="#0f4d7d" ,fg="white").pack(side=TOP,fill=X)

        #======colum1==============

        lbl_category=Label(product_Frame,text="Category",font=("goudy old style",18),bg="white").place(x=120,y= 60)
        lbl_supplier=Label(product_Frame,text="Supplier",font=("goudy old style",18),bg="white").place(x=120,y= 110)
        lbl_product=Label(product_Frame,text="Name",font=("goudy old style",18),bg="white").place(x=120,y= 160)
        lbl_price=Label(product_Frame,text="Price",font=("goudy old style",18),bg="white").place(x=120,y= 210)
        lbl_quantity=Label(product_Frame,text="Quantity",font=("goudy old style",18),bg="white").place(x=120,y=260)
        lbl_status=Label(product_Frame,text="Status",font=("goudy old style",18),bg="white").place(x=120,y= 310)
       
        #======colum2==============
       
        cmb_cat=ttk.Combobox(product_Frame,textvariable=self.var_cat,values=self.cat_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_cat.place(x=260,y=60,width=200) 
        cmb_cat.current(0)

        cmb_sup=ttk.Combobox(product_Frame,textvariable=self.var_sup,values=self.sup_list,state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_sup.place(x=260,y=110,width=200) 
        cmb_sup.current(0)

        txt_name=Entry(product_Frame,textvariable=self.var_name,font=("goudy old style",15),bg="lightyellow").place(x=260,y= 160,width=200) 
        txt_price=Entry(product_Frame,textvariable=self.var_price,font=("goudy old style",15),bg="lightyellow").place(x=260,y= 210,width=200) 
        txt_qty=Entry(product_Frame,textvariable=self.var_qty,font=("goudy old style",15),bg="lightyellow").place(x=260,y= 260,width=200) 

        cmb_status=ttk.Combobox(product_Frame,textvariable=self.var_status,values=("Active","Inactive"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_status.place(x=260,y=310,width=200) 
        cmb_status.current(0)

        #=========buttons================

        btn_add=Button(product_Frame, text="Save", command=self.add ,font=("goudy old style",15),bg="#2196f3" ,fg="white", cursor="hand2").place(x=40,y=370,width=250,height=40)
        btn_update=Button(product_Frame, text="Update", command=self.update ,font=("goudy old style",15),bg="#4caf50" ,fg="white", cursor="hand2").place(x=300,y=370,width=250,height=40)
        btn_delete=Button(product_Frame, text="Delete", command=self.delete ,font=("goudy old style",15),bg="#f44336" ,fg="white", cursor="hand2").place(x=40,y=415,width=250,height=40)
        btn_clear=Button(product_Frame, text="Clear", command=self.clear ,font=("goudy old style",15),bg="#607d8b",fg="white", cursor="hand2").place(x=300,y=415,width=250,height=40)
        
         #======searchframe===========
        searchframe=LabelFrame(self.root,text="Search Products",font=("goudy old style", 12, "bold"), bd=2, relief=RIDGE ,bg="white")
        searchframe.place(x=10,y=75,width=1510,height=77)

        #======option================

        cmb_search=ttk.Combobox(searchframe,textvariable=self.var_searchby,values=("Select","Category","Supplier","Name"),state='readonly',justify=CENTER,font=("goudy old style",15))
        cmb_search.place(x=450,y=10,width=180) 
        cmb_search.current(0)

        txt_search=Entry(searchframe,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=650,y=9)

        btn_search=Button(searchframe, text="Search", command=self.search ,font=("goudy old style",15),bg="#4caf50" ,fg="white", cursor="hand2").place(x=870,y=9,width=150,height=30)


        #=========Product details================

        p_frame=Frame(self.root,bd=3,relief=RIDGE)
        p_frame.place(x=609,y=170,width=920,height=550)

        scrolly=Scrollbar(p_frame,orient=VERTICAL)
        scrollx=Scrollbar(p_frame,orient=HORIZONTAL)

        self.product_Table=ttk.Treeview(p_frame,columns=("pid","Supplier","Category","name","price","qty","status"),yscrollcommand=scrolly.set,xscrollcommand=scrollx.set)
        
        scrollx.pack(side=BOTTOM,fill=X)
        scrolly.pack(side=RIGHT,fill=Y)
        scrollx.config(command=self.product_Table.xview)
        scrolly.config(command=self.product_Table.yview)

        self.product_Table.heading("pid",text="P-ID")
        self.product_Table.heading("Category",text="Category")
        self.product_Table.heading("Supplier",text="Supplier")
        self.product_Table.heading("name",text="Name")
        self.product_Table.heading("price",text="Price")
        self.product_Table.heading("qty",text="Quantity")
        self.product_Table.heading("status",text="Status")

        self.product_Table["show"]="headings"

        self.product_Table.column("pid",width=90)
        self.product_Table.column("Category",width=100)
        self.product_Table.column("Supplier",width=100)
        self.product_Table.column("name",width=100)
        self.product_Table.column("price",width=100)
        self.product_Table.column("qty",width=100)
        self.product_Table.column("status",width=100)
        self.product_Table.pack(fill=BOTH,expand=1)
        self.product_Table.bind("<ButtonRelease-1>",self.get_data)

        self.show()

#================================Footer================================

        footer=Label(self.root,text="ESM",font=("times new roman",15),bg="#4d636d",fg="white",bd=0,cursor="hand2").pack(side=BOTTOM,fill=X)

#=======================================================================
    def fetch_cat_sup(self): 
        self.cat_list.append("Empty")
        self.sup_list.append("Empty")
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:   
            cur.execute("Select name  from category")
            cat=cur.fetchall()
            if len(cat)>0:
                del self.cat_list[:]
                self.cat_list.append("Select")
                for i in cat:
                    self.cat_list.append(i[0])

            cur.execute("Select name from Supplier")
            sup=cur.fetchall() 
            if len(sup)>0:
                del self.sup_list[:]
                self.sup_list.append("Select")
                for i in sup:
                    self.sup_list.append(i[0])
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

    def add(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:        
            if self.var_cat.get()=="Select" or self.var_cat.get()=="Empty" or self.var_sup.get()=="Select" or self.var_name.get()=="" :
                messagebox.showerror("Error","All Fields are required", parent=self.root)
            else: 
                cur.execute("Select * from product where name=? ",(self.var_name.get(),))
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","Product is already Present, Try different id",parent=self.root)
                    
                else:
                    cur.execute("Insert into product (Category,Supplier,name,price,qty,status) values(?,?,?,?,?,?)",(
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                    ))
                    con.commit()
                    messagebox.showwarning("Sucess","Product Added Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

#========================================================================

    def show(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            row=cur.fetchall()
            self.product_Table.delete(*self.product_Table.get_children())
            for row in row:
                self.product_Table.insert('',END,values=row)
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root )


    def get_data(self,ev):
        f=self.product_Table.focus()
        content=(self.product_Table.item(f))
        row=content['values']
        
        self.var_pid.set(row[0])
        self.var_sup.set(row[1])
        self.var_cat.set(row[2])
        self.var_name.set(row[3])
        self.var_price.set(row[4])
        self.var_qty.set(row[5])
        self.var_status.set(row[6])

    def update(self):
        con=sqlite3.connect(database='ims.db')
        cur=con.cursor()
        try:        
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Please Select product from list", parent=self.root)
            else: 
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()
                if row==None:
                    messagebox.showerror("Error","Invalid product",parent=self.root)
                    
                else:
                    cur.execute("Update product set category=?,Supplier=?,name=?,price=?,qty=?,status=? where pid=?",(
                                        
                                        self.var_cat.get(),
                                        self.var_sup.get(),
                                        self.var_name.get(),
                                        self.var_price.get(),
                                        self.var_qty.get(),
                                        self.var_status.get(),
                                        self.var_pid.get()
                    ))
                    con.commit()
                    messagebox.showwarning("Sucess","product Updated Sucessfully",parent=self.root)
                    self.show()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)


    def delete(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try: 
            if self.var_pid.get()=="":
                messagebox.showerror("Error","Select product from the list", parent=self.root)
            else: 
                cur.execute("Select * from product where pid=?",(self.var_pid.get(),))
                row=cur.fetchone()

                if row==None:
                    messagebox.showerror("Error","INVALID PRODUCT ID",parent=self.root)
                    
                else:
                    op=messagebox.askyesno("Confirm","Do you really want to delete?",parent=self.root)
                    if op==True:
                        cur.execute("delete from product where pid=?",(self.var_pid.get(),))
                        con.commit()
                        messagebox.showinfo("Delete","product Deleted Sucessfully",parent=self.root)
                        self.clear()
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to : {str(ex)}",parent=self.root)

        
    def clear(self):
        
        self.var_cat.set("Select"),
        self.var_sup.set("Select"),
        self.var_name.set(""),
        self.var_price.set(""),
        self.var_qty.set(""),
        self.var_status.set("Active"),
        self.var_pid.set("")
        self.var_searchtxt.set("")
        self.var_searchby.set("Select")
        self.show()

    
    def search(self):
        con=sqlite3.connect(database=r'ims.db')
        cur=con.cursor()
        try:
            if self.var_searchby.get()=="Select":
                messagebox.showerror("Error","Select Search By option",parent=self.root)
            elif self.var_searchtxt.get()=="":
                messagebox.showerror("Error","Search input should shoult be required ",parent=self.root)

            else:
                cur.execute("select * from product where "+self.var_searchby.get()+" LIKE '%"+self.var_searchtxt.get()+"%'")
                rows=cur.fetchall()
                if len(rows)!=0:
                    self.product_Table.delete(*self.product_Table.get_children())
                    for row in rows:
                       self.product_Table.insert('',END,values=row)
                else:
                        messagebox.showerror("Error","No record found",parent=self.root)  
        except Exception as ex:
            messagebox.showerror("Error",f"Error due to :{str(ex)}",parent=self.root )


if __name__=="__main__":
    root=Tk()
    OBJ=productClass(root)
    root.mainloop()