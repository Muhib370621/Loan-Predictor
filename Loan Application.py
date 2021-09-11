# -------------------------Import Tkinter and SQLite3------------------------
from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import sqlite3

# -------------------------Creating Window-----------------------------------

window = Tk()
window.configure(background='grey')

# -------------------------Setting Window Size------------------------------

window.geometry('800x550')

# -------------------------Fixing window size-------------------------------

window.resizable(0, 0)

# -------------------------Setting Window Title------------------------------

window.title("Application Form")

# -------------------------Setting a heading for Window---------------------

label_0 = Label(window, text="Apply for Loan", relief='solid', width=20, bg='grey', fg='white', font=("bold", 25))
label_0.place(x=240, y=50)

# -------------------------Declaring all variables---------------------------

var_name = StringVar()
var_cnic = StringVar()
var_age = StringVar()
var_gender = StringVar()
var_city = StringVar()
var_contact = StringVar()
var_education = StringVar()
var_segment = StringVar()
var_credit = StringVar()
var_income = StringVar()
var_dependents = StringVar()
check_cnic = IntVar()
cnic2 = StringVar()
amount_var = StringVar()
period_var = StringVar()

#----------------------------------Function for saving loan info in DB--------------------------------------------------

def loan_db():
    'This function is made for saving loan details into Loaninfo table in Loan database.'
    cnic1 = cnic2.get()
    amount1 = amount_var.get()
    period1 = period_var.get()
    conn = sqlite3.connect('Loan.db')
    ask = tkinter.messagebox.askquestion('Message', 'Are you confirm?')
    if ask == 'yes':
        if cnic1 == '' or amount1 == '' or len(cnic1) != 13:
            tkinter.messagebox.showerror('Warning', 'Fill Complete Form!')
        else:
            with conn:
                cur = conn.cursor()
            cur.execute('CREATE TABLE IF NOT EXISTS LoanInfo(CNIC INEGER PRIMARY KEY, Amount REAL, Period INTEGER)')
            cur.execute('INSERT INTO LoanInfo(CNIC, Amount, Period) Values(?, ?, ?)', (cnic1, amount1, period1))
            conn.commit()
            tkinter.messagebox.showinfo('Message', 'Form Submitted Succesfully!')
        return
    else:
        tkinter.messagebox.showinfo('Message', 'Submission Cancelled!')

# ------------------------Defining Function for Continue-----------------------------------

def open_window():
    'This functon opens new window for loan details and it is binded with continue button.'
    window3 = Toplevel()
    window3.geometry('800x650')
    window3.configure(background='Grey')
    window3.title('Application Form')
    window3.resizable(0, 0)
    label_1 = Label(window3, text="Loan Details", relief='solid', width=20, bg='grey', fg='white', font=("bold", 25))
    label_1.place(x=240, y=50)
    ###-----------------------------------------------------------------
    Label(window3, text="Enter CNIC", width=20, bg='grey', fg='white', font=("bold", 10)).place(x=80, y=130)
    Entry(window3, textvar=cnic2).place(x=240, y=130)
    ###-----------------------------------------------------------------
    label_reason = Label(window3, text="What is the main purpose of your loan?", width=30, bg='grey', fg='white',
                         font=("bold", 10))
    label_reason.place(x=119, y=180)
    check1 = Checkbutton(window3, text="Home Improvement", bg='grey', fg='Black').place(x=125, y=210)
    check2 = Checkbutton(window3, text="Child Education Fee", bg='grey', fg='Black').place(x=125, y=240)
    check3 = Checkbutton(window3, text="Wedding Expenses", bg='grey', fg='Black').place(x=125, y=270)
    check4 = Checkbutton(window3, text="Debt Consolidation", bg='grey', fg='Black').place(x=125, y=300)
    check5 = Checkbutton(window3, text="Buying Household Items", bg='grey', fg='Black').place(x=125, y=330)
    check6 = Checkbutton(window3, text="Going On Vacation", bg='grey', fg='Black').place(x=125, y=360)
    check7 = Checkbutton(window3, text="Buying Another Car", bg='grey', fg='Black').place(x=125, y=390)
    check8 = Checkbutton(window3, text="Purchasing Property", bg='grey', fg='Black').place(x=125, y=420)
    check9 = Checkbutton(window3, text="Business Startup", bg='grey', fg='Black').place(x=125, y=450)
    ###-----------------------------------------------------------------
    label_amount = Label(window3, text="How much do you want to borrow?", width=30, bg='grey', fg='white',
                         font=("bold", 10))
    label_amount.place(x=450, y=130)

    Entry(window3, textvar=amount_var).place(x=473, y=165)
    Label(window3, text="In PKR", width=5, bg='grey', fg='white', font=("bold", 10)).place(x=620, y=165)
    ###-----------------------------------------------------------------
    label_period = Label(window3, text="Select the Loan Period:", width=20, bg='grey', fg='white', font=("bold", 10))
    label_period.place(x=460, y=205)
    period = ttk.Combobox(window3, values=["12", "24", "36", "48", "60"], width=10, textvar=period_var)
    period.current(0)
    period.place(x=480, y=240)
    Label(window3, text="Months", width=7, bg='grey', fg='white', font=("bold", 10)).place(x=580, y=240)
    ###-----------------------------------------------------------------
    label_agreement = Label(window3, text="Declarations:", width=10, bg='grey', fg='Black', font=("bold", 12))
    label_agreement.place(x=400, y=275)

    T = Text(window3, height=11, width=41, bg='grey', fg='white', font=("bold", 10))
    T.place(x=400, y=300)
    T.insert(END,
             "- I declare and confirm that all information stated herein and in other documents provided to the bank by me or"
             ' at my request is true and accurate in all respects. My loan liabilities, to all sources, institutions and persons '
             'have been fully and accurately reported in this application form and there are no liabilities on me other than the '
             'one stated herein. Further, I declare I have not been defaulter of any financial institution in the past, neither in '
             'my personal capacity, not as a proprietor / partner of any business concern.')
    T.configure(state='disabled')
    check_agreement = Checkbutton(window3, text="I agree the terms and conditions.", bg='grey', fg='Black').place(x=400,
                                                                                                                  y=490)
    ###-----------------------------------------------------------------
    final_submit = Button(window3, text='Submit', width=20, bg='green', fg='white', command=loan_db).place(x=340, y=540)

    window3.mainloop()

