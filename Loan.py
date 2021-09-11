#-------------------------Import Tkinter and SQLite3------------------------

from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3

#-------------------------Creating Window-----------------------------------

window = Tk()
window.configure(background='grey')

#-------------------------Setting Window Size------------------------------

window.geometry('800x650')

#-------------------------Fixing window size-------------------------------

window.resizable(0,0)

#-------------------------Setting Window Title------------------------------

window.title("Application Form")

#-------------------------Setting a heading for Window---------------------

label_0 = Label(window, text="Apply for Loan",relief='solid',width=20,bg='grey',fg='white',font=("bold", 25))
label_0.place(x=240,y=50)

#-------------------------Declaring all variables---------------------------

var_name=StringVar()
var_cnic=StringVar()
var_age=StringVar()
var_gender=StringVar()
var_city=StringVar()
var_contact=StringVar()
var_education=StringVar()
var_segment=StringVar()
var_credit=StringVar()
var_income=StringVar()
var_dependents=StringVar()
var_check_cnic=StringVar()

#------------------------Definig Function for Database----------------------------------

def database(status):
    'This function is for inserting the data of applicant in database named Loan.db.'
    name=var_name.get()
    cnic=var_cnic.get()
    age=var_age.get()
    gender=var_gender.get()
    city=var_city.get()
    contact=var_contact.get()
    education=var_education.get()
    segment=var_segment.get()
    credit=var_credit.get()
    income=var_income.get()
    dependents=var_dependents.get()
    conn = sqlite3.connect('Loan.db')
    with conn:
        cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ApplicantInfo(CNIC TEXT, Name TEXT, Gender TEXT, Age TEXT, Contact TEXT, Education TEXT, Segment TEXT, Income TEXT, Credit TEXT, Dependents TEXT, Status TEXT)')
    cur.execute('INSERT INTO ApplicantInfo(CNIC, Name, Gender, Age, Contact, Education, Segment, Income, Credit, Dependents, Status) VALUES(?,?,?,?,?,?,?,?,?,?,?)',(cnic, name, gender, age, contact, education, segment, income, credit, dependents, status))
    conn.commit()
    
#------------------------Definig Function for Conitnue-------------------------------------

def open_window():
    window3 = Tk()
    window3.title('Application Form')
    window3.geometry('500x500')
    window3.configure(background='grey')
    window3.resizable(0,0)
    window.mainloop()

#------------------------Definig Function for loan status----------------------------------

def loan_status():
    'This function is used to check the conditions of loan approval/not approval status and takes no argument.'
    age=var_age.get()
    segment=var_segment.get()
    credit=var_credit.get()
    income=var_income.get()
    dependents=var_dependents.get()
    if segment=='Salaried' and eval(age) >=21 and eval(age) <=60 and eval(income) >= 25000:
        tkinter.messagebox.showinfo('Message','Congratulations! Your Application Approved')
        database('Approved')
        window.quit()
        open_window()
    elif segment=='Self-Employed' or segment=='Other':
        if eval(age) >=21 and eval(age) <=65 and eval(income)>= 50000:
            tkinter.messagebox.showinfo('Message','Congratulations! Your Application is Approved.')
            database('Approved')
            open_window()
        else:
            tkinter.messagebox.showinfo('Message','Sorry! Your Application got Rejected')
            database('Not Approved')
    else:
        tkinter.messagebox.showinfo('Message','Sorry! Your Application got Rejected')
        database('Not Approved')
        
#------------------------Definig Function for Submit Button----------------------------------
        
def btn_submit():
    'This function is used to check the form that there is no any important information is left blank.'
    name=var_name.get()
    cnic=var_cnic.get()
    age=var_age.get()
    contact=var_contact.get()
    income=var_income.get()
    dependents=var_dependents.get()
    if name=='' or cnic=='' or age=='' or contact=='' or income=='' or dependents=='':  
        tkinter.messagebox.showinfo('Warning','Fill Complete Form!')
    else:
        loan_status()
        
#------------------------Definig Function for Button Check Status----------------------------------

def btn_check_status():
    'This function will search the given cnic in database and wil give applicatn information.'
    cnic=var_cnic.get()
    conn = sqlite3.connect('Loan.db')
    with conn:
        cur = conn.cursor()
    cur.execute('SELECT * FROM ApplicantInfo WHERE CNIC=cnic')
    db=cur.fetchone()
    window2 = Tk()
    window2.title('Application Status')
    window2.geometry('300x250')
    window2.configure(background='grey')
    window2.resizable(0,0)
    label_name = Label(window2, text="NAME:",bg='grey',fg='white',width=10,font=("bold", 12))
    label_name.place(x=20,y=60)
    name = Label(window2, text=db[1],width=15,bg='grey',fg='white',font=("bold", 12))
    name.place(x=100,y=60)
    label_cnic = Label(window2, text="CNIC:",width=10,bg='grey',fg='white',font=("bold", 12))
    label_cnic.place(x=20,y=100)
    cnic = Label(window2, text=db[0],width=15,bg='grey',fg='white',font=("bold", 12))
    cnic.place(x=100,y=100)
    label_status = Label(window2, text="Status:",width=10,bg='grey',fg='white',font=("bold", 12))
    label_status.place(x=20,y=140)
    status = Label(window2, text=db[-1],width=15,bg='grey',fg='white',font=("bold", 12))
    status.place(x=100,y=140)
        

