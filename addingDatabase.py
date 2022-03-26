# from sre_constants import BRANCH
from multiprocessing.dummy.connection import Connection
import tkinter as tk
from tkinter import END, Tk, ttk, messagebox
import sqlite3


login = tk.Tk()
login.title(" Student Management System")
login.geometry("700x400")

# for labels
appLabel = tk.Label (login, bg = 'black',text = "Student Management System", fg = "#ff853a", width = 25)
appLabel.config(anchor = 'center',font = ("Bold", 20)) 
appLabel.grid(row=0, columnspan=2, padx=(140, 20), pady=(10, 0))
usernameLabel =  tk.Label(login, text =  "Username:", width  = 10, anchor = 'center', font =  ("Bold", 15)).grid(row = 1, column = 0, padx =  (10, 0),pady = (100, 0))
passwordLabel =  tk.Label (login, text = "Password :", width = 10, anchor = 'center', font = ("Bold", 15)).grid(row = 2, column = 0, padx = (10, 0))

# for entry box
nameEntry = tk.Entry(login,width = 30)
nameEntry.grid(row=1, column=1, padx=(0,10), pady=(117, 20))

passEntry = tk.Entry(login,width = 30)
passEntry.grid(row=2, column=1, padx=(0,10), pady=20)

# for login button 
LogButton =  tk.Button (login, text = "Log In", command =  lambda: menu())
LogButton.grid(row = 3, column = 0, padx = (250,0) , pady=60)

# login.destroy()

# for Menu UI

def menu():
    global root
    root = tk.Tk()
    root.title("Menu")
    root.geometry("400x500") #wxh
    rootLabel = tk.Label (root, bg = 'black',text = "Menu", fg = "#ff8aba53a", width = 25)
    rootLabel.config(anchor = 'center',font = ("Bold", 20)) 
    rootLabel.grid(row=0, columnspan=2, padx=(4,4), pady=(0, 0))
    login.destroy()
     
    # add data 
    Add_Button =  tk.Button (root, anchor = 'center',font =  ("Bold", 15),text = "Add Student ",command =  lambda: addData())
    Add_Button.grid(row = 1, column = 0, padx = (55,0) , pady=30)
    
    # remove data 

    remove_Button =  tk.Button (root,anchor = 'center',font =  ("Bold", 15),text = " Delete Student",command =  lambda: removeData())
    remove_Button.grid(row = 2, column = 0, padx = (55,0) , pady=30)
    
    # show data 

    show_Button =  tk.Button (root, anchor = 'center',font =  ("Bold", 15),padx = 25,text = "View Student",command =  lambda: showData())
    show_Button.grid(row = 3, column = 0, padx = (55,0) , pady=30)

    # exit 

    exit_Button =  tk.Button (root, anchor = 'center',font =  ("Bold", 15),padx = 44,text = "Log Out",command =  lambda: exit())
    exit_Button.grid(row = 4, column = 0, padx = (60,0) , pady=30)
    
    # Button functions

    def exit():
        root.destroy()

