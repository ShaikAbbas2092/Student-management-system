
                                        #=====Student Managament System=====#

from tkinter import *
from tkinter import ttk
from tkinter import messagebox as m
import pymysql as p
count=0
txt=" "

class student:

    def slider(self):
        global txt,count
        if count==len(self.s):
            count=0
            txt=' '
        txt=txt+self.s[count]
        self.label.config(text=txt)
        count+=1
        self.label.after(500,self.slider)


    def __init__(self,root):
        root.geometry("1200x810+190+10")
        root.title("Student Management System")
        root.resizable(0,0)
        self.s="Student Management System"
        self.label=Label(root,text=self.s,relief=GROOVE,
                    width=45,bg='magenta3',fg='gray13',font=("Algerian", 30,'bold'),bd=12)
        self.label.place(x=0,y=0)
        self.slider()
        # ================================Variables=========================================
        self.sl_var = StringVar()
        self.name_var = StringVar()
        self.branch_var = StringVar()
        self.batch_var = StringVar()
        self.date_var = StringVar()
        self.mob_var = StringVar()
        self.pmob_var = StringVar()

        self.amount_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

                                        #-------frame_1--------

        frame1=Frame(root,bg='white')
        frame1.place(x=1,y=72)
        head1=LabelFrame(frame1,width=450,height=740,text="Manage Students",font=("century schoolbook",20,'bold'),
                        fg='purple4',bd=10,bg='plum2')
        head1.grid(row=0,column=0)
    #reg_no
        reg=Label(frame1,text="Reg.No",font=("century schoolbook",15,'bold'),fg='black',bg='plum2',bd=0)
        reg.place(x=15,y=60)
        regentry=Entry(bd=1,fg='black',textvariable=self.sl_var,font=("century schoolbook",15),bg='white')
        regentry.place(x=180,y=135)
    #name
        name=Label(frame1,text="Name",font=("century schoolbook",15,'bold'),fg='black',bg='plum2',bd=0)
        name.place(x=15,y=115)
        namentry=Entry(bd=1,fg='black',textvariable=self.name_var,font=("century schoolbook",15),bg='white')
        namentry.place(x=180,y=186)
    #branch
        branch=Label(frame1,text="Branch",font=("century schoolbook",15,'bold'),fg='black',bg='plum2',bd=0)
        branch.place(x=15,y=173)
        combo_class = ttk.Combobox(frame1, textvariable=self.branch_var, font=("century schoolbook", 13),
                                   state='readonly')
        combo_class['values'] = ("CSE","ECE","EEE","Mechanical","Civil","BME","Biotechnology")
        combo_class.place(x=180,y=175)
    #batch
        batch = Label(frame1, text="Batch", font=("century schoolbook", 15, 'bold'), fg='black', bg='plum2', bd=0)
        batch.place(x=15, y=235)
        batchentry = Entry(bd=1, fg='black', textvariable=self.batch_var, font=("century schoolbook", 15), bg='white')
        batchentry.place(x=180, y=305)
    #date of birth
        date=Label(frame1,text="Date of Birth",font=("century schoolbook", 15, 'bold'), fg='black', bg='plum2', bd=0)
        date.place(x=15,y=290)
        datentry=Entry(bd=1, fg='black', textvariable=self.date_var, font=("century schoolbook", 15), bg='white')
        datentry.insert(0,"dd/mm/yyyy")
        datentry.place(x=180,y=360)
    #Mobile
        mobile=Label(frame1,text="Mobile",font=("century schoolbook", 15, 'bold'), fg='black', bg='plum2', bd=0)
        mobile.place(x=15,y=350)
        mobilentry=Entry(bd=1, fg='black', textvariable=self.mob_var, font=("century schoolbook", 15), bg='white')
        mobilentry.place(x=180,y=420)
    #parent_mobile
        pmob=Label(frame1,text="Parent Mobile",font=("century schoolbook", 15, 'bold'),fg='black', bg='plum2', bd=0)
        pmob.place(x=15,y=410)
        pmobentry=Entry(bd=1, fg='black', textvariable=self.pmob_var, font=("century schoolbook", 15), bg='white')
        pmobentry.place(x=180,y=480)
    #fee
        fee = Label(frame1, text="Amount", font=("century schoolbook", 15, 'bold'), fg='black', bg='plum2', bd=0)
        fee.place(x=15, y=480)
        feentry = ttk.Combobox(frame1, textvariable=self.amount_var, font=("century schoolbook", 13, 'bold'),
                                   state='readonly')
        feentry['values'] = ("Paid","Not Paid")
        feentry.place(x=180, y=480)
    #buttons
        addbt=Button(frame1,text="ADD",bg="maroon2",activebackground="maroon1",
                     font=("century schoolbook",15,"bold"),width=10,command=self.add_students).place(x=35,y=540)

        updatebt=Button(frame1,text="UPDATE",bg="maroon2",activebackground="maroon1",
                        font=("century schoolbook",15,"bold"),width=10,command=self.update_data).place(x=250,y=540)

        deletebt=Button(frame1,text="DELETE",bg="maroon2",activebackground="maroon1",
                        font=("century schoolbook",15,"bold"),width=10,command=self.delete_data).place(x=35,y=600)

        clearbt=Button(frame1,text="CLEAR",bg="maroon2",activebackground="maroon1",
                       font=("century schoolbook",15,"bold"),width=10,command=self.clear).place(x=250,y=600)

                                        #-------frame_2--------

        frame2=Frame(root,bg='white')
        frame2.place(x=452,y=72)
        head2=LabelFrame(frame2,width=748,height=740,text="Student Database",font=("century schoolbook",20,'bold'),
                        fg='purple4',bd=10,bg='plum2')
        head2.grid(row=0,column=0)
        search = Label(frame2, text="Search By", font=("century schoolbook", 15, "bold"), fg='black', bg='plum2')
        search.place(x=30,y=60)
        searchentry=ttk.Combobox(frame2,width=7,textvariable=self.search_by,font=("century schoolbook", 13),
                                   state='readonly')
        searchentry['values']=("Reg","Name","Branch")
        searchentry.place(x=145,y=61)
        txtentry=Entry(frame2,bd=1,width=10, fg='black', textvariable=self.search_txt, font=("century schoolbook", 14), bg='white')
        txtentry.place(x=228,y=61)
        searchbtn=Button(frame2,bg="dodger blue",activebackground="cornflowerblue",bd=2,text="Search",
                         width=10,font=("century schoolbook",13,"bold"),command=self.search_data).place(x=350,y=58)
        searchall=Button(frame2,bg="dodger blue",activebackground="cornflowerblue",bd=2,text="Show All",
                         width=10,font=("century schoolbook",13,"bold"),command=self.fetch_data).place(x=500,y=58)

                                        #--------frame_3------
        tab_frame=Frame(frame2,bd=2,relief=RIDGE,bg='linen')
        tab_frame.place(x=20,y=130,width=710,height=550)
        scroll_x = Scrollbar(tab_frame, orient="horizontal")
        scroll_y = Scrollbar(tab_frame, orient="vertical")

        self.student_table = ttk.Treeview(tab_frame, columns=("sl", "name", "branch", "batch", "date", "mob", "pmob","amount"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("sl", text="Reg.No")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("branch", text="Branch")
        self.student_table.heading("batch", text="Batch")
        self.student_table.heading("date", text="D.O.B")
        self.student_table.heading("mob", text="Mobile")
        self.student_table.heading("pmob", text="Parents Mobile")
        self.student_table.heading("amount", text="Fee")

        self.student_table['show'] = 'headings'

        self.student_table.column("sl", width=80,anchor=CENTER)
        self.student_table.column("name", width=200,anchor=CENTER)
        self.student_table.column("branch", width=140,anchor=CENTER)
        self.student_table.column("batch", width=140,anchor=CENTER)
        self.student_table.column("date", width=140,anchor=CENTER)
        self.student_table.column("mob", width=140,anchor=CENTER)
        self.student_table.column("pmob", width=160,anchor=CENTER)
        self.student_table.column("amount", width=100, anchor=CENTER)
        self.style=ttk.Style()
        self.style.configure('Treeview',rowheight=30,font=("century schoolbook",12))
        self.style.configure("Treeview.Heading",font=("century schoolbook",10,"bold"),foreground='brown4')
        self.student_table.pack(fill=BOTH, expand=1)

        self.student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.sl_var.get()==''or self.name_var.get()=='' \
                or self.batch_var.get()==''or self.mob_var.get()=='' or self.pmob_var.get()==''\
                or self.amount_var.get()==''or self.date_var.get()==''or self.branch_var.get()=='':
            m.showerror('Error', 'All fields are required')
        else:
            try:
                conn = p.connect(host='127.0.0.1', user='root', passwd='taher', database='userdata')
                cur = conn.cursor()
            except:
                m.showerror("Error", "Database Connectivity Issue, Please Try Again")
                return
            try:
                query = 'create table if not exists students(Reg int primary key ,Name varchar(50),' \
                        'Branch varchar(20),Batch varchar(20),DOB varchar(30),Mobile varchar(20),Parent_mobile varchar(20),' \
                        'Amount varchar(20))'
                cur.execute(query)
            except:
                query = "use userdata"
                cur.execute(query)

            query = "insert into students (Reg, Name, Branch, Batch, DOB, Mobile, Parent_mobile, Amount) " \
                    "values (%s,%s, %s, %s, %s, %s, %s, %s)"
            cur.execute(query, (self.sl_var.get(),self.name_var.get(), self.branch_var.get(), self.batch_var.get(),
                                self.date_var.get(), self.mob_var.get(), self.pmob_var.get(),
                                self.amount_var.get()))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            m.showinfo("Success", "Data has been inserted successfully")

    def fetch_data(self):
        try:
            co = p.connect(host='127.0.0.1', user='root', passwd='taher', database='userdata')
            cu = co.cursor()
            cu.execute("select * from students")
            rows = cu.fetchall()
            if len(rows) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in rows:
                    self.student_table.insert("", END, values=row)
                co.commit()
            else:
                m.showerror("Error", "No records found")
        except Exception as e:
            print("Error fetching data:", e)
        finally:
            co.close()

    def clear(self):
        self.sl_var.set("")
        self.name_var.set("")
        self.branch_var.set("")
        self.batch_var.set("")
        self.date_var.set("")
        self.mob_var.set("")
        self.pmob_var.set("")
        self.amount_var.set("")

    def get_cursor(self, event):
        cursor_row = self.student_table.focus()
        contents = self.student_table.item(cursor_row)
        row = contents['values']
        if row:
            self.sl_var.set(row[0])
            self.name_var.set(row[1])
            self.branch_var.set(row[2])
            self.batch_var.set(row[3])
            self.date_var.set(row[4])
            self.mob_var.set(row[5])
            self.pmob_var.set(row[6])

    def update_data(self):
        reg_no = self.sl_var.get()
        if not reg_no:
            m.showerror("Error", "Please select a record to update.")
            return

        try:
            reg_no = int(reg_no)
            conn = p.connect(host='127.0.0.1', user='root', passwd='taher', database='userdata')
            cur = conn.cursor()
            query = "update students set Name=%s,Branch=%s,Batch=%s,DOB=%s,Mobile=%s,Parent_mobile=%s,Amount=%s " \
                    "where Reg=%s"
            cur.execute(query, (self.name_var.get(), self.branch_var.get(), self.batch_var.get(),
                                self.date_var.get(), self.mob_var.get(), self.pmob_var.get(),
                                self.amount_var.get(), reg_no))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            m.showinfo("Success", "Record has been updated successfully.")
        except ValueError:
            m.showerror("Error", "Invalid Reg.No. Please select a valid record.")
        except Exception as e:
            m.showerror("Error", f"An error occurred: {e}")

    def delete_data(self):
        reg_no = self.sl_var.get()
        if not reg_no:
            m.showerror("Error", "Please select a record to delete.")
            return

        try:
            reg_no = int(reg_no)
            conn = p.connect(host='127.0.0.1', user='root', passwd='taher', database='userdata')
            cur = conn.cursor()
            cur.execute("delete from students where Reg=%s", reg_no)
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            m.showinfo("Success", "Record has been deleted successfully.")
        except ValueError:
            m.showerror("Error", "Invalid Reg.No. Please select a valid record.")
        except Exception as e:
            m.showerror("Error", f"An error occurred: {e}")

    def search_data(self):
        conn = p.connect(host='127.0.0.1', user='root', passwd='taher', database='userdata')
        cur = conn.cursor()
        query = "SELECT * FROM students WHERE {} LIKE %s".format(self.search_by.get())
        value = '%' + self.search_txt.get() + '%'
        cur.execute(query, (value,))
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert("", END, values=row)
            conn.commit()
        else:
            m.showerror("Error", "Record doesn't find")
        conn.close()

root = Tk()
ob=student(root)
root.mainloop()