# ------------------------Defining Function for Database----------------------------------

def database(status):
    'This function is for inserting the data of applicant in database named Loan.db.'
    name = var_name.get()
    cnic = var_cnic.get()
    age = var_age.get()
    gender = var_gender.get()
    city = var_city.get()
    contact = var_contact.get()
    education = var_education.get()
    segment = var_segment.get()
    credit = var_credit.get()
    income = var_income.get()
    dependents = var_dependents.get()
    conn = sqlite3.connect('Loan.db')
    with conn:
        cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS ApplicantInfo(CNIC INTEGER PRIMARY KEY, Name TEXT, Gender TEXT, Age TEXT, Contact TEXT, Education TEXT, Segment TEXT, Income TEXT, Credit TEXT, Dependents TEXT, Status TEXT)')
    cur.execute(
        'INSERT INTO ApplicantInfo(CNIC, Name, Gender, Age, Contact, Education, Segment, Income, Credit, Dependents, Status) VALUES(?,?,?,?,?,?,?,?,?,?,?)',
        (cnic, name, gender, age, contact, education, segment, income, credit, dependents, status))
    conn.commit()

# ------------------------Definig Function for application status----------------------------------

def app_status():
    'This function is used to check the conditions of loan application approval/not approval status and takes no argument.'
    age = var_age.get()
    segment = var_segment.get()
    income = var_income.get()
    if segment == 'Salaried' and eval(age) >= 21 and eval(age) <= 60 and eval(income) >= 25000:
        database('Approved')
        open_window()
    elif segment == 'Self-Employed' or segment == 'Other':
        if eval(age) >= 21 and eval(age) <= 65 and eval(income) >= 50000:
            database('Approved')
            open_window()
        else:
            tkinter.messagebox.showinfo('Message', 'Sorry! Your Application got Rejected')
            database('Not Approved')
    else:
        tkinter.messagebox.showinfo('Message', 'Sorry! Your Application got Rejected')
        database('Not Approved')

# ------------------------Definig Function for Submit Button----------------------------------

def btn_continue():
    'This function is used to check the form that there is no any important information is left blank.'
    name = var_name.get()
    cnic = var_cnic.get()
    age = var_age.get()
    contact = var_contact.get()
    income = var_income.get()
    dependents = var_dependents.get()
    ask = tkinter.messagebox.askquestion('Message', 'Are you confirm?')
    if ask == 'yes':
        if name == '' or cnic == '' or age == '' or contact == '' or income == '' or dependents == '':
            tkinter.messagebox.showerror('Warning', 'Fill Complete Form!')
        else:
            app_status()
        return
    else:
        tkinter.messagebox.showinfo('Message', 'Submission Cancelled!')

# -------------------------------Function for checking status in applicantinfo DB----------------------------------------------

def btn_check_status():
    'This function will search the given cnic in database and wil give applicatn information.'
    ccnic = check_cnic.get()
    conn = sqlite3.connect('Loan.db')
    cur = conn.cursor()
    cur.execute('SELECT CNIC FROM ApplicantInfo')
    data = cur.fetchall()
    cnic_list = ()
    print(ccnic)
    for one in data:
        cnic_list += one
    print(cnic_list)
    if ccnic not in cnic_list:
        tkinter.messagebox.showinfo('Message', 'No Record Found!')
    else:
        cur.execute('SELECT * FROM ApplicantInfo WHERE CNIC=cnic')
        db = cur.fetchone()
        window2 = Tk()
        window2.title('Application Status')
        window2.geometry('300x250')
        window2.configure(background='grey')
        window2.resizable(0, 0)
        Label(window2, text="NAME:", bg='grey', fg='white', width=10, font=("bold", 12)).place(x=20, y=60)

        Label(window2, text=db[1], width=15, bg='grey', fg='white', font=("bold", 12)).place(x=100, y=60)

        Label(window2, text="CNIC:", width=10, bg='grey', fg='white', font=("bold", 12)).place(x=20, y=100)

        Label(window2, text=db[0], width=15, bg='grey', fg='white', font=("bold", 12)).place(x=100, y=100)

        Label(window2, text="Status:", width=10, bg='grey', fg='white', font=("bold", 12)).place(x=20, y=140)

        Label(window2, text=db[-1], width=15, bg='grey', fg='white', font=("bold", 12)).place(x=100, y=140)

