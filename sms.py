from tkinter import*
import time      #inbuilt module
import ttkthemes
from tkinter import ttk,messagebox,filedialog
import pymysql
import pandas

# Functionality part

def iexit():
    reult=messagebox.askyesno('Confirm','Do you want to exit?')
    if reult:
        root.destroy()
    else:
        pass
def export_data():
    url=filedialog.asksaveasfilename(defaultextension='.csv')  # saveas file dialogbox will appear
    indexing=studentTable.get_children()                       #will get fields of viewtree
    newlist=[]                                                 #whole tuple list will store in single list
    for index in indexing:
        content=studentTable.item(index)                       #get content of all fields
        datalist=content['values']                             #print all the values of fiels
        newlist.append(datalist)
    table = pandas.DataFrame(newlist,
                             columns=['Id', 'Name', 'Mobile', 'Email', 'Address', 'Gender', 'DOB', 'Added Date', ])
#pandas will store all the values in tabular form
    table.to_csv(url, index=False) #saves it in exel file
    messagebox.showinfo('Success', 'Data is saved succesfully')

def update_student():
     def update_data():
        query='update students set name=%s,email=%s,mobile_no=%s,address=%s,gender=%s,dob=%s,date=%s where id=%s'
        mycursor.execute(query, (
            nameentry.get(), emailentry.get(), mobileentry.get(),
            addressentry.get(), genderentry.get(), dobentry.get(),date,identry.get()

        ))
        con.commit()
        messagebox.showinfo('SUCCESS',f'id {identry.get()} is succesufully updated',parent=updatewindow)
        updatewindow.destroy()
        show_student()


     updatewindow = Toplevel()
     updatewindow.title('Update Students')
     updatewindow.resizable(False, False)
     updatewindow.grab_set()
     idLabel = Label(updatewindow, text='id', font=('times new roman', 20, 'bold'))
     idLabel.grid(padx=20, pady=10, sticky=W)
     identry = Entry(updatewindow, font=('roman', 20), width=25)
     identry.grid(row=0, column=1, pady=10, padx=15)

     nameLabel = Label(updatewindow, text='Name', font=('times new roman', 20, 'bold'))
     nameLabel.grid(padx=20, pady=10, sticky=W)
     nameentry = Entry(updatewindow, font=('roman', 20), width=25)
     nameentry.grid(row=1, column=1, pady=10, padx=15)

     mobile_noLabel = Label(updatewindow, text='Mobile_no', font=('times new roman', 20, 'bold'))
     mobile_noLabel.grid(padx=20, pady=10, sticky=W)
     mobileentry = Entry(updatewindow, font=('roman', 20), width=25)
     mobileentry.grid(row=2, column=1, pady=10, padx=15)

     emailLabel = Label(updatewindow, text='Email', font=('times new roman', 20, 'bold'))
     emailLabel.grid(padx=20, pady=10, sticky=W)
     emailentry = Entry(updatewindow, font=('roman', 20), width=25)
     emailentry.grid(row=3, column=1, pady=10, padx=15)

     addressLabel = Label(updatewindow, text='Address', font=('times new roman', 20, 'bold'))
     addressLabel.grid(padx=20, pady=10, sticky=W)
     addressentry = Entry(updatewindow, font=('roman', 20), width=25)
     addressentry.grid(row=4, column=1, pady=10, padx=15)

     genderLabel = Label(updatewindow, text='Gender', font=('times new roman', 20, 'bold'))
     genderLabel.grid(padx=20, pady=10, sticky=W)
     genderentry = Entry(updatewindow, font=('roman', 20), width=25)
     genderentry.grid(row=5, column=1, pady=10, padx=15)

     dobLabel = Label(updatewindow, text='D.O.B', font=('times new roman', 20, 'bold'))
     dobLabel.grid(padx=20, pady=10, sticky=W)
     dobentry = Entry(updatewindow, font=('roman', 20), width=25)
     dobentry.grid(row=6, column=1, pady=10, padx=15)

     update_studentbutton = ttk.Button(updatewindow, text='Update Student',command=update_data)
     update_studentbutton.grid(row=7, columnspan=2, pady=15)

     indexing=studentTable.focus()
     print(indexing)
     content=studentTable.item(indexing)
     listdata=content['values']
     identry.insert(0,listdata[0])
     nameentry.insert(0,listdata[1])
     mobileentry.insert(0,listdata[2])
     emailentry.insert(0, listdata[3])
     addressentry.insert(0,listdata[4])
     genderentry.insert(0,listdata[5])
     dobentry.insert(0,listdata[6])


