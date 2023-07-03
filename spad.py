# CSCI Masters project
# John Hiers


from tkinter import *
from tkinter import ttk
import tkinter as tk

import sqlite3
import os

import pandas as pd


# Main Menu:
# ----------

def main_menu():
    global current_database
    global lbl12
    
    main = tk.Tk()
    
    main.title('(SPAD) Sequel Personal Address Database')
    main.geometry("700x550+20+20")
    main.resizable(False, False)
    
    help1 = tk.Button(main, text="?", command = help_main_menu, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500) 
    
    create1 = tk.Button(main, text="|", command = create, height=1, width=1, relief=tk.RAISED)
    create1.place(x=300, y=20)
    choose2 = tk.Button(main, text="|", command = choose, height=1, width=1, relief=tk.RAISED)
    choose2.place(x=300, y=60)
    add3 = tk.Button(main, text="|", command = add, height=1, width=1, relief=tk.RAISED)
    add3.place(x=300, y=100)
    delete4 = tk.Button(main, text="|", command = delete, height=1, width=1, relief=tk.RAISED)
    delete4.place(x=300, y=140)
    edit5 = tk.Button(main, text="|", command = edit, height=1, width=1, relief=tk.RAISED)
    edit5.place(x=300, y=180)
    view6 = tk.Button(main, text="|", command = view, height=1, width=1, relief=tk.RAISED)
    view6.place(x=300, y=220)
    extra7 = tk.Button(main, text="|", command = extra, height=1, width=1, relief=tk.RAISED)
    extra7.place(x=300, y=260)
    export8 = tk.Button(main, text="|", command = export, height=1, width=1, relief=tk.RAISED)
    export8.place(x=300, y=300)
    custom9 = tk.Button(main, text="|", command = custom, height=1, width=1, relief=tk.RAISED)
    custom9.place(x=300, y=340)
    
    help1 = tk.Button(main, text="|", command = help, height=1, width=1, relief=tk.RAISED)
    help1.place(x=300, y=380)
    
    exit_program10 = tk.Button(main, text="|", command = main.destroy, height=1, width=1, relief=tk.RAISED)
    exit_program10.place(x=300, y=420)

    lbl1 = tk.Label(main, text="Create New Database", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(main, text="Choose Current Database", font=("Helvetica", 10))
    lbl2.place(x=80, y=60)
    lbl3 = tk.Label(main, text="Add Record(s)", font=("Helvetica", 10))
    lbl3.place(x=80, y=100)
    lbl4 = tk.Label(main, text="Delete Record(s)", font=("Helvetica", 10))
    lbl4.place(x=80, y=140)
    lbl5 = tk.Label(main, text="Edit Record(s)", font=("Helvetica", 10))
    lbl5.place(x=80, y=180)
    lbl6 = tk.Label(main, text="View Record(s)", font=("Helvetica", 10))
    lbl6.place(x=80, y=220)
    lbl7 = tk.Label(main, text="Extra Functions", font=("Helvetica", 10))
    lbl7.place(x=80, y=260)
    lbl8 = tk.Label(main, text="Export Data", font=("Helvetica", 10))
    lbl8.place(x=80, y=300)
    lbl9 = tk.Label(main, text="Custom SQL", font=("Helvetica", 10))
    lbl9.place(x=80, y=340)
    lbl10 = tk.Label(main, text="Help", font=("Helvetica", 10))
    lbl10.place(x=80, y=380)
    lbl11 = tk.Label(main, text="Exit Program", font=("Helvetica", 10))
    lbl11.place(x=80, y=420)
    
    lbl11 = tk.Label(main, text=u'\u2022', font=("Helvetica", 10))
    lbl11.place(x=80, y=480)
    
    lbl12 = tk.Label(main, text="Current database:", font=("Helvetica", 10))
    lbl12.place(x=100, y=480)
    
    create1.focus_force()
    main.bind("<Escape>", lambda e: main.destroy())
    
    main.mainloop()
    
def create():
    global create1
    global lbl20
    global lbl21
    global lbl22
    global lbl111
    global lbl211
    global lbl311
    global lbl111b
    global lbl211b
    global lbl311b
    
    global input_database_name1
    global input_database_name2
    global input_database_name3
    
    
    with open("./data.dat", mode='r') as fp:
        input_database_name1_use_title = fp.readline()
        input_database_name2_use_title = fp.readline()
        input_database_name3_use_title = fp.readline()
        
    fp.close()
    
    
    create1 = tk.Tk()
    create1.title('Create New Database')
    create1.geometry("700x550+20+20")
    create1.resizable(False, False)
    
    help1 = tk.Button(create1, text="?", command = help_create1, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    db1 = tk.Button(create1, text="|", command = create_database1, height=1, width=1, relief=tk.RAISED)
    db1.place(x=300, y=20)
    db2 = tk.Button(create1, text="|", command = create_database2, height=1, width=1, relief=tk.RAISED)
    db2.place(x=300, y=60)
    db3 = tk.Button(create1, text="|", command = create_database3, height=1, width=1, relief=tk.RAISED)
    db3.place(x=300, y=100)
    
    lbl1 = tk.Label(create1, text="Create database1.db", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(create1, text="Create database2.db", font=("Helvetica", 10))
    lbl2.place(x=80, y=60)
    lbl3 = tk.Label(create1, text="Create database3.db", font=("Helvetica", 10))
    lbl3.place(x=80, y=100)
    
    lbl20 = tk.Label(create1, text='', font=("Helvetica", 24))
    lbl20.place(x=350, y=10)
    lbl21 = tk.Label(create1, text='', font=("Helvetica", 24))
    lbl21.place(x=350, y=50)
    lbl22 = tk.Label(create1, text='', font=("Helvetica", 24))
    lbl22.place(x=350, y=90)
    
    path = './database1.db'
    check_file1 = os.path.isfile(path)
    
    if check_file1 == TRUE:
        lblcheck1 = tk.Label(create1, text=u'\u25FE', font=("Helvetica", 24))
        lblcheck1.place(x=350, y=10)
    
    path = './database2.db'
    check_file2 = os.path.isfile(path)
    
    if check_file2 == TRUE:
        lblcheck2 = tk.Label(create1, text=u'\u25FE', font=("Helvetica", 24))
        lblcheck2.place(x=350, y=50)
        
    path = './database3.db'
    check_file3 = os.path.isfile(path)
    
    if check_file3 == TRUE:
        lblcheck3 = tk.Label(create1, text=u'\u25FE', font=("Helvetica", 24))
        lblcheck3.place(x=350, y=90)


    lbl100 = tk.Label(create1, text="Name for database1.db", font=("Helvetica", 10))
    lbl100.place(x=80, y=160)

    input_database_name1 = tk.Text(create1, height = 1, width = 25, relief=tk.RAISED)
    input_database_name1.place(x=300, y=160)
    input_database_name1.bind("<Tab>", focus_next_window)
    
    input_database_name2 = tk.Text(create1, height = 1, width = 25, relief=tk.RAISED)
    input_database_name2.place(x=300, y=240)
    input_database_name2.bind("<Tab>", focus_next_window)
    
    input_database_name3 = tk.Text(create1, height = 1, width = 25, relief=tk.RAISED)
    input_database_name3.place(x=300, y=320)
    input_database_name3.bind("<Tab>", focus_next_window)

    edit100 = tk.Button(create1, text="|", command = name1, height=1, width=1, relief=tk.RAISED)
    edit100.place(x=600, y=160)
    
    lbl1111 = tk.Label(create1, text=u'\u2022', font=("Helvetica", 10))
    lbl1111.place(x=80, y=200)
    
    lbl111 = tk.Label(create1, text=input_database_name1_use_title, font=("Helvetica", 10))
    lbl111.place(x=100, y=200)
    
    lbl101 = tk.Label(create1, text="Name for database2.db", font=("Helvetica", 10))
    lbl101.place(x=80, y=240)


    edit101 = tk.Button(create1, text="|", command = name2, height=1, width=1, relief=tk.RAISED)
    edit101.place(x=600, y=240)
    
    lbl1111 = tk.Label(create1, text=u'\u2022', font=("Helvetica", 10))
    lbl1111.place(x=80, y=280)
    
    lbl211 = tk.Label(create1, text=input_database_name2_use_title, font=("Helvetica", 10))
    lbl211.place(x=100, y=280)
    
    
    lbl102 = tk.Label(create1, text="Name for database3.db", font=("Helvetica", 10))
    lbl102.place(x=80, y=320)


    edit102 = tk.Button(create1, text="|", command = name3, height=1, width=1, relief=tk.RAISED)
    edit102.place(x=600, y=320)
    
    lbl1111 = tk.Label(create1, text=u'\u2022', font=("Helvetica", 10))
    lbl1111.place(x=80, y=360)
    
    lbl311 = tk.Label(create1, text=input_database_name3_use_title, font=("Helvetica", 10))
    lbl311.place(x=100, y=360)
    
    lbl103 = tk.Label(create1, text="Clear names", font=("Helvetica", 10))
    lbl103.place(x=80, y=420)

    edit103 = tk.Button(create1, text="|", command = name4, height=1, width=1, relief=tk.RAISED)
    edit103.place(x=300, y=420)
    
    db1.focus_force()
    create1.bind("<Escape>", lambda e: create1.destroy())
    
    
    create1.mainloop()
    
    
def create_database1():
    global create1
    con = sqlite3.connect("database1.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE database(id INTEGER PRIMARY KEY, lastname text, firstname text, address1 text, address2 text, \
                city text, state text, zipcode text, phone1 text, phone2 text, \
                emailaddress text, notes text, contactdate text, confirmation text)""")
    lbl20.config(text=u'\u25FE')
    lbl1111.config(text=u'\u25FE')
    
    con.commit()
    con.close()

def create_database2():
    global create1
    con = sqlite3.connect("database2.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE database(id INTEGER PRIMARY KEY, lastname text, firstname text, address1 text, address2 text, \
                city text, state text, zipcode text, phone1 text, phone2 text, \
                emailaddress text, notes text, contactdate text, confirmation text)""")
    lbl21.config(text=u'\u25FE')
    lbl1112.config(text=u'\u25FE')
    
    con.commit()
    con.close()
    
def create_database3():
    global create1
    con = sqlite3.connect("database3.db") 
    cur = con.cursor()
    cur.execute("""CREATE TABLE database(id INTEGER PRIMARY KEY, lastname text, firstname text, address1 text, address2 text, \
                city text, state text, zipcode text, phone1 text, phone2 text, \
                emailaddress text, notes text, contactdate text, confirmation text)""")
    lbl22.config(text=u'\u25FE')
    lbl1113.config(text=u'\u25FE')
    
    con.commit()
    con.close()

def choose():
    global choose1
    global input_database_name1_use_title
    global input_database_name2_use_title
    global input_database_name3_use_title
    
    global lbl111b
    global lbl211b
    global lbl311b
    global current_database_display
    
    global lbl1111
    global lbl1112
    global lbl1113
    
    with open("./data.dat", mode='r') as fp:
        input_database_name1_use_title = fp.readline()
        input_database_name2_use_title = fp.readline()
        input_database_name3_use_title = fp.readline()
        
    fp.close()
        
    choose1 = tk.Tk()
    choose1.title('Choose Currrent Database - ' + current_database_name)
    choose1.geometry("700x550+20+20")
    choose1.resizable(False, False)
    
    help1 = tk.Button(choose1, text="?", command = help_choose, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    choose11 = tk.Button(choose1, text="|", command = choose_database1, height=1, width=1, relief=tk.RAISED)
    choose11.place(x=300, y=20)
    choose12 = tk.Button(choose1, text="|", command = choose_database2, height=1, width=1, relief=tk.RAISED)
    choose12.place(x=300, y=60)
    choose13 = tk.Button(choose1, text="|", command = choose_database3, height=1, width=1, relief=tk.RAISED)
    choose13.place(x=300, y=100)
    
    lbl1 = tk.Label(choose1, text="Choose database1.db", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(choose1, text="Choose database2.db", font=("Helvetica", 10))
    lbl2.place(x=80, y=60)
    lbl3 = tk.Label(choose1, text="Choose database3.db", font=("Helvetica", 10))
    lbl3.place(x=80, y=100)
        
    
        
    if current_database == "database1.db":
        lblcheck1 = tk.Label(choose1, text=u'\u2713', font=("Helvetica", 24))
        lblcheck1.place(x=350, y=10)
        
    
    if current_database == "database2.db":
        lblcheck2 = tk.Label(choose1, text=u'\u2713', font=("Helvetica", 24))
        lblcheck2.place(x=350, y=50)
        
    if current_database == "database3.db":
        lblcheck3 = tk.Label(choose1, text=u'\u2713', font=("Helvetica", 24))
        lblcheck3.place(x=350, y=90)
        
    
    lbl1111 = tk.Label(choose1, text='', font=("Helvetica", 10))
    lbl1111.place(x=80, y=160)
    lbl1112 = tk.Label(choose1, text='', font=("Helvetica", 10))
    lbl1112.place(x=80, y=200)
    lbl1113 = tk.Label(choose1, text='', font=("Helvetica", 10))
    lbl1113.place(x=80, y=240)
    
    lbl11 = tk.Label(choose1, text="database1.db", font=("Helvetica", 10))
    lbl11.place(x=120, y=160)
    lbl21 = tk.Label(choose1, text="database2.db", font=("Helvetica", 10))
    lbl21.place(x=120, y=200)
    lbl31 = tk.Label(choose1, text="database3.db", font=("Helvetica", 10))
    lbl31.place(x=120, y=240)
    
    lbl111b = tk.Label(choose1, text=input_database_name1_use_title, font=("Helvetica", 10))
    lbl111b.place(x=300, y=160)
    lbl211b = tk.Label(choose1, text=input_database_name2_use_title, font=("Helvetica", 10))
    lbl211b.place(x=300, y=200)
    lbl311b = tk.Label(choose1, text=input_database_name3_use_title, font=("Helvetica", 10))
    lbl311b.place(x=300, y=240)
    
    path = './database1.db'
    check_file1 = os.path.isfile(path)
    
    path = './database2.db'
    check_file2 = os.path.isfile(path)
    
    path = './database3.db'
    check_file3 = os.path.isfile(path)
    
    if check_file1 == TRUE:
        lbl1111 = tk.Label(choose1, text=u'\u25FE', font=("Helvetica", 24))
        lbl1111.place(x=80, y=150)
    
    if check_file2 == TRUE:
        lbl1112 = tk.Label(choose1, text=u'\u25FE', font=("Helvetica", 24))
        lbl1112.place(x=80, y=190)
        
    if check_file3 == TRUE:
        lbl1113 = tk.Label(choose1, text=u'\u25FE', font=("Helvetica", 24))
        lbl1113.place(x=80, y=230)
    
        
    
    
    
    choose11.focus_force()
    choose1.bind("<Escape>", lambda e: choose1.destroy())
    
    choose1.mainloop()
    
def choose_database1():
    global choose1
    global current_database
    global current_database_name
    
    current_database_name = input_database_name1_use_title
    
    path = './database1.db'
    check_file1 = os.path.isfile(path)
    
    if check_file1 == TRUE:
        current_database = "database1.db"
        
        lbl12.config(text="Current database: database1.db - " + current_database_name)
        
    else:
        print("Database not created.")
        not_created1()
    
    choose1.destroy()
    
def choose_database2():
    global choose1
    global current_database
    global current_database_name
    
    current_database_name = input_database_name2_use_title
    
    path = './database2.db'
    check_file2 = os.path.isfile(path)
    
    if check_file2 == TRUE:
        current_database = "database2.db"
        
        lbl12.config(text="Current database: database2.db - " + current_database_name)
      
    else:
        print('Database not created.')
        not_created2()
        
    choose1.destroy()
    
def choose_database3():
    global choose1
    global current_database
    global current_database_name
    
    current_database_name = input_database_name3_use_title
    
    path = './database3.db'
    check_file3 = os.path.isfile(path)
    
    if check_file3 == TRUE:
        current_database = "database3.db"
        
        lbl12.config(text="Current database: database3.db - " + current_database_name)
      
    else:
        print('Database not created.')
        not_created3()
        
    choose1.destroy()
    

def add():
    global current_database
    global input_lastname
    global input_firstname
    global input_address1
    global input_address2
    global input_city
    global input_state
    global input_zipcode
    global input_phone1
    global input_phone2
    global input_email
    
    add1 = tk.Tk()
    add1.title('Add Record(s)')
    add1.geometry("700x550+20+20")
    add1.resizable(False, False)
    
    help1 = tk.Button(add1, text="?", command = help_add, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    lbl1 = tk.Label(add1, text="Last Name", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(add1, text="First Name", font=("Helvetica", 10))
    lbl2.place(x=80, y=60)
    lbl3 = tk.Label(add1, text="Address 1", font=("Helvetica", 10))
    lbl3.place(x=80, y=100)
    lbl4 = tk.Label(add1, text="Address 2", font=("Helvetica", 10))
    lbl4.place(x=80, y=140)
    lbl5 = tk.Label(add1, text="City", font=("Helvetica", 10))
    lbl5.place(x=80, y=180)
    lbl6 = tk.Label(add1, text="State", font=("Helvetica", 10))
    lbl6.place(x=80, y=220)
    lbl7 = tk.Label(add1, text="Zip Code", font=("Helvetica", 10))
    lbl7.place(x=80, y=260)
    lbl8 = tk.Label(add1, text="Phone 1", font=("Helvetica", 10))
    lbl8.place(x=80, y=300)
    lbl9 = tk.Label(add1, text="Phone 2", font=("Helvetica", 10))
    lbl9.place(x=80, y=340)
    lbl10 = tk.Label(add1, text="Email Address", font=("Helvetica", 10))
    lbl10.place(x=80, y=380)
    
    input_lastname = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_lastname.place(x=300, y=20)
    input_lastname.bind("<Tab>", focus_next_window)
    input_firstname = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_firstname.place(x=300, y=60)
    input_firstname.bind("<Tab>", focus_next_window)
    input_address1 = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_address1.place(x=300, y=100)
    input_address1.bind("<Tab>", focus_next_window)
    input_address2 = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_address2.place(x=300, y=140)
    input_address2.bind("<Tab>", focus_next_window)
    input_city = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_city.place(x=300, y=180)
    input_city.bind("<Tab>", focus_next_window)
    input_state = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_state.place(x=300, y=220)
    input_state.bind("<Tab>", focus_next_window)
    input_zipcode = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_zipcode.place(x=300, y=260)
    input_zipcode.bind("<Tab>", focus_next_window)
    input_phone1 = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_phone1.place(x=300, y=300)
    input_phone1.bind("<Tab>", focus_next_window)
    input_phone2 = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_phone2.place(x=300, y=340)
    input_phone2.bind("<Tab>", focus_next_window)
    input_email = tk.Text(add1, height = 1, width = 25, relief=tk.RAISED)
    input_email.place(x=300, y=380)
    input_email.bind("<Tab>", focus_next_window)

    
    
    lbl10 = tk.Label(add1, text="Add Record", font=("Helvetica", 10))
    lbl10.place(x=80, y=440)
    
    add2 = tk.Button(add1, text="|", command = add_record, height=1, width=1, relief=tk.RAISED)
    add2.place(x=300, y=440)
    
    input_lastname.focus_force()
    add1.bind("<Escape>", lambda e: add1.destroy())

    
    
    add1.mainloop()
    
def add_record():
    global input_lastname
    global input_firstname
    global input_address1
    global input_address2
    global input_city
    global input_state
    global input_zipcode
    global input_phone1
    global input_phone2
    global input_email
    
    if current_database != '':
    
        input_lastname_use = input_lastname.get("1.0","end-1c")
        input_firstname_use = input_firstname.get("1.0","end-1c")
        input_address1_use = input_address1.get("1.0","end-1c")
        input_address2_use = input_address2.get("1.0","end-1c")
        input_city_use = input_city.get("1.0","end-1c")
        input_state_use = input_state.get("1.0","end-1c")
        input_zipcode_use = input_zipcode.get("1.0","end-1c")
        input_phone1_use = input_phone1.get("1.0","end-1c")
        input_phone2_use = input_phone2.get("1.0","end-1c")
        input_email_use = input_email.get("1.0","end-1c")
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""INSERT INTO database(lastname, firstname, address1, \
                    address2, city, state, zipcode, phone1, phone2, emailaddress, \
                    notes, contactdate, confirmation) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, '*', '*', '*')""", \
                    (input_lastname_use, input_firstname_use, input_address1_use, input_address2_use, input_city_use, \
                    input_state_use, input_zipcode_use, input_phone1_use, input_phone2_use, input_email_use))
        con.commit()
        con.close()   

        view_all_records()
    else:
        view_all_records()
    
def delete():
    global input_id
    global input_filter_name
    
    delete1 = tk.Tk()
    delete1.title('Delete Record(s)')
    delete1.geometry("700x550+20+20")
    delete1.resizable(False, False)
    
    help1 = tk.Button(delete1, text="?", command = help_delete, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    lbl1 = tk.Label(delete1, text="Delete Record with ID", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    
    lbl2 = tk.Label(delete1, text="Remove Empty Records", font=("Helvetica", 10))
    lbl2.place(x=80, y=80)
    
    lbl3 = tk.Label(delete1, text="Remove Duplicate Records", font=("Helvetica", 10))
    lbl3.place(x=80, y=120)
    
    lbl4 = tk.Label(delete1, text="Count Empty Records", font=("Helvetica", 10))
    lbl4.place(x=80, y=180)
    
    lbl5 = tk.Label(delete1, text="Count Duplicate Records", font=("Helvetica", 10))
    lbl5.place(x=80, y=220)
    
    

    input_id = tk.Text(delete1, height = 1, width = 25, relief=tk.RAISED)
    input_id.place(x=300, y=20)
    input_id.bind("<Tab>", focus_next_window)

    delete2 = tk.Button(delete1, text="|", command = delete_confirm, height=1, width=1, relief=tk.RAISED)
    delete2.place(x=600, y=20)
    
    delete3 = tk.Button(delete1, text="|", command = delete_empty, height=1, width=1, relief=tk.RAISED)
    delete3.place(x=300, y=80)
    
    delete4 = tk.Button(delete1, text="|", command = delete_duplicates, height=1, width=1, relief=tk.RAISED)
    delete4.place(x=300, y=120)
    
    delete5 = tk.Button(delete1, text="|", command = count_empty, height=1, width=1, relief=tk.RAISED)
    delete5.place(x=300, y=180)
    
    delete6 = tk.Button(delete1, text="|", command = count_duplicates, height=1, width=1, relief=tk.RAISED)
    delete6.place(x=300, y=220)
    
    
    view_selected11 = tk.Button(delete1, text="|", command = filter_name, height=1, width=1, relief=tk.RAISED)
    view_selected11.place(x=600, y=280)

    lbl1b = tk.Label(delete1, text="Filter Records by Last Name", font=("Helvetica", 10))
    lbl1b.place(x=80, y=280)

    input_filter_name = tk.Text(delete1, height = 1, width = 25, relief=tk.RAISED)
    input_filter_name.place(x=300, y=280)
    
    
    
    input_id.focus_force()
    delete1.bind("<Escape>", lambda e: delete1.destroy())
    
    delete1.mainloop()
    
def delete_confirm():
    
    if current_database != '':
        input_id_use = input_id.get("1.0","end-1c")
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""DELETE FROM database WHERE id = ?""",(input_id_use, ))
        
        con.commit()
        con.close()
        
        view_all_records()
    else:
        view_all_records()
    
def edit():
    global input_id_edit
    global input_lastname_edit
    global input_firstname_edit
    global input_address1_edit
    global input_address2_edit
    global input_city_edit
    global input_state_edit
    global input_zipcode_edit
    global input_phone1_edit
    global input_phone2_edit
    global input_email_edit
    
    edit1 = tk.Tk()
    edit1.title('Edit Record(s)')
    edit1.geometry("700x550+20+20")
    edit1.resizable(False, False)
    
    help1 = tk.Button(edit1, text="?", command = help_edit, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    lbl0 = tk.Label(edit1, text="Record ID", font=("Helvetica", 10))
    lbl0.place(x=80, y=20)
    
    lbl1 = tk.Label(edit1, text="Edit Last Name", font=("Helvetica", 10))
    lbl1.place(x=80, y=80)
    lbl2 = tk.Label(edit1, text="Edit First Name", font=("Helvetica", 10))
    lbl2.place(x=80, y=120)
    lbl3 = tk.Label(edit1, text="Edit Address 1", font=("Helvetica", 10))
    lbl3.place(x=80, y=160)
    lbl4 = tk.Label(edit1, text="Edit Address 2", font=("Helvetica", 10))
    lbl4.place(x=80, y=200)
    lbl5 = tk.Label(edit1, text="Edit City", font=("Helvetica", 10))
    lbl5.place(x=80, y=240)
    lbl6 = tk.Label(edit1, text="Edit State", font=("Helvetica", 10))
    lbl6.place(x=80, y=280)
    lbl7 = tk.Label(edit1, text="Edit Zip Code", font=("Helvetica", 10))
    lbl7.place(x=80, y=320)
    lbl8 = tk.Label(edit1, text="Edit Phone 1", font=("Helvetica", 10))
    lbl8.place(x=80, y=360)
    lbl9 = tk.Label(edit1, text="Edit Phone 2", font=("Helvetica", 10))
    lbl9.place(x=80, y=400)
    lbl10 = tk.Label(edit1, text="Edit Email Address", font=("Helvetica", 10))
    lbl10.place(x=80, y=440)
    
    input_id_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_id_edit.place(x=300, y=20)
    input_id_edit.bind("<Tab>", focus_next_window)
    
    input_lastname_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_lastname_edit.place(x=300, y=80)
    input_lastname_edit.bind("<Tab>", focus_next_window)
    input_firstname_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_firstname_edit.place(x=300, y=120)
    input_firstname_edit.bind("<Tab>", focus_next_window)
    input_address1_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_address1_edit.place(x=300, y=160)
    input_address1_edit.bind("<Tab>", focus_next_window)
    input_address2_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_address2_edit.place(x=300, y=200)
    input_address2_edit.bind("<Tab>", focus_next_window)
    input_city_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_city_edit.place(x=300, y=240)
    input_city_edit.bind("<Tab>", focus_next_window)
    input_state_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_state_edit.place(x=300, y=280)
    input_state_edit.bind("<Tab>", focus_next_window)
    input_zipcode_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_zipcode_edit.place(x=300, y=320)
    input_zipcode_edit.bind("<Tab>", focus_next_window)
    input_phone1_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_phone1_edit.place(x=300, y=360)
    input_phone1_edit.bind("<Tab>", focus_next_window)
    input_phone2_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_phone2_edit.place(x=300, y=400)
    input_phone2_edit.bind("<Tab>", focus_next_window)
    input_email_edit = tk.Text(edit1, height = 1, width = 25, relief=tk.RAISED)
    input_email_edit.place(x=300, y=440)
    input_email_edit.bind("<Tab>", focus_next_window)
    
    edit11 = tk.Button(edit1, text="|", command = edit_lastname, height=1, width=1, relief=tk.RAISED)
    edit11.place(x=600, y=80)
    edit12 = tk.Button(edit1, text="|", command = edit_firstname, height=1, width=1, relief=tk.RAISED)
    edit12.place(x=600, y=120)
    edit13 = tk.Button(edit1, text="|", command = edit_address1, height=1, width=1, relief=tk.RAISED)
    edit13.place(x=600, y=160)
    edit14 = tk.Button(edit1, text="|", command = edit_address2, height=1, width=1, relief=tk.RAISED)
    edit14.place(x=600, y=200)
    edit15 = tk.Button(edit1, text="|", command = edit_city, height=1, width=1, relief=tk.RAISED)
    edit15.place(x=600, y=240)
    edit16 = tk.Button(edit1, text="|", command = edit_state, height=1, width=1, relief=tk.RAISED)
    edit16.place(x=600, y=280)
    edit17 = tk.Button(edit1, text="|", command = edit_zipcode, height=1, width=1, relief=tk.RAISED)
    edit17.place(x=600, y=320)
    edit18 = tk.Button(edit1, text="|", command = edit_phone1, height=1, width=1, relief=tk.RAISED)
    edit18.place(x=600, y=360)
    edit19 = tk.Button(edit1, text="|", command = edit_phone2, height=1, width=1, relief=tk.RAISED)
    edit19.place(x=600, y=400)
    edit110 = tk.Button(edit1, text="|", command = edit_emailaddress, height=1, width=1, relief=tk.RAISED)
    edit110.place(x=600, y=440)
    
    input_id_edit.focus_force()
    edit1.bind("<Escape>", lambda e: edit1.destroy())
    
    
    edit1.mainloop()
    
def view():
    view1 = tk.Tk()
    view1.title('View Record(s)')
    view1.geometry("700x550+20+20")
    view1.resizable(False, False)
    
    help1 = tk.Button(view1, text="?", command = help_view, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    view11 = tk.Button(view1, text="|", command = view_all_records, height=1, width=1, relief=tk.RAISED)
    view11.place(x=300, y=20)
    view12 = tk.Button(view1, text="|", command = view_selected, height=1, width=1, relief=tk.RAISED)
    view12.place(x=300, y=60)
    view13 = tk.Button(view1, text="|", command = view_sorted, height=1, width=1, relief=tk.RAISED)
    view13.place(x=300, y=100)
    view14 = tk.Button(view1, text="|", command = count_records, height=1, width=1, relief=tk.RAISED)
    view14.place(x=300, y=140)
    
    lbl1 = tk.Label(view1, text="View All Records", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(view1, text="View Selected Record(s)", font=("Helvetica", 10))
    lbl2.place(x=80, y=60)
    lbl3 = tk.Label(view1, text="View Sorted Records", font=("Helvetica", 10))
    lbl3.place(x=80, y=100)
    lbl4 = tk.Label(view1, text="Count of Records", font=("Helvetica", 10))
    lbl4.place(x=80, y=140)
    
    view11.focus_force()
    view1.bind("<Escape>", lambda e: view1.destroy())
    
    
    view1.mainloop()
    
def extra():
    global input_id
    global input_date
    global input_confirm
    global input_search
    global input_notes
    global input_search2
    global search_notes
    
    extra1 = tk.Tk()
    extra1.title('Extra Functions')
    extra1.geometry("700x550+20+20")
    extra1.resizable(False, False)
    
    lbl1 = tk.Label(extra1, text="Record ID", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    
    extra11 = tk.Button(extra1, text="|", command = set_date, height=1, width=1, relief=tk.RAISED)
    extra11.place(x=600, y=80)
    extra12 = tk.Button(extra1, text="|", command = confirm_contact, height=1, width=1, relief=tk.RAISED)
    extra12.place(x=600, y=120)
    extra12 = tk.Button(extra1, text="|", command = search_date, height=1, width=1, relief=tk.RAISED)
    extra12.place(x=600, y=160)
    extra13 = tk.Button(extra1, text="|", command = edit_notes, height=1, width=1, relief=tk.RAISED)
    extra13.place(x=600, y=200)
    extra13b = tk.Button(extra1, text="|", command = search_n, height=1, width=1, relief=tk.RAISED)
    extra13b.place(x=600, y=304)
    extra14 = tk.Button(extra1, text="|", command = search_name2, height=1, width=1, relief=tk.RAISED)
    extra14.place(x=600, y=344)
    extra15 = tk.Button(extra1, text="|", command = view_all, height=1, width=1, relief=tk.RAISED)
    extra15.place(x=300, y=384)
    extra16 = tk.Button(extra1, text="|", command = delete_by_id, height=1, width=1, relief=tk.RAISED)
    extra16.place(x=300, y=424)
    extra17 = tk.Button(extra1, text="|", command = delete_all, height=1, width=1, relief=tk.RAISED)
    extra17.place(x=300, y=464)
    
    help1 = tk.Button(extra1, text="?", command = help_extra, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
   
    lbl1 = tk.Label(extra1, text="Set Contact Date", font=("Helvetica", 10))
    lbl1.place(x=80, y=80)
    lbl2 = tk.Label(extra1, text="Confirm Contact", font=("Helvetica", 10))
    lbl2.place(x=80, y=120)
    lbl3 = tk.Label(extra1, text="Search Contacts by Date", font=("Helvetica", 10))
    lbl3.place(x=80, y=160)
    lbl4 = tk.Label(extra1, text="Edit Notes", font=("Helvetica", 10))
    lbl4.place(x=80, y=200)
    lbl4b = tk.Label(extra1, text="Search Notes", font=("Helvetica", 10))
    lbl4b.place(x=80, y=304)
    lbl5 = tk.Label(extra1, text="Search Extra by Last Name", font=("Helvetica", 10))
    lbl5.place(x=80, y=344)
    lbl5 = tk.Label(extra1, text="View All Extra", font=("Helvetica", 10))
    lbl5.place(x=80, y=384)
    lbl6 = tk.Label(extra1, text="Delete Extra by ID", font=("Helvetica", 10))
    lbl6.place(x=80, y=424)
    lbl7 = tk.Label(extra1, text="Delete All Extra", font=("Helvetica", 10))
    lbl7.place(x=80, y=464)
    
    
    input_id = tk.Text(extra1, height = 1, width = 25, relief=tk.RAISED)
    input_id.place(x=300, y=20)
    input_id.bind("<Tab>", focus_next_window)
    
    
    input_date = tk.Text(extra1, height = 1, width = 25, relief=tk.RAISED)
    input_date.place(x=300, y=80)
    input_date.bind("<Tab>", focus_next_window)
    
    input_confirm = tk.Text(extra1, height = 1, width = 25, relief=tk.RAISED)
    input_confirm.place(x=300, y=120)
    input_confirm.bind("<Tab>", focus_next_window)
    
    input_search = tk.Text(extra1, height = 1, width = 25, relief=tk.RAISED)
    input_search.place(x=300, y=160)
    input_search.bind("<Tab>", focus_next_window)
    
    input_notes = tk.Text(extra1, height = 5, width = 25, relief=tk.RAISED, wrap=WORD)
    input_notes.place(x=300, y=200)
    input_notes.bind("<Tab>", focus_next_window)
    
    search_notes = tk.Text(extra1, height = 1, width = 25, relief=tk.RAISED)
    search_notes.place(x=300, y=304)
    search_notes.bind("<Tab>", focus_next_window)
    
    input_search2 = tk.Text(extra1, height = 1, width = 25, relief=tk.RAISED)
    input_search2.place(x=300, y=344)
    input_search2.bind("<Tab>", focus_next_window)
    
    
    input_id.focus_force()
    extra1.bind("<Escape>", lambda e: extra1.destroy())
    
    extra1.mainloop()
    
def exit_program():
    main.destroy()


# View Record(s) Menu:
# --------------------

def view_all_records():
    
    global input_lastname
    global input_firstname
    global input_address1
    global input_address2
    global input_city
    global input_state
    global input_zipcode
    global input_phone1
    global input_phone2
    global input_email
    
    view_all1 = tk.Tk()
    view_all1.title('View All Records - ' + current_database_name)
    view_all1.geometry("1300x550+20+20")
    view_all1.resizable(True, False)
    
    view_all1.bind("<Escape>", lambda e: view_all1.destroy())
    
    a111 = tk.Label(view_all1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    
    cur.execute("SELECT * FROM database")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute('''SELECT * FROM database''')
    
    main_frame = Frame(view_all1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")

    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1
    
    con.commit()
    con.close()
    
    
    
    view_all1.mainloop()

def view_selected():

    global input_filter_name
    global input_filter_city
    global input_filter_state
    global input_filter_zipcode
    global input_filter_phone1
    global input_filter_phone2
    
    view_selected1 = tk.Tk()
    view_selected1.title('View Selected Record(s)')
    view_selected1.geometry("700x550+20+20")
    view_selected1.resizable(False, False)
    
    help1 = tk.Button(view_selected1, text="?", command = help_view_selected, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    view_selected11 = tk.Button(view_selected1, text="|", command = filter_name, height=1, width=1, relief=tk.RAISED)
    view_selected11.place(x=600, y=20)
    view_selected12 = tk.Button(view_selected1, text="|", command = filter_city, height=1, width=1, relief=tk.RAISED)
    view_selected12.place(x=600, y=60)
    view_selected13 = tk.Button(view_selected1, text="|", command = filter_state, height=1, width=1, relief=tk.RAISED)
    view_selected13.place(x=600, y=100)
    view_selected14 = tk.Button(view_selected1, text="|", command = filter_zipcode, height=1, width=1, relief=tk.RAISED)
    view_selected14.place(x=600, y=140)
    view_selected15 = tk.Button(view_selected1, text="|", command = filter_phone1, height=1, width=1, relief=tk.RAISED)
    view_selected15.place(x=600, y=200)
    view_selected16 = tk.Button(view_selected1, text="|", command = filter_phone2, height=1, width=1, relief=tk.RAISED)
    view_selected16.place(x=600, y=240)
    
    lbl1 = tk.Label(view_selected1, text="Filter by Last Name", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(view_selected1, text="Filter by City", font=("Helvetica", 10))
    lbl2.place(x=80, y=60)
    lbl3 = tk.Label(view_selected1, text="Filter by State", font=("Helvetica", 10))
    lbl3.place(x=80, y=100)
    lbl4 = tk.Label(view_selected1, text="Filter by Zip Code", font=("Helvetica", 10))
    lbl4.place(x=80, y=140)
    lbl5 = tk.Label(view_selected1, text="Filter by Area Code of Phone 1", font=("Helvetica", 10))
    lbl5.place(x=80, y=200)
    lbl6 = tk.Label(view_selected1, text="Filter by Area Code of Phone 2", font=("Helvetica", 10))
    lbl6.place(x=80, y=240)
    
    input_filter_name = tk.Text(view_selected1, height = 1, width = 25, relief=tk.RAISED)
    input_filter_name.place(x=300, y=20)
    input_filter_name.bind("<Tab>", focus_next_window)
    input_filter_city = tk.Text(view_selected1, height = 1, width = 25, relief=tk.RAISED)
    input_filter_city.place(x=300, y=60)
    input_filter_city.bind("<Tab>", focus_next_window)
    input_filter_state = tk.Text(view_selected1, height = 1, width = 25, relief=tk.RAISED)
    input_filter_state.place(x=300, y=100)
    input_filter_state.bind("<Tab>", focus_next_window)
    input_filter_zipcode = tk.Text(view_selected1, height = 1, width = 25, relief=tk.RAISED)
    input_filter_zipcode.place(x=300, y=140)
    input_filter_zipcode.bind("<Tab>", focus_next_window)
    input_filter_phone1 = tk.Text(view_selected1, height = 1, width = 25, relief=tk.RAISED)
    input_filter_phone1.place(x=300, y=200)
    input_filter_phone1.bind("<Tab>", focus_next_window)
    input_filter_phone2 = tk.Text(view_selected1, height = 1, width = 25, relief=tk.RAISED)
    input_filter_phone2.place(x=300, y=240)
    input_filter_phone2.bind("<Tab>", focus_next_window)
    
    input_filter_name.focus_force()
    view_selected1.bind("<Escape>", lambda e: view_selected1.destroy())
    
    view_selected1.mainloop()

def view_sorted():
    view_sorted1 = tk.Tk()
    view_sorted1.title('View Sorted Records')
    view_sorted1.geometry("700x550+20+20")
    view_sorted1.resizable(False, False)
    
    help1 = tk.Button(view_sorted1, text="?", command = help_view_sorted, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    view_sorted11 = tk.Button(view_sorted1, text="|", command = sort_lastName, height=1, width=1, relief=tk.RAISED)
    view_sorted11.place(x=300, y=20)
    view_sorted11.bind("<Tab>", focus_next_window)
    view_sorted12 = tk.Button(view_sorted1, text="|", command = sort_city, height=1, width=1, relief=tk.RAISED)
    view_sorted12.place(x=300, y=60)
    view_sorted12.bind("<Tab>", focus_next_window)
    view_sorted13 = tk.Button(view_sorted1, text="|", command = sort_state, height=1, width=1, relief=tk.RAISED)
    view_sorted13.place(x=300, y=100)
    view_sorted13.bind("<Tab>", focus_next_window)
    view_sorted14 = tk.Button(view_sorted1, text="|", command = sort_zip_code, height=1, width=1, relief=tk.RAISED)
    view_sorted14.place(x=300, y=140)
    view_sorted14.bind("<Tab>", focus_next_window)
    view_sorted15 = tk.Button(view_sorted1, text="|", command = sort_phone1, height=1, width=1, relief=tk.RAISED)
    view_sorted15.place(x=300, y=180)
    view_sorted15.bind("<Tab>", focus_next_window)
    view_sorted16 = tk.Button(view_sorted1, text="|", command = sort_phone2, height=1, width=1, relief=tk.RAISED)
    view_sorted16.place(x=300, y=220)
    view_sorted16.bind("<Tab>", focus_next_window)
    
    
    lbl1 = tk.Label(view_sorted1, text="Sort by Last Name", font=("Helvetica", 10))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(view_sorted1, text="Sort by City", font=("Helvetica", 10))
    lbl2.place(x=80, y=60)
    lbl3 = tk.Label(view_sorted1, text="Sort by State", font=("Helvetica", 10))
    lbl3.place(x=80, y=100)
    lbl4 = tk.Label(view_sorted1, text="Sort by Zip Code", font=("Helvetica", 10))
    lbl4.place(x=80, y=140)
    lbl5 = tk.Label(view_sorted1, text="Sort by Phone 1", font=("Helvetica", 10))
    lbl5.place(x=80, y=180)
    lbl6 = tk.Label(view_sorted1, text="Sort by Phone 2", font=("Helvetica", 10))
    lbl6.place(x=80, y=220)
    
    view_sorted11.focus_force()
    view_sorted1.bind("<Escape>", lambda e: view_sorted1.destroy())
    
    view_sorted1.mainloop()


def count_records():
    count1 = tk.Tk()
    count1.title('Count of Records - ' + current_database_name)
    count1.geometry("1300x550+20+20")
    count1.resizable(True, False)
    
    count1.bind("<Escape>", lambda e: count1.destroy())
    
    a111 = tk.Label(count1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT COUNT(*) FROM database")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print("Number of records: ")
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("SELECT COUNT(*) FROM database")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(count1, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    count1.mainloop()


# View Sorted Record(s):
# ----------------------

def sort_lastName():
    sort_last1 = tk.Tk()
    sort_last1.title('Sort by Last Name - ' + current_database_name)
    sort_last1.geometry("1300x550+20+20")
    sort_last1.resizable(True, False)
    
    sort_last1.bind("<Escape>", lambda e: sort_last1.destroy())
    
    a111 = tk.Label(sort_last1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT * FROM database ORDER BY lastname, firstname")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute('''SELECT * FROM database ORDER BY lastname, firstname''')
    
    main_frame = Frame(sort_last1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1
    con.commit()
    con.close()
    
    
    
    sort_last1.mainloop()

def sort_city():
    sort_city1 = tk.Tk()
    sort_city1.title('Sort by City - ' + current_database_name)
    sort_city1.geometry("1300x550+20+20")
    sort_city1.resizable(True, False)
    
    sort_city1.bind("<Escape>", lambda e: sort_city1.destroy())
    
    a111 = tk.Label(sort_city1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT * FROM database ORDER BY city, lastname, firstname")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute('''SELECT * FROM database ORDER BY city, lastname, firstname''')
    
    main_frame = Frame(sort_city1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1
    con.commit()
    con.close()
    
    
    
    sort_city1.mainloop()


def sort_state():
    sort_state1 = tk.Tk()
    sort_state1.title('Sort by State - ' + current_database_name)
    sort_state1.geometry("1300x550+20+20")
    sort_state1.resizable(True, False)
    
    sort_state1.bind("<Escape>", lambda e: sort_state1.destroy())
    
    a111 = tk.Label(sort_state1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT * FROM database ORDER BY state, lastname, firstname")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute('''SELECT * FROM database ORDER BY state, lastname, firstname''')
    
    main_frame = Frame(sort_state1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1
        
    con.commit()
    con.close()
    
    
    
    sort_state1.mainloop()


def sort_zip_code():
    sort_zip_code1 = tk.Tk()
    sort_zip_code1.title('Sort by Zip Code - ' + current_database_name)
    sort_zip_code1.geometry("1300x550+20+20")
    sort_zip_code1.resizable(True, False)
    
    sort_zip_code1.bind("<Escape>", lambda e: sort_zip_code1.destroy())
    
    a111 = tk.Label(sort_zip_code1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT * FROM database ORDER BY zipcode, lastname, firstname")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute('''SELECT * FROM database ORDER BY zipcode, lastname, firstname''')
    
    main_frame = Frame(sort_zip_code1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    sort_zip_code1.mainloop()


# Extra Functions:
# ----------------


def set_date():
    input_id_use = input_id.get("1.0","end-1c")
    input_date_use = input_date.get("1.0","end-1c")
    
    if input_date_use == "":
        input_date_use = "*"
    
    if current_database != '':
    
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET contactdate = ? WHERE id = ?""",(input_date_use, input_id_use))
        
        con.commit()
        con.close()
        
        view_all()
    else:
        view_all()


def confirm_contact():
    if current_database != '':
    
        input_id_use = input_id.get("1.0","end-1c")
        input_confirm_use = input_confirm.get("1.0","end-1c")
        
        if input_confirm_use == "":
            input_confirm_use = "*"
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET confirmation = ? WHERE id = ?""",(input_confirm_use, input_id_use))
        
        con.commit()
        con.close()

        view_all()
    else:
        view_all()

def search_date():
    
    search1 = tk.Tk()
    search1.title('Search Contacts by Date - ' + current_database_name)
    search1.geometry("1300x550+20+20")
    search1.resizable(True, False)
    
    search1.bind("<Escape>", lambda e: search1.destroy())
    
    a111 = tk.Label(search1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    input_id_use = input_id.get("1.0","end-1c")
    input_search_use = input_search.get("1.0","end-1c")
    
    if input_search_use == "":
        input_search_use = "*"
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("""SELECT id, lastname, firstname, contactdate, confirmation \
                FROM database WHERE contactdate = ? ORDER BY lastname, firstname""",(input_search_use,))
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("""SELECT id, lastname, firstname, contactdate, confirmation FROM database WHERE contactdate = ? ORDER BY lastname, firstname""",(input_search_use,))
    
    main_frame = Frame(search1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    search1.mainloop()
    
def edit_notes():
    input_id_use = input_id.get("1.0","end-1c")
    input_notes_use = input_notes.get("1.0","end-1c")
    
    if input_notes_use == "":
        input_notes_use = "*"
        
    if current_database != '':
    
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET notes = ? WHERE id = ?""",(input_notes_use, input_id_use))
        
        con.commit()
        con.close()

        view_all()
    else:
        view_all()
    
def search_name2():
    
    
    search2 = tk.Tk()
    search2.title('Search Extra by Last Name - ' + current_database_name)
    search2.geometry("1300x550+20+20")
    search2.resizable(True, False)
    
    search2.bind("<Escape>", lambda e: search2.destroy())
    
    a111 = tk.Label(search2, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    input_search2_use = input_search2.get("1.0","end-1c")
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("""SELECT id, lastname, firstname, notes, contactdate, confirmation \
                FROM database WHERE lastname = ?""",(input_search2_use,))
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("""SELECT id, lastname, firstname, notes, contactdate, confirmation FROM database WHERE lastname = ?""",(input_search2_use,))
    
    main_frame = Frame(search2)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    search2.mainloop()
    
def view_all():
    view_all2 = tk.Tk()
    view_all2.title('View All Extra - ' + current_database_name)
    view_all2.geometry("1300x550+20+20")
    view_all2.resizable(True, False)
    
    view_all2.bind("<Escape>", lambda e: view_all2.destroy())
    
    a111 = tk.Label(view_all2, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT id, lastname, firstname, notes, contactdate, confirmation \
                from database ORDER BY lastname, firstname")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("SELECT id, lastname, firstname, notes, contactdate, confirmation \
                      from database ORDER BY lastname, firstname")
    
    main_frame = Frame(view_all2)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    view_all2.bind("<Escape>", lambda e: view_all2.destroy())
    
    view_all2.mainloop()

def export():
    global current_database
    global current_csv
    
    
    if current_database != '':
    
        if current_database == "database1.db":
            current_csv = "database1.csv"
            
        if current_database == "database2.db":
            current_csv = "database2.csv"
        
        if current_database == "database3.db":
            current_csv = "database3.csv"
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        all = pd.read_sql('SELECT * FROM database' ,con)
        all.to_csv(current_csv, index=False)
        
        con.commit()
        con.close()
        folder_contents()
        
    else:
        not_export()
        

def custom():
    global input_code
    
    custom1 = tk.Tk()
    custom1.title('Custom SQL')
    custom1.geometry("700x550+20+20")
    custom1.resizable(False, False)
    
    help1 = tk.Button(custom1, text="?", command = help_custom, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    custom_button = tk.Button(custom1, text="|", command = custom_query, height=1, width=1, relief=tk.RAISED)
    custom_button.place(x=600, y=20)

    lbl = tk.Label(custom1, text="SQL Statement", font=("Helvetica", 10))
    lbl.place(x=80, y=20)

    input_code = tk.Text(custom1, height = 8, width = 35, relief=tk.RAISED, wrap=WORD)
    input_code.place(x=220, y=20)
    input_code.bind("<Tab>", focus_next_window)
    

    lbl138 = tk.Label(custom1, text=u'\u2022', font=("Helvetica", 10))
    lbl138.place(x=80, y=180)
    lbl139 = tk.Label(custom1, text=u'\u2022', font=("Helvetica", 10))
    lbl139.place(x=80, y=220)
        
    lbl40 = tk.Label(custom1, text='"database" is the name of the table.', font=("Helvetica", 10))
    lbl40.place(x=100, y=180)
    lbl40 = tk.Label(custom1, text="The fields are as follows:", font=("Helvetica", 10))
    lbl40.place(x=100, y=220)
    
    lbl41 = tk.Label(custom1, text="id, lastname, firstname, address1, address2, city, state, zipcode,", font=("Helvetica", 10))
    lbl41.place(x=100, y=240)
    lbl42 = tk.Label(custom1, text="phone1, phone2, emailaddress, notes, contactdate, confirmation.", font=("Helvetica", 10))
    lbl42.place(x=100, y=260)
    
    input_code.focus_force()
    
    custom1.bind("<Escape>", lambda e: custom1.destroy())
    
    custom1.mainloop()


def custom_query():
    
    input_code_use = str(input_code.get("1.0","end-1c"))
    
    custom2 = tk.Tk()
    custom2.title('Custom SQL - ' + current_database_name)
    custom2.geometry("1300x550+20+20")
    custom2.resizable(True, False)
    
    custom2.bind("<Escape>", lambda e: custom2.destroy())
    
    a111 = tk.Label(custom2, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute(input_code_use)
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute(input_code_use)
    
    main_frame = Frame(custom2)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    custom2.mainloop()
    
def filter_name():
    input_filter_name_use = input_filter_name.get("1.0","end-1c")
    
    filter_lastname = tk.Tk()
    filter_lastname.title('Filter by Last Name - ' + current_database_name)
    filter_lastname.geometry("1300x550+20+20")
    filter_lastname.resizable(True, False)
    
    filter_lastname.bind("<Escape>", lambda e: filter_lastname.destroy())
    
    a111 = tk.Label(filter_lastname, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute('''SELECT * FROM database WHERE lastname = ? ORDER BY lastname, firstname''',(input_filter_name_use,))
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("""SELECT * FROM database WHERE lastname = ? ORDER BY lastname, firstname""",(input_filter_name_use,))
    
    main_frame = Frame(filter_lastname)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    filter_lastname.mainloop()
    
def filter_city():
    input_filter_city_use = input_filter_city.get("1.0","end-1c")
    
    filter_city1 = tk.Tk()
    filter_city1.title('Filter by City - ' + current_database_name)
    filter_city1.geometry("1300x550+20+20")
    filter_city1.resizable(True, False)
    
    filter_city1.bind("<Escape>", lambda e: filter_city1.destroy())
    
    a111 = tk.Label(filter_city1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("""SELECT * FROM database WHERE city = ? ORDER BY lastname, firstname""",(input_filter_city_use,))
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("""SELECT * FROM database WHERE city = ? ORDER BY lastname, firstname""",(input_filter_city_use,))
    
    main_frame = Frame(filter_city1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    filter_city1.mainloop()
    
    
def filter_state():
    input_filter_state_use = input_filter_state.get("1.0","end-1c")
    
    filter_state2 = tk.Tk()
    filter_state2.title('Filter by State - ' + current_database_name)
    filter_state2.geometry("1300x550+20+20")
    filter_state2.resizable(True, False)
    
    filter_state2.bind("<Escape>", lambda e: filter_state2.destroy())
    
    a111 = tk.Label(filter_state2, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("""SELECT * FROM database WHERE state = ? ORDER BY lastname, firstname""",(input_filter_state_use,))
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("""SELECT * FROM database WHERE state = ? ORDER BY lastname, firstname""",(input_filter_state_use,))
    
    main_frame = Frame(filter_state2)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    filter_state2.mainloop()
    
def filter_zipcode():
    input_filter_zipcode_use = input_filter_zipcode.get("1.0","end-1c")
    
    filter_zipcode2 = tk.Tk()
    filter_zipcode2.title('Filter by Zip Code - ' + current_database_name)
    filter_zipcode2.geometry("1300x550+20+20")
    filter_zipcode2.resizable(True, False)
    
    filter_zipcode2.bind("<Escape>", lambda e: filter_zipcode2.destroy())
    
    a111 = tk.Label(filter_zipcode2, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("""SELECT * FROM database WHERE zipcode = ? ORDER BY lastname, firstname""",(input_filter_zipcode_use,))
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("""SELECT * FROM database WHERE zipcode = ? ORDER BY lastname, firstname""",(input_filter_zipcode_use,))
    
    main_frame = Frame(filter_zipcode2)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    filter_zipcode2.mainloop()
    
def edit_lastname():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_lastname_edit_use = input_lastname_edit.get("1.0","end-1c")
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET lastname = ? WHERE id = ?""",(input_lastname_edit_use, input_id_edit_use))
        
        con.commit()
        con.close()
        
        view_all_records()
    else:
        view_all_records()

def edit_firstname():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_firstname_edit_use = input_firstname_edit.get("1.0","end-1c")
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET firstname = ? WHERE id = ?""",(input_firstname_edit_use, input_id_edit_use))
        
        con.commit()
        con.close()
        
        view_all_records()
    else:
        view_all_records()
    
def edit_address1():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_address1_edit_use = input_address1_edit.get("1.0","end-1c")
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET address1 = ? WHERE id = ?""",(input_address1_edit_use, input_id_edit_use))
        
        con.commit()
        con.close()
        
        view_all_records()
    else:
        view_all_records()
    
def edit_address2():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_address2_edit_use = input_address2_edit.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
            
        cur.execute("""UPDATE database SET address2 = ? WHERE id = ?""",(input_address2_edit_use, input_id_edit_use))
            
        con.commit()
        con.close()
        
        view_all_records()
    else:
        view_all_records()
    
def edit_city():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_city_edit_use = input_city_edit.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
            
        cur.execute("""UPDATE database SET city = ? WHERE id = ?""",(input_city_edit_use, input_id_edit_use))
            
        con.commit()
        con.close()
        
        view_all_records()
    else:
        view_all_records()
    
def edit_state():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_state_edit_use = input_state_edit.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
            
        cur.execute("""UPDATE database SET state = ? WHERE id = ?""",(input_state_edit_use, input_id_edit_use))
            
        con.commit()
        con.close()
        
        view_all_records()
        
    else:
        view_all_records()
    
def edit_zipcode():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_zipcode_edit_use = input_zipcode_edit.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
            
        cur.execute("""UPDATE database SET zipcode = ? WHERE id = ?""",(input_zipcode_edit_use, input_id_edit_use))
            
        con.commit()
        con.close()
        
        view_all_records()
        
    else:
        view_all_records()
    
def edit_phone1():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_phone1_edit_use = input_phone1_edit.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
            
        cur.execute("""UPDATE database SET phone1 = ? WHERE id = ?""",(input_phone1_edit_use, input_id_edit_use))
            
        con.commit()
        con.close()
        
        view_all_records()
    
    else:
        view_all_records()
    
def edit_phone2():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_phone2_edit_use = input_phone2_edit.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
            
        cur.execute("""UPDATE database SET phone2 = ? WHERE id = ?""",(input_phone2_edit_use, input_id_edit_use))
            
        con.commit()
        con.close()
        
        view_all_records()
        
    else:
        view_all_records()
    
def edit_emailaddress():
    if current_database != '':
    
        input_id_edit_use = input_id_edit.get("1.0","end-1c")
        input_email_edit_use = input_email_edit.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
            
        cur.execute("""UPDATE database SET emailaddress = ? WHERE id = ?""",(input_email_edit_use, input_id_edit_use))
            
        con.commit()
        con.close()
        
        view_all_records()
        
    else:
        view_all_records()

def delete_empty():
    if current_database != '':
    
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""DELETE FROM database WHERE \
                    (lastname = '') AND \
                    (firstname = '') AND \
                    (address1 = '') AND \
                    (address2 = '') AND \
                    (city = '') AND \
                    (state = '') AND
                    (zipcode = '') AND \
                    (phone1 = '') AND \
                    (phone2 = '') AND \
                    (emailaddress = '') AND \
                    (notes = '*') AND \
                    (contactdate = '*') AND \
                    (confirmation = '*')""")
        
        con.commit()
        con.close()
        
        view_all_records()
        
    else:
        view_all_records()
    
def delete_duplicates():
    if current_database != '':
    
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""DELETE FROM database WHERE id NOT IN ( \
                    SELECT MAX(id) FROM database GROUP BY \
                    lastname, firstname, address1, address2, city, state, zipcode, \
                    phone1, phone2, emailaddress, notes, contactdate, confirmation)""")
        
        con.commit()
        con.close()
        
        view_all_records()
        
    else:
        view_all_records()

def help():
    help = tk.Tk()
    
    help.title('Help')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    help1 = tk.Button(help, text="?", command = help, height=1, width=1, relief=tk.RAISED)
    help1.place(x=650, y=500)
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl1 = tk.Label(help, text="Create New Database: ", font=("Helvetica", 10, 'bold'))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(help, text="Create a new database and confirm that it exists by a checkmark.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl2 = tk.Label(help, text="Create custom names for each database or clear names.", font=("Helvetica", 10))
    lbl2.place(x=260, y=40)
    lbl3 = tk.Label(help, text="Choose Current Database: ", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=60)
    lbl4 = tk.Label(help, text="Choose the working database and confirm it by a checkmark.", font=("Helvetica", 10))
    lbl4.place(x=260, y=60)
    lbl5 = tk.Label(help, text="Make sure database exists. See the names of databases.", font=("Helvetica", 10))
    lbl5.place(x=260, y=80)
    lbl6 = tk.Label(help, text="Add Record(s): ", font=("Helvetica", 10, 'bold'))
    lbl6.place(x=80, y=100)
    lbl7 = tk.Label(help, text="Populate a record. Enter all relevant fields and click on Add Record.", font=("Helvetica", 10))
    lbl7.place(x=260, y=100)
    lbl8 = tk.Label(help, text="Delete Record(s): ", font=("Helvetica", 10, 'bold'))
    lbl8.place(x=80, y=120)
    lbl9 = tk.Label(help, text="Delete a record by ID, delete all empty records, or delete", font=("Helvetica", 10))
    lbl9.place(x=260, y=120)
    lbl10 = tk.Label(help, text="duplicate records. Count empty and duplicate records.", font=("Helvetica", 10))
    lbl10.place(x=260, y=140)
    lbl11 = tk.Label(help, text="Edit Record(s):", font=("Helvetica", 10, 'bold'))
    lbl11.place(x=80, y=160)
    lbl12 = tk.Label(help, text="Choose the current record by ID. Edit the relevant fields to update", font=("Helvetica", 10))
    lbl12.place(x=260, y=160)
    lbl13 = tk.Label(help, text="the record.", font=("Helvetica", 10))
    lbl13.place(x=260, y=180)
    lbl14 = tk.Label(help, text="View All Records: ", font=("Helvetica", 10, 'bold'))
    lbl14.place(x=80, y=200)
    lbl15 = tk.Label(help, text="Choose to see the complete, unmodified database.", font=("Helvetica", 10))
    lbl15.place(x=260, y=200)
    lbl16 = tk.Label(help, text="View Selected Record(s): ", font=("Helvetica", 10, 'bold'))
    lbl16.place(x=80, y=220)
    lbl17 = tk.Label(help, text="Filter the data by attribute.", font=("Helvetica", 10))
    lbl17.place(x=260, y=220)
    lbl18 = tk.Label(help, text="View Sorted Record(s):", font=("Helvetica", 10, 'bold'))
    lbl18.place(x=80, y=240)
    lbl19 = tk.Label(help, text="Choose the implementation for sorting the data.", font=("Helvetica", 10))
    lbl19.place(x=260, y=240)
    lbl20 = tk.Label(help, text="Count of Records:", font=("Helvetica", 10, 'bold'))
    lbl20.place(x=80, y=260)
    lbl21 = tk.Label(help, text="Display the number of records in the database.", font=("Helvetica", 10))
    lbl21.place(x=260, y=260)
    
    lbl22 = tk.Label(help, text="Extra Functions: ", font=("Helvetica", 10, 'bold'))
    lbl22.place(x=80, y=280)
    lbl23 = tk.Label(help, text="Edit by choosing the current record ID.", font=("Helvetica", 10))
    lbl23.place(x=260, y=280)
    lbl24 = tk.Label(help, text="Set Contact Date:", font=("Helvetica", 10, 'bold'))
    lbl24.place(x=80, y=300)
    lbl25 = tk.Label(help, text="Update the record with a contact date.", font=("Helvetica", 10))
    lbl25.place(x=260, y=300)
    lbl26 = tk.Label(help, text="Confirm Contact:", font=("Helvetica", 10, 'bold'))
    lbl26.place(x=80, y=320)
    lbl27 = tk.Label(help, text="Update the record with a confirmation of the contact.", font=("Helvetica", 10))
    lbl27.place(x=260, y=320)
    lbl28 = tk.Label(help, text="Search Contacts by Date:", font=("Helvetica", 10, 'bold'))
    lbl28.place(x=80, y=340)
    lbl29 = tk.Label(help, text="View all contacts with a certain contact date.", font=("Helvetica", 10))
    lbl29.place(x=260, y=340)
    
    lbl30 = tk.Label(help, text="Edit Notes:", font=("Helvetica", 10, 'bold'))
    lbl30.place(x=80, y=360)
    lbl31 = tk.Label(help, text="Update the record with notes.", font=("Helvetica", 10))
    lbl31.place(x=260, y=360)
    lbl30b = tk.Label(help, text="Search Notes:", font=("Helvetica", 10, 'bold'))
    lbl30b.place(x=80, y=380)
    lbl31b = tk.Label(help, text="Search for specific string in notes.", font=("Helvetica", 10))
    lbl31b.place(x=260, y=380)
    
    lbl32 = tk.Label(help, text="Search Extra by Last:", font=("Helvetica", 10, 'bold'))
    lbl32.place(x=80, y=400)
    lbl33 = tk.Label(help, text="View all extra based on last name.", font=("Helvetica", 10))
    lbl33.place(x=260, y=400)
    lbl34 = tk.Label(help, text="View All Extra:", font=("Helvetica", 10, 'bold'))
    lbl34.place(x=80, y=420)
    lbl35 = tk.Label(help, text="View contact management fields and notes for all records.", font=("Helvetica", 10))
    lbl35.place(x=260, y=420)
    
    lbl50 = tk.Label(help, text="Delete Extra by ID:", font=("Helvetica", 10, 'bold'))
    lbl50.place(x=80, y=440)
    lbl51 = tk.Label(help, text="Delete extra information by a certain ID.", font=("Helvetica", 10))
    lbl51.place(x=260, y=440)
    
    lbl52 = tk.Label(help, text="Delete All Extra:", font=("Helvetica", 10, 'bold'))
    lbl52.place(x=80, y=460)
    lbl53 = tk.Label(help, text="Delete extra information from all records.", font=("Helvetica", 10))
    lbl53.place(x=260, y=460)
    
    
    lbl36 = tk.Label(help, text="Export Data:", font=("Helvetica", 10, 'bold'))
    lbl36.place(x=80, y=480)
    lbl37 = tk.Label(help, text="Create a CSV file based on the current database.", font=("Helvetica", 10))
    lbl37.place(x=260, y=480)
    lbl36b = tk.Label(help, text="Custom SQL:", font=("Helvetica", 10, 'bold'))
    lbl36b.place(x=80, y=500)
    lbl37b = tk.Label(help, text="User generated SQL code.", font=("Helvetica", 10))
    lbl37b.place(x=260, y=500)
    
    lbl38 = tk.Label(help, text="?:", font=("Helvetica", 10, 'bold'))
    lbl38.place(x=80, y=520)
    lbl39 = tk.Label(help, text="Open the help window.", font=("Helvetica", 10))
    lbl39.place(x=260, y=520)
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()
    
def name1():
    global input_database_name1_use
    
    
    input_database_name1_use = str(input_database_name1.get("1.0","end-1c"))
    
    input_database_name1_use = input_database_name1_use.replace("\n", " ")
    
    if input_database_name1_use == "":
        input_database_name1_use = "Database not named"
    
    print(input_database_name1_use)
    
    with open('data.dat', 'r') as file:
        data = file.readlines()
        data[0] = input_database_name1_use + "\n"

    with open('data.dat', 'w') as file:
        file.writelines( data )
        
    lbl111.config(text=input_database_name1_use)
    lbl111b.config(text=input_database_name1_use)
    
def name2():
    global input_database_name2_use
    input_database_name2_use = str(input_database_name2.get("1.0","end-1c"))
    
    input_database_name2_use = input_database_name2_use.replace("\n", " ")
    
    if input_database_name2_use == "":
        input_database_name2_use = "Database not named"
    
    print(input_database_name2_use)
    
    with open('data.dat', 'r') as file:
        data = file.readlines()
        data[1] = input_database_name2_use + "\n"

    with open('data.dat', 'w') as file:
        file.writelines( data )
    
    lbl211.config(text=input_database_name2_use)
    lbl211b.config(text=input_database_name2_use)
    

def name3():
    global input_database_name3_use
    input_database_name3_use = str(input_database_name3.get("1.0","end-1c"))
    
    input_database_name3_use = input_database_name3_use.replace("\n", " ")
    
    if input_database_name3_use == "":
        input_database_name3_use = "Database not named"
    
    print(input_database_name3_use)
    
    with open('data.dat', 'r') as file:
        data = file.readlines()
        data[2] = input_database_name3_use

    with open('data.dat', 'w') as file:
        file.writelines( data )
    
    lbl311.config(text=input_database_name3_use)
    lbl311b.config(text=input_database_name3_use)
    
def name4():
    path = './data.dat'
    check_file_data = os.path.isfile(path)
    
    if check_file_data == TRUE:
        os.remove("./data.dat")
    
    with open("data.dat", "a") as myfile:
        myfile.write("Database not named\n")
        myfile.write("Database not named\n")
        myfile.write("Database not named")

    lbl111.config(text="Database not named\n")
    lbl211.config(text="Database not named\n")
    lbl311.config(text="Database not named")
    
    lbl111b.config(text="Database not named\n")
    lbl211b.config(text="Database not named\n")
    lbl311b.config(text="Database not named")

    
def delete_by_id():
    if current_database != '':
    
        input_id_use = input_id.get("1.0","end-1c")
            
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET notes = '*', contactdate = '*', confirmation = '*' WHERE id = ? """,(input_id_use, ))
        
        con.commit()
        con.close()
        
        view_all()
        
    else:
        view_all()
    
def delete_all():
    if current_database != '':
    
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""UPDATE database SET notes = '*', contactdate = '*', confirmation = '*'""")
        
        con.commit()
        con.close()
        
        view_all()
    
    else:
        view_all()

def help_main_menu():
    help = tk.Tk()
    
    help.title('Main Menu')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    
    lbl3 = tk.Label(help, text="Export Data: ", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=20)
    lbl4 = tk.Label(help, text="Choose to save a current database as a csv file, for example", font=("Helvetica", 10))
    lbl4.place(x=260, y=20)
    lbl5 = tk.Label(help, text="database2.csv.", font=("Helvetica", 10))
    lbl5.place(x=260, y=40)
    lbl6 = tk.Label(help, text="Exit Program:", font=("Helvetica", 10, 'bold'))
    lbl6.place(x=80, y=80)
    lbl7 = tk.Label(help, text="Will terminate the program.", font=("Helvetica", 10))
    lbl7.place(x=260, y=80)
    lbl2 = tk.Label(help, text="See other help windows for details.", font=("Helvetica", 10))
    lbl2.place(x=260, y=120)
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()
   
def help_create1():
    help = tk.Tk()
    
    help.title('Create New Database')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl1 = tk.Label(help, text="Create database?.db: ", font=("Helvetica", 10, 'bold'))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(help, text="Click to create the specific database.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl2 = tk.Label(help, text="The squares indicate that the certain database files exist.", font=("Helvetica", 10))
    lbl2.place(x=260, y=60)
    lbl4 = tk.Label(help, text="Enter specific names in the fields to identify your databases.", font=("Helvetica", 10))
    lbl4.place(x=260, y=100)
    lbl6 = tk.Label(help, text="Clear names : ", font=("Helvetica", 10, 'bold'))
    lbl6.place(x=80, y=140)
    lbl7 = tk.Label(help, text="Removes the names from the databases, so that you can", font=("Helvetica", 10))
    lbl7.place(x=260, y=140)
    lbl7 = tk.Label(help, text="rename them if required.", font=("Helvetica", 10))
    lbl7.place(x=260, y=160)
    lbl9 = tk.Label(help, text="To proceed, make sure a database has been created.", font=("Helvetica", 10))
    lbl9.place(x=260, y=200)
    lbl9 = tk.Label(help, text="The current names are indicated.", font=("Helvetica", 10))
    lbl9.place(x=260, y=240)
    lbl10 = tk.Label(help, text="After naming a database, be sure to choose it to set it as current.", font=("Helvetica", 10))
    lbl10.place(x=260, y=280)
   
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def help_choose():
    help = tk.Tk()
    
    help.title('Choose Current Database')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    

    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl2 = tk.Label(help, text="Click on the specific database file to make it the current.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl2 = tk.Label(help, text="To proceed, make sure a database has been designated as current.", font=("Helvetica", 10))
    lbl2.place(x=260, y=60)
    lbl4 = tk.Label(help, text="After naming a database, click to set the name as current.", font=("Helvetica", 10))
    lbl4.place(x=260, y=100)
    lbl5 = tk.Label(help, text="The checkmarks indicate which database has previously been selected.", font=("Helvetica", 10))
    lbl5.place(x=260, y=140)
    lbl6 = tk.Label(help, text="The squares indicate that the certain database files exist.", font=("Helvetica", 10))
    lbl6.place(x=260, y=180)
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()
    
def help_add():
    help = tk.Tk()
    
    help.title('Add Record(s)')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl1 = tk.Label(help, text="Add Record: ", font=("Helvetica", 10, 'bold'))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(help, text="Populate each relevant field and click to add the record to the", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl3 = tk.Label(help, text="database.", font=("Helvetica", 10))
    lbl3.place(x=260, y=40)
    
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def help_delete():
    help = tk.Tk()
    
    help.title('Delete Record(s)')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl2 = tk.Label(help, text="Enter the ID for the current deletion and click to confirm.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)

    lbl3 = tk.Label(help, text="Remove Empty Records:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=60)
    lbl4 = tk.Label(help, text="Deletes all the empty records from the current database.", font=("Helvetica", 10))
    lbl4.place(x=260, y=60)
    lbl6 = tk.Label(help, text="Remove Duplicate", font=("Helvetica", 10, 'bold'))
    lbl6.place(x=80, y=100)
    lbl6b = tk.Label(help, text="Records:", font=("Helvetica", 10, 'bold'))
    lbl6b.place(x=80, y=120)
    lbl7 = tk.Label(help, text="Deletes the duplicates while leaving one.", font=("Helvetica", 10))
    lbl7.place(x=260, y=120)
    lbl8 = tk.Label(help, text="Count Empty Records:", font=("Helvetica", 10, 'bold'))
    lbl8.place(x=80, y=160)
    lbl9 = tk.Label(help, text="Count of Empty Records in current database.", font=("Helvetica", 10))
    lbl9.place(x=260, y=160)
    lbl10 = tk.Label(help, text="Count Duplicate Records:", font=("Helvetica", 10, 'bold'))
    lbl10.place(x=80, y=200)
    lbl11 = tk.Label(help, text="Counts of Duplicate records in current database.", font=("Helvetica", 10))
    lbl11.place(x=260, y=200)
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def help_edit():
    help = tk.Tk()
    
    help.title('Edit Record(s)')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl2 = tk.Label(help, text="Enter the ID of the record for current editing.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl4 = tk.Label(help, text="Enter all relevant values and click on the relevant buttons to", font=("Helvetica", 10))
    lbl4.place(x=260, y=60)
    lbl5 = tk.Label(help, text="replace the current values with the desired values.", font=("Helvetica", 10))
    lbl5.place(x=260, y=80)
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def help_view():
    help = tk.Tk()
    
    help.title('View Record(s)')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl1 = tk.Label(help, text="View All Records:", font=("Helvetica", 10, 'bold'))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(help, text="Displays all the records in unordered status, by ID.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl3 = tk.Label(help, text="View Selected Record(s): ", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=60)
    lbl4 = tk.Label(help, text="Explained in the relevant help window.", font=("Helvetica", 10))
    lbl4.place(x=260, y=60)
    lbl6 = tk.Label(help, text="View Sorted Record(s): ", font=("Helvetica", 10, 'bold'))
    lbl6.place(x=80, y=100)
    lbl7 = tk.Label(help, text="Explained in the relevant help window.", font=("Helvetica", 10))
    lbl7.place(x=260, y=100)
    lbl8 = tk.Label(help, text="Count of Records:", font=("Helvetica", 10, 'bold'))
    lbl8.place(x=80, y=140)
    lbl9 = tk.Label(help, text="Displays the number of records in the current database.", font=("Helvetica", 10))
    lbl9.place(x=260, y=140)
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()
   
def help_extra():
    help = tk.Tk()
    
    help.title('Extra Functions')
    help.geometry("700x550+750+20")
    help.resizable(False, False)

    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl1 = tk.Label(help, text="Record ID:", font=("Helvetica", 10, 'bold'))
    lbl1.place(x=80, y=20)
    lbl2 = tk.Label(help, text="Confirm the current record in the input field.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl3 = tk.Label(help, text="Set Contact Date:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=60)
    lbl4 = tk.Label(help, text="Edits the record by adding a date for the contacting of the record by ID.", font=("Helvetica", 10))
    lbl4.place(x=260, y=60)
    lbl5 = tk.Label(help, text="Enter or edit date with a valid and appropriate format.", font=("Helvetica", 10))
    lbl5.place(x=260, y=80)
    lbl6 = tk.Label(help, text="Confirm Contact:", font=("Helvetica", 10, 'bold'))
    lbl6.place(x=80, y=120)
    lbl7 = tk.Label(help, text="Allows for the confirmation of the contact. Enter or edit with a valid and", font=("Helvetica", 10))
    lbl7.place(x=260, y=120)
    lbl9 = tk.Label(help, text="appropriate format.", font=("Helvetica", 10))
    lbl9.place(x=260, y=140)
    lbl11 = tk.Label(help, text="Search Contacts by Date:", font=("Helvetica", 10, 'bold'))
    lbl11.place(x=80, y=180)
    lbl12 = tk.Label(help, text="Displays all the contact information for the specified date.", font=("Helvetica", 10))
    lbl12.place(x=260, y=180)
    lbl14 = tk.Label(help, text="Edit Notes:", font=("Helvetica", 10, 'bold'))
    lbl14.place(x=80, y=220)
    lbl15 = tk.Label(help, text="Adds an appropriate reminder to the record with the current ID.", font=("Helvetica", 10))
    lbl15.place(x=260, y=220)
    lbl14b = tk.Label(help, text="Search Notes:", font=("Helvetica", 10, 'bold'))
    lbl14b.place(x=80, y=260)
    lbl15b = tk.Label(help, text="Search for specific string in notes.", font=("Helvetica", 10))
    lbl15b.place(x=260, y=260)
    lbl16 = tk.Label(help, text="Search Extra by", font=("Helvetica", 10, 'bold'))
    lbl16.place(x=80, y=300)
    lbl16b = tk.Label(help, text="Last Name:", font=("Helvetica", 10, 'bold'))
    lbl16b.place(x=80, y=320)
    lbl17 = tk.Label(help, text="Displays the current extra information for the specified last name.", font=("Helvetica", 10))
    lbl17.place(x=260, y=320)
    lbl18 = tk.Label(help, text="View All Extra:", font=("Helvetica", 10, 'bold'))
    lbl18.place(x=80, y=360)
    lbl19 = tk.Label(help, text="Displays the extra information for all records in the current database.", font=("Helvetica", 10))
    lbl19.place(x=260, y=360)
    lbl20 = tk.Label(help, text="Delete Extra By ID:", font=("Helvetica", 10, 'bold'))
    lbl20.place(x=80, y=400)
    lbl21 = tk.Label(help, text="Removes all extra information from the record with the current ID.", font=("Helvetica", 10))
    lbl21.place(x=260, y=400)
    lbl22 = tk.Label(help, text="Delete All Extra:", font=("Helvetica", 10, 'bold'))
    lbl22.place(x=80, y=440)
    lbl23 = tk.Label(help, text="Removes all extra information from all records.", font=("Helvetica", 10))
    lbl23.place(x=260, y=440)
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def help_view_selected():
    help = tk.Tk()
    
    help.title('View Selected Record(s)')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl2 = tk.Label(help, text="This shows all records with the value specified.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl3 = tk.Label(help, text="Filter by State:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=60)
    lbl4 = tk.Label(help, text="For instance, would display all records with specified state.", font=("Helvetica", 10))
    lbl4.place(x=260, y=60)
    lbl5 = tk.Label(help, text="Filter by Area Code:", font=("Helvetica", 10, 'bold'))
    lbl5.place(x=80, y=100)
    lbl6 = tk.Label(help, text="For instance, would display all records with specified area code.", font=("Helvetica", 10))
    lbl6.place(x=260, y=100)
    
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def help_view_sorted():
    help = tk.Tk()
    
    help.title('View Sorted Record(s)')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl2 = tk.Label(help, text="This sorts the data.", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl3 = tk.Label(help, text="Sort by Last Name:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=60)
    lbl4 = tk.Label(help, text="For instance, would display all the records based on last name,", font=("Helvetica", 10))
    lbl4.place(x=260, y=60)
    lbl4b = tk.Label(help, text="in order.", font=("Helvetica", 10))
    lbl4b.place(x=260, y=80)
    
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def help_custom():
    help = tk.Tk()
    
    help.title('Custom SQL')
    help.geometry("700x550+750+20")
    help.resizable(False, False)
    
    
    a111 = tk.Label(help, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl2 = tk.Label(help, text="This allows for the creation of specific user generated SQL code", font=("Helvetica", 10))
    lbl2.place(x=260, y=20)
    lbl2 = tk.Label(help, text="to query the database.", font=("Helvetica", 10))
    lbl2.place(x=260, y=40)
    
    help.bind("<Escape>", lambda e: help.destroy())
    
    help.mainloop()

def not_created1():
    not1 = tk.Tk()
    
    not1.title('Choose Current Database')
    not1.geometry("700x550+750+20")
    not1.resizable(False, False)
    
    
    a111 = tk.Label(not1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl3 = tk.Label(not1, text="database1.db:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=20)
    lbl4 = tk.Label(not1, text="This database does not exist.", font=("Helvetica", 10))
    lbl4.place(x=260, y=20)
    lbl5 = tk.Label(not1, text="Check Create New Database window.", font=("Helvetica", 10))
    lbl5.place(x=260, y=40)
    
    
    not1.bind("<Escape>", lambda e: not1.destroy())
    
    not1.mainloop()
    
def not_created2():
    not2 = tk.Tk()
    
    not2.title('Choose Current Database')
    not2.geometry("700x550+750+20")
    not2.resizable(False, False)
    
    
    a111 = tk.Label(not2, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl3 = tk.Label(not2, text="database2.db:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=20)
    lbl4 = tk.Label(not2, text="This database does not exist.", font=("Helvetica", 10))
    lbl4.place(x=260, y=20)
    lbl5 = tk.Label(not2, text="Check Create New Database window.", font=("Helvetica", 10))
    lbl5.place(x=260, y=40)
    
    
    not2.bind("<Escape>", lambda e: not2.destroy())
    
    not2.mainloop()

def not_created3():
    not3 = tk.Tk()
    
    not3.title('Choose Current Database')
    not3.geometry("700x550+750+20")
    not3.resizable(False, False)
    
    
    a111 = tk.Label(not3, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl3 = tk.Label(not3, text="database3.db:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=20)
    lbl4 = tk.Label(not3, text="This database does not exist.", font=("Helvetica", 10))
    lbl4.place(x=260, y=20)
    lbl5 = tk.Label(not3, text="Check Create New Database window.", font=("Helvetica", 10))
    lbl5.place(x=260, y=40)
    
    
    not3.bind("<Escape>", lambda e: not3.destroy())
    
    not3.mainloop()
    
def count_empty():
    count_empty = tk.Tk()
    count_empty.title('Count Empty Records - ' + current_database_name)
    count_empty.geometry("1300x550+20+20")
    count_empty.resizable(True, False)
    
    count_empty.bind("<Escape>", lambda e: count_empty.destroy())
    
    a111 = tk.Label(count_empty, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT COUNT(*) FROM database \
                WHERE (lastname = '') AND (firstname = '') AND (address1 = '') AND \
                (address2 = '') AND (city = '') AND (state = '') AND \
                (zipcode = '') AND (phone1 = '') AND (phone2 = '') AND \
                (emailaddress = '') AND (notes = '*') AND (contactdate = '*') AND \
                (confirmation = '*')")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print("Number of empty records: ")
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("SELECT COUNT(*) FROM database \
                WHERE (lastname = '') AND (firstname = '') AND (address1 = '') AND \
                (address2 = '') AND (city = '') AND (state = '') AND \
                (zipcode = '') AND (phone1 = '') AND (phone2 = '') AND \
                (emailaddress = '') AND (notes = '*') AND (contactdate = '*') AND \
                (confirmation = '*')")
    
    main_frame = Frame(count_empty)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    count_empty.bind("<Escape>", lambda e: count_empty.destroy())
    
    count_empty.mainloop()
    
def count_duplicates():
    count_duplicates = tk.Tk()
    count_duplicates.title('Count Duplicate Records - ' + current_database_name)
    count_duplicates.geometry("1300x550+20+20")
    count_duplicates.resizable(True, False)
    
    count_duplicates.bind("<Escape>", lambda e: count_duplicates.destroy())
    
    a111 = tk.Label(count_duplicates, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT lastname, firstname, address1, address2, city, state, \
                    zipcode, phone1, phone2, emailaddress, notes, contactdate, confirmation, COUNT(*) \
                    FROM database \
                    GROUP BY lastname, firstname, address1, address2, city, state, \
                    zipcode, phone1, phone2, emailaddress, notes, contactdate, confirmation \
                    HAVING COUNT(*) > 1")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("SELECT lastname, firstname, address1, address2, city, state, \
                    zipcode, phone1, phone2, emailaddress, notes, contactdate, confirmation, COUNT(*) \
                    FROM database \
                    GROUP BY lastname, firstname, address1, address2, city, state, \
                    zipcode, phone1, phone2, emailaddress, notes, contactdate, confirmation \
                    HAVING COUNT(*) > 1")
    
    main_frame = Frame(count_duplicates)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    count_duplicates.bind("<Escape>", lambda e: count_duplicates.destroy())
    
    count_duplicates.mainloop()
  
def filter_phone1():
    input_filter_phone1_use = input_filter_phone1.get("1.0","end-1c")
    
    if (len(input_filter_phone1_use) == 3) & (input_filter_phone1_use.isnumeric() == True):
    
        filter_phone1 = tk.Tk()
        filter_phone1.title('Filter by Area Code of Phone 1 - ' + current_database_name)
        filter_phone1.geometry("1300x550+20+20")
        filter_phone1.resizable(True, False)
        
        filter_phone1.bind("<Escape>", lambda e: filter_phone1.destroy())
        
        a111 = tk.Label(filter_phone1, text="")
        a111.place(x=0, y=0)
        a111.focus_force()
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""SELECT * FROM database WHERE SUBSTRING(phone1, 1, 3) = ? \
                    ORDER BY lastname, firstname""",(input_filter_phone1_use,))
        
        rows=cur.fetchall()
        
        for row in rows:
            for col in row:
                print(col,end=' ')
                print()
            print("-------------------------")
        
        r_set=cur.execute("""SELECT * FROM database WHERE SUBSTRING(phone1, 1, 3) = ? \
                          ORDER BY lastname, firstname""",(input_filter_phone1_use,))
        
        main_frame = Frame(filter_phone1)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)

        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        
        i=0
        for name in r_set: 
            for j in range(len(name)):
                e = Label(second_frame, text=name[j], anchor='w') 
                e.grid(row=i, column=j)
            i=i+1

        con.commit()
        con.close()
        
        
        
        filter_phone1.mainloop()
    else:
        not_area_code1()
    
def filter_phone2():
    input_filter_phone2_use = input_filter_phone2.get("1.0","end-1c")
    
    if (len(input_filter_phone2_use) == 3) & (input_filter_phone2_use.isnumeric() == True):
        filter_phone2 = tk.Tk()
        filter_phone2.title('Filter by Area Code of Phone 2 - ' + current_database_name)
        filter_phone2.geometry("1300x550+20+20")
        filter_phone2.resizable(True, False)
        
        filter_phone2.bind("<Escape>", lambda e: filter_phone2.destroy())
        
        a111 = tk.Label(filter_phone2, text="")
        a111.place(x=0, y=0)
        a111.focus_force()
        
        con = sqlite3.connect(current_database) 
        cur = con.cursor()
        
        cur.execute("""SELECT * FROM database WHERE SUBSTRING(phone2, 1, 3) = ? \
                    ORDER BY lastname, firstname""",(input_filter_phone2_use,))
        
        rows=cur.fetchall()
        
        for row in rows:
            for col in row:
                print(col,end=' ')
                print()
            print("-------------------------")
        
        r_set=cur.execute("""SELECT * FROM database WHERE SUBSTRING(phone2, 1, 3) = ? \
                          ORDER BY lastname, firstname""",(input_filter_phone2_use,))
        
        main_frame = Frame(filter_phone2)
        main_frame.pack(fill=BOTH, expand=1)

        my_canvas = Canvas(main_frame)
        my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=RIGHT, fill=Y)

        my_canvas.configure(yscrollcommand=my_scrollbar.set)
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

        second_frame = Frame(my_canvas)

        my_canvas.create_window((0,0), window=second_frame, anchor="nw")
        
        i=0
        for name in r_set: 
            for j in range(len(name)):
                e = Label(second_frame, text=name[j], anchor='w') 
                e.grid(row=i, column=j)
            i=i+1

        con.commit()
        con.close()
        
        
        
        filter_phone2.mainloop()
    else:
        not_area_code2()

def sort_phone1():
    sort_phone1 = tk.Tk()
    sort_phone1.title('Sort by Phone 1 - ' + current_database_name)
    sort_phone1.geometry("1300x550+20+20")
    sort_phone1.resizable(True, False)
    
    sort_phone1.bind("<Escape>", lambda e: sort_phone1.destroy())
    
    a111 = tk.Label(sort_phone1, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT * FROM database ORDER BY phone1, lastname, firstname")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute('''SELECT * FROM database ORDER BY phone1, lastname, firstname''')
    
    main_frame = Frame(sort_phone1)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1
    con.commit()
    con.close()
    
    
    
    sort_phone1.mainloop()
    
def sort_phone2():
    sort_phone2 = tk.Tk()
    sort_phone2.title('Sort by Phone 2 - ' + current_database_name)
    sort_phone2.geometry("1300x550+20+20")
    sort_phone2.resizable(True, False)
    
    sort_phone2.bind("<Escape>", lambda e: sort_phone2.destroy())
    
    a111 = tk.Label(sort_phone2, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("SELECT * FROM database ORDER BY phone2, lastname, firstname")
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute('''SELECT * FROM database ORDER BY phone2, lastname, firstname''')
    
    main_frame = Frame(sort_phone2)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1
    con.commit()
    con.close()
    
    
    
    sort_phone2.mainloop()
    
def not_area_code1():
    not4 = tk.Tk()
    
    not4.title('Filter by Area Code of Phone 1')
    not4.geometry("700x550+750+20")
    not4.resizable(False, False)
    
    
    a111 = tk.Label(not4, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl3 = tk.Label(not4, text="Filter by Area Code", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=20)
    lbl3b = tk.Label(not4, text="of Phone 1:", font=("Helvetica", 10, 'bold'))
    lbl3b.place(x=80, y=40)
    
    lbl4 = tk.Label(not4, text="Enter a 3 digit number.", font=("Helvetica", 10))
    lbl4.place(x=260, y=40)
    
    
    not4.bind("<Escape>", lambda e: not4.destroy())
    
    not4.mainloop()
    
def not_area_code2():
    not5 = tk.Tk()
    
    not5.title('Filter by Area Code of Phone 2')
    not5.geometry("700x550+750+20")
    not5.resizable(False, False)
    
    
    a111 = tk.Label(not5, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl3 = tk.Label(not5, text="Filter by Area Code", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=20)
    lbl3b = tk.Label(not5, text="of Phone 2:", font=("Helvetica", 10, 'bold'))
    lbl3b.place(x=80, y=40)
    
    lbl4 = tk.Label(not5, text="Enter a 3-digit number.", font=("Helvetica", 10))
    lbl4.place(x=260, y=40)
    
    
    not5.bind("<Escape>", lambda e: not5.destroy())
    
    not5.mainloop()

def not_export():
    not6 = tk.Tk()
    
    not6.title('Export Data')
    not6.geometry("700x550+750+20")
    not6.resizable(False, False)
    
    
    a111 = tk.Label(not6, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    lbl3 = tk.Label(not6, text="Export Data:", font=("Helvetica", 10, 'bold'))
    lbl3.place(x=80, y=20)
    
    lbl4 = tk.Label(not6, text="Choose database before export.", font=("Helvetica", 10))
    lbl4.place(x=260, y=20)
    
    
    not6.bind("<Escape>", lambda e: not6.destroy())
    
    not6.mainloop()

def search_n():
    searchn = tk.Tk()
    searchn.title('Search Notes - ' + current_database_name)
    searchn.geometry("1300x550+20+20")
    searchn.resizable(True, False)
    
    searchn.bind("<Escape>", lambda e: searchn.destroy())
    
    a111 = tk.Label(searchn, text="")
    a111.place(x=0, y=0)
    a111.focus_force()
    
    search_notes_use = search_notes.get("1.0","end-1c")
    
    if search_notes_use == "":
        search_notes_use = "*"
    
    search_notes_use = '%' + search_notes_use + '%'
    
    con = sqlite3.connect(current_database) 
    cur = con.cursor()
    
    cur.execute("""SELECT id, lastname, firstname, notes \
                FROM database WHERE notes LIKE ? ORDER BY lastname, firstname""",(search_notes_use,))
    
    rows=cur.fetchall()
    
    for row in rows:
        for col in row:
            print(col,end=' ')
            print()
        print("-------------------------")
    
    r_set=cur.execute("""SELECT id, lastname, firstname, notes \
                      FROM database WHERE notes LIKE ? ORDER BY lastname, firstname""",(search_notes_use,))
    
    main_frame = Frame(searchn)
    main_frame.pack(fill=BOTH, expand=1)

    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

    my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

    second_frame = Frame(my_canvas)

    my_canvas.create_window((0,0), window=second_frame, anchor="nw")
    
    i=0
    for name in r_set: 
        for j in range(len(name)):
            e = Label(second_frame, text=name[j], anchor='w') 
            e.grid(row=i, column=j)
        i=i+1

    con.commit()
    con.close()
    
    
    
    searchn.mainloop()
    
def folder_contents():
    path = './'
    print("CSV files:\n----------")
    for x in os.listdir(path):
        if x.endswith(".csv"):
            print(x)
            
    contents = tk.Tk()
    contents.title('Existing CSV Files - ' + current_database_name)
    contents.geometry("700x550+20+20")
    contents.resizable(False, False)

    a112 = tk.Label(contents, text="")
    a112.place(x=0, y=0)
    a112.focus_force()
    
    contents.bind("<Escape>", lambda e: contents.destroy())
    
    path = './database1.csv'
    check_file1 = os.path.isfile(path)
    
    path = './database2.csv'
    check_file2 = os.path.isfile(path)
    
    path = './database3.csv'
    check_file3 = os.path.isfile(path)
    
    
    lbl1 = tk.Label(contents, text="Existing CSV Files", font=("Helvetica", 10, "underline"))
    lbl1.place(x=80, y=20)
    
    lbl11 = tk.Label(contents, text=u'\u2022', font=("Helvetica", 10))
    lbl11.place(x=80, y=60)
    lbl12 = tk.Label(contents, text=u'\u2022', font=("Helvetica", 10))
    lbl12.place(x=80, y=100)
    lbl13 = tk.Label(contents, text=u'\u2022', font=("Helvetica", 10))
    lbl13.place(x=80, y=140)
    
    lbl7 = tk.Label(contents, text="", font=("Helvetica", 10))
    lbl7.place(x=100, y=60)
    lbl8 = tk.Label(contents, text="", font=("Helvetica", 10))
    lbl8.place(x=100, y=100)
    lbl9 = tk.Label(contents, text="", font=("Helvetica", 10))
    lbl9.place(x=100, y=140)
    
    lbl110 = tk.Label(contents, text=u'\u2022', font=("Helvetica", 10))
    lbl110.place(x=80, y=200)
    lbl11 = tk.Label(contents, text="Current database: " + current_database + " - " + current_database_name, font=("Helvetica", 10))
    lbl11.place(x=100, y=200)
    
    if check_file1 == TRUE:
        lbl7.config(text="database1.csv")
    if check_file2 == TRUE:
        lbl8.config(text="database2.csv")
    if check_file3 == TRUE:
        lbl9.config(text="database3.csv")

    
    contents.mainloop()
    
    
    
def focus_next_window(event):
    event.widget.tk_focusNext().focus_force()
    return("break")


path = './data.dat'
check_file_data = os.path.isfile(path)
    
if check_file_data == FALSE:
    with open("data.dat", "a") as myfile:
        myfile.write("Database not named\n")
        myfile.write("Database not named\n")
        myfile.write("Database not named")

    
current_database = ""
current_database_name = ""

main_menu()