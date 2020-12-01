import os
import sqlite3
from tkinter import *
from sqlite3 import *
from sqlite3 import  Error
from datetime import datetime
import reportlab
from reportlab.graphics.shapes import String
from reportlab.pdfgen import canvas
from datetime import datetime
import os

#creating DataBase
from tkinter.ttk import Treeview
PressBtn="null"
serachWindow="null"
windows=[]
try:
        con = sqlite3.connect("CLAS.db")
        c=con.cursor()
        '''command = "create table users( username text primary key ,phnumber int,name text,userAddress text,password text,date text,type text)"
        c.execute(command)'''

        command1 = "create table Books( rgNO int primary key ,bookName text,author text,price int, quantity int,date text)"
        c.execute(command1)
except Error as e:
    if not e=="table users already exists":
        print(e)

#end
window=Tk()
container=Frame(window, width=800, height=1050)
window.geometry("1366x768+0+0")
window.title("LogIn Form..")
#component Section
mainHeading=Label(window,text="College Library Automation",font=("bold arial",18),fg="white",bg="green")
formTitle=Label(container,text="LogIn Form",font=("bold arial",18),fg="white",bg="black")
hint=Label(container,text="(Provide correct username & password)",font=("bold arial",8),fg="white",bg="black")
userNameLabel=Label(container,text="Username",font=("bold arial",15),fg="white",bg="black")
passwordLabel=Label(container,text="Password",font=("bold arial",15),fg="white",bg="black")
usernameEntry=Entry(container,font=("arial",15))
passwordEntry=Entry(container,font=("arial",15),show="*")
info=Label(window,text="For Best view Use(1368x768 screen resolution)",font=("bold arial",12),fg="#bbb2b2")

