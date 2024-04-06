


                                    #***** Student Managament System  ******#

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql as p

count=0
txt=" "

class student():

    # ================Variables=============
    def __init__(self,nan):
        self.roll_no = StringVar()
        self.nam = StringVar()
        self.bra = StringVar()
        self.mob = StringVar()
        self.par = StringVar()
        self.bat = StringVar()
        self.amo = StringVar()
        self.search_txt = StringVar()
        self.search_by = StringVar()

                                            #--------------Frame 1-----------------

        nan.title("Student Management s/m")
        nan.geometry("1000x600+0+0")
        nan.resizable(width=False, height=False)
        self.n = "Student Management System"
        self.bas = Label(nan, text=self.n, relief=GROOVE, fg="purple4"
                    , font=("century schoolbook", 18, "bold"), bd=7)
        self.bas.pack(side=TOP, fill=X)
        self.basu()


        per_obj = Label(nan, width=44, height=32, bd=5, relief=RIDGE)
        per_obj.place(x=40, y=70)

        data_obj = Frame(nan, width=600, height=492, bd=5, relief=RIDGE)
        data_obj.place(x=360, y=70)


                            # ------------------------Manage student----------------


        main_title = Label(per_obj, text="Manage Students", font=("Algerian", 17, "bold underline"), fg="purple4")
        main_title.place(x=60, y=20)

        reg_title = Label(per_obj, text="Reg.No", font=("century schoolbook", 12, "bold"), fg="purple4")
        reg_title.place(x=20, y=80)
        reg_entry = Entry(per_obj, fg="Black", width=20, font=("century schoolbook", 12, "bold"),
                          textvariable=self.roll_no)
        reg_entry.place(x=120, y=83)

        name_title = Label(per_obj, text="Name", font=("century schoolbook", 12, "bold"), fg="purple4")
        name_title.place(x=20, y=120)
        name_entry = Entry(per_obj, fg="Black", width=20, font=("century schoolbook", 12, "bold"),
                           textvariable=self.nam)
        name_entry.place(x=120, y=123)

        bra_title = Label(per_obj, text="Branch", font=("century schoolbook", 12, "bold"), fg="purple4")
        bra_title.place(x=20, y=160)
        bra_entry = Entry(per_obj, fg="Black", width=20, font=("century schoolbook", 12, "bold"), textvariable=self.bra)
        bra_entry.place(x=120, y=163)

        mob_title = Label(per_obj, text="Mobile", font=("century schoolbook", 12, "bold"), fg="purple4")
        mob_title.place(x=20, y=200)
        mob_entry = Entry(per_obj, fg="Black", width=20, font=("century schoolbook", 12, "bold"), textvariable=self.mob)
        mob_entry.place(x=120, y=203)

        par_title = Label(per_obj, text="Par Mob", font=("century schoolbook", 12, "bold"), fg="purple4")
        par_title.place(x=20, y=240)
        par_entry = Entry(per_obj, fg="Black", width=20, font=("century schoolbook", 12, "bold"), textvariable=self.par)
        par_entry.place(x=120, y=243)

        bat_title = Label(per_obj, text="Batch", font=("century schoolbook", 12, "bold"), fg="purple4")
        bat_title.place(x=20, y=280)
        bat_entry = Entry(per_obj, fg="Black", width=20, font=("century schoolbook", 12, "bold"), textvariable=self.bat)
        bat_entry.place(x=120, y=283)

        amo_title = Label(per_obj, text="Amount", font=("century schoolbook", 12, "bold"), fg="purple4")
        amo_title.place(x=20, y=320)
        amo_entry = Entry(per_obj, fg="Black", width=20, font=("century schoolbook", 12, "bold"), textvariable=self.amo)
        amo_entry.place(x=120, y=323)


                                    # ------------------------Buttons----------------


        # ---add button----

        add_button = Button(per_obj, text="Add", bd=0, cursor="hand2",
                            fg="purple4", font=("century schoolbook", 12, "bold"), activeforeground="purple4",
                            command=self.add_data)
        add_button.place(x=10, y=410)

        # ------update button------

        update_button = Button(per_obj, text="Update", bd=0, cursor="hand2",
                               fg="purple4", font=("century schoolbook", 12, "bold"), activeforeground="purple4",
                               command=self.update_data)
        update_button.place(x=65, y=410)

        # ---delete button-----

        del_button = Button(per_obj, text="Delete", bd=0, cursor="hand2",
                            fg="purple4", font=("century schoolbook", 12, "bold"), activeforeground="purple4",
                            command=self.delete_data)
        del_button.place(x=145, y=410)

        # ------cancel button------

        can_button = Button(per_obj, text="Cancel", bd=0, cursor="hand2",
                            fg="purple4", font=("century schoolbook", 12, "bold"), activeforeground="purple4",
                            command=self.cancle_data)
        can_button.place(x=225, y=410)

                                    # ------------------------Frame 2 ----------------

        ser_data = Label(data_obj, text="Search By", fg="purple4", font=("century schoolbook", 12, "bold"))
        ser_data.place(x=20, y=20)

        ser_data = ttk.Combobox(data_obj, font=("century schoolbook", 12, "bold"), state="readonly", width=8,
                                textvariable=self.search_by)
        ser_data["values"] = ("Roll_no", "Name", "Batch", "Branch", "Amount")
        ser_data.place(x=120, y=20)

        ser_entry=Entry(data_obj, bd=2,fg="Black", width=15, font=("century schoolbook", 12, "bold"), textvariable=self.search_txt)
        ser_entry.place(x=215,y=20)

        # -------Search Buttons-----------

        serch_button = Button(data_obj, text="Search", cursor="hand2",
                              fg="purple4", font=("century schoolbook", 12, "bold"), activeforeground="purple4",
                              bg="white", activebackground="white",command=self.search_data)
        serch_button.place(x=370, y=15)

        show_button = Button(data_obj, text="Show All", cursor="hand2",
                             fg="purple4", font=("century schoolbook", 12, "bold"), activeforeground="purple4",
                             bg="white", activebackground="white",command=self.fetch_data)
        show_button.place(x=470, y=15)

        cr_label = Label(data_obj, width=84, height=27)
        cr_label.place(x=0, y=55)

                                                #--------TreeView--------

        cr_frame = Frame(cr_label)
        cr_frame.place(x=10,y=10,width=580,height=400)
        y_scroll = Scrollbar(cr_frame, orient='vertical')
        x_scroll = Scrollbar(cr_frame, orient='horizontal')

        self.student_details = ttk.Treeview(cr_frame,
                                       columns=("sno","reg", "name", "branch", "mobile", "parmobile", "batch", "amount"),
                                       xscrollcommand=x_scroll.set, yscrollcommand=y_scroll.set, height=19)

        y_scroll.pack(side=RIGHT, fill=Y)
        x_scroll.pack(side=BOTTOM, fill=X)
        x_scroll.config(command=self.student_details.xview)
        y_scroll.config(command=self.student_details.yview)

        self.student_details.heading("sno",text="S.No")
        self.student_details.heading("reg", text="Reg")
        self.student_details.heading("name", text="Name")
        self.student_details.heading("branch", text="Branch")
        self.student_details.heading("mobile", text="Mobile")
        self.student_details.heading("parmobile", text="Parents Mobile")
        self.student_details.heading("batch", text="Batch")
        self.student_details.heading("amount", text="Amount")

        self.student_details['show'] = "headings"

        self.student_details.column("sno", width=30, anchor=CENTER)
        self.student_details.column("reg", width=70,anchor=CENTER)
        self.student_details.column("name", width=130,anchor=CENTER)
        self.student_details.column("branch", width=90,anchor=CENTER)
        self.student_details.column("mobile", width=130,anchor=CENTER)
        self.student_details.column("parmobile", width=150,anchor=CENTER)
        self.student_details.column("batch", width=90,anchor=CENTER)
        self.student_details.column("amount", width=90,anchor=CENTER)
        self.style = ttk.Style()
        self.style.configure('Treeview', rowheight=30, font=("century schoolbook", 12))
        self.style.configure("Treeview.Heading", font=("century schoolbook", 13, "bold"), foreground='brown4')
        self.student_details.pack(fill=BOTH, expand=True)

        self.student_details.bind("<ButtonRelease-1>", self.get_data)
        self.add_data()
        self.fetch_data()


    def basu(self):
        global count,txt
        if count==len(self.n):
            count=0
            txt=' '
        txt=txt+self.n[count]
        self.bas.config(text=txt)
        count+=1
        self.bas.after(500,self.basu)

    def clear(self):
        self.roll_no.set("")
        self.nam.set("")
        self.bra.set("")
        self.mob.set("")
        self.par.set("")
        self.bat.set("")
        self.amo.set("")

    def add_data(self):
        if (self.roll_no.get()=="" or self.nam.get()=="" or self.bra.get()=="" or
                self.mob.get()=="" or self.par.get()=="" or self.bat.get()=="" or self.amo.get()==""):
            messagebox.showerror("Error","All Fields are Required")
        else:
            try:
                nan=p.connect(host="127.0.0.1",user="root",passwd="taher",database="data")
                bas=nan.cursor()
            except:
                messagebox.showerror("Error","Database doesn't exist")
                return

            try:
                query = 'create table if not exists students(S_No int primary key autoincrement, Reg varchar(50),Name varchar(50),' \
                        'Branch varchar(20),Mobile varchar(20),Parent_mobile varchar(20),Batch varchar(20)' \
                        'Amount varchar(20))'
                bas.execute(query)
            except:
                query = "use data"
                bas.execute(query)

            mam='insert into students(reg,name,branch,mobile,parmobile,batch,amount) values(%s,%s,%s,%s,%s,%s,%s)'
            bas.execute(mam,(self.roll_no.get(),self.nam.get(),self.bra.get(),
                               self.mob.get(),self.par.get(),self.bat.get(),
                               self.amo.get()))
            nan.commit()
            self.fetch_data()
            self.clear()
            nan.close()
            messagebox.showinfo("Success","Data Successfully Added")



    def update_data(self):
        try:
            mom=p.connect(host="127.0.0.1", user="root", passwd="taher", database="data")
            basu = mom.cursor()

        except:
            messagebox.showerror("Error", "the database doesn't exist")
            return

        query = "select * from students where reg=%s or mobile=%s or name=%s"
        basu.execute(query, (self.roll_no.get(),self.mob.get(),self.nam.get()))
        abi = basu.fetchone()
        if abi == None:
            messagebox.showerror("Error","Data doesn't exist")
        else:
            jef= "update students set reg=%s,name=%s,branch=%s,mobile=%s,parmobile=%s,batch=%s,amount=%s where reg=%s"
            basu.execute(jef, (self.roll_no.get(),self.nam.get(),self.bra.get(),
                               self.mob.get(),self.par.get(),self.bat.get(),
                               self.amo.get(),self.roll_no.get()))
            mom.commit()
            mom.close()
            messagebox.showinfo("Success", "Successfully updated")

    def get_data(self,event):
        cursor_row=self.student_details.focus()
        content=self.student_details.item(cursor_row)
        row=content['values']

        if row:
            self.roll_no.set(row[0])
            self.nam.set(row[1])
            self.bra.set(row[2])
            self.mob.set(row[3])
            self.par.set(row[4])
            self.bat.set(row[5])
            self.amo.set(row[6])

    def delete_data(self):
        try:
            sip=p.connect(host="127.0.0.1", user="root", passwd="taher", database="data")
            base = sip.cursor()

        except:
            messagebox.showerror("Error", "the database doesn't exist")
            return
        bam="delete * from students where reg=%s or name=%s or mobile=%s or parmobile=%s"
        base.execute(bam,(self.roll_no.get(),self.nam.get(),self.mob.get(),self.par.get()))
        sip.commit()
        sip.close()
        messagebox.showinfo("Success", "Successfully Deleted")

    def cancle_data(self):
        try:
            sip=p.connect(host="127.0.0.1", user="root", passwd="taher", database="data")
            base = sip.cursor()

        except:
            messagebox.showerror("Error", "the database doesn't exist")
            return
        base.execute("delete * from students")
        sip.commit()
        sip.close()
        messagebox.showinfo("Success", "Sucessfully cleared data")

    def fetch_data(self):
        try:
            sip=p.connect(host="127.0.0.1", user="root", passwd="taher", database="data")
            base = sip.cursor()
            base.execute("select * from students")
            rows = base.fetchall()
            if len(rows) != 0:
                self.student_details.delete(*self.student_details.get_children())
                for row in rows:
                    self.student_details.insert("", END, values=row)
                sip.commit()
            else:
                messagebox.showerror("Error", "the database doesn't exist")
        except Exception as e:
            print("Error fetching data:", e)
        finally:
            sip.close()

    def search_data(self):
        con = p.connect(host='127.0.0.1', user='root', passwd='taher', database='data')
        cur = con.cursor()
        query = "SELECT * FROM students WHERE {} LIKE %s".format(self.search_by.get())
        value = '%' + self.search_txt.get() + '%'
        cur.execute(query, (value,))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_details.delete(*self.student_details.get_children())
            for row in rows:
                self.student_details.insert("", END, values=row)
            con.commit()
        else:
            messagebox.showerror("Error", "Record doesn't find")
        con.close()

nan=Tk()
ob=student(nan)
nan.mainloop()

