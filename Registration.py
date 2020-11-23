from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import pyttsx3
from PIL import Image, ImageTk
import mysql.connector
import csv
import webbrowser

db = mysql.connector.connect(host="localhost",user="root",passwd="abhignaabhi2000",database="mynewdb")
cur = db.cursor()

def exitt():
    exit()

root = Tk()
root.title("ACE-Artifical Computer Education")
root.geometry("500x760+550+20")
root["bg"]="#cfebed"
root.iconbitmap("C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\ace-logo.ico")

root.resizable(0,0)


my_image = ImageTk.PhotoImage(Image.open("C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\Instructions-01.png"))
img_lab = Label(root,image=my_image,anchor=CENTER)
img_lab.place(x=30,y=100)

label_1 = Label(root,text="ARTIFICIAL COMPUTER EDUCATION",relief="solid",font=('arial',20,"bold")).pack(pady=10)
label_2 = Label(root,text="INSTRUCTIONS",relief="solid",font=('arial',15,"bold")).pack(pady=5)
but_quit = Button(root, text='Close', width=12, bg='red', fg='white', command=exitt).place(x=10,y=730)

#path="C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\background.jpg"

def welcome_voice():
    engine1 = pyttsx3.init()
    engine1.say("Welcome to Artificial Computer Education, Let's ACE it")
    rate = engine1.getProperty('rate')
    # print(rate)
    engine1.setProperty('rate', 90)
    engine1.runAndWait()

welcome_voice()
def insert():
    global Reg_no,regno2,first,sec,dob1,age1,momname1,dadname1,phno1,alno1,ID1,address1,var4
    Reg_no = regno.get()
    first = fn.get()
    sec = ln.get()
    dob1 = dob.get()
    age1 = age.get()
    momname1 = momname.get()
    dadname1 = dadname.get()
    phno1 = phno.get()
    alno1 = alno.get()
    ID1 = ID.get()
    address1 = address.get()
    var4 = radio_var.get()
    #top.attributes("-topmost", "true")
    flag=1
    if first == "" or sec == "" or phno1 == "" or Reg_no == "" or dob1==""or momname1==""or age=="":
        tkinter.messagebox.showerror("Null", "Empty fields to be filled",parent=top)
        flag=0
        top.destroy()
    elif len(phno1)!=10 or len(alno1)!=10:
        tkinter.messagebox.showerror("Error", "Phone Numbe should be of 10 digits",parent=top)
        flag=0
    elif len(age1)>2:
        tkinter.messagebox.showerror("Error","Age should be BETWEEN 10 AND 12!",parent=top)
        flag=0
    sel = "SELECT * FROM ACE_new"
    cur.execute(sel)
    records = cur.fetchall()
    fin = [list(i) for i in records]
    exist=0
    if flag==1:
        for row in fin:
            if Reg_no in row[0]:
                exist=1
                tkinter.messagebox.showinfo("Present","Record exists",parent=top)
                top.destroy()
    if exist==0:
            #registration_number, first_name, last_name, age, dob, mother_name, father_name, phone_number, alternate_numer, email_id, home_address
            ins_sql = "INSERT INTO ACE_new(registration_number, first_name, last_name, age, dob, gender,mother_name,father_name, phone_number, alternate_number, email_id, home_address) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            val_ins = (Reg_no,first,sec,age1,dob1,var4,momname1,dadname1,phno1,alno1,ID1,address1)
            cur.execute(ins_sql, val_ins)
            tkinter.messagebox.showinfo("Congratulations", f"{first} {sec} has signed up successfully!",parent=top)
    db.commit()

    
