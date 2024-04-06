from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import pymysql as p
import webbrowser as w

                                #functionality
def fb():
    w.open_new("https://www.facebook.com/")
def linkdin():
    w.open_new("https://www.linkedin.com/")
def google():
    w.open_new("https://accounts.google.com/InteractiveLogin/"
               "signinchooser?continue=https%3A%2F%2Fmail.google.com%"
               "2Fmail%2Fu%2F1%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%"
               "2Fmail%2Fu%2F1%2F&osid=1&passive=1209600&service=mail&ifkv="
               "AeDOFXhjp9SQbisU_GOCf7KdlfGB19xEd3nCeTt9pOHHvxibSIiD6pch2s531q-"
               "zAizL6e754k6EtA&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
def forgot():
    def submit():
        if userentry.get() == '' or passentry.get() == '' or cpassentry.get() == '':
            messagebox.showerror('Error', 'All fields are required', parent=d)
        elif passentry.get() != cpassentry.get():
            messagebox.showerror("Error", "Password Mismatch", parent=d)
        else:
            try:
                co = p.connect(host='127.0.0.1', user='root', passwd='taher', database='userdata')
                cu = co.cursor()
            except:
                messagebox.showerror('Error', 'Database Connectivity Issue,Please Try Again')
                return
            query = "select * from data where Username=%s"
            cu.execute(query, (userentry.get()))
            row = cu.fetchone()
            if row == None:
                messagebox.showerror('Error', 'Username Not Found', parent=d)
            else:
                query = "update data set Password=%s where Username=%s"
                cu.execute(query, (passentry.get(), userentry.get()))
                co.commit()
                co.close()
                messagebox.showinfo('Success', 'Password is Reset,Please Login With New Password', parent=d)
                d.destroy()

    d=Toplevel()
    d.title('Change Password')
    bg = ImageTk.PhotoImage(file="imag-1.png")
    bg_label = Label(d, image=bg).grid()
    head = Label(d, text="RESET PASSWORD", font=("century schoolbook", 20, 'bold underline'), bg='White', fg='magenta4')
    head.place(x=380,y=280)
    username = Label(d, text="Username", font=("century schoolbook", 13, 'bold'), bg='White', fg='orchid3')
    username.place(x=310,y=340)
    userentry = Entry(d, width=45, font=("century schoolbook", 13, 'bold'), fg='magenta4', bd=0)
    userentry.place(x=310,y=370)
    Frame(d, width=350, height=2, bg='salmon4').place(x=310, y=395)
    password = Label(d, text="New Password", font=("century schoolbook", 13, 'bold'), bg='White', fg='orchid3')
    password.place(x=310,y=420)
    passentry = Entry(d, width=40, font=("century schoolbook", 13, 'bold'), fg='magenta4', bd=0)
    passentry.place(x=310,y=450)
    Frame(d, width=350, height=2, bg='salmon4').place(x=310, y=480)
    conpass = Label(d, text="Confirm Password", font=("century schoolbook", 13, 'bold'), bg='White', fg='orchid3')
    conpass.place(x=310,y=500)
    cpassentry = Entry(d, width=40, font=("century schoolbook", 13, 'bold'), fg='magenta4', bd=0)
    cpassentry.place(x=310,y=530)
    Frame(d, width=350, height=2, bg='salmon4').place(x=310, y=550)
    submitbutton = Button(d, text='SUBMIT', bd=0, bg='orchid2', cursor='hand2', fg='black', width=25,
                          activebackground='orchid4',font=('century schoolbook', 18, 'bold'),command=submit)
    submitbutton.place(x=310,y=630)
    d.mainloop()

def log():
    if username.get()=="" or password.get()=='':
        messagebox.showerror('Error','All fields are required')
    else:
        try:
            con=p.connect(host="127.0.0.1",user='root',passwd='taher')
            cu=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue')
            return
        query="use userdata"
        cu.execute(query)
        query='select * from data where Username=%s and Password=%s'
        cu.execute(query,(username.get(),password.get()))
        row=cu.fetchone()
        if row==None:
            messagebox.showerror('Error','Invalid Username and password')
        else:
            messagebox.showinfo('Welcome','Login  Successful')
            a.destroy()
            import std
def signup():
    a.destroy()
    import signuppage

def close():
    o_img.config(file='closeeye.png')
    password.config(show="*")
    eybutton.config(command=show)

def show():
    o_img.config(file='openeye.png')
    password.config(show="")
    eybutton.config(command=show)

def user_entry(name):
    if username.get()=='Username':
        username.delete(0,END)
def pas_entry(name):
    if password.get()=="Password":
        password.delete(0,END)

a=Tk()
a.title("Login-Form")
a.geometry("1000x820+190+10")
a.resizable(False,False)


bg=ImageTk.PhotoImage(file="imag-1.png")
bg_label=Label(a,image=bg).place(x=0,y=0)
head=Label(a,text="LOG-IN",font=("century schoolbook",35,'bold'),bg='White',fg='sienna4')
head.place(x=410,y=280)

username=Entry(a,width=30,font=("century schoolbook",15),bd=0,fg='salmon4')
username.place(x=360,y=380)
username.insert(0,'Username')
username.bind('<FocusIn>',user_entry)
Frame(a,width=250,height=2,bg='salmon4').place(x=360,y=405)

password=Entry(a,width=30,font=("century schoolbook",15),bd=0,fg='salmon4')
password.place(x=360,y=450)
password.insert(0,'Password')
password.bind('<FocusIn>',pas_entry)
Frame(a,width=250,height=2,bg='salmon4').place(x=360,y=475)

o_img=PhotoImage(file="openeye.png")
eybutton=Button(a,image=o_img,bd=0,bg='white',activebackground='white',cursor='hand2',command=close)
eybutton.place(x=580,y=450)

forgetbutton=Button(a,text='Forgot Password?',bd=0,bg='white',activebackground='white',cursor='hand2',fg='salmon4',command=forgot)
forgetbutton.place(x=520,y=480)

signbutton=Button(a,text='SIGN IN',bd=0,bg='salmon4',cursor='hand2',fg='black',width=17,activebackground='salmon4',
                  font=('Century schoolbook',20,'bold'),command=log)
signbutton.place(x=340,y=510)

orlabel=Label(a,text='-------- OR --------',font=("century schoolbook",20),fg='salmon4',
              width=25,bg='white',bd=0).place(x=280,y=570)

facebk=PhotoImage(file="f_logo.png")
facebutton=Button(a,image=facebk,bd=0,bg='white',command=fb)
facebutton.place(x=413,y=610)

linkdn=PhotoImage(file="lk.png.png")
lkdnbutton=Button(a,image=linkdn,bd=0,bg='white',command=linkdin)
lkdnbutton.place(x=480,y=610)

gog=PhotoImage(file="google.png")
gogbutton=Button(a,image=gog,bd=0,bg='white',command=google)
gogbutton.place(x=544,y=610)

newlabel=Label(a,text="Don't have an account?",font=("century schoolbook",13),fg='salmon4',
             bg='white',bd=0).place(x=360,y=700)
create=Button(a,text='Create new',bd=0,cursor='hand2',bg='white',fg='blue',
                  font=('century schoolbook',12,'bold underline'),command=signup)
create.place(x=544,y=697)
mainloop()