def show_student():
    query = 'select * from students '
    mycursor.execute(query)
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)

def delete_student():

    indexing=studentTable.focus()                                     #select the particular index eg:id
    print(indexing)
    content=studentTable.item(indexing)                               #select the whole row and its content
    content_id = content['values'][0]
    query='delete from students where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'ID {content_id} is deleted successfully')
    query='select * from students '
    mycursor.execute(query)
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)
def search_student():
     def search_data():

             query = 'SELECT * FROM students WHERE id=%s OR name=%s OR email=%s OR mobile_no=%s OR address=%s OR gender=%s OR dob=%s'
             mycursor.execute(query, (
                 identry.get(), nameentry.get(), emailentry.get(), mobileentry.get(),
                 addressentry.get(), genderentry.get(), dobentry.get()
             ))
             studentTable.delete(*studentTable.get_children())
             fetched_data = mycursor.fetchall()
             for data in fetched_data:
                 studentTable.insert('',END, values=data)

     searchwindow = Toplevel()
     searchwindow.title('Search Students')
     searchwindow.resizable(False, False)
     searchwindow.grab_set()
     idLabel = Label(searchwindow, text='id', font=('times new roman', 20, 'bold'))
     idLabel.grid(padx=20, pady=10, sticky=W)
     identry = Entry(searchwindow, font=('roman', 20), width=25)
     identry.grid(row=0, column=1, pady=10, padx=15)

     nameLabel = Label(searchwindow, text='Name', font=('times new roman', 20, 'bold'))
     nameLabel.grid(padx=20, pady=10, sticky=W)
     nameentry = Entry(searchwindow, font=('roman', 20), width=25)
     nameentry.grid(row=1, column=1, pady=10, padx=15)

     mobile_noLabel = Label(searchwindow, text='Mobile_no', font=('times new roman', 20, 'bold'))
     mobile_noLabel.grid(padx=20, pady=10, sticky=W)
     mobileentry = Entry(searchwindow, font=('roman', 20), width=25)
     mobileentry.grid(row=2, column=1, pady=10, padx=15)

     emailLabel = Label(searchwindow, text='Email', font=('times new roman', 20, 'bold'))
     emailLabel.grid(padx=20, pady=10, sticky=W)
     emailentry = Entry(searchwindow, font=('roman', 20), width=25)
     emailentry.grid(row=3, column=1, pady=10, padx=15)

     addressLabel = Label(searchwindow, text='Address', font=('times new roman', 20, 'bold'))
     addressLabel.grid(padx=20, pady=10, sticky=W)
     addressentry = Entry(searchwindow, font=('roman', 20), width=25)
     addressentry.grid(row=4, column=1, pady=10, padx=15)

     genderLabel = Label(searchwindow, text='Gender', font=('times new roman', 20, 'bold'))
     genderLabel.grid(padx=20, pady=10, sticky=W)
     genderentry = Entry(searchwindow, font=('roman', 20), width=25)
     genderentry.grid(row=5, column=1, pady=10, padx=15)

     dobLabel = Label(searchwindow, text='D.O.B', font=('times new roman', 20, 'bold'))
     dobLabel.grid(padx=20, pady=10, sticky=W)
     dobentry = Entry(searchwindow, font=('roman', 20), width=25)
     dobentry.grid(row=6, column=1, pady=10, padx=15)

     search_studentbutton = ttk.Button(searchwindow, text='Search Student',command=search_data)
     search_studentbutton.grid(row=7, columnspan=2,pady=15)