def okay():
    regno1 = regno.get()
    sel = "SELECT * FROM ACE_new"
    cur.execute(sel)
    records = cur.fetchall()
    fin = [list(i) for i in records]

    tree_frame = Frame(top2)
    tree_frame.pack(pady=100)

    tree_scroll = Scrollbar(tree_frame,orient="horizontal")
    tree_scroll.pack(side=BOTTOM,fill="x")
    my_tree = ttk.Treeview(tree_frame,xscrollcommand=tree_scroll.set)

    tree_scroll.config(command=my_tree.xview)

    my_tree['columns'] = ("registration_number", "first_name", "last_name", "age","dob", "gender","mother_name","father_name", "phone_number", "alternate_number", "email_id", "home_address")
    my_tree.column("#0",width=0,stretch=NO)
    my_tree.column("registration_number",anchor=CENTER,width=120)
    my_tree.column("first_name", anchor=CENTER, width=80)
    my_tree.column("last_name", anchor=CENTER, width=120)
    my_tree.column("age", anchor=CENTER, width=120)
    my_tree.column("dob", anchor=CENTER, width=120)
    my_tree.column("gender", anchor=CENTER, width=120)
    my_tree.column("mother_name", anchor=CENTER, width=120)
    my_tree.column("father_name", anchor=CENTER, width=120)
    my_tree.column("phone_number", anchor=CENTER, width=120)
    my_tree.column("alternate_number", anchor=CENTER, width=120)
    my_tree.column("email_id", anchor=CENTER, width=120)
    my_tree.column("home_address", anchor=CENTER, width=120)


    my_tree.heading("#0",text= "",anchor=W)
    my_tree.heading("registration_number",text="Registration Number",anchor=CENTER)
    my_tree.heading("first_name", text="First Name", anchor=CENTER)
    my_tree.heading("last_name", text="Last Name", anchor=CENTER)
    my_tree.heading("age", text="Age", anchor=CENTER)
    my_tree.heading("dob", text="Date Of Birth", anchor=CENTER)
    my_tree.heading("gender", text="Gender", anchor=CENTER)
    my_tree.heading("mother_name", text="Mother Name", anchor=CENTER)
    my_tree.heading("father_name", text="Father Name", anchor=CENTER)
    my_tree.heading("phone_number", text="Phone Number", anchor=CENTER)
    my_tree.heading("alternate_number", text="Alternate Number", anchor=CENTER)
    my_tree.heading("email_id", text="Email-ID", anchor=CENTER)
    my_tree.heading("home_address", text="Address", anchor=CENTER)
    flag=1
    if regno1 =="":
        tkinter.messagebox.showwarning("Null","Please fill your REGISTRATION NUMBER!",parent=top2)
        flag=0
    my_tree.pack(pady=100)
    count=0
    #if flag==1:
    for row in fin:
            if regno1 in row[0] and flag==1:
                my_tree.insert(parent='',index='end',iid=count,text="", values=row)
                count+=1
                tkinter.messagebox.showinfo("Display",f"{row[0]} details are being displayed!",parent=top2)
def update():
    #print("yes")
    first_name = first.get()
    second_name = second.get()
    my_age = age.get()
    my_dob = dob.get()
    my_gender = gender.get()
    mother_name = mom_name.get()
    father_name = dad_name.get()
    phone_number = phno.get()
    alternate_number = alno.get()
    mail_ID = mail.get()
    home_address = address.get()
    sel1 = "SELECT * FROM ACE_new "
    cur.execute(sel1)
    records = cur.fetchall()
    fin = [list(i) for i in records]
    regno1 = regno.get()
    #top3.attributes("-topmost", "true")
    exist = 0
    for row in fin:
        if regno1 in row[0]:
            exist=1
            sql_up = "UPDATE ACE_new SET first_name = %s, last_name= %s, age= %s, dob= %s, gender= %s,mother_name= %s,father_name= %s, phone_number= %s, alternate_number= %s, email_id= %s, home_address= %s WHERE registration_number =%s"
            values = (first_name,second_name,my_age,my_dob,my_gender,mother_name,father_name,phone_number,alternate_number,mail_ID,home_address,regno1)

            cur.execute(sql_up,values)
            tkinter.messagebox.showinfo("Update","Updated Successfully!",parent=top3)
    if exist==0:
        tkinter.messagebox.showwarning("NULL","Record does not exist")
        top3.destroy()
    db.commit()


