from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql as p

def clear():
    emailentry.delete(0,END)
    userentry.delete(0,END)
    passwordentry.delete(0,END)
    cpassentry.delete(0,END)
    check.set(0)
def signup():
    if emailentry.get()=='' or userentry.get()=='' or passwordentry.get()=='' or cpassentry.get()=='':
        messagebox.showerror('Error','All fields are required')
    elif passwordentry.get()!=cpassentry.get():
        messagebox.showerror("Error","Password Mismatch")
    elif check.get()==0:
        messagebox.showerror('Error','Please Accept Terms & Conditions')
    else:
        try:
            con=p.connect(host="127.0.0.1",user='root',passwd='taher')
            cu=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
        try:
            query="create database userdata"
            cu.execute(query)
            query="use userdata"
            cu.execute(query)
            query='create table data(Id int auto_increment primary key not null,' \
                  'Email varchar(50),Username varchar(100),Password varchar(100))'
            cu.execute(query)
        except:
            query="use userdata"
            cu.execute(query)
        query="insert into data(Email,Username,Password) values(%s,%s,%s)"
        cu.execute(query,(emailentry.get(),userentry.get(),passwordentry.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Success",'Registration is Successful')
        clear()

def Signin():
    a.destroy()
    import loginpage
a=Tk()
a.title("Signup Page")
a.geometry("1000x820+190+10")
a.resizable(False,False)

bg=ImageTk.PhotoImage(file="imag-1.png")
bg_label=Label(a,image=bg).grid()

frame=Frame(a,bg='white')
frame.place(x=255,y=260)
head=Label(frame,text="CREATE AN ACCOUNT",font=("century schoolbook",20,'bold'),bg='White',fg='sienna4')
head.grid(row=0,column=0,padx=90,pady=(20,5))

email=Label(frame,text="Email",font=("century schoolbook",13,'bold'),bg='White',fg='sienna4')
email.grid(row=1,column=0,sticky='w',padx=20,pady=(10,0))
emailentry=Entry(frame,width=40,font=("century schoolbook",13,'bold'),fg='white',bg='sienna4')
emailentry.grid(row=2,column=0,sticky='w',padx=20)

username=Label(frame,text="Username",font=("century schoolbook",13,'bold'),bg='White',fg='sienna4')
username.grid(row=3,column=0,sticky='w',padx=20,pady=(10,0))
userentry=Entry(frame,width=40,font=("century schoolbook",13,'bold'),fg='white',bg='sienna4')
userentry.grid(row=4,column=0,sticky='w',padx=20)

password=Label(frame,text="Password",font=("century schoolbook",13,'bold'),bg='White',fg='sienna4')
password.grid(row=5,column=0,sticky='w',padx=20,pady=(10,0))
passwordentry=Entry(frame,width=40,font=("century schoolbook",13,'bold'),fg='white',bg='sienna4')
passwordentry.grid(row=6,column=0,sticky='w',padx=20)

conpass=Label(frame,text="Confirm Password",font=("century schoolbook",13,'bold'),bg='White',fg='sienna4')
conpass.grid(row=7,column=0,sticky='w',padx=20,pady=(10,0))
cpassentry=Entry(frame,width=40,font=("century schoolbook",13,'bold'),fg='white',bg='sienna4')
cpassentry.grid(row=8,column=0,sticky='w',padx=20)

check=IntVar()
terms=Checkbutton(frame,text="I Agree to the Terms & Conditions",font=("century schoolbook",12,'bold'),
                  activebackground='white',bd=0,bg='white',fg='salmon4',variable=check)
terms.grid(row=9,column=0,sticky='w',padx=20,pady=(10,5))

signupbutton=Button(frame,text='SIGN UP',bd=0,bg='salmon4',cursor='hand2',fg='black',width=25,
                  font=('century schoolbook',18,'bold'),command=signup)
signupbutton.grid(row=10,column=0,sticky='w',padx=30,pady=(20,5))

newlabel=Label(frame,text="Already have an account?",font=("century schoolbook",13),fg='salmon4',
             bg='white',bd=0)
newlabel.grid(row=11,column=0,sticky='w',padx=30,pady=15)

log=Button(a,text='Sign In',bd=0,cursor='hand2',bg='white',fg='blue',
                  font=('century schoolbook',12,'bold underline'),command=Signin)
log.place(x=490,y=697)
a.mainloop()