def addData():
    global EnternameLabel,EnterNumberLabel,EnterFatherNumLabel,EnterBranchLabel,EnterYearLabel,Connection,TABLE_NAME,STUDENT_NAME, STUDENT_PHONE,FATHER_NUMBER,BRANCH,YEAR

    data = tk.Tk()
    data.title("AddData")
    data.geometry("800x500") #wxh
    

    # For database :
    #change
    sqlite3.Connection = sqlite3.connect('Student_management.db')
    TABLE_NAME = "management_table"
    STUDENT_NAME = "student_name"
    STUDENT_PHONE = "student_phone"
    FATHER_NUMBER = "fatherNumber"
    BRANCH = 'Branch'
    YEAR = 'Year'

    sqlite3.Connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_NAME +
                   " TEXT, " +
                   STUDENT_PHONE + " INTEGER, " + FATHER_NUMBER + " INTEGER, " +
                   BRANCH + " TEXT, " + YEAR + " INTEGER);")

    # for labels 
    dataLabel = tk.Label (data, bg = 'black',text = "Student Management System", fg = "#ff8aba53a", width = 25)
    dataLabel.config(anchor = 'center',font = ("Bold", 20)) 
    dataLabel.grid(row=0, columnspan=2, padx=(180,4), pady=(0, 0))

    # classes
    
    class student:
        studentName = ""
        studentNumber = 0
        fatherNumber = 0
        branchName = ""
        year = 0

        def __init__(self,studentName,studentNumber,fatherNumber,branchName,year) :
            self.studentName = studentName
            self.studentNumber = studentNumber
            self.fatherNumber = fatherNumber
            self.branchName = branchName
            self.year = year
        
        


    #

    EnternameLabel =  tk.Label(data, text =  "Enter Your Name :", width  = 20, font =  ("Normal", 15)).grid(row = 1, column = 0, padx =  (10, 0),pady = (40, 20))
    EnterNumberLabel =  tk.Label (data, text = "Enter Your Number :", width = 20, font = ("Normal", 15)).grid(row = 2, column = 0, padx = (10, 0),pady=(10,40))
    EnterFatherNumLabel =  tk.Label(data, text =  "Enter Father Number:", width  = 20, font =  ("Normal", 15)).grid(row = 3, column = 0, padx =  (10, 0),pady = (10, 40))
    EnterBranchLabel =  tk.Label (data, text = "Enter Branch :", width = 20, font = ("Normal", 15)).grid(row = 4, column = 0, padx = (10, 0),pady=(10,40))
    EnterYearLabel =  tk.Label(data, text =  "Enter Year :", width  = 10,font =  ("Normal", 15)).grid(row = 5, column = 0, padx =  (10, 0),pady = (10,40))
        
    # for entryboxes

    EnternameLabel = tk.Entry(data,width = 30)
    EnternameLabel.grid(row=1, column=1, padx=(0,10), pady=(45, 20))

    EnterNumberLabel = tk.Entry(data,width = 30)
    EnterNumberLabel.grid(row=2, column=1, padx=(0,10), pady=(5, 20))

    EnterFatherNumLabel = tk.Entry(data,width = 30)
    EnterFatherNumLabel.grid(row=3, column=1, padx=(0,10), pady=(5, 20))

    EnterBranchLabel = tk.Entry(data,width = 30)
    EnterBranchLabel.grid(row=4, column=1, padx=(0,10), pady=(5, 20))

    EnterYearLabel = tk.Entry(data,width = 30)
    EnterYearLabel.grid(row=5, column=1, padx=(0,10), pady=(5, 20))


    def takeInput():
        global EnternameLabel,EnterNumberLabel,EnterFatherNumLabel,EnterBranchLabel,EnterYearLabel
        global list
        global TABLE_NAME,STUDENT_NAME,STUDENT_PHONE,FATHER_NUMBER, BRANCH ,YEAR

        name = EnternameLabel.get()
        EnternameLabel.delete(0,tk.END)

        studentNumber = EnterNumberLabel
        EnterNumberLabel.delete(0,tk.END)

        fatherNumber = EnterFatherNumLabel
        EnterFatherNumLabel.delete(0,tk.END)

        branch = EnterBranchLabel.get()
        EnterBranchLabel.delete(0,tk.END)

        year = EnterYearLabel.get()
        EnterYearLabel.delete(0,tk.END)

        sqlite3.Connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_PHONE + ", " + FATHER_NUMBER + ", " +
                       BRANCH + " , " + YEAR + " ) VALUES ( '"
                       + name + "', '" + str(studentNumber) + "', '" +
                       str(fatherNumber) + "', " + branch + "'," + str(year) + " ); ")

    SubButton =  tk.Button (data, text = "Submit",font = ("normal",15), command =  lambda: show())
    SubButton.grid(row = 6, column = 0, padx = (310,20) , pady= (3,0))
    
    def show():
        messagebox.showinfo("Success", "Data Saved Successfully.")
        root.destroy()
        data.destroy()
          
            
def showData():
    secondWindow = tk.Tk()
    secondWindow.title("Display Data")
    secondWindow.geometry("800x500") #wxh
    secondWindow = tk.Label (secondWindow, bg = 'black',text = " Data of Students ", fg = "#ff853a", width = 25)
    secondWindow.config(anchor = 'center',font = ("Bold", 20)) 
    secondWindow.grid(row=0, columnspan=2, padx=(200, 20), pady=(10, 0))

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four","five")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="Student Number")
    tree.heading("three", text="Father Number")
    tree.heading("four", text="Branch")
    tree.heading("five", text="Year")

    cursor = sqlite3.Connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
                    values=(row[1], row[2],
                            row[3], row[4],row[5]))
        i = i + 1

    # root.destroy
    tree.pack()
    secondWindow.mainloop()
    




login.mainloop()