def edit():
    global first_name,second_name,my_age,my_dob,gender2,mother_name,father_name,phone_number,alternate_number,mail_ID,home_address,top3
    first_name = StringVar()
    second_name = StringVar()
    my_age = StringVar()
    my_dob = StringVar()
    gender2 = StringVar()
    mother_name= StringVar()
    father_name = StringVar()
    phone_number = StringVar()
    alternate_number = StringVar()
    mail_ID = StringVar()
    home_address = StringVar()
    top3 = Toplevel()
    top3["bg"] = "#cfebed"
    x = root.winfo_x()
    y = root.winfo_y()
    top3.geometry("%dx%d+%d+%d" % (500, 760, x, y))
    regno1 = regno.get()
    top3.resizable(0,0)
    #top2.attributes("-topmost", "true")
    #top3.attributes("-topmost", "true")
    top3.iconbitmap("C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\ace-logo.ico")

    sel2 = "SELECT * FROM ACE_new "
    cur.execute(sel2)
    records = cur.fetchall()
    fin = [list(i) for i in records]
    exist = 0

    global enrty_reg
    label_1 = Label(top3, text="EDIT INFORMATION", relief="solid", font=('arial', 20, "bold")).place(x=90, y=50)
    label_reg = Label(top3, text="Registration Number:", width=20, font=("bold", 10),state="disabled")
    label_reg.place(x=80, y=200)
    enrty_reg = Entry(top3, textvar=regno,state="disabled")
    enrty_reg.place(x=242, y=200)

    global first
    first= Label(top3, text="FirstName :", width=20, font=("bold", 10))
    first.place(x=80, y=240)
    first = Entry(top3, textvar=first_name)
    first.place(x=240, y=242)

    global second
    second = Label(top3, text="LastName :", width=20, font=("bold", 10))
    second.place(x=80, y=280)
    second = Entry(top3, textvar=second_name)
    second.place(x=240, y=282)

    global age
    age = Label(top3, text="Age :", width=20, font=("bold", 10))
    age.place(x=80, y=320)
    age = Entry(top3, textvar=my_age)
    age.place(x=240, y=320)

    global dob
    dob = Label(top3, text="DOB:", width=20, font=('bold', 10))
    dob.place(x=80, y=360)
    dob = Entry(top3, textvar=my_dob)
    dob.place(x=240, y=360)

    global gender
    gender = Label(top3, text="Gender :", width=20, font=("bold", 10))
    gender.place(x=83, y=400)
    gender = Entry(top3,textvar=gender2)
    gender.place(x=240,y=400)

    global mom_name
    mom_name = Label(top3, text="Mother's Name:", width=20, font=('bold', 10))
    mom_name.place(x=82, y=440)
    mom_name = Entry(top3, textvar=mother_name)
    mom_name.place(x=240, y=440)

    global dad_name
    dad_name = Label(top3, text="Father's Name:", width=20, font=('bold', 10))
    dad_name.place(x=82, y=480)
    dad_name = Entry(top3, textvar=father_name)
    dad_name.place(x=240, y=480)

    global phno
    phno = Label(top3, text="Phone Number:", width=20, font=('bold', 10))
    phno.place(x=82, y=520)
    phno = Entry(top3, textvar=phone_number)
    phno.place(x=240, y=520)

    global alno
    alno = Label(top3, text="Alternate Number:", width=20, font=('bold', 10))
    alno.place(x=82, y=560)
    alno = Entry(top3, textvar=alternate_number)
    alno.place(x=240, y=560)

    global mail
    mail = Label(top3, text="Email-ID:", width=20, font=('bold', 10))
    mail.place(x=82, y=600)
    mail = Entry(top3, textvar=mail_ID)
    mail.place(x=240, y=600)

    global address
    address = Label(top3, text="Personal Address:", width=20, font=('bold', 10))
    address.place(x=82, y=640)
    address = Entry(top3, textvar=home_address)
    address.place(x=240, y=640)
    but_submit = Button(top3,text="Update",width=12,bg='green',fg='white',command=update).place(x=150,y=680)
    but_close = Button(top3,text="Close", width=12, bg='red', fg='white', command=top3.destroy).place(x=250, y=680)
    exist=0
    if regno1 == "":
        tkinter.messagebox.showerror("Error", "Enter your REGISTRATION NUMBER to edit/update",parent=top3)
        top3.destroy()
    for row in fin:
        if regno1 in row[0]:
            exist=1
            first.insert(0,row[1])
            second.insert(0, row[2])
            age.insert(0,row[3])
            dob.insert(0,row[4])
            gender.insert(0,row[5])
            mom_name.insert(0, row[6])
            dad_name.insert(0, row[7])
            phno.insert(0, row[8])
            alno.insert(0, row[9])
            mail.insert(0,row[10])
            address.insert(0,row[11])
    if exist == 0 :
        tkinter.messagebox.showerror("Error", "Record does not exist",parent=top3)

