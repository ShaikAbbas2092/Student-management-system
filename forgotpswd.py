from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import pymysql as p

def submit():
    if userentry.get()=='' or passentry.get()=='' or cpassentry.get()=='':
        messagebox.showerror('Error','All Fields Are Required',parent=a)
    elif passentry.get()!=cpassentry.get():
        messagebox.showerror("Error","Password Mismatch",parent=a)
    else:
        try:
            co=p.connect(host='127.0.0.1',user='root',passwd='taher',database='userdata')
            cu=co.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue,Please Try Again')
            return
        query = "select * from data where Username=%s"
        cu.execute(query, (userentry.get()))
        row=cu.fetchone()
        if row==None:
            messagebox.showerror('Error','Username Not Found',parent=a)
        else:
            query="update data set Password=%s where Username=%s"
            cu.execute(query,(userentry,userentry))
            co.commit()
            co.close()
            messagebox.showinfo('Success','Password is reset,Please login with new Password',parent=a)
            a.login()



a=Tk()
a.title("Password Reset")
a.geometry("1000x820+190+10")
a.resizable(False,False)

bg=ImageTk.PhotoImage(file="imag-1.png")
bg_label=Label(a,image=bg).grid()

frame=Frame(a,bg='white')
frame.place(x=255,y=260)

head=Label(frame,text="RESET PASSWORD",font=("century schoolbook",20,'bold'),bg='White',fg='sienna4')
head.grid(row=0,column=0,padx=110,pady=(20,5))

username=Label(frame,text="Username",font=("century schoolbook",13,'bold'),bg='White',fg='sienna4')
username.grid(row=1,column=0,sticky='w',padx=30,pady=(35,0))
userentry=Entry(frame,width=40,font=("century schoolbook",13,'bold'),fg='white',bg='sienna4')
userentry.grid(row=2,column=0,sticky='w',padx=30)

password=Label(frame,text="New Password",font=("century schoolbook",13,'bold'),bg='White',fg='sienna4')
password.grid(row=3,column=0,sticky='w',padx=30,pady=(35,0))
passentry=Entry(frame,width=40,font=("century schoolbook",13,'bold'),fg='white',bg='sienna4')
passentry.grid(row=4,column=0,sticky='w',padx=30)

conpass=Label(frame,text="Confirm Password",font=("century schoolbook",13,'bold'),bg='White',fg='sienna4')
conpass.grid(row=5,column=0,sticky='w',padx=30,pady=(35,0))
cpassentry=Entry(frame,width=40,font=("century schoolbook",13,'bold'),fg='white',bg='sienna4')
cpassentry.grid(row=6,column=0,sticky='w',padx=30)

submitbutton=Button(frame,text='SUBMIT',bd=0,bg='salmon4',cursor='hand2',fg='black',width=25,activebackground='salmon4',
                  font=('century schoolbook',18,'bold'),command=submit)
submitbutton.grid(row=7,column=0,sticky='w',padx=30,pady=(45,0))
mainloop()