# ------------------------Function for opening menu window----------------------------------

def open_menu():
    window3 = Tk()
    window3.title('Status')
    window3.configure(background='grey')
    window3.resizable(0, 0)
    window3.geometry('300x200')
    label_ask = Label(window3, text="Enter CNIC to check status:", width=20, bg='grey', fg='white', font=("bold", 12))
    label_ask.place(x=30, y=40)
    #global check_cnic
    Entry(window3,textvar=check_cnic).place(x=30, y=80)

    Button(window3, text='Check Status', width=10, bg='green', fg='white',
           command=btn_check_status).place(x=105, y=130)

    window3.mainloop()

# ---------------------------Menu Bar---------------------------------------

menu = Menu(window)
window.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='Already Submitted?', menu=filemenu)
filemenu.add_command(label='Check Status', command=open_menu)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.destroy)

# -------------------------Full name---------------------------------------

label_name = Label(window, text="Full Name", width=20, bg='grey', fg='white', font=("bold", 10))
label_name.place(x=80, y=130)
Entry(window, textvar=var_name).place(x=240, y=130)

# ---------------------------CNIC-------------------------------------------

label_cnic = Label(window, text="CNIC", width=20, bg='grey', fg='white', font=("bold", 10))
label_cnic.place(x=68, y=180)
Entry(window, textvar=var_cnic).place(x=240, y=180)

# ----------------------------Age-------------------------------------------

label_age = Label(window, text="Age", width=20, bg='grey', fg='white', font=("bold", 10))
label_age.place(x=70, y=280)
Entry(window, textvar=var_age).place(x=240, y=280)

# ----------------------------Gender------------------------------------------

label_gender = Label(window, text="Gender", width=20, bg='grey', fg='white', font=("bold", 10))
label_gender.place(x=70, y=230)
Radiobutton(window, text="Male", variable=var_gender, bg='grey', fg='black', value='Male').place(x=235, y=230)
Radiobutton(window, text="Female", variable=var_gender, bg='grey', fg='black', value='Female').place(x=290,
                                                                                                              y=230)

# -----------------------------City------------------------------------------

label_city = Label(window, text="City", width=20, bg='grey', fg='white', font=("bold", 10))
label_city.place(x=70, y=320)
Entry(window, textvar=var_city).place(x=240, y=320)

# -----------------------------Contact---------------------------------------------

label_number = Label(window, text="Contact", width=20, bg='grey', fg='white', font=("bold", 10))
label_number.place(x=70, y=360)
Entry(window, textvar=var_contact).place(x=240, y=360)

# -----------------------------Education---------------------------------------

label_education = Label(window, text="Education", width=20, bg='grey', fg='white', font=("bold", 10))
label_education.place(x=390, y=130)
education = ttk.Combobox(window, values=["Matriculation", "Intermediate",
                                         "Bachelor's", "Master's", "Phd.", "Un-Educated"], textvar=var_education)
education.current(0)
education.place(x=540, y=130)

# -------------------------------Segment-----------------------------------------

label_segment = Label(window, text="Segment", bg='grey', fg='white', width=20, font=("bold", 10))
label_segment.place(x=390, y=180)
segment = ttk.Combobox(window, values=["Salaried", "Self-Employed MBA ", "Other"], textvar=var_segment)
segment.current(0)
segment.place(x=540, y=180)

# --------------------------------Credit--------------------------------------------

label_credit = Label(window, text="Salary Credit Into This Bank? ", width=21, bg='grey', fg='white', font=("bold", 10))
label_credit.place(x=445, y=230)
Radiobutton(window, text="Yes", variable=var_credit, bg='grey', fg='black', value='Yes').place(x=460, y=260)
Radiobutton(window, text="No", variable=var_credit, bg='grey', fg='black', value='No').place(x=510, y=260)

# -------------------------------Monthly Income-----------------------------------

label_salary = Label(window, text="Monthly Income(Rs):", width=20, bg='grey', fg='white', font=("bold", 10))
label_salary.place(x=420, y=300)
Entry(window, textvar=var_income).place(x=590, y=300)

# -------------------------------No. of Dependents------------------------------------

label_dependents = Label(window, text="No. of Dependents:", width=20, bg='grey', fg='white', font=("bold", 10))
label_dependents.place(x=420, y=350)
Entry(window, textvar=var_dependents).place(x=590, y=350)

# -------------------------------Continue Button---------------------------------------

Button(window, text='Continue', width=20, bg='green', fg='white', command=btn_continue).place(x=340, y=430)

# ---------------------------------Main Loop------------------------------------------

window.mainloop()