def view():
    global regno,top2
    regno = StringVar()
    regno1 = regno.get()
    top2 = Toplevel()
    top2["bg"] = "#cfebed"
    x = root.winfo_x()
    y = root.winfo_y()
    top2.geometry("%dx%d+%d+%d" % (500, 760, x, y))
    top2.resizable(0,0)
    top2.iconbitmap("C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\ace-logo.ico")
    label_1 = Label(top2, text="VIEW INFORMATION", relief="solid", font=('arial', 12, "bold")).place(x=140, y=20)
    label_reg = Label(top2, text="Registration Number:", width=20, font=("bold", 10))
    label_reg.place(x=40, y=70)
    enrty_reg = Entry(top2, textvar=regno)
    enrty_reg.place(x=262, y=70)


    btn2 = Button(top2, text="Close",width=12,bg="red",fg="white",command=top2.destroy).place(x=130, y=680)
    btn1 = Button(top2, text="Check",width=20, bg= "green",fg="white",command=okay).place(x=170, y=580)

    label_reg = Label(top2, text="Registration Number (EDIT):", width=20, font=("bold", 10))
    label_reg.place(x=70, y=620)
    enrty_reg = Entry(top2, textvar=regno)
    enrty_reg.place(x=262, y=620)
    but_edit = Button(top2, text="Edit", width=12, bg="grey", fg="black", command=edit).place(x=280,y=680)




