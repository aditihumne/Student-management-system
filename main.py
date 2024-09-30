from tkinter import *
from PIL import ImageTk
from tkinter import messagebox

def login():
 if usernameEntry.get()==''or passwordEntry.get()=='':
     messagebox.showerror('ERROR','Fields cant be empty')

 elif usernameEntry.get()=='aditi' and passwordEntry.get()=='aditi_19h':
     messagebox.showinfo('SUCCESS','welcome')
     window.destroy()
     import sms


 else:
     messagebox.showerror('ERROR','please enter correct credentials')

window=Tk()
window.geometry('1280x700+0+0')
window.resizable(False,False)
window.title('login for student management system')

backgroundImage=ImageTk.PhotoImage(file='bg.jpg')

bgLabel=Label(window,image=backgroundImage)
bgLabel.place(x=0,y= 0)

loginFrame=Frame(window,bg='white')
loginFrame.place(x=400,y=150)

logoImage=PhotoImage(file='logo.png')
logoLabel=Label(loginFrame,image=logoImage,bg='white')
logoLabel.grid(row=0,column=0,columnspan=2,pady=10)


usernameImage=PhotoImage(file='user.png')
usernameLabel=Label(loginFrame,image=usernameImage,text='Username',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10)
usernameEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='navyblue')
usernameEntry.grid(row=1,column=1,pady=10,padx=20)


passwordImage=PhotoImage(file='password.png')
passwordLabel=Label(loginFrame,image=passwordImage,text='password',compound=LEFT
                    ,font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10)
passwordEntry=Entry(loginFrame,font=('times new roman',20,'bold'),bd=5,fg='navyblue')
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

LoginBotton=Button(loginFrame,text='Login',font=('times new roman',20,'bold'),width=10,
                   fg='white',bg='cornflowerblue',cursor='hand2',command=login)
LoginBotton.grid(row=3,column=0,columnspan=2,pady=20)



window.mainloop()