#doLogInFuntion
def doLogIn():
    userName=usernameEntry.get()
    password=passwordEntry.get()
    if userName=="" and password=="":
       hint.configure(text="provide username and password..!",font=("bold arial",10),bg="red")
       return
    '''if userName!="ali" and password!="123":
        hint.configure(text="wrong username and password provided..!", font=("bold arial", 10), bg="red")
        return'''

    c = con.cursor()
    c.execute("select*from users where username=? and password=? ", (userName,password,))
    resut = c.fetchall()
    dataStr = "null"
    for x in resut:
        dataStr = x

    dataStrNew = list(dataStr)
    if len(dataStrNew) >=7:
        #print(dataStr[5])
        if dataStr[5]=="Admin":
            menuWindow=Tk()
            windows.append(menuWindow)
            menuWindow.geometry("1366x768+0+0")
            menuWindow.title("Library Section..")
            adminFrame=Frame(menuWindow,width="450",height=500,background="#bbb2b2")
            mainHeading = Label(menuWindow, text="Library Section...", font=("bold arial", 18), fg="white",bg="black")
            cv = Label(adminFrame, text="Library Menu...", font=("bold arial", 15), fg="white", bg="black")
            type=Label(menuWindow, text="Type:Admin", font=("bold arial", 8), fg="white", bg="black")
            #adminFunctions
            def createUser():
                userCreateWindow=Tk()
                windows.append(userCreateWindow)
                userCreateWindow.title("Create new User...")
                userCreateWindow.geometry("1366x768+0+0")
                mainHeading = Label(userCreateWindow, text="Create New User....", font=("bold arial", 18), fg="white",bg="black")
                Errorput=Label(userCreateWindow, text="", font=("bold arial", 9))
                userNameLabel=Label(userCreateWindow,text="Username",font=("bold arial",15),fg="white",bg="black")
                usernameEntry=Entry(userCreateWindow)
                name=Label(userCreateWindow,text="Full Name",font=("bold arial",15),fg="white",bg="black")
                nameEntry=Entry(userCreateWindow)
                phoneNumber=Label(userCreateWindow,text="Phone Number",font=("bold arial",15),fg="white",bg="black")
                phoneNumberEntry=Entry(userCreateWindow)
                address = Label(userCreateWindow, text="Address", font=("bold arial", 15), fg="white",bg="black")
                addressEntry = Entry(userCreateWindow)
                password = Label(userCreateWindow, text="Passowrd", font=("bold arial", 15), fg="white", bg="black")
                passwordEntry = Entry(userCreateWindow)
                rpassword = Label(userCreateWindow, text="Repeat Password", font=("bold arial", 15), fg="white", bg="black")
                rPasswordEntry = Entry(userCreateWindow)
                type=Label(userCreateWindow, text="Select type", font=("bold arial", 15), fg="white", bg="black")
                # variable Area
                var = IntVar()
                def getType():
                    pass
                # end
                #user = Radiobutton(userCreateWindow, text="User", value=1, variable=var, font=("arial blod", 12),command=getType)
                user=Radiobutton(userCreateWindow, text="User", variable=var, value=1,
                            command=getType)
                admin = Radiobutton(userCreateWindow, text="Admin", value=2, variable=var, font=("arial blod", 12),command=getType)
                default = StringVar(userCreateWindow)
                types = {'User', 'Admin'}
                default.set("---Select your User Type---")
                optionManu = OptionMenu(userCreateWindow, default, *types)

                #function
                def doCreate():
                    username=usernameEntry.get()
                    fullName=nameEntry.get()
                    phoneNumber=phoneNumberEntry.get()
                    address=addressEntry.get()
                    password=passwordEntry.get()
                    rpassword=rPasswordEntry.get()
                    userType=default.get()
                    if username=="" or fullName=="" or phoneNumber=="" or address=="" or password=="" or rpassword=="" or userType =="---Select your User Type---" :
                        Errorput.configure(text="Fields are Empty..!",fg="white",bg="red")
                        return
                    if password!=rpassword:
                        Errorput.configure(text="Password didn't match..!", fg="white", bg="red")
                        return

                    if not  phoneNumber.isdigit():
                        Errorput.configure(text="PhoneNumber couldn't alphabet..!", fg="white", bg="red")
                        return
                    c = con.cursor()
                    c.execute("select*from users where username=?  ", (username,))
                    resut = c.fetchall()
                    dataStr = "null"
                    for x in resut:
                        dataStr = x

                    dataStrNew = list(dataStr)
                    if len(dataStrNew) >4:
                        Errorput.configure(text="User already Exits with this UserName ...!", fg="white", bg="red")

                    else:
                        crurentDate=str(datetime.today().strftime('%Y-%m-%d'))
                        c = con.cursor()
                        c.execute("insert into users values(?,?,?,?,?,?,?,?)",
                                  (username,phoneNumber,fullName,address,password,userType,crurentDate,0))
                        con.commit()
                        Errorput.configure(text="User added successfully..!", fg="white", bg="green")

                #end
                def Logout():
                    for x in windows:
                        x.destroy()
                    windows.clear()
                createNewUserBtn=Button(userCreateWindow,text="Create User",fg="white",bg="green",command=doCreate)
                rMeuBtn = Button(userCreateWindow, text="Log out", fg="white", bg="green",command=Logout)

                mainHeading.pack(pady=20)
                Errorput.pack()
                rMeuBtn.place(x=1190,y=100,width=160,height=36)
                userNameLabel.place(x=350,y=230)
                usernameEntry.place(x=650,y=230,width=220,height=30)
                name.place(x=350, y=300)
                nameEntry.place(x=650, y=300, width=220, height=30)
                phoneNumber.place(x=350, y=370)
                phoneNumberEntry.place(x=650, y=370, width=220, height=30)
                address.place(x=350, y=440)
                addressEntry.place(x=650, y=440, width=220, height=30)
                password.place(x=350, y=510)
                passwordEntry.place(x=650, y=510, width=220, height=30)
                rpassword.place(x=350,y=580)
                rPasswordEntry.place(x=650,y=580,width=220, height=30)
                type.place(x=350,y=650)
                optionManu.place(x=650,y=650, width=220, height=30)
                createNewUserBtn.place(x=920,y=645,width=180,height=36)

                userCreateWindow.mainloop()

            #end
            #addBookFunction
            def addBook():
                addBookWindow = Tk()
                windows.append(addBookWindow)
                addBookWindow.title("Add Book...")
                addBookWindow.geometry("1366x768+0+0")
                mainHeading = Label(addBookWindow, text="College Library Automation", font=("bold arial", 18), fg="white",
                                    bg="black")
                mainHeading2 = Label(addBookWindow, text="Book Addtion Form", font=("bold arial", 18),
                                    fg="white",
                                    bg="green")

                Errorput = Label(addBookWindow, text="", font=("bold arial", 9))
                regNo = Label(addBookWindow, text="Reg_No", font=("bold arial", 15), fg="white",
                                      bg="black")
                regNoEntry = Entry(addBookWindow)
                name = Label(addBookWindow, text="Book Name", font=("bold arial", 15), fg="white", bg="black")
                nameEntry = Entry(addBookWindow)
                authorName = Label(addBookWindow, text="Author", font=("bold arial", 15), fg="white", bg="black")
                authorNameEntry = Entry(addBookWindow)

                price = Label(addBookWindow, text="Book Price", font=("bold arial", 15), fg="white",
                                    bg="black")
                priceEntry = Entry(addBookWindow)

                quantity = Label(addBookWindow, text="Book Quantity", font=("bold arial", 15), fg="white", bg="black")
                quantityEntry = Entry(addBookWindow)
                # function
                def doCreate():
                    rgNO = regNoEntry.get()
                    bookName = nameEntry.get()
                    authoname = authorNameEntry.get()
                    bookPrice = priceEntry.get()
                    bookQuantity = quantityEntry.get()

                    if rgNO == "" or bookName == "" or authoname == "" or bookPrice == "" or bookQuantity == "" :
                        Errorput.configure(text="Fields are Empty..!", fg="white", bg="red")
                        return

                    if not bookPrice.isdigit():
                        Errorput.configure(text="price couldn't alphabet..!", fg="white", bg="red")
                        return

                    if not bookQuantity.isdigit():
                        Errorput.configure(text="Book quantity must be alphabet..!", fg="white", bg="red")
                        return

                    c = con.cursor()
                    c.execute("select*from Books where rgNo=?  ", (rgNO,))
                    resut = c.fetchall()
                    dataStr = "null"
                    for x in resut:
                        dataStr = x

                    dataStrNew = list(dataStr)
                    if len(dataStrNew) > 4:
                        Errorput.configure(text="Book already Exits with this Reg_ no ...!", fg="white", bg="red")


                    else:
                        crurentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        c = con.cursor()
                        c.execute("insert into Books values(?,?,?,?,?,?)",
                                  (rgNO, bookName, authoname, bookPrice, bookQuantity,  crurentDate))
                        con.commit()
                        Errorput.configure(text="Book added successfully..!", fg="white", bg="green")

                # end
                def logout():
                    for x in windows:
                        x.destroy()
                    windows.clear()

                addBookBtn = Button(addBookWindow, text="Add Book",font=("arial bold",15) ,fg="white", bg="green",
                                          command=doCreate)
                rMeuBtn = Button(addBookWindow, text="Log out", font=("arial bold",15) ,fg="white", bg="green",command=logout)

                mainHeading.pack(pady=20)
                Errorput.pack()
                mainHeading2.place(x=450,y=145,width=400)
                regNo.place(x=350,y=250)
                regNoEntry .place(x=650,y=250,width=220,height=30)
                name.place(x=350,y=320)
                nameEntry.place(x=650,y=320,width=220,height=30)
                authorName .place(x=350, y=390)
                authorNameEntry .place(x=650, y=390, width=220, height=30)
                price .place(x=350,y=460)
                priceEntry .place(x=650,y=460,width=220, height=30)
                quantity  .place(x=350, y=530)
                quantityEntry .place(x=650, y=530,width=220, height=30)
                addBookBtn.place(x=350,y=600)
                rMeuBtn.place(x=795,y=600)
                addBookWindow.mainloop()
            #end
            #seachBookFunction
            def searchBook():
                searchBookWindow = Tk()
                windows.append(searchBookWindow)
                print(windows)
                searchBookWindow.title("Search Book...")
                searchBookWindow.geometry("1366x768+0+0")
                mainHeading = Label(searchBookWindow, text="Search Book form", font=("bold arial", 18), fg="white",
                                    bg="black")
                hint=Label(searchBookWindow, text="(Reg_No/BookName,AuthoName)", font=("bold arial", 8), fg="white",
                                    bg="green")
                Error = Label(searchBookWindow, text="", font=("bold arial", 8), )

                SearchResults = Label(searchBookWindow, text="", font=("bold arial", 18))
                serachEntry=Entry(searchBookWindow)
                tv = Treeview(searchBookWindow)
                tv['columns'] = ('Rg_No', 'Book Name', 'Author Name', 'Price', 'quanitity', 'date')

                tv.heading("#0", text="", anchor="w")
                tv.column("#0", anchor="center", width=2)
                tv.column('Rg_No', anchor='center', width=100)

                tv.heading('Rg_No', text='Rg_No',anchor="center")
                tv.heading('Book Name', text='Book Name',anchor="center")
                tv.heading('Author Name', text='Author Name',anchor="center")
                tv.heading('Price', text='Price',anchor="center")
                tv.heading('quanitity', text='Quanitity',anchor="center")
                tv.heading('date', text='Date')
                #updateForm
                mainHeadingUp = Label(searchBookWindow, text="Book Update Form", font=("bold arial", 18), fg="white",
                                    bg="green")
                regNo = Label(searchBookWindow, text="Reg_No", font=("bold arial", 12), fg="white",
                              bg="black")
                regNoEntry = Entry(searchBookWindow, state=DISABLED)
                name = Label(searchBookWindow, text="Book Name", font=("bold arial", 12), fg="white", bg="black")
                nameEntry = Entry(searchBookWindow,font=("arial ",15))
                authorName = Label(searchBookWindow, text="Author", font=("bold arial", 12), fg="white", bg="black")
                authorNameEntry = Entry(searchBookWindow,font=("arial ",15))

                price = Label(searchBookWindow, text="Book Price", font=("bold arial", 12), fg="white",
                              bg="black")
                priceEntry = Entry(searchBookWindow,font=("arial ",15))

                quantity = Label(searchBookWindow, text="Book Quantity", font=("bold arial", 12), fg="white", bg="black")
                quantityEntry = Entry(searchBookWindow,font=("arial ",15))
                Dateb = Label(searchBookWindow, text="Date", font=("bold arial", 12), fg="white",
                                 bg="black")
                dateEntry = Entry(searchBookWindow,font=("arial ",15))
                #function
                def doUpdate():
                    curItem = tv.focus()
                    data = list(tv.item(curItem).values())
                    getValuesList = data[2]
                    if len(getValuesList) == 0:
                        SearchResults.configure(text="----First Load Data with Load Button Then Update----", fg="white", bg="red")
                        return
                    getRg_No = getValuesList[0]
                    nameVal = getRg_No
                    addressVal = nameEntry.get()
                    memeberTypesVal = authorNameEntry.get()
                    cityVal = priceEntry.get()
                    phnbr = quantityEntry.get()
                    dated = dateEntry.get()
                    #print("rgNo",nameVal)
                    if   addressVal != "" and memeberTypesVal != "" and memeberTypesVal!="" and cityVal!="" and phnbr!="" and dated!="":
                        cc = con.cursor()
                        cc.execute("update Books set  bookName=? ,author =?,price=?,quantity=?,date=? where rgNO=?",
                                   (addressVal, memeberTypesVal, cityVal, phnbr,dated,nameVal))
                        con.commit()
                        SearchResults.configure(text="----Successfully Update Data----", fg="white", bg="green")

                    else:
                        SearchResults.configure(text="----First Load Data with Load Button----", fg="white", bg="red")


                #end
                updateBtn=Button(searchBookWindow,text="Update Data",font=("arial bold",12),fg="white",bg="green",command=doUpdate)
                #end
                #end
                def doSearch():
                        rm=tv.get_children()
                        for child in rm:
                            tv.delete(child)
                        getKeyword = serachEntry.get()
                        rgNO=00;
                        if getKeyword.isdigit():
                            rgNO=int(getKeyword)
                        else:
                            rgNO=str(getKeyword)
                        if getKeyword =="":
                            Error.configure(text="Search Filed Empty..!",fg="white",bg="red")
                            return
                        Error.configure(text="", bg="white")
                        c = con.cursor()
                        c.execute(" select*from Books  where rgNo=? or bookName=? or author=?;", (rgNO,rgNO,rgNO,))
                        resut = c.fetchall()
                        dataStr = "null"
                        o=[]

                        for y in resut:
                            o.append(list(y))
                        olen=len(o)
                        #print(olen)
                        if len(o) == 0:
                            Error.configure(text="NO Data Exit....!", fg="white", bg="red")
                            return

                        Error.configure(text="", bg="white")

                        for x in range(olen):
                                tv.insert('','end',text="",values=(o[x][0],o[x][1],o[x][2],o[x][3],o[x][4],o[x][5]))



                        for x in resut:
                            dataStr = x

                        dataStrNew = list(dataStr)
                        i=1
                        namelist=[]
                        i=0;

                        lene=len(dataStrNew)
                        for x in dataStrNew:
                            pass

                def doDelete():

                    curItem = tv.focus()
                    data=list(tv.item(curItem).values())
                    getValuesList=data[2]
                    if len(getValuesList)==0:
                        SearchResults.configure(text="----No selection Exit----",fg="white",bg="red")
                        return
                    getRg_No=getValuesList[0]
                    #print(getRg_No)
                    c=con.cursor()
                    c.execute("delete from Books where rgNO=?", (getRg_No,))
                    con.commit()
                    SearchResults.configure(text="----Deleted Successfully----", fg="white", bg="green")
                    selected_item = tv.selection()[0]  ## get selected item
                    tv.delete(selected_item)
                    tv.pack()
                # end
                #start
                def doLoad():
                    curItem = tv.focus()
                    data = list(tv.item(curItem).values())
                    getValuesList = data[2]
                    if len(getValuesList) == 0:
                        SearchResults.configure(text="----No selection Exit----", fg="white", bg="red")
                        return
                    getRg_No = getValuesList[0]
                    #print(getRg_No)
                    c = con.cursor()
                    c.execute("select*from Books where rgNO=?", (getRg_No,))
                    resut = c.fetchall()
                    dataStr = "null"
                    for x in resut:
                        dataStr = x

                    dataStrNew = list(dataStr)
                    #print(dataStrNew)
                    if len(dataStrNew) >= 5:
                        regNoEntry.delete(0, 'end')
                        nameEntry.delete(0,'end')
                        authorNameEntry.delete(0, 'end')
                        priceEntry.delete(0,'end')
                        quantityEntry.delete(0,'end')
                        dateEntry.delete(0,'end')
                        regNoEntry.insert(0, dataStrNew[0])
                        nameEntry.insert(0, dataStrNew[1])
                        authorNameEntry.insert(0,dataStrNew[2])
                        priceEntry.insert(0,dataStrNew[3])
                        quantityEntry.insert(0,dataStrNew[4])
                        dateEntry.insert(0,dataStrNew[5])



                #end
                def logout():
                    for x in windows:
                        x.destroy()
                    windows.clear()

                searchBtn=Button(searchBookWindow,text="Search",fg="white",bg="green",command=doSearch)
                deleteBtn = Button(searchBookWindow, text="Delete Selection",font=("arial bold",15) ,fg="white", bg="green", command=doDelete)
                loadBtn = Button(searchBookWindow, text="Load Data ", font=("arial bold", 15), fg="white",
                                   bg="green", command=doLoad)
                logoutBtn = Button(searchBookWindow, text="Log out ", fg="white",
                                 bg="green",command=logout)

                #elemenstsAdd
                mainHeading.pack(pady=20)
                SearchResults.pack()
                hint.place(x=12,y=75)
                serachEntry.place(x=10,y=100,width=180,height=25)
                searchBtn.place(x=200,y=100)
                logoutBtn.place(x=1190, y=95, width=160, height=36)

                Error.place(x=250,y=104)
                tv.pack(pady=40)
                deleteBtn.place(x=130,y=390)
                loadBtn.place(x=1115,y=390)
                mainHeadingUp.place(x=510,y=430,width=350)
                regNo.place(x=350,y=500)
                regNoEntry.place(x=350,y=530,width=250,height=32)
                name.place(x=700,y=500)
                nameEntry.place(x=700,y=530,width=250,height=32)
                authorName.place(x=350,y=575)
                authorNameEntry.place(x=350,y=605,width=250,height=32)
                price.place(x=700,y=575)
                priceEntry.place(x=700,y=605,width=250,height=32)
                quantity.place(x=350,y=650)
                quantityEntry.place(x=350,y=680,width=250,height=32)
                Dateb.place(x=700,y=650)
                dateEntry.place(x=700, y=680, width=250, height=32)
                updateBtn.place(x=1000,y=680)
                #end
                searchBookWindow.mainloop()

            #end
            #isseBookFunction
            def issueBook():
                issueBookWindow=Tk()
                windows.append(issueBookWindow)
                issueBookWindow.geometry("1366x768")
                issueBookWindow.title("Issue Book...........")
                mainHeading=Label(issueBookWindow,text="Issue Book Form",font=("arial bold",18),fg="white",bg="black")
                mainHeadingc = Label(issueBookWindow, text="College Library Automation", font=("arial bold", 18), fg="white",
                                    bg="green")

                Error=Label(issueBookWindow,text="",font=("arial bold",8))
                searcBookfield=Entry(issueBookWindow)
                regNo=Label(issueBookWindow,text="Book Reg_No",font=("arial bold",12),fg="white",bg="black")
                regNoEntry=Entry(issueBookWindow)

                bookName = Label(issueBookWindow, text="Book Name", font=("arial bold", 12), fg="white", bg="black")
                booNameEntry = Entry(issueBookWindow)
                userName = Label(issueBookWindow, text="Borrowed Username", font=("arial bold", 12), fg="white", bg="black")
                userNameEntry = Entry(issueBookWindow)
                issueQuantity = Label(issueBookWindow, text="Book Quantity", font=("arial bold", 12), fg="white", bg="black")
                issueQuantityEntry = Entry(issueBookWindow)
                remainQuantity = Label(issueBookWindow, text="current Quantity", font=("arial bold", 16), fg="white",
                                      bg="green")
                q = Label(issueBookWindow, text="0", font=("arial bold", 16), fg="white",
                                       bg="black")

                returnBook = Label(issueBookWindow, text="Books Return Date", font=("arial bold", 12), fg="white",
                                      bg="black")
                returnBookEntry= Entry(issueBookWindow)
                def doSearchy():
                    keyword=searcBookfield.get()
                    if keyword=="":
                        Error.configure(text="Search Field is Empty....!",fg="white",bg="red")
                        return
                    if not keyword.isdigit():
                        #print("yesss")
                        Error.configure(text="Search Support only Reg_No!", fg="white", bg="red")
                        Error.pack()
                        return
                    Error.forget()
                    c = con.cursor()
                    c.execute(" select*from Books  where rgNo=? ;", (keyword,))
                    resut = c.fetchall()
                    if len(resut)==0:
                        Error.configure(text="No Record Found Related to this Reg_no!", fg="white", bg="red")
                        Error.pack()
                        return
                    Error.forget()
                    dataStr = "null"
                    o = []
                    for y in resut:
                        o.append(list(y))

                    regNoEntry.delete(0,'end')
                    booNameEntry.delete(0,'end')
                    regNoEntry.insert(0,y[0])
                    booNameEntry.insert(0,y[1])
                    q.configure(text=y[4])
                #end
                #issueFuntion
                def doIssue():
                    regNo=regNoEntry.get()
                    bookName=booNameEntry.get()
                    borrowUserName=userNameEntry.get()
                    quantity=issueQuantityEntry.get()
                    returnDate=returnBookEntry.get()
                    issuedDate=str(datetime.today().strftime('%Y-%m-%d'))
                    if regNo=="" or bookName=="" or borrowUserName=="" or quantity=="" or returnDate=="" :
                        Error.configure(text="Some Fields remain Empty...!",fg="white",bg="red")
                        Error.pack()
                        return
                    Error.forget()
                    if not regNo.isdigit():
                        Error.configure(text="Reg_No can not Alphabet...!", fg="white", bg="red")
                        Error.pack()
                        return
                    Error.forget()
                    if not quantity.isdigit():
                        Error.configure(text="Quantity can not Alphabet...!", fg="white", bg="red")
                        Error.pack()
                        return
                    Error.forget()


                    Error.forget()
                    c = con.cursor()
                    c.execute(" select*from users  where username=? ;", (borrowUserName,))
                    resut = c.fetchall()
                    if len(resut) == 0:
                        Error.configure(text="No Record Found Related to this Username!", fg="white", bg="red")
                        Error.pack()
                        return
                    Error.forget()
                    c = con.cursor()
                    c.execute(" select*from Books  where rgNO=?;", (regNo,))
                    resutc = c.fetchall()
                    o = []
                    for y in resutc:
                        o.append(list(y))

                    crurrentQ = o[0][4]
                    if int(quantity) > int(crurrentQ):
                        Error.config(text="Quantity OUt of Bound......!", fg="white", bg="red")
                        Error.pack()
                        return
                    Error.forget
                    year=issuedDate
                    year=year.split("-")

                    c = con.cursor()
                    c.execute("insert into issuedBooks(reg_No,bookName,userName,quantity,issueDate,returnDate,status,year) values(?,?,?,?,?,?,?,?)",
                              (int(regNo), bookName, borrowUserName, quantity, issuedDate,returnDate,"Borrowed",year[0]))
                    con.commit()



                    Error.configure(text="Book Issued successfully..!", fg="white", bg="green")
                    Error.pack()
                    acctualQ = int(crurrentQ) - int(quantity)
                    cc = con.cursor()
                    cc.execute("update Books set  quantity=? where rgNO=?",
                               (int(acctualQ),regNo))
                    con.commit()
                    q.configure(text=str(acctualQ))
                def logout():
                    for x in windows:
                        x.destroy()
                    windows.clear()

                #end
                searchBtn = Button(issueBookWindow, text="Search", fg="white", bg="green",command=doSearchy)
                menuBtn = Button(issueBookWindow, text="Log out",font=("arial bold",15), fg="white", bg="green",command=logout)
                issuedBookBtn = Button(issueBookWindow, text="Issue Book", font=("arial bold", 15), fg="white",
                                       bg="green",command=doIssue)

                mainHeading.pack(pady=20)
                Error.pack(pady=5)

                searcBookfield.place(x=10,y=100,width=220,height=25)
                searchBtn.place(x=250,y=100)
                remainQuantity.place(x=1130,y=100)
                q.place(x=1315,y=100)
                regNo.place(x=350,y=250)
                regNoEntry.place(x=650,y=250,width=220,height=30)
                bookName.place(x=350,y=320)
                booNameEntry.place(x=650,y=320,width=220,height=30)
                userName.place(x=350, y=390)
                userNameEntry.place(x=650, y=390, width=220, height=30)
                issueQuantity.place(x=350,y=460)
                issueQuantityEntry.place(x=650,y=460,width=220, height=30)
                returnBook.place(x=350, y=530)
                returnBookEntry.place(x=650, y=530,width=220, height=30)
                issuedBookBtn.place(x=350,y=600)
                menuBtn.place(x=780,y=600)
                issueBookWindow.mainloop()

            #end
            #returnBookFuntion
            def returnBook():
                    issueBookWindow = Tk()
                    windows.append(issueBookWindow)
                    issueBookWindow.geometry("1366x768")
                    issueBookWindow.title("Return Book...........")
                    mainHeading = Label(issueBookWindow, text="Return Book Form....", font=("arial bold", 18),
                                        fg="white", bg="black")
                    Error = Label(issueBookWindow, text="", font=("arial bold", 8))
                    searcBookfield = Entry(issueBookWindow)
                    regNo = Label(issueBookWindow, text="Book Reg_No", font=("arial bold", 12), fg="white", bg="black")
                    regNoEntry = Entry(issueBookWindow)

                    bookName = Label(issueBookWindow, text="Book Name", font=("arial bold", 12), fg="white", bg="black")
                    booNameEntry = Entry(issueBookWindow)
                    userName = Label(issueBookWindow, text="Return Username", font=("arial bold", 12), fg="white",
                                     bg="black")
                    userNameEntry = Entry(issueBookWindow)
                    issueQuantity = Label(issueBookWindow, text="Book Quantity", font=("arial bold", 12), fg="white",
                                          bg="black")
                    issueQuantityEntry = Entry(issueBookWindow)
                    remainQuantity = Label(issueBookWindow, text="current Quantity", font=("arial bold", 16),
                                           fg="white",
                                           bg="green")
                    q = Label(issueBookWindow, text="0", font=("arial bold", 16), fg="white",
                              bg="black")

                    returnBook = Label(issueBookWindow, text="Books return Date", font=("arial bold", 12), fg="white",
                                       bg="black")
                    returnBookEntry = Entry(issueBookWindow)
                    fineLabel= Label(issueBookWindow, text="User Fine", font=("arial bold", 12), fg="white",
                                       bg="green")
                    fineq = Label(issueBookWindow, text="0rps", font=("arial bold", 12), fg="white",
                                      bg="black")

                    def doSearchy():
                        keyword = searcBookfield.get()
                        if keyword == "":
                            Error.configure(text="Search Field is Empty....!", fg="white", bg="red")
                            return
                        if not keyword.isdigit():
                            #print("yesss")
                            Error.configure(text="Search Support only Reg_No!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget()
                        c = con.cursor()
                        c.execute(" select*from Books  where rgNo=? ;", (keyword,))
                        resut = c.fetchall()
                        if len(resut) == 0:
                            Error.configure(text="No Record Found Related to this Reg_no!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget()
                        dataStr = "null"
                        o = []
                        for y in resut:
                            o.append(list(y))

                        regNoEntry.delete(0, 'end')
                        booNameEntry.delete(0, 'end')
                        regNoEntry.insert(0, y[0])
                        booNameEntry.insert(0, y[1])
                        q.configure(text=y[4])

                    # end
                    # issueFuntion
                    def doIssue():
                        regNo = regNoEntry.get()
                        bookName = booNameEntry.get()
                        borrowUserName = userNameEntry.get()
                        quantity = issueQuantityEntry.get()
                        returnDate = returnBookEntry.get()
                        issuedDate = str(datetime.today().strftime('%Y-%m-%d'))
                        if regNo == "" or bookName == "" or borrowUserName == "" or quantity == "" or returnDate == "":
                            Error.configure(text="Some Fields remain Empty...!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget()
                        if not regNo.isdigit():
                            Error.configure(text="Reg_No can not Alphabet...!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget()
                        if not quantity.isdigit():
                            Error.configure(text="Quantity can not Alphabet...!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget()

                        Error.forget()
                        c = con.cursor()
                        c.execute(" select*from users  where username=? ;", (borrowUserName,))
                        resut = c.fetchall()
                        if len(resut) == 0:
                            Error.configure(text="No Record Found Related to this Username!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget()
                        c = con.cursor()
                        c.execute(" select*from Books  where rgNO=?;", (regNo,))
                        resutc = c.fetchall()
                        o = []
                        for y in resutc:
                            o.append(list(y))

                        crurrentQ = o[0][4]
                        if int(quantity) > int(crurrentQ):
                            Error.config(text="Quantity OUt of Bound......!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget
                        c = con.cursor()
                        c.execute(" select returnDate  from issuedBooks where reg_No=? and userName=?", (regNo,borrowUserName))
                        resutc = c.fetchall()
                        if len(resutc)==0:
                            Error.config(text="First Issued Book......!", fg="white", bg="red")
                            Error.pack()
                            return
                        Error.forget()
                        issuedDateBook=resutc[0][0]
                        #print(issuedDateBook)
                        datainSlpitForm=issuedDateBook.split("-")
                        getDate=returnDate.split("-");
                        #print(datainSlpitForm)
                        if int(getDate[0])>int(datainSlpitForm[0]):
                            fineq.configure(text="50rps")
                            c = con.cursor()
                            c.execute("select fine from users   where  username=?",
                                      (borrowUserName,))
                            restt=c.fetchall()
                            previousFine=restt[0][0]
                            con.commit()
                            totalFine=int(previousFine)+50
                            c = con.cursor()
                            c.execute("update issuedBooks set fine=? , retrurnDay=?  where  username=?",
                                      (int(totalFine),returnDate, borrowUserName,))

                            con.commit()


                        else:
                            fineq.configure(text="0rps")
                            c = con.cursor()
                            c.execute("update issuedBooks set fine=? , retrurnDay=?  where  username=?",(int(0), returnDate, borrowUserName,))
                            con.commit()

                        Error.configure(text="Return Issued successfully..!", fg="white", bg="green")
                        Error.pack()
                        acctualQ = int(crurrentQ)+int(quantity)
                        cc = con.cursor()
                        cc.execute("update Books set  quantity=? where rgNO=?",
                                   (int(acctualQ), regNo,))
                        con.commit()

                        # print(resutc)

                        q.configure(text=str(acctualQ))

                    def logout():
                        for x in windows:
                            x.destroy()
                        windows.clear()

                    # end
                    searchBtn = Button(issueBookWindow, text="Search", fg="white", bg="green", command=doSearchy)
                    menuBtn = Button(issueBookWindow, text="Log out", font=("arial bold", 15), fg="white", bg="green",command=logout)
                    issuedBookBtn = Button(issueBookWindow, text="Return Book", font=("arial bold", 15), fg="white",
                                           bg="green", command=doIssue)

                    mainHeading.pack(pady=20
                                     )
                    Error.pack(pady=5)
                    searcBookfield.place(x=10, y=100, width=220, height=25)
                    searchBtn.place(x=250, y=100)
                    remainQuantity.place(x=1130, y=100)
                    q.place(x=1315, y=100)
                    regNo.place(x=350, y=250)
                    regNoEntry.place(x=650, y=250, width=220, height=30)
                    bookName.place(x=350, y=320)
                    booNameEntry.place(x=650, y=320, width=220, height=30)
                    fineLabel.place(x=1000,y=530,width=220,height=30)
                    fineq.place(x=1230,y=530,height=30)
                    userName.place(x=350, y=390)
                    userNameEntry.place(x=650, y=390, width=220, height=30)
                    issueQuantity.place(x=350, y=460)
                    issueQuantityEntry.place(x=650, y=460, width=220, height=30)
                    returnBook.place(x=350, y=530)
                    returnBookEntry.place(x=650, y=530, width=220, height=30)
                    issuedBookBtn.place(x=350, y=600)
                    menuBtn.place(x=780,y=600)
                    issueBookWindow.mainloop()
#------------------------------------------------------------------------------------------------#
            #End
            #==============================================================================ReportFunction==================================================================

            def generateReport():
                generateReportWindow=Tk()
                windows.append(generateReportWindow)
                generateReportWindow.title("Report Generate")
                generateReportWindow.geometry("1366x768")
                reportFrame=Frame(generateReportWindow,width="700",height="560",background="white")
                reportFrame1 = Frame(generateReportWindow, width="200", height="300", background="red")

                mainHeading=Label(generateReportWindow,text="Generate Report Section",font=("arial bold",18),fg="white",bg="green")
                default = StringVar(generateReportWindow)
                cities = {'Daliy Base Report', 'Weekly Base Report', 'Yearly Base Report'}
                default.set("Select Report Type")
                optionManu = OptionMenu(generateReportWindow, default, *cities)
                Errorc=Label(generateReportWindow,text="")
                tv = Treeview(reportFrame)
                tv['columns'] = ('Rg_No', 'Book Name', 'Author Name', 'Price', 'quanitity', 'date')
                tv.column("#0", width=0, minwidth=0)
                tv.column("Rg_No", width=100, minwidth=100)
                tv.column("Book Name", width=100, minwidth=100)
                tv.column("Author Name", width=100, minwidth=100)
                tv.column("Price", width=100, minwidth=100)
                tv.column("quanitity", width=100, minwidth=100)
                tv.column("date", width=100, minwidth=100)

                tv.heading("#0", text="", anchor="w")
                tv.column("#0", anchor="center", width=2)
                tv.column('Rg_No', anchor='center', width=100)
                tv.heading('Rg_No', text='Rg_No', anchor="center")
                tv.heading('Book Name', text='Book Name', anchor="center")
                tv.heading('Author Name', text='Borrowed Name', anchor="center")
                tv.heading('Price', text='Quanitity', anchor="center")
                tv.heading('quanitity', text='Issued Date', anchor="center")
                tv.heading('date', text='Return Date')
                #---------------------------------------------------------------g-----------------------------------------
                tv1 = Treeview(reportFrame)
                tv1['columns'] = ('Rg_No', 'Book Name', 'Borrower Name', 'Price', 'quanitity', 'date')
                tv1.column("#0", width=0, minwidth=0)
                tv1.column("Rg_No", width=100, minwidth=100)
                tv1.column("Book Name", width=100, minwidth=100)
                tv1.column("Borrower Name", width=100, minwidth=100)
                tv1.column("Price", width=100, minwidth=100)
                tv1.column("quanitity", width=100, minwidth=100)
                tv1.column("date", width=100, minwidth=100)

                tv1.heading("#0", text="", anchor="w")
                tv1.column("#0", anchor="center", width=2)
                tv1.column('Rg_No', anchor='center', width=100)
                tv1.heading('Rg_No', text='Rg_No', anchor="center")
                tv1.heading('Book Name', text='Book Name', anchor="center")
                tv1.heading('Borrower Name', text='Borrower Name', anchor="center")
                tv1.heading('Price', text='Quanitity', anchor="center")
                tv1.heading('quanitity', text='Issued Date', anchor="center")
                tv1.heading('date', text='Return Date')

                tv2 = Treeview(reportFrame)
                tv2['columns'] = ('Rg_No', 'Book Name', 'Return UserName', 'Quanitity', 'Issued Date', 'Return Date','Date on Return','Fine')
                tv2.column("#0", width=0, minwidth=0)
                tv2.column("Rg_No", width=80, minwidth=80)
                tv2.column("Book Name", width=100, minwidth=100)
                tv2.column("Return UserName", width=80, minwidth=80)
                tv2.column("Quanitity", width=80, minwidth=80)
                tv2.column("Issued Date", width=80, minwidth=80)
                tv2.column("Return Date", width=80, minwidth=80)
                tv2.column("Date on Return", width=80, minwidth=80)
                tv2.column("Fine", width=80, minwidth=80)

                tv2.heading("#0", text="", anchor="w")
                tv2.column("#0", anchor="center", width=2)
                tv2.column('Rg_No', anchor='center', width=100)
                tv2.heading('Rg_No', text='Rg_No', anchor="center")
                tv2.heading('Book Name', text='Book Name', anchor="center")
                tv2.heading('Return UserName', text='Return UserName', anchor="center")
                tv2.heading('Quanitity', text='Quanitity', anchor="center")
                tv2.heading('Issued Date', text='Issued Date', anchor="center")
                tv2.heading('Return Date', text='Return Date')
                tv2.heading('Date on Return', text='Date on Return')
                tv2.heading('Fine', text='Fine')

                #---------------------------------------------------------------g-----------------------------------------
                starts=Label(reportFrame,text="**********************************************************************",font=("arial bold",18),fg="#bbb2b2",bg="white")
                startsB = Label(reportFrame,text="**********************************************************************",font=("arial bold", 18), fg="#bbb2b2", bg="white")
                startsc = Label(reportFrame,
                                text="**********************************************************************",
                                font=("arial bold", 18), fg="#bbb2b2", bg="white")
                startsD = Label(reportFrame,
                                text="**********************************************************************",
                                font=("arial bold", 18), fg="#bbb2b2", bg="white")

                hashSymblo=["##","##","##","##","##","##"]
                hash1=Label(reportFrame,text="##",font=("arial bold",18),fg="#bbb2b2",bg="white")
                hash2 = Label(reportFrame, text="##", font=("arial bold", 18), fg="#bbb2b2", bg="white")
                hash3 = Label(reportFrame, text="##", font=("arial bold", 18), fg="#bbb2b2", bg="white")
                hash4 = Label(reportFrame, text="##", font=("arial bold", 18), fg="#bbb2b2", bg="white")
                hash5 = Label(reportFrame, text="##", font=("arial bold", 18), fg="#bbb2b2", bg="white")
                hash6 = Label(reportFrame, text="##", font=("arial bold", 18), fg="#bbb2b2", bg="white")
                reportTitle=Label(reportFrame, text="Over all College Library - Report", font=("arial bold", 15), fg="black", bg="white")
                lbAddress=Label(reportFrame, text="Address - Riwind Lahore , Pakistan", font=("arial", 12), fg="black", bg="white")
                ContactUs = Label(reportFrame, text="Contact Us - (92) 42 99 230 140", font=("arial ", 12),
                                  fg="black", bg="white")
                crureentDate=str(datetime.today().strftime('%Y-%m-%d'))

                x = datetime.now()
                crurrentDay=x.strftime("%A")

                dateAndDay=Label(reportFrame,text=crurrentDay+" "+crureentDate, font=("arial", 12), fg="black", bg="white")
                Signature = Label(reportFrame, text="Signature", font=("arial bold ", 12), fg="black",
                                   bg="white")
                issuedBooksCount=Label(reportFrame, text="", font=("arial bold ", 15), fg="black",
                                   bg="white")
                returnBooksCount = Label(reportFrame, text="", font=("arial bold ", 15),
                                         fg="black",
                                         bg="white")
                createdUserCount = Label(reportFrame, text="", font=("arial bold ", 15),
                                         fg="black",
                                         bg="white")
                createddBooksCount = Label(reportFrame, text="", font=("arial bold ", 15),
                                         fg="black",
                                         bg="white")
                reportBadge = Label(reportFrame, text="", font=("arial bold ", 15),
                                           fg="black",
                                           bg="white")

                def doProcess():
                    reportType=default.get()
                    if reportType=="Select Report Type":
                        Errorc.configure(text="Please select Report type",font=("arial bold",10),fg="white",bg="red")
                        return
                    else:
                       Errorc.configure(text="",bg="white")
                def doLoadAll():
                    x = datetime.now()
                    crurrentDay = x.strftime("%A")
                    keyword=default.get()
                    if keyword=="Select Report Type":
                        Errorc.configure(text="Please Select first report type",bg="red",fg="white")

                        return
                    else:
                        Errorc.place_forget()
                    global PressBtn
                    PressBtn = "overall"
                    if keyword=="Daliy Base Report":
#========================================================================ReprtPrint==========================================================================#
                         os.remove("Report.pdf")
                         pdf=canvas.Canvas("Report.pdf")
                         pdf.setTitle("Daliy Report")
                         pdf.setFont("Courier", 18)
                         pdf.drawString(140,800,"Over all Library Managment Report")
                         pdf.setFont("Courier", 11)
                         pdf.drawString(200,770,"Address - Riwind Lahore , Pakistan")
                         pdf.drawString(210,750,"Contac Us - (92) 42 99 230 140")
                         pdf.drawString(25,730,"************************************************************************************")
                         pdf.setFont("Courier", 11)
                         crueentDate=str(datetime.today().strftime('%Y-%m-%d'))
                         pdf.drawString(25,700,str(crurrentDay+" "+crueentDate))
                         pdf.setFont("Courier", 15)
                         pdf.drawString(230,700,str("Daliy Base Report"))
                         pdf.setFont("Courier", 11)
                         pdf.drawString(25,670,"************************************************************************************")
                         pdf.drawString(510,20,"Signature")
                         pdf.drawString(25,0,"************************************************************************************")

#========================================================================End=================================================================================#
                         reportTitle.configure(text="Over all College Library - Report", fg="black", bg="white")
                         tv.place_forget()
                         tv1.place_forget()
                         tv2.place_forget()
                         issuedBooksCount.place(x=35, y=240)
                         returnBooksCount.place(x=35, y=280)
                         createdUserCount.place(x=35, y=320)
                         createddBooksCount.place(x=35, y=360)

                         reportBadge.configure(text="Daliy Base Report")
                         crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                         c=con.cursor()
                         c.execute("select issueDate from issuedBooks where issueDate=? and status=?",(str(crureentDate),"Borrowed"))

                         allrs=c.fetchall()

                         totallIssued=len(allrs)
                         issuedBooksCount.configure(text="overall Issued Books: "+str(totallIssued))


                         pdf.drawString(25, 600, "overall Issued Books: "+str(totallIssued))
                         c = con.cursor()
                         c.execute("select issueDate from issuedBooks where issueDate=? and status=?",
                                   (str(crureentDate), "return"))
                         allrs = c.fetchall()
                         totallReturn = len(allrs)
                         returnBooksCount.configure(text="overall Return Books: "+str(totallReturn))
                         pdf.drawString(25,570,text="overall Return Books: "+str(totallReturn))

                         c = con.cursor()
                         c.execute("select*from users where date=?",(str(crureentDate),))
                         allrsU = c.fetchall()
                         totallReturnU = len(allrsU)
                         createdUserCount.configure(text="overall Register User:  " + str(totallReturnU))
                         pdf.drawString(25,540,"overall Register User:  " + str(totallReturnU))
                         c = con.cursor()
                         c.execute("select*from Books where date=?", (str(crureentDate),))
                         allrsBB = c.fetchall()
                         totallReturnUBB = len(allrsBB)
                         #print(len(allrsBB))
                         createddBooksCount.configure(text="overall Added  Books:  " + str(totallReturnUBB))
                         pdf.drawString(25,510,"overall Added  Books:  " + str(totallReturnUBB))
                         pdf.save()
                    if keyword=="Weekly Base Report":
                        os.remove("WeeklyBaseReport.pdf")
                        pdf = canvas.Canvas("WeeklyBaseReport.pdf")
                        pdf.setTitle("Weekly Base Report")
                        pdf.setFont("Courier", 18)
                        pdf.drawString(140, 800, "Over all Library Managment Report")
                        pdf.setFont("Courier", 11)
                        pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                        pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                        pdf.drawString(25, 730,
                                       "************************************************************************************")
                        pdf.setFont("Courier", 11)
                        crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        pdf.drawString(25, 700, str(crurrentDay + " " + crueentDate))
                        pdf.setFont("Courier", 15)
                        pdf.drawString(230, 700, str("Weekly Base Report"))
                        pdf.setFont("Courier", 11)
                        pdf.drawString(25, 670,
                                       "************************************************************************************")
                        pdf.drawString(510, 20, "Signature")
                        pdf.drawString(25, 0,
                                       "************************************************************************************")
                        reportTitle.configure(text="Over all College Library - Report", fg="black", bg="white")
                        reportBadge.configure(text="weekly Base Report")
                        tv.place_forget()
                        tv1.place_forget()
                        tv2.place_forget()
                        issuedBooksCount.place(x=35, y=240)
                        returnBooksCount.place(x=35, y=280)
                        createdUserCount.place(x=35, y=320)
                        createddBooksCount.place(x=35, y=360)

                        crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        dateArray=crureentDate.split("-")
                        day=int(dateArray[2])
                        days=[]
                        startDay=0
                        for x in range(6):
                            day=day-1
                        #print(day)
                        for y in range(7):
                                days.append(day)
                                day=days[y]+1
                        newList=[]
                        preformat="2020-05-0"
                        preformat2="2020-05-"
                        for z in days:
                            if z<10:
                               newList.append(preformat+str(z))
                            else:
                                newList.append(preformat2 + str(z))

                        count=0
                        for jk in newList:
                            c = con.cursor()
                            c.execute("select * from issuedBooks where issueDate=? and status=?",
                                      (str(jk), "Borrowed"))
                            allrs = c.fetchall()
                            #print(allrs)
                            count = count +len(allrs)
                        issuedBooksCount.configure(text="overall Issued Books: " + str(count))
                        pdf.drawString(25, 600, "overall Issued Books: " + str(count))
                        for jk in newList:
                            c = con.cursor()
                            c.execute("select*from users where date=?",(str(jk),))
                            allrs = c.fetchall()
                            #print(allrs)
                            count = count + len(allrs)
                        createdUserCount.configure(text="overall Register User:  " + str(count))
                        pdf.drawString(25, 570, "overall Register User:  " + str(count))

                        for jk in newList:
                            c = con.cursor()
                            c.execute("select issueDate from issuedBooks where issueDate=? and status=?",
                                   (str(jk), "return"))
                            allrs = c.fetchall()
                            count = count + len(allrs)
                        returnBooksCount.configure(text="overall Return Books:  " + str(count))
                        pdf.drawString(25, 540, text="overall Return Books: " + str(count))



                        for jk in newList:
                            c = con.cursor()
                            c.execute("select*from Books where date=?", (str(jk),))
                            allrs = c.fetchall()
                            count = count + len(allrs)
                        createddBooksCount.configure(text="overall Added Books:  " + str(count))
                        pdf.drawString(25, 510, "overall Added  Books:  " + str(count))
                        pdf.save()
                    def getYearCount(allData):
                            #print(allData)
                            daaa = []
                            cc = 0
                            for x in allData:
                                daaa.append(list(x))
                            daalen = len(daaa)
                            acurateList = []
                            pureCount = []
                            for y in daaa:
                                acurateList.append(y[0])
                            # print(acurateList)
                            strDate = "null-"
                            for x in acurateList:
                                strDate = strDate + str(x + "-")
                            strDate = strDate.split("-")
                            strDate.remove("null")
                            strDate.remove('')
                            pureCount = []
                            for x in strDate:
                                if int(x) == int(getYeart):
                                    pureCount.append(x)
                            getAnum = len(pureCount)
                            return (getAnum)

                    if keyword=="Yearly Base Report":
                           #os.remove("YearBaseReport.pdf")
                           pdf = canvas.Canvas("YearBaseReport.pdf")
                           pdf.setTitle("Year Base Report")
                           pdf.setFont("Courier", 18)
                           pdf.drawString(140, 800, "Over all Library Managment Report")
                           pdf.setFont("Courier", 11)
                           pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                           pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                           pdf.drawString(25, 730,
                                       "************************************************************************************")
                           pdf.setFont("Courier", 11)
                           crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                           pdf.drawString(25, 700, str(crurrentDay + " " + crueentDate))
                           pdf.setFont("Courier", 15)
                           pdf.drawString(230, 700, str("Year  Base Report"))
                           pdf.setFont("Courier", 11)
                           pdf.drawString(25, 670,
                                       "************************************************************************************")
                           pdf.drawString(510, 20, "Signature")
                           pdf.drawString(25, 0,
                                       "************************************************************************************")

                           reportTitle.configure(text="Over all College Library - Report", fg="black", bg="white")
                           reportBadge.configure(text="Yearly Base Report")
                           tv.place_forget()
                           tv1.place_forget()
                           tv2.place_forget()
                           issuedBooksCount.place(x=35, y=240)
                           returnBooksCount.place(x=35, y=280)
                           createdUserCount.place(x=35, y=320)
                           createddBooksCount.place(x=35, y=360)
                           crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                           getYeart=crureentDate.split("-")
                           getYeart=getYeart[0]
                           c = con.cursor()
                           c.execute("select issueDate from issuedBooks where  status='Borrowed'")
                           allrs = c.fetchall()
                           issuedBooksCount.configure(text="overall Issued Books: " + str(getYearCount(allrs)))
                           pdf.drawString(25, 600, "overall Issued Books: " + str(getYearCount(allrs)))
                           c = con.cursor()
                           c.execute("select type from users")
                           allrs = c.fetchall()
                           createdUserCount.configure(text="overall Register User:  " + str(getYearCount(allrs)))
                           pdf.drawString(25, 570, "overall Register User:  " + str(getYearCount(allrs)))
                           c = con.cursor()
                           c.execute("select issueDate from issuedBooks where  status='return'")
                           allrs = c.fetchall()
                           returnBooksCount.configure(text="overall Return Books:  " + str(getYearCount(allrs)))
                           pdf.drawString(25, 540, "overall Return  Books:  " + str(getYearCount(allrs)))
                           c = con.cursor()
                           c.execute("select date from Books")
                           allrs = c.fetchall()
                           createddBooksCount.configure(text="overall Added Books:  " + str(getYearCount(allrs)))
                           pdf.drawString(25, 510, "overall Added  Books:  " + str(getYearCount(allrs)))
                           pdf.save()

                def generateIssueBookReport():
                    x = datetime.now()
                    crurrentDay = x.strftime("%A")
                    global PressBtn
                    PressBtn="issedbooks"


                    reportTitle.configure(text="Issued Books College Library - Report", fg="black", bg="white")
                    reportType = default.get()
                    if reportType == "Select Report Type":
                        Errorc.configure(text="Please select Report type", font=("arial bold", 10), fg="white",
                                         bg="red")
                        return
                    else:
                        Errorc.place_forget()
                    if reportType == "Daliy Base Report":
                        pdf = canvas.Canvas("issuedReport.pdf")
                        pdf.setTitle("Daliy Report")
                        pdf.setFont("Courier", 18)
                        pdf.drawString(140, 800, "Issued Books Library Managment Report")
                        pdf.setFont("Courier", 11)
                        pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                        pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                        pdf.drawString(25, 730,
                                       "************************************************************************************")
                        pdf.setFont("Courier", 11)
                        crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        pdf.drawString(25, 700, str("Sunday" + " " + crueentDate))
                        pdf.setFont("Courier", 15)
                        pdf.drawString(230, 700, str("Daliy Base Report"))
                        pdf.setFont("Courier", 11)
                        pdf.drawString(25, 670,
                                       "************************************************************************************")
                        pdf.drawString(510, 20, "Signature")
                        pdf.drawString(25, 0,
                                       "************************************************************************************")
                        pdf.drawString(25, 600, str("Reg_No    |"))
                        pdf.drawString(100, 600, str("Book Name    |"))
                        pdf.drawString(195, 600, str("Borrowed Name    |"))
                        pdf.drawString(315, 600, str("Quantity    |"))
                        pdf.drawString(400, 600, str("Issued Date    |"))
                        pdf.drawString(510, 600, str("Return  Date    |"))
                        pdf.drawString(25, 590,
                                       "--------------------------------------------------------------------------------------")

                        reportBadge.configure(text="Daliy Base Report")
                        crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        issuedBooksCount.place_forget()
                        returnBooksCount.place_forget()
                        createdUserCount.place_forget()
                        createddBooksCount.place_forget()
                        tv1.place_forget()
                        tv2.place_forget()

                        tv.place(x=50, y=250)

                        c = con.cursor()
                        c.execute("select * from issuedBooks where issueDate=? and status=?",
                                  (str(crureentDate), "Borrowed"))
                        allrs = c.fetchall()
                        dataStr = "null"
                        o = []
                        #print(allrs)
                        for y in allrs:
                            o.append(list(y))
                        olen = len(o)
                        for i in tv.get_children():
                            tv.delete(i)
                        yxy=570
                        for x in range(olen):
                            tv.insert('', 'end', text="", values=(o[x][0], o[x][1], o[x][2], o[x][3], o[x][4], o[x][5]))
                            pdf.drawString(25, yxy, str(o[x][0]))
                            pdf.drawString(100, yxy, str(o[x][1]))
                            pdf.drawString(240, yxy, str(o[x][2]))
                            pdf.drawString(315, yxy, str(o[x][3]))
                            pdf.drawString(400, yxy, str(o[x][4]))
                            pdf.drawString(510, yxy, str(o[x][5]))
                            yxy=yxy-40
                        pdf.save()
                    if reportType == "Weekly Base Report":
                        os.remove("weeklyBaseissuedReport.pdf")
                        pdf = canvas.Canvas("weeklyBaseissuedReport.pdf")
                        pdf.setTitle("Weekly Report")
                        pdf.setFont("Courier", 18)
                        pdf.drawString(140, 800, "Issued Books Library Managment Report")
                        pdf.setFont("Courier", 11)
                        pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                        pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                        pdf.drawString(25, 730,
                                       "************************************************************************************")
                        pdf.setFont("Courier", 11)
                        crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        pdf.drawString(25, 700, str(crurrentDay + " " + crueentDate))
                        pdf.setFont("Courier", 15)
                        pdf.drawString(230, 700, str("Weekly Base Report"))
                        pdf.setFont("Courier", 11)
                        pdf.drawString(25, 670,
                                       "************************************************************************************")
                        pdf.drawString(510, 20, "Signature")
                        pdf.drawString(25, 0,
                                       "************************************************************************************")
                        pdf.drawString(25, 600, str("Reg_No    |"))
                        pdf.drawString(100, 600, str("Book Name    |"))
                        pdf.drawString(195, 600, str("Borrowed Name    |"))
                        pdf.drawString(315, 600, str("Quantity    |"))
                        pdf.drawString(400, 600, str("Issued Date    |"))
                        pdf.drawString(510, 600, str("Return  Date    |"))
                        pdf.drawString(25, 590,
                                       "--------------------------------------------------------------------------------------")

                        reportBadge.configure(text="Weekly Base Report")
                        issuedBooksCount.place_forget()
                        returnBooksCount.place_forget()
                        createdUserCount.place_forget()
                        createddBooksCount.place_forget()
                        tv.place_forget()
                        tv2.place_forget()
                        tv1.place(x=50, y=250)
                        crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        dateArray = crureentDate.split("-")
                        day = int(dateArray[2])
                        days = []
                        startDay = 0
                        for x in range(6):
                            day = day - 1
                        #print(day)
                        for y in range(7):
                            days.append(day)
                            day = days[y] + 1
                        newList = []
                        preformat = "2020-05-0"
                        preformat2 = "2020-05-"
                        for z in days:
                            if z<10:
                               newList.append(preformat + str(z))
                            else:
                                newList.append(preformat2 + str(z))

                        count = 0
                        for jk in newList:
                            #print(jk)
                            c = con.cursor()
                            c.execute("select * from issuedBooks where issueDate=? and status=?",
                                      (str(jk), "Borrowed"))
                            allrs = c.fetchall()
                            #print(allrs)
                            dataStr = "null"
                            o = []
                            for y in allrs:
                                o.append(list(y))
                            olen = len(o)
                            for i in tv1.get_children():
                                tv1.delete(i)
                            yxy=570
                            for x in range(olen):
                                tv1.insert('', 'end', text="",
                                          values=(o[x][0], o[x][1], o[x][2], o[x][3], o[x][4], o[x][5]))
                                pdf.drawString(25, yxy, str(o[x][0]))
                                pdf.drawString(100, yxy, str(o[x][1]))
                                pdf.drawString(240, yxy, str(o[x][2]))
                                pdf.drawString(315, yxy, str(o[x][3]))
                                pdf.drawString(400, yxy, str(o[x][4]))
                                pdf.drawString(510, yxy, str(o[x][5]))

                                yxy = yxy - 40
                        pdf.save()
                    if reportType== "Yearly Base Report":
                            os.remove("yearlyBaseissuedReport.pdf")
                            pdf = canvas.Canvas("yearlyBaseissuedReport.pdf")
                            pdf.setTitle("Yearly Report")
                            pdf.setFont("Courier", 18)
                            pdf.drawString(140, 800, "Issued Books Library Managment Report")
                            pdf.setFont("Courier", 11)
                            pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                            pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                            pdf.drawString(25, 730,
                                       "************************************************************************************")
                            pdf.setFont("Courier", 11)
                            crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                            pdf.drawString(25, 700, str(crurrentDay + " " + crueentDate))
                            pdf.setFont("Courier", 15)
                            pdf.drawString(230, 700, str("Yearly Base Report"))
                            pdf.setFont("Courier", 11)
                            pdf.drawString(25, 670,
                                       "************************************************************************************")
                            pdf.drawString(510, 20, "Signature")
                            pdf.drawString(25, 0,
                                       "************************************************************************************")
                            pdf.drawString(25, 600, str("Reg_No    |"))
                            pdf.drawString(100, 600, str("Book Name    |"))
                            pdf.drawString(195, 600, str("Borrowed Name    |"))
                            pdf.drawString(315, 600, str("Quantity    |"))
                            pdf.drawString(400, 600, str("Issued Date    |"))
                            pdf.drawString(510, 600, str("Return  Date    |"))
                            pdf.drawString(25, 590,
                                       "--------------------------------------------------------------------------------------")

                            reportBadge.configure(text="Year Base Report")
                            issuedBooksCount.place_forget()
                            returnBooksCount.place_forget()
                            createdUserCount.place_forget()
                            createddBooksCount.place_forget()
                            tv.place_forget()
                            tv2.place_forget()
                            tv1.place(x=50, y=250)
                            crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                            dateArray = crureentDate.split("-")
                            day = int(dateArray[0])
                            days = []
                            c = con.cursor()
                            c.execute("select * from issuedBooks where year=? and status=?",
                                          (str(day), "Borrowed"))
                            allrs = c.fetchall()
                            #print(allrs)
                            dataStr = "null"
                            o = []
                            for y in allrs:
                                o.append(list(y))
                                olen = len(o)
                            for i in tv1.get_children():
                                    tv1.delete(i)
                            yxy=570
                            for x in range(olen):
                                    tv1.insert('', 'end', text="",
                                               values=(o[x][0], o[x][1], o[x][2], o[x][3], o[x][4], o[x][5]))
                                    pdf.drawString(25, yxy, str(o[x][0]))
                                    pdf.drawString(100, yxy, str(o[x][1]))
                                    pdf.drawString(240, yxy, str(o[x][2]))
                                    pdf.drawString(315, yxy, str(o[x][3]))
                                    pdf.drawString(400, yxy, str(o[x][4]))
                                    pdf.drawString(510, yxy, str(o[x][5]))

                                    yxy = yxy - 40
                            pdf.save()
                #---------------    ------------------------------------------------------------------------------------------------------------------------------------------------------------#
                def generateReturnBookReport():
                    reportType = default.get()
                    if reportType == "Select Report Type":
                        Errorc.configure(text="Please select Report type", font=("arial bold", 10), fg="white",
                                         bg="red")
                        return
                    else:
                        Errorc.place_forget()
                    reportTitle.configure(text="Return Books College Library - Report", fg="black", bg="white")
                    global PressBtn
                    PressBtn="returnBtn"
                    if reportType == "Daliy Base Report":
                        os.remove("DaliyyBasereturnReport.pdf")
                        pdf = canvas.Canvas("DaliyyBasereturnReport.pdf")
                        pdf.setTitle("Yearly Report")
                        pdf.setFont("Courier", 18)
                        pdf.drawString(140, 800, "Return Books Library Managment Report")
                        pdf.setFont("Courier", 11)
                        pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                        pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                        pdf.drawString(25, 730,
                                       "************************************************************************************")
                        pdf.setFont("Courier", 11)
                        crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        pdf.drawString(25, 700, str(crurrentDay + " " + crueentDate))
                        pdf.setFont("Courier", 15)
                        pdf.drawString(230, 700, str("Daliy Base Report"))
                        pdf.setFont("Courier", 11)
                        pdf.drawString(25, 670,
                                       "************************************************************************************")
                        pdf.drawString(510, 20, "Signature")
                        pdf.drawString(25, 0,
                                       "************************************************************************************")
                        pdf.drawString(25, 600, str("Reg_No    |"))
                        pdf.drawString(100, 600, str("Book Name    |"))
                        pdf.drawString(195, 600, str("Borrowed Name |"))
                        pdf.drawString(300, 600, str("Quantity |"))
                        pdf.drawString(380, 600, str("Issued Date |"))
                        pdf.drawString(470, 600, str("Return  Date |"))
                        pdf.drawString(560, 600, str("Fine"))
                        pdf.drawString(25, 590,
                                       "--------------------------------------------------------------------------------------")

                        reportBadge.configure(text="Daliy Base Report")
                        crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        issuedBooksCount.place_forget()
                        returnBooksCount.place_forget()
                        createdUserCount.place_forget()
                        createddBooksCount.place_forget()
                        tv.place_forget()
                        tv2.place(x=10, y=250)
                        c = con.cursor()
                        c.execute("select * from issuedBooks where issueDate=? and status=?",
                                  (str(crureentDate), "return"))
                        allrs = c.fetchall()
                        print(allrs)
                        dataStr = "null"
                        o = []
                        #print(allrs)
                        for y in allrs:
                            o.append(list(y))
                        olen = len(o)
                        for i in tv2.get_children():
                            tv2.delete(i)
                        xyx=570
                        for x in range(olen):
                            tv2.insert('', 'end', text="", values=(o[x][0], o[x][1], o[x][2], o[x][3], o[x][4], o[x][5],o[x][7],o[x][8]))
                            pdf.drawString(25, xyx, str(o[x][0]))
                            pdf.setFont("Courier", 8)
                            pdf.drawString(100, xyx, str( o[x][1]))
                            pdf.setFont("Courier", 11)
                            pdf.drawString(220, xyx, str(o[x][2]))
                            pdf.drawString(315, xyx, str(o[x][3]))
                            pdf.drawString(380, xyx, str(o[x][4]))
                            pdf.drawString(475, xyx, str(o[x][5]))
                            pdf.drawString(560, xyx, str(o[x][8]))
                            xyx=xyx-40
                        pdf.save()

                    if reportType == "Weekly Base Report":
                        #os.remove("DaliyyBasereturnReport.pdf")
                        pdf = canvas.Canvas("WeeklyBasereturnReport.pdf")
                        pdf.setTitle("Weekly Report")
                        pdf.setFont("Courier", 18)
                        pdf.drawString(140, 800, "Return Books Library Managment Report")
                        pdf.setFont("Courier", 11)
                        pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                        pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                        pdf.drawString(25, 730,
                                       "************************************************************************************")
                        pdf.setFont("Courier", 11)
                        crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        pdf.drawString(25, 700, str(crurrentDay + " " + crueentDate))
                        pdf.setFont("Courier", 15)
                        pdf.drawString(230, 700, str("Weekly Base Report"))
                        pdf.setFont("Courier", 11)
                        pdf.drawString(25, 670,
                                       "************************************************************************************")
                        pdf.drawString(510, 20, "Signature")
                        pdf.drawString(25, 0,
                                       "************************************************************************************")
                        pdf.drawString(25, 600, str("Reg_No    |"))
                        pdf.drawString(100, 600, str("Book Name    |"))
                        pdf.drawString(195, 600, str("Borrowed Name |"))
                        pdf.drawString(300, 600, str("Quantity |"))
                        pdf.drawString(380, 600, str("Issued Date |"))
                        pdf.drawString(470, 600, str("Return  Date |"))
                        pdf.drawString(560, 600, str("Fine"))
                        pdf.drawString(25, 590,
                                       "--------------------------------------------------------------------------------------")

                        reportBadge.configure(text="Weekly Base Report")
                        issuedBooksCount.place_forget()
                        returnBooksCount.place_forget()
                        createdUserCount.place_forget()
                        createddBooksCount.place_forget()
                        tv.place_forget()
                        tv.place_forget()
                        tv2.place(x=10, y=250)
                        crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                        dateArray = crureentDate.split("-")
                        day = int(dateArray[2])
                        days = []
                        startDay = 0
                        for x in range(6):
                            day = day - 1
                        #print(day)
                        for y in range(7):
                            days.append(day)
                            day = days[y] + 1
                        newList = []
                        preformat = "2020-05-0"
                        preformat2 = "2020-05-"
                        for z in days:
                            if z<10:
                               newList.append(preformat + str(z))
                            else:
                                newList.append(preformat2 + str(z))

                        count = 0
                        for jk in newList:
                            #print(jk)
                            c = con.cursor()
                            c.execute("select * from issuedBooks where issueDate=? and status=?",
                                      (str(jk), "return"))
                            allrs = c.fetchall()
                            #print(allrs)
                            dataStr = "null"
                            o = []
                            for y in allrs:
                                o.append(list(y))
                            olen = len(o)
                            for i in tv2.get_children():
                                tv2.delete(i)
                            xyx=570
                            for x in range(olen):
                                tv2.insert('', 'end', text="", values=(o[x][0], o[x][1], o[x][2], o[x][3], o[x][4], o[x][5],o[x][7],o[x][8]))
                                pdf.drawString(25, xyx, str(o[x][0]))
                                pdf.setFont("Courier", 8)
                                pdf.drawString(100, xyx, str(o[x][1]))
                                pdf.setFont("Courier", 11)
                                pdf.drawString(220, xyx, str(o[x][2]))
                                pdf.drawString(315, xyx, str(o[x][3]))
                                pdf.drawString(380, xyx, str(o[x][4]))
                                pdf.drawString(475, xyx, str(o[x][5]))
                                pdf.drawString(560, xyx, str(o[x][8]))
                                xyx = xyx - 40
                        pdf.save()
                    if reportType== "Yearly Base Report":
                            # os.remove("YearlyBasereturnReport.pdf")
                            pdf = canvas.Canvas("YearlyBasereturnReport.pdf")
                            pdf.setTitle("Weekly Report")
                            pdf.setFont("Courier", 18)
                            pdf.drawString(140, 800, "Return Books Library Managment Report")
                            pdf.setFont("Courier", 11)
                            pdf.drawString(200, 770, "Address - Riwind Lahore , Pakistan")
                            pdf.drawString(210, 750, "Contac Us - (92) 42 99 230 140")
                            pdf.drawString(25, 730,
                                       "************************************************************************************")
                            pdf.setFont("Courier", 11)
                            crueentDate = str(datetime.today().strftime('%Y-%m-%d'))
                            pdf.drawString(25, 700, str(crurrentDay + " " + crueentDate))
                            pdf.setFont("Courier", 15)
                            pdf.drawString(230, 700, str("Yearly Base Report"))
                            pdf.setFont("Courier", 11)
                            pdf.drawString(25, 670,
                                       "************************************************************************************")
                            pdf.drawString(510, 20, "Signature")
                            pdf.drawString(25, 0,
                                       "************************************************************************************")
                            pdf.drawString(25, 600, str("Reg_No    |"))
                            pdf.drawString(100, 600, str("Book Name    |"))
                            pdf.drawString(195, 600, str("Borrowed Name |"))
                            pdf.drawString(300, 600, str("Quantity |"))
                            pdf.drawString(380, 600, str("Issued Date |"))
                            pdf.drawString(470, 600, str("Return  Date |"))
                            pdf.drawString(560, 600, str("Fine"))
                            pdf.drawString(25, 590,
                                       "--------------------------------------------------------------------------------------")

                            reportBadge.configure(text="Year Base Report")
                            issuedBooksCount.place_forget()
                            returnBooksCount.place_forget()
                            createdUserCount.place_forget()
                            createddBooksCount.place_forget()
                            tv.place_forget()
                            tv1.place_forget()
                            tv2.place(x=10, y=250)
                            crureentDate = str(datetime.today().strftime('%Y-%m-%d'))
                            dateArray = crureentDate.split("-")
                            day = int(dateArray[0])
                            days = []
                            c = con.cursor()
                            c.execute("select * from issuedBooks where year=? and status=?",
                                          (str(day), "return"))
                            allrs = c.fetchall()
                            #print(allrs)
                            dataStr = "null"
                            o = []
                            for y in allrs:
                                o.append(list(y))
                                olen = len(o)
                            for i in tv2.get_children():
                                    tv2.delete(i)
                            xyx=570
                            for x in range(olen):
                                    tv2.insert('', 'end', text="", values=(o[x][0], o[x][1], o[x][2], o[x][3], o[x][4], o[x][5],o[x][7],o[x][8]))
                                    pdf.drawString(25, xyx, str(o[x][0]))
                                    pdf.setFont("Courier", 8)
                                    pdf.drawString(100, xyx, str(o[x][1]))
                                    pdf.setFont("Courier", 11)
                                    pdf.drawString(220, xyx, str(o[x][2]))
                                    pdf.drawString(315, xyx, str(o[x][3]))
                                    pdf.drawString(380, xyx, str(o[x][4]))
                                    pdf.drawString(475, xyx, str(o[x][5]))
                                    pdf.drawString(560, xyx, str(o[x][8]))
                                    xyx = xyx - 40
                            pdf.save()
                def PrintReport():
                    #print(PressBtn)
                    getType=default.get()
                    if PressBtn=="overall":
                       if getType=="Daliy Base Report":
                            os.system("Report.pdf")
                            return
                       if getType == "Weekly Base Report":
                            os.system("WeeklyBaseReport.pdf")
                            return
                       if getType=="Yearly Base Report":
                           os.system("YearBaseReport.pdf")
                           return
                    if PressBtn=="issedbooks":
                        if getType=="Daliy Base Report":
                            os.system("issuedReport.pdf")
                            return
                        if getType=="Weekly Base Report":
                            os.system("weeklyBaseissuedReport.pdf")
                            return
                        if getType == "Yearly Base Report":
                            os.system("yearlyBaseissuedReport.pdf")
                            return
                    if PressBtn=="returnBtn":
                        if getType=="Daliy Base Report":
                            os.system("DaliyyBasereturnReport.pdf")
                        if getType == "Weekly Base Report":
                            os.system("WeeklyBasereturnReport.pdf")
                        if getType == "Yearly Base Report":
                            os.system("YearlyBasereturnReport.pdf")

                def logout():
                    for x in windows:
                        x.destroy()
                    windows.clear()

                #end
                generateBtn=Button(generateReportWindow,text="Logout",command=logout)
                topLevelReport = Button(generateReportWindow, text="Overl all Report", font=("arial bold", 12),command=doLoadAll)
                issuedBooksReport = Button(generateReportWindow, text="Issued Books Report", font=("arial bold", 12),command=generateIssueBookReport)
                ReturnBooksReport = Button(generateReportWindow, text="Return Books Report", font=("arial bold", 12),command=generateReturnBookReport)
                NewUserReport = Button(generateReportWindow, text="new Created Users Report", font=("arial bold", 12))
                newAddedBooksReport = Button(generateReportWindow, text="new AddedBooks Report",
                                             font=("arial bold", 12))


                LogoutBtn = Button(generateReportWindow, text="Logout", font=("arial bold", 12),command=logout)
                printReport = Button(generateReportWindow, text="Print Report", font=("arial bold", 15),command=PrintReport)

                #elementsAdd
                mainHeading.pack(pady=20)
                optionManu.place(x=10,y=100,width=280)
                generateBtn.place(x=330,y=100)
                Errorc.place(x=400,y=103)
                reportFrame.place(x=400,y=160)
                topLevelReport.place(x=80,y=200)
                issuedBooksReport.place(x=80,y=260)
                ReturnBooksReport.place(x=80,y=320)

                printReport.place(x=1200,y=80)

                starts.place(x=35,y=0)
                hash1.place(x=35,y=20)
                hash2.place(x=35, y=60)
                hash3.place(x=35, y=100)
                hash4.place(x=640,y=20)
                hash5.place(x=640,y=60)
                hash6.place(x=640,y=100)
                startsB.place(x=35, y=130)
                reportTitle.place(x=200,y=20)
                lbAddress.place(x=230,y=60)
                ContactUs.place(x=240,y=100)
                dateAndDay.place(x=35,y=165)
                reportBadge.place(x=300,y=165)
                startsc.place(x=35, y=200)
                Signature.place(x=599,y=520)
                startsD.place(x=35,y=535)
                issuedBooksCount.place(x=35,y=240)
                returnBooksCount.place(x=35,y=280)
                createdUserCount.place(x=35,y=320)
                createddBooksCount.place(x=35,y=360)

                #tv.place(x=50, y=250)

                #end
            def Close():

                   for x in windows:
                       x.destroy()
                   windows.clear()


                   #menuWindow.destroy()

            #==============================================================================End=============================================================================
            createNewUser=Button(adminFrame,text="CREATE NEW USER",font=("bold arial",15),fg="white",bg="green",command=createUser)
            addBook = Button(adminFrame, text="ADD BOOK", font=("bold arial", 15), fg="white", bg="green",command=addBook)
            searchBook = Button(adminFrame, text="SEARCH A BOOK", font=("bold arial", 15), fg="white", bg="green",command=searchBook)
            borrowBook = Button(adminFrame, text="Issue BOOK", font=("bold arial", 15), fg="white", bg="green",command=issueBook)
            returnBook = Button(adminFrame, text="RETURN BOOK", font=("bold arial", 15), fg="white", bg="green",command=returnBook)
            generateReport = Button(adminFrame, text="GENERAE REPORT", font=("bold arial", 15), fg="white", bg="green",command=generateReport)
            logoutBtn = Button(adminFrame, text="LOGOUT", font=("bold arial", 15), fg="white", bg="green",command=Close)

            #addingComponets

            mainHeading.pack(pady=20)
            type.pack()

            adminFrame.pack(pady=100)
            cv.place(x=150,y=20)
            createNewUser.place(x=130,y=110,width=200,height=36)
            addBook.place(x=130,y=160,width=200,height=36)
            searchBook.place(x=130, y=210, width=200, height=36)
            borrowBook.place(x=130, y=260, width=200, height=36)
            returnBook.place(x=130, y=310, width=200, height=36)
            generateReport.place(x=130, y=360, width=200, height=36)
            logoutBtn.place(x=130, y=410, width=200, height=36)

            menuWindow.mainloop()


            #end
        else:
            usermenu = Tk()
            windows.append(usermenu)
            usermenu.geometry("1366x768+0+0")
            usermenu.title("Library Section..")
            adminFrame = Frame(usermenu, width="450", height=350, background="#bbb2b2")
            mainHeading = Label(usermenu, text="Library Section...", font=("bold arial", 18), fg="white", bg="black")
            cv = Label(adminFrame, text="Library Menu...", font=("bold arial", 15), fg="white", bg="black")
            type = Label(usermenu, text="Type:user", font=("bold arial", 8), fg="white", bg="black")
            createNewUser = Button(adminFrame, text="CREATE NEW USER", font=("bold arial", 15), fg="white", bg="green")
            borrowBook = Button(adminFrame, text="BORROW BOOK", font=("bold arial", 15), fg="white", bg="green")
            #----------------=================================================================================================================================
            # userSearchFunction
            def doSearchU():
                searchBookWindow = Tk()
                windows.append(searchBookWindow)
                global serachWindow
                serachWindow=searchBookWindow
                searchBookWindow.title("Search Book...")
                searchBookWindow.geometry("1366x768+0+0")
                mainHeading = Label(searchBookWindow, text="Search Book form", font=("bold arial", 18), fg="white",
                                    bg="black")
                hint = Label(searchBookWindow, text="(Reg_No/BookName,AuthoName)", font=("bold arial", 8), fg="white",
                             bg="green")
                Error = Label(searchBookWindow, text="", font=("bold arial", 8), )

                SearchResults = Label(searchBookWindow, text="", font=("bold arial", 18))
                serachEntry = Entry(searchBookWindow)
                tv = Treeview(searchBookWindow)
                tv['columns'] = ('Rg_No', 'Book Name', 'Author Name', 'Price', 'quanitity', 'date')

                tv.heading("#0", text="", anchor="w")
                tv.column("#0", anchor="center", width=2)
                tv.column('Rg_No', anchor='center', width=100)

                tv.heading('Rg_No', text='Rg_No', anchor="center")
                tv.heading('Book Name', text='Book Name', anchor="center")
                tv.heading('Author Name', text='Author Name', anchor="center")
                tv.heading('Price', text='Price', anchor="center")
                tv.heading('quanitity', text='Quanitity', anchor="center")
                tv.heading('date', text='Registation Date')
                # updateForm

                # function

                # end
                # end
                def doSearch():
                    rm = tv.get_children()
                    for child in rm:
                        tv.delete(child)
                    getKeyword = serachEntry.get()
                    rgNO = 00;
                    if getKeyword.isdigit():
                        rgNO = int(getKeyword)
                    else:
                        rgNO = str(getKeyword)
                    if getKeyword == "":
                        Error.configure(text="Search Filed Empty..!", fg="white", bg="red")
                        return
                    Error.configure(text="", bg="white")
                    c = con.cursor()
                    c.execute(" select*from Books  where rgNo=? or bookName=? or author=?;", (rgNO, rgNO, rgNO,))
                    resut = c.fetchall()
                    dataStr = "null"
                    o = []

                    for y in resut:
                        o.append(list(y))
                    olen = len(o)
                    #print(olen)
                    if len(o) == 0:
                        Error.configure(text="NO Data Exit....!", fg="white", bg="red")
                        return

                    Error.configure(text="", bg="white")

                    for x in range(olen):
                        tv.insert('', 'end', text="", values=(o[x][0], o[x][1], o[x][2], o[x][3], o[x][4], o[x][5]))
                    SearchResults.configure(text="Your Searched Results", fg="white", bg="green")

                    for x in resut:
                        dataStr = x

                    dataStrNew = list(dataStr)
                    i = 1
                    namelist = []
                    i = 0;

                    lene = len(dataStrNew)
                    for x in dataStrNew:
                        pass

                def logout():
                    for x in windows:
                        x.destroy()
                    windows.clear()

                # end
                searchBtn = Button(searchBookWindow, text="Search", fg="white", bg="green", command=doSearch)
                logoutBtn = Button(searchBookWindow, text="Log out ", fg="white",
                                   bg="green",command=logout)

                # elemenstsAdd
                mainHeading.pack(pady=20)
                SearchResults.pack()
                hint.place(x=12, y=75)
                serachEntry.place(x=10, y=100, width=180, height=25)
                searchBtn.place(x=200, y=100)
                logoutBtn.place(x=1190, y=95, width=160, height=36)

                Error.place(x=250, y=104)
                tv.pack(pady=150)
                # end
                searchBookWindow.mainloop()

            # end

            #---------------==================================================================================================================================
            def logout():
                for x in windows:
                    x.destroy()
                windows.clear()
            searchBook = Button(adminFrame, text="SEARCH A BOOK", font=("bold arial", 15), fg="white", bg="green",command=doSearchU)
            logoutBtn = Button(adminFrame, text="LOGOUT", font=("bold arial", 15), fg="white", bg="green",command=logout)
            # addingComponets
            mainHeading.pack(pady=20)
            type.pack()
            adminFrame.pack(pady=120)
            cv.place(x=150, y=20)

            searchBook.place(x=130, y=100, width=200, height=36 )
            logoutBtn.place(x=130, y=150, width=200, height=36)

            usermenu.mainloop()

    #component
        
        #end
        #addingComponent
        #end
        
    else:
        hint.configure(text="wrong username and password provided..!", font=("bold arial", 10), bg="red")


#end
loinBtn=Button(container,text="LogIn",fg="white",bg="green",command=doLogIn)
#end
#addingSection
mainHeading.pack(pady=30)
container.pack(pady=150)
formTitle.place(x=250,y=10,width=320)
hint.place(x=300,y=55)
userNameLabel.place(x=180,y=160)
usernameEntry.place(x=350,y=160,width=220,height=32)
passwordLabel.place(x=180,y=240)
passwordEntry.place(x=350,y=240,width=220,height=32)
loinBtn.place(x=420,y=300,width=150,height=40)
info.place(x=520,y=610)
#end
window.mainloop()