def open1():
    global regno,fn,ln,dob,var,radio_var,imge,age,momname,dadname,phno,alno,ID,address,top
    regno = StringVar()
    fn = StringVar()
    ln = StringVar()
    dob = StringVar()
    age = StringVar()
    momname = StringVar()
    dadname = StringVar()
    phno = StringVar()
    alno = StringVar()
    ID = StringVar()
    address = StringVar()
    radio_var = StringVar()

    top = Toplevel(root)
    top.title("Rgistration Form")
    top["bg"] = "#cfebed"
    top.iconbitmap("C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\ace-logo.ico")
    top.resizable(0,0)
    x= root.winfo_x()
    y= root.winfo_y()
    top.geometry("%dx%d+%d+%d" %(500,760,x,y))

    imge = ImageTk.PhotoImage(Image.open("C:\\Users\\Abhigna\\Desktop\\Mini Project 5th sem\\Team Male.png"))
    lab = Label(top,image=imge).pack()

    label_0 = Label(top, text="Registration form", relief="solid", width=20, font=("arial", 19, "bold"))
    label_0.place(x=90, y=130)

    label_reg = Label(top, text="Registration Number:", width=20, font=("bold", 10))
    label_reg.place(x=80,y=200)
    enrty_reg = Entry(top, textvar=regno)
    enrty_reg.place(x=242,y=200)

    label_1 = Label(top, text="FirstName :", width=20, font=("bold", 10))
    label_1.place(x=80, y=240)
    entry_1 = Entry(top, textvar=fn)
    entry_1.place(x=240, y=242)

    label_2 = Label(top, text="LastName :", width=20, font=("bold", 10))
    label_2.place(x=80, y=280)
    entry_2 = Entry(top, textvar=ln)
    entry_2.place(x=240, y=282)

    label_3 = Label(top, text="Age :", width=20, font=("bold", 10))
    label_3.place(x=80, y=320)
    entry_3 = Entry(top, textvar=age)
    entry_3.place(x=240, y=320)

    label_4 = Label(top, text="DOB:", width=20,font=('bold',10))
    label_4.place(x=80,y=360)
    enrty_4 = Entry(top, textvar = dob)
    enrty_4.place(x=240,y=360)

    label_5 = Label(top, text="Gender :", width=20, font=("bold", 10))
    label_5.place(x=83, y=400)
    # radio_var=StringVar()
    r1 = Radiobutton(top, text="Male", variable=radio_var, value="Male").place(x=240, y=400)  # radio 1
    r2 = Radiobutton(top, text="Female", variable=radio_var, value="Female").place(x=300, y=400)  # radio 2

    label_6 = Label(top, text="Mother's Name:", width=20, font=('bold', 10))
    label_6.place(x=82, y=440)
    enrty_6 = Entry(top, textvar=momname)
    enrty_6.place(x=240, y=440)

    label_7 = Label(top, text="Father's Name:", width=20, font=('bold', 10))
    label_7.place(x=82, y=480)
    enrty_7 = Entry(top, textvar=dadname)
    enrty_7.place(x=240, y=480)

    label_8 = Label(top, text="Phone Number:", width=20, font=('bold', 10))
    label_8.place(x=82, y=520)
    enrty_8 = Entry(top, textvar=phno)
    enrty_8.place(x=240, y=520)

    label_9 = Label(top, text="Alternate Number:", width=20, font=('bold', 10))
    label_9.place(x=82, y=560)
    enrty_9 = Entry(top, textvar=alno)
    enrty_9.place(x=240, y=560)

    label_10 = Label(top, text="Email-ID:", width=20, font=('bold', 10))
    label_10.place(x=82, y=600)
    enrty_10 = Entry(top, textvar=ID)
    enrty_10.place(x=240, y=600)

    label_11 = Label(top, text="Personal Address:", width=20, font=('bold', 10))
    label_11.place(x=82, y=640)
    enrty_11 = Entry(top, textvar=address)
    enrty_11.place(x=240, y=640)

    but_login = Button(top, text='Register', width=12, bg='green', fg='white', command=insert).place(x=130, y=680)
    but_quit = Button(top, text='View', width=12, bg='blue', fg='white', command=view).place(x=280, y=680)
    btn1= Button(top,text="Close",bg="red",fg="white",width=12,command= top.destroy).place(x=130,y=722)
    btn2 = Button(top, text="Next", bg="orange",fg="white",width=12,command=second_win).place(x=280,y=720)