def add_student():
    def add_data():
        if identry.get() == '' or nameentry.get() == '' or mobileentry.get() == '' or emailentry.get() == '' or \
                addressentry.get() == '' or genderentry.get() == '' or dobentry.get() == '':
            messagebox.showerror('ERROR', 'All fields are required', parent=addwindow)
        else:
            try:
             query = 'insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)'
             mycursor.execute(query, (identry.get(), nameentry.get(), mobileentry.get(), emailentry.get(),
                                     addressentry.get(), genderentry.get(), dobentry.get(),date))
             con.commit()
             result = messagebox.askyesno('Data is added successfully', 'Do you want to clean the form', parent=addwindow)
             if result:
                 identry.delete(0, END)
                 nameentry.delete(0, END)
                 mobileentry.delete(0, END)
                 emailentry.delete(0, END)
                 addressentry.delete(0, END)
                 genderentry.delete(0, END)
                 dobentry.delete(0, END)
             else:
                 pass
            except:
                messagebox.showerror('Error','Id cannot be repeated',parent=addwindow)
                return

            query='select *from students'
            mycursor.execute(query)
            fetched_data=mycursor.fetchall()
            studentTable.delete(*studentTable.get_children())
            for data in fetched_data:
                datalist=list(data)
                studentTable.insert('',END,values=datalist)



    addwindow = Toplevel()
    addwindow.resizable(False, False)
    addwindow.grab_set()
    idLabel = Label(addwindow, text='id', font=('times new roman', 20, 'bold'))
    idLabel.grid(padx=20, pady=10, sticky=W)
    identry = Entry(addwindow, font=('roman', 20), width=25)
    identry.grid(row=0, column=1, pady=10, padx=15)


    nameLabel = Label(addwindow, text='Name', font=('times new roman', 20, 'bold'))
    nameLabel.grid(padx=20, pady=10,sticky=W)
    nameentry = Entry(addwindow, font=('roman', 20), width=25)
    nameentry.grid(row=1, column=1, pady=10, padx=15)

    mobile_noLabel = Label(addwindow, text='Mobile_no', font=('times new roman', 20, 'bold'))
    mobile_noLabel.grid(padx=20, pady=10,sticky=W)
    mobileentry = Entry(addwindow, font=('roman', 20), width=25)
    mobileentry.grid(row=2, column=1, pady=10, padx=15)

    emailLabel = Label(addwindow, text='Email', font=('times new roman', 20, 'bold'))
    emailLabel.grid(padx=20, pady=10,sticky=W)
    emailentry = Entry(addwindow, font=('roman', 20), width=25)
    emailentry.grid(row=3, column=1, pady=10, padx=15)

    addressLabel = Label(addwindow, text='Address', font=('times new roman', 20, 'bold'))
    addressLabel.grid(padx=20, pady=10,sticky=W)
    addressentry = Entry(addwindow, font=('roman', 20), width=25)
    addressentry.grid(row=4, column=1, pady=10, padx=15)

    genderLabel = Label(addwindow, text='Gender', font=('times new roman', 20, 'bold'))
    genderLabel.grid(padx=20, pady=10,sticky=W)
    genderentry = Entry(addwindow, font=('roman', 20), width=25)
    genderentry.grid(row=5, column=1, pady=10, padx=15)

    dobLabel = Label(addwindow, text='D.O.B', font=('times new roman', 20, 'bold'))
    dobLabel.grid(padx=20, pady=10,sticky=W)
    dobentry = Entry(addwindow, font=('roman', 20), width=25)
    dobentry.grid(row=6, column=1, pady=10, padx=15)

    add_studentbutton=ttk.Button(addwindow,text='Add Student',command=add_data)
    add_studentbutton.grid(row=7,columnspan=2,pady=15)

def connect_database():
    def connect():
        global mycursor, con
        try:
                 con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get(),
                                      database='studentmanagementsystem')
                 mycursor = con.cursor()
        except pymysql.Error as e:
                messagebox.showerror('Error', f'invalid details: {e}', parent=connectWindow)
                return

        # Execute the query to create the table
        query = 'CREATE TABLE IF NOT EXISTS students(id int not null primary key, name varchar(50), mobile_no varchar(10), ' \
                'email varchar(50), address varchar(100), gender varchar(20), dob varchar(20), date varchar(50))'
        try:
            mycursor.execute(query)
        except pymysql.Error as e:
            messagebox.showerror('Error', f'Error creating table: {e}', parent=connectWindow)
            return

        messagebox.showinfo('Success', 'Database connection is successful', parent=connectWindow)
        addstudents.config(state=NORMAL)
        searchstudents.config(state=NORMAL)
        deletestudents.config(state=NORMAL)
        updatestudents.config(state=NORMAL)
        showstudents.config(state=NORMAL)
        exportstudents.config(state=NORMAL)
        connectWindow.destroy()

    connectWindow=Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('450x300+750+250')
    connectWindow.title('Database connection')
    connectWindow.resizable(0,0)

    hostLabel=Label(connectWindow,text='Host Name',font=('arial',20,'bold'))
    hostLabel.grid(row=0,column=0)
    hostEntry=Entry(connectWindow,font=('times in roman',16,'bold'))
    hostEntry.grid(row=0,column=1,padx=30,pady=25)

    userLabel = Label(connectWindow, text='User Name', font=('arial', 20, 'bold'))
    userLabel.grid(row=1, column=0)
    userEntry = Entry(connectWindow, font=('times in roman', 16, 'bold'))
    userEntry.grid(row=1, column=1, padx=30, pady=25)

    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'))
    passwordLabel.grid(row=2, column=0)
    passwordEntry = Entry(connectWindow, font=('times in roman', 16, 'bold'))
    passwordEntry.grid(row=2, column=1, padx=30, pady=25)

    connectButton=ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.place(x=170,y=250)