# -------------------------Full name---------------------------------------

label_name = Label(window, text="Full Name",width=20,bg='grey',fg='white',font=("bold", 10))
label_name.place(x=80,y=130)
name = Entry(window,textvar=var_name)
name.place(x=240,y=130)

#---------------------------CNIC-------------------------------------------

label_cnic = Label(window, text="CNIC",width=20,bg='grey',fg='white',font=("bold", 10))
label_cnic.place(x=68,y=180)
cnic = Entry(window,textvar=var_cnic)
cnic.place(x=240,y=180)

#----------------------------Age-------------------------------------------

label_age = Label(window, text="Age",width=20,bg='grey',fg='white',font=("bold", 10))
label_age.place(x=70,y=280)
age = Entry(window,textvar=var_age)
age.place(x=240,y=280)

#----------------------------Gender------------------------------------------

label_gender = Label(window, text="Gender",width=20,bg='grey',fg='white',font=("bold", 10))
label_gender.place(x=70,y=230)
male= Radiobutton(window, text="Male", variable=var_gender,bg='grey',fg='black', value='Male').place(x=235,y=230)
female=Radiobutton(window, text="Female", variable=var_gender,bg='grey',fg='black', value='Female').place(x=290,y=230)

#-----------------------------City------------------------------------------

label_city = Label(window, text="City",width=20,bg='grey',fg='white',font=("bold", 10))
label_city.place(x=70,y=320)
city = Entry(window,textvar=var_city)
city.place(x=240,y=320)

#-----------------------------Contact---------------------------------------------

label_number = Label(window, text="Contact",width=20,bg='grey',fg='white',font=("bold", 10))
label_number.place(x=70,y=360)
number = Entry(window,textvar=var_contact)
number.place(x=240,y=360)

#-----------------------------Education---------------------------------------

label_education = Label(window, text="Education",width=20,bg='grey',fg='white',font=("bold", 10))
label_education.place(x=390,y=130)
education= ttk.Combobox(window,values=["Matriculation","Intermediate",
                                       "Bachelor's","Master's","Phd.","Un-Educated"],textvar=var_education)
education.current(0)
education.place(x=540,y=130)

#-------------------------------Segment-----------------------------------------

label_segment = Label(window, text="Segment",bg='grey',fg='white',width=20,font=("bold", 10))
label_segment.place(x=390,y=180)
segment= ttk.Combobox(window,values=["Salaried","Self-Employed","Other"],textvar=var_segment)
segment.current(0)
segment.place(x=540,y=180)

#--------------------------------Credit--------------------------------------------

label_credit = Label(window, text="Salary Credit Into This Bank? ",width=21,bg='grey',fg='white',font=("bold", 10))
label_credit.place(x=445,y=230)
yes= Radiobutton(window, text="Yes",variable=var_credit,bg='grey',fg='black', value='Yes').place(x=460,y=260)
no=Radiobutton(window, text="No",variable=var_credit,bg='grey',fg='black', value='No').place(x=510,y=260)

#-------------------------------Monthly Income-----------------------------------

label_salary = Label(window, text="Monthly Income(Rs):",width=20,bg='grey',fg='white',font=("bold", 10))
label_salary.place(x=420,y=300)
salary = Entry(window,textvar=var_income)
salary.place(x=590,y=300)

#-------------------------------No. of Dependents------------------------------------

label_dependents = Label(window, text="No. of Dependents:",width=20,bg='grey',fg='white',font=("bold", 10))
label_dependents.place(x=420,y=350)
dependents = Entry(window,textvar=var_dependents)
dependents.place(x=590,y=350)

#-------------------------------Submit Button---------------------------------------

submit= Button(window, text='Submit',width=20,bg='green',fg='white',command=btn_submit).place(x=340,y=430)

#--------------------------------Label For Search---------------------------------------

label_ask = Label(window, text="Already Submitted?",width=20,bg='grey',fg='white',font=("bold", 14))
label_ask.place(x=100,y=480)
label_search_cnic = Label(window, text="Enter CNIC:",width=20,bg='grey',fg='white',font=("bold", 10))
label_search_cnic.place(x=80,y=540)
check_cnic = Entry(window,textvar=var_check_cnic)
check_cnic.place(x=240,y=540)

#----------------------------------Check Status Button--------------------------------------

status_check = Button(window, text='Check Status',width=20,bg='green',fg='white',command=btn_check_status).place(x=340,y=590)

#---------------------------------Main Loop------------------------------------------

window.mainloop()