def second_win():
    global regno,var_swim,var_writing,var_sing,var_inst,var_dance,var_dance,var_drama,var_art,var_sports,var_cook,var_story,var_paint,var_draw,var_extra_hobby,var_extra_sports,top1
    top1 = Toplevel()
    top1["bg"] = "#cfebed"
    x = root.winfo_x()
    y = root.winfo_y()
    top1.geometry("%dx%d+%d+%d" % (500, 760, x, y))
    top1.resizable(0,0)
    top1.iconbitmap("C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\ace-logo.ico")
    def save_excel():
        exist = 0
        sel1 = "SELECT * FROM ACE_new "
        cur.execute(sel1)
        records = cur.fetchall()
        fin = [list(i) for i in records]
        regno1 = regno.get()
        var_hobby_get = var_extra_hobby.get()
        var_sports_get = var_extra_sports.get()
        var_writing1 = var_writing.get()
        var_swim1 = var_swim.get()
        var_sing1 = var_sing.get()
        var_inst1 = var_inst.get()
        var_dance1 = var_dance.get()
        var_drama1 = var_drama.get()
        var_art1 = var_art.get()
        var_sports1 = var_sports.get()
        var_cook1 = var_cook.get()
        var_story1 = var_story.get()
        var_paint1 = var_paint.get()
        var_draw1 = var_draw.get()
        flag=1
        if regno1 =="":
            tkinter.messagebox.showerror("Null","Please fill your REGISTRATION NUMBER!",parent=top1)
            flag=0
        for row in fin:
            if regno1 in row[0]:
                exist=1
        if exist == 1 and flag==1:
            with open('final.csv', 'a') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(
                    [regno1, var_swim1, var_writing1, var_sing1, var_inst1, var_dance1, var_drama1, var_art1,
                     var_sports1, var_cook1, var_story1, var_paint1, var_draw1, var_hobby_get, var_sports_get])
                tkinter.messagebox.showinfo("Success", "Your interests, saved successfully!",parent=top1)
            csvfile.close()
        if exist==0:
            tkinter.messagebox.showwarning("Error Message", "Record does not exists!",parent=top1)


    var_extra_hobby = StringVar()
    var_extra_sports = StringVar()
    var_hobby_get = var_extra_hobby.get()
    var_sports_get = var_extra_sports.get()
    regno = StringVar()
    regno1 = regno.get()

    lab1 = Label(top1, text=" CANDIDATE HOBBIES/INTEREST ", relief="solid", font=('arial', 20, "bold")).place(x=20, y=40)
    global enrty_reg
    label_reg = Label(top1, text="Registration Number:", width=20, font=("bold", 15))
    label_reg.place(x=40, y=140)
    enrty_reg = Entry(top1, textvar=regno)
    enrty_reg.place(x=262, y=140,height=30)

    var_swim = BooleanVar()
    var_writing = BooleanVar()
    var_sing = BooleanVar()
    var_inst = BooleanVar()
    var_dance = BooleanVar()
    var_drama = BooleanVar()
    var_art = BooleanVar()
    var_sports = BooleanVar()
    var_cook = BooleanVar()
    var_story = BooleanVar()
    var_paint = BooleanVar()
    var_draw = BooleanVar()


    var_swim1 = var_swim.get()
    regno1 = regno.get()
    var_writing1 = var_writing.get()
    var_sing1 = var_sing.get()
    var_inst1 = var_inst.get()
    var_dance1 = var_dance.get()
    var_drama1 = var_drama.get()
    var_art1 = var_art.get()
    var_sports1 = var_sports.get()
    var_cook1 = var_cook.get()
    var_story1 = var_story.get()
    var_paint1 = var_paint.get()
    var_draw1= var_draw.get()

    global c1
    c1= Checkbutton(top1,text= "Swimming",font=("arial",11),variable=var_swim)
    c1.place(x=50,y=200)
    c1.deselect()

    global c2
    c2 = Checkbutton(top1, text="Creative Writing", font=("arial", 11), variable=var_writing)
    c2.place(x=200, y=200)
    c2.deselect()

    global c3
    c3 = Checkbutton(top1, text="Singing", font=("arial", 11), variable=var_sing)
    c3.place(x=50, y=250)
    c3.deselect()

    global c4
    c4 = Checkbutton(top1, text="Musical Instruments", font=("arial", 11), variable=var_inst)
    c4.place(x=200, y=250)
    c4.deselect()

    global c6
    c6 = Checkbutton(top1, text="Dance", font=("arial", 11), variable=var_dance)
    c6.place(x=50, y=300)
    c6.deselect()

    global c7
    c7 = Checkbutton(top1, text="Drama", font=("arial", 11), variable=var_drama)
    c7.place(x=200, y=300)
    c7.deselect()

    global c8
    c8 = Checkbutton(top1, text="Art", font=("arial", 11), variable=var_art)
    c8.place(x=50, y=350)
    c8.deselect()

    global c9
    c9 = Checkbutton(top1, text="Sports", font=("arial", 11), variable=var_sports)
    c9.place(x=200, y=350)
    c9.deselect()

    global c10
    c10 = Checkbutton(top1, text="Cooking", font=("arial", 11), variable=var_cook)
    c10.place(x=50, y=400)
    c10.deselect()

    global c11
    c11 = Checkbutton(top1, text="Books", font=("arial", 11), variable=var_story)
    c11.place(x=200, y=400)
    c11.deselect()

    global c12
    c12 = Checkbutton(top1, text="Painting", font=("arial", 11), variable=var_paint)
    c12.place(x=50, y=450)
    c12.deselect()

    global c13
    c13 = Checkbutton(top1, text="Drawing", font=("arial", 11), variable=var_draw)
    c13.place(x=200, y=450)
    c13.deselect()

    global extra_hobby
    extra_hobby = Label(top1,text="Do you have any other hobby?",font=("arial",12))
    extra_hobby.place(x=50,y=500)
    extra_hobby = Entry(top1,text=var_extra_hobby,width=35)
    extra_hobby.place(x=50,y=540,height=25)

    global extra_sports
    extra_sports = Label(top1, text="Specify the sport you play: ", font=("arial", 12))
    extra_sports.place(x=50, y=580)
    extra_sports = Entry(top1, text=var_extra_sports, width=35)
    extra_sports.place(x=50, y=620, height=25)


    btn1 = Button(top1, text="Close", bg="red", fg="white", width=12, command=top1.destroy).place(x=190, y=722)
    btn_excel = Button(top1,text="Save",bg="green",fg="white",width=12,command=save_excel).place(x=190,y=680)
    btn_next = Button(top1,text="Next",bg="orange",fg="black",width=12,command=choice_win).place(x=380,y=720)