count=0
text=''
def slider():
    global text,count
    if count==len(s):                                             #to repeat the s again and again
        count=0
        text=''
    text=text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(300,slider)
def clock():
    global date,currenttime
    date=time.strftime('%d/%m/%Y')                                                #date is a variable
    currenttime=time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f' Date:{date}\nTime:{currenttime}')                #config method is used for updating
    datetimeLabel.after(1000,clock)                                               #after method is used for update after a time


#GUI part
root=ttkthemes.ThemedTk()                                                         #similar to classTk
root.get_themes()
root.set_theme('radiance')


root.geometry('1510x880+0+0')
root.resizable(False,False)
root.title('Student Management System')

datetimeLabel=Label(root,font=('times new roman',20,'bold'),fg='navyblue')
datetimeLabel.place(x=10,y=10)
clock()

s='Student Management System'
sliderLabel=Label(root,text=s,font=('arial',25,'italic bold'),fg='navyblue',width=30)
sliderLabel.place(x=500,y=0)
slider()                                                    #function

connectButton=ttk.Button(root, text='Connect Database', command=connect_database)
connectButton.place(x=1250, y=1)

leftFrame=Frame(root)
leftFrame.place(x=60,y=90,width=500,height=600)

logo_image=PhotoImage(file='student.png')
logo_Label=Label(leftFrame,image=logo_image)
logo_Label.grid(row=0,column=0,)

addstudents=ttk.Button(leftFrame,text='Add Students',width=25,state=DISABLED,command=add_student)
addstudents.grid(row=1,column=0,pady=15)

searchstudents=ttk.Button(leftFrame,text='Search Students',width=25,state=DISABLED,command=search_student)
searchstudents.grid(row=2,column=0,pady=15)

deletestudents=ttk.Button(leftFrame,text='Delete Students',width=25,state=DISABLED,command=delete_student)
deletestudents.grid(row=3,column=0,pady=15)

updatestudents=ttk.Button(leftFrame,text='Update Students',width=25,state=DISABLED,command=update_student)
updatestudents.grid(row=4,column=0,pady=15)

showstudents=ttk.Button(leftFrame,text='Show Students',width=25,state=DISABLED,command=show_student)
showstudents.grid(row=5,column=0,pady=15)

exportstudents=ttk.Button(leftFrame,text='Export Data',width=25,state=DISABLED,command=export_data)
exportstudents.grid(row=6,column=0,pady=15)

exitButton=ttk.Button(leftFrame,text='Exit',width=25,command=iexit)
exitButton.grid(row=7,column=0,pady=15)

rightFrame=Frame(root)
rightFrame.place(x=350,y=90,width=1100,height=600)
#to create a column table

scrollBarX=Scrollbar(rightFrame,orient=HORIZONTAL)
scrollBarY=Scrollbar(rightFrame,orient=VERTICAL)
studentTable=ttk.Treeview(rightFrame,columns=('Id','Name','Mobile No','Email','Address','Gender','D.O.B','Added Date')
                          ,xscrollcommand=scrollBarX.set,yscrollcommand=scrollBarY.set)  #scroll to bind with table

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)
scrollBarX.pack(side=BOTTOM,fill=X)
scrollBarY.pack(side=RIGHT,fill=Y)
studentTable.pack(fill=BOTH,expand=1)

studentTable.heading('Id',text='Id')
studentTable.heading('Name',text='Name')
studentTable.heading('Mobile No',text='Mobile No')
studentTable.heading('Email',text='Email')
studentTable.heading('Address',text='Address')
studentTable.heading('Gender',text='Gender')
studentTable.heading('D.O.B',text='D.O.B')
studentTable.heading('Added Date',text='Added Date')
studentTable.config(show='headings')

studentTable.column('Id',width=50,anchor=CENTER)
studentTable.column('Name',width=300,anchor=CENTER)
studentTable.column('Mobile No',width=300,anchor=CENTER)
studentTable.column('Email',width=300,anchor=CENTER)
studentTable.column('Address',width=300,anchor=CENTER)
studentTable.column('Gender',width=100,anchor=CENTER)
studentTable.column('D.O.B',width=100,anchor=CENTER)
studentTable.column('Added Date',width=100,anchor=CENTER)

style=ttk.Style()

style.configure('treeview',rowheight=40,font=('arial',13,'bold'),foreground='red4')
style.configure('treeview.heading',rowheight=40,font=('arial',15,'bold'))
root.mainloop()