def save_choice():
    global var_code2,var_essay2,var_drama2,regno_choice

    exist=0
    sel_main = "SELECT * FROM ACE_new"
    cur.execute(sel_main)
    records_main = cur.fetchall()
    fin_main = [list(i) for i in records_main]

    exist_choice = 0
    sel_choice = "SELECT * FROM choice1 "
    cur.execute(sel_choice)
    records_choice = cur.fetchall()
    fin_choice = [list(j) for j in records_choice]
    regno_choice = regno.get()
    #print(regno_choice)

    var_code2 = var_code.get()
    var_essay2 = var_essay.get()
    var_drama2 = var_drama.get()
    #print(var_code2)
    #print(var_essay2)
    #print(var_drama2)

    flag = 1
    if regno_choice == "":
        tkinter.messagebox.showerror("Null", "Please fill your REGISTRATION NUMBER!", parent=top4)
        flag = 0
    elif var_code2 ==" " or var_essay2=="" or var_drama2=="":
        tkinter.messagebox.showerror("Null","Please fill the required details",parent=top4)

    for row in fin_main:
        if regno_choice in row[0]:
            exist = 1
    if exist==1 and flag==1:

        for row in fin_choice:
            if regno_choice in row[0]:
                #print(row1[0],row[0])
                exist_choice = 1
                tkinter.messagebox.showwarning("Error Message", "Your interests have already been stored!", parent=top4)
    if exist==0:
        tkinter.messagebox.showwarning("Error","Record Does not exist",parent=top4)
    if exist_choice==0 and exist==1 and flag==1:
        ins_choice = "INSERT INTO choice1(registration_number,code_computer,writing,drama) VALUES(%s,%s,%s,%s)"
        val_choice = (regno_choice,var_code2,var_essay2,var_drama2)
        cur.execute(ins_choice, val_choice)
        tkinter.messagebox.showinfo("Success", "Interests saved successfully", parent=top4)
    db.commit()

def choice_win():
    global var_code,var_essay,var_drama,top4,regno
    top4 = Toplevel()
    x = root.winfo_x()
    y = root.winfo_y()
    top4["bg"] = "#cfebed"
    top4.geometry("%dx%d+%d+%d" % (500, 760, x, y))
    top4.iconbitmap("C:\\Users\\Abhigna\\PycharmProjects\\ABHIASH\\venv\\ace-logo.ico")
    top4.resizable(0, 0)
    top4_label=Label(top4,text="CHOICE OF INTEREST",relief="solid",font=('arial',22,"bold")).place(x=97,y=40)
    regno = StringVar()

    note_lab = Label(top4,text="***NOTE: Please enter yes or no to choose your interest***",font=("arial",10,"bold")).place(x=70,y=190)

    var_code = StringVar()
    var_essay = StringVar()
    var_drama = StringVar()

    code = Label(top4, text="Coding and Computer :", width=20, font=("arial", 11,"bold"))
    code.place(x=80, y=242)
    code= Entry(top4, textvar=var_code)
    code.place(x=265, y=242, height=30)

    writte = Label(top4, text="Creative Writing:", width=20, font=("arial", 11,"bold"))
    writte.place(x=80, y=282)
    writte = Entry(top4, textvar=var_essay)
    writte.place(x=265, y=282, height=30)

    act = Label(top4, text="Drama :", width=20, font=("arial", 11,"bold"))
    act.place(x=80, y=320)
    act = Entry(top4, textvar=var_drama)
    act.place(x=265, y=320, height=30)

    label_reg = Label(top4, text="Registration Number:", width=20, font=("bold", 15))
    label_reg.place(x=50, y=140)
    enrty_reg = Entry(top4, textvar=regno)
    enrty_reg.place(x=265, y=140, height=30)
    btn_choice = Button(top4,text="Save Choice",bg='green',fg='white',width=12,command=save_choice).pack(pady=10,side=BOTTOM)
    btn_close = Button(top4,text="Close",bg="red",fg="white",width=12,command=top4.destroy).pack(pady=5,side=BOTTOM)

    btn_next = Button(top4,text="Next",bg="orange",fg="black",width=8,font=('arial',10,'bold'),command=test_choice).place(x=420,y=720)

def voice():
    engine = pyttsx3.init()
    engine.say("Thank you for visiting artificial computer education, Let's ACE it ")
    rate = engine.getProperty('rate')
    # print(rate)
    engine.setProperty('rate', 150)
    engine.runAndWait()


def test_choice():
    global regno
    top5 = Toplevel()
    x = root.winfo_x()
    y = root.winfo_y()
    top5.resizable(0,0)
    top5["bg"] = "#cfebed"
    top5.geometry("%dx%d+%d+%d" % (500, 760, x, y))
    regno = StringVar()
    sel1 = "SELECT * FROM ACE_new "
    cur.execute(sel1)
    records = cur.fetchall()
    fin = [list(i) for i in records]

    def take_test():

        exist = 0
        sel_choice = "SELECT * FROM choice1 "
        cur.execute(sel_choice)
        records_choice = cur.fetchall()
        fin_choice = [list(j) for j in records_choice]
        regno_choice = regno.get()
        flag=1
        if regno_choice =="":
            tkinter.messagebox.showwarning("Null","Please enter your registration",parent=top5)
            flag =0
        if flag==1:
            for row in fin_choice:
                if regno_choice in row[0]:
                    if row[1]=="yes" or row[1]=="YES" or row[1]=="Yes":
                        exist = 1
                        webbrowser.open("https://forms.gle/M95CdtMz2sqfUsQm6")

        if exist==0:
            tkinter.messagebox.showerror("Error","You have not chosen code and compute as your stream",parent=top5)


    lab1 = Label(top5, text="Test Section", relief="solid", font=('arial', 20, "bold")).place(x=180, y=40)

    label_reg = Label(top5, text="Registration Number:", width=20, font=("bold", 15))
    label_reg.place(x=40, y=140)
    enrty_reg = Entry(top5, textvar=regno)
    enrty_reg.place(x=262, y=140,height=30)


    btn_test = Button(top5,text="Take a Test",width=12,bg="green",fg="white",command=lambda :{take_test(),voice()})
    btn_test.pack(pady=10,side=BOTTOM)
    btn_cls = Button(top5,text="END",width=12,bg="red",fg='white',command=exitt)
    btn_cls.pack(pady=10,side=BOTTOM)

btn = Button(root,text="Next",width=12,bg="orange",fg="white",font=("Arial",10,"bold"),command=open1)
btn.place(x=380,y=730)

mainloop()