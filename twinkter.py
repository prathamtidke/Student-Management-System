
from logging import root
from os import remove
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from sqlite3.dbapi2 import sqlite_version
from turtle import width

from tkinter2 import STUDENT_PHONE, destroyRootWindow, takeNameInput

login = tk.Tk()
# set window title
login.title("Student Management System")
login.geometry("700x500") # width x height
# Label is used to display text
appLabel = tk.Label (login, text = "Student Management System", fg = "#06a099", width = 25) 
appLabel.config(font = ("Bold", 20)) 
appLabel.grid (row = 0, columnspan = 2, padx = (5, 5), pady = (10, 0))
usernameLabel =  tk.Label(login, text =  "Username:", width  = 10, anchor = 'center', font =  ("Bold", 15)).grid(row = 1, column = 0, padx =  (10, 0),pady = (120, 0))
passwordLabel =  tk.Label (login, text = "Password :", width = 10, anchor = 'center', font = ("Bold", 15)).grid(row = 2, column = 0, padx = (10, 0))

username  = tk.Entry(login, width = 30) 
password= tk.Entry (login, width=30)

# write funtion for menu 
LogButton =  tk.Button (login, text = "Log In", command =  lambda: third())
LogButton.grid(row = 3, column = 0, padx = (250,0) , pady=60)

##

connection = sqlite3.connect('studentManagement.db')

def third():
    root = tk.Tk()
    root.title("StudentManagement")

    connection = sqlite3.connect('studentManagement.db')

    TABLE_Name = "StudentManagement_table"
    STUDENT_NAME =  " Student Name "
    STUDENT_NUMBER = " Student Number"
    FATHER_NUMBER = "Father Number"
    BRANCH_NAME = " Branch Name "
    YEAR = "Year"

    connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_NUMBER +
                   " INTEGER, " + STUDENT_NAME + " TEXT, " + FATHER_NUMBER + " INTEGER, " +
                   BRANCH_NAME + " TEXT, " + YEAR + " INTEGER);")

    appLabel = tk.Label(root, text = "Student Management System", fg =  "#06a099",width = 35)
    appLabel.config (font = ('Normal', 30))
    appLabel.grid (row = 0, columnspan = 2, padx = (15, 15), pady = (50, 0))

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

        nameLabel = tk.Label (root, text =  " Enter your name ", width = 40, anchor = 'w', 
        font = ("Normal", 12)).grid (row = 1, column = 0, padx =  (10,0),pady = (60,0))

        phoneLabel = tk.Label (root, text =  " Enter your Number ", width = 40, anchor = 'w', 
        font = ("Normal", 12)).grid (row = 2, column = 0, padx =  (10,0),pady = (60,0))

        fatherLabel = tk.Label (root, text =  " Enter your father number ", width = 40, anchor = 'w', 
        font = ("Normal", 12)).grid (row = 3, column = 0, padx =  (10,0),pady = (60,0))

        branchLabel =  tk.Label (root, text =  " Enter your Branch name ", width = 40, anchor = 'w', 
        font = ("Normal", 12)).grid (row = 4, column = 0, padx =  (10,0),pady = (60,0))
        
        yearLabel = tk.Label (root, text =  " Enter your Year ", width = 40, anchor = 'w', 
        font = ("Normal", 12)).grid (row = 5, column = 0, padx =  (10,0),pady = (60,0))

        nameEntry = tk.Entry (root, width = 30)
        phoneEntry = tk.Entry (root, width = 30)
        fatherphoneEntry = tk.Entry (root, width = 30)
        branchEntry = tk.Entry (root, width = 30)
        yearEntry = tk.Entry (root, width = 30)

        nameEntry.grid(row = 1, column = 1, padx =(0,10), pady = (30, 20))
        phoneEntry.grid(row = 2, column = 1, padx =(0,10), pady =  20)
        fatherphoneEntry.grid(row = 3, column = 1, padx =(0,10), pady = 20)
        branchEntry.grid(row = 4, column = 1, padx =(0,10), pady = 20)
        yearEntry.grid(row = 5, column = 1, padx =(0,10), pady = 20)

        def takeNameInput ():
            global nameEntry, fatherphoneEntry, phoneEntry, branchEntry,yearEntry
            global list
            global TABLE_NAME, STUDENT_NAME, STUDENT_NUMBER, YEAR, FATHER_NUMBER,BRANCH_NAME

            username = nameEntry.get() 
            nameEntry.delete (0, tk.END)
            phoneEntry = phoneEntry.get()
            phoneEntry.delete (0, tk.END) 
            fatherphoneEntry = fatherphoneEntry.get()
            fatherphoneEntry.delete(0,tk.END)
            branchEntry = branchEntry.get()
            branchEntry.delete(0, tk.END)
            yearEntry = yearEntry.get()
            yearEntry.delete(0,tk.END)

            connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                       STUDENT_NUMBER + ", " + BRANCH_NAME + ", " +
                       FATHER_NUMBER + " ) VALUES ( '"
                       + username + "', '" + YEAR + "', '" +
                        " + str(phone) + " ); 
            connection.commit()
            messagebox.showinfo("Data Saved Successfully.")
            root.destroy()

        def destroyRootWindow():

            root.destroy()
            secondWindow = tk.Tk()

            secondWindow.title("Display results")

            appLabel = tk.Label(secondWindow, text="Student Management System",
                                fg="#06a099", width=40)
            appLabel.config(font=("Sylfaen", 30))
            appLabel.pack()

            tree = ttk.Treeview(secondWindow)
            tree["columns"] = ("one", "two", "three", "four","five")

            tree.heading("one", text="Student Name")
            tree.heading("two", text="Student  Number")
            tree.heading("three", text="Branch Name")
            tree.heading("four", text=" Father Phone Number")
            tree.heading("five", text=" Year")

            cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
            i = 0

            for row in cursor:
                tree.insert('', i, text="Student " + str(row[0]),
                            values=(row[1], row[2],
                                    row[3], row[4],row[5]))
                i = i + 1

            # root.destroy
            tree.pack()
            secondWindow.mainloop()

            button = tk.Button(root, text="Add Data", command=lambda: takeNameInput())
            button.grid(row=5, column=0, pady=30)

            displayButton = tk.Button(root, text="Display result",
                                command=lambda: destroyRootWindow())
            displayButton.grid(row=5, column=1)

        def show_data():
            root = tk.Tk()
            secondWindow = tk.Tk()
            secondWindow.title("Sisplay result")
            appLabel = tk.Label(secondWindow, text="Student Management System",
                                fg="#06a099", width=40)
            appLabel.config(font=("Sylfaen", 30))
            appLabel.pack()

            tree = ttk.Treeview(secondWindow)
            tree["columns"] = ("one", "two", "three", "four","five")

            tree.heading("one", text="Student Name")
            tree.heading("two", text="Student  Number")
            tree.heading("three", text="Branch Name")
            tree.heading("four", text=" Father Phone Number")
            tree.heading("five", text=" Year")

            cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
            i = 0

            for row in cursor:
                tree.insert('', i, text="Student " + str(row[0]),
                            values=(row[1], row[2],
                                    row[3], row[4],row[5]))
                i = i + 1
            root.destroy()
            tree.pack()
            secondWindow.mainloop()

        def remove():
            STUDENT_PHONE = "Student phone"
            remove = tk.Tk()
            remove.title("remove")
            appLabel = tk.Label(remove, text="Student Detail delete",
                                fg="#06a099", width=40)
            appLabel.config(font=("Sylfaen", 30))
            appLabel.grid(row = 1,columnspan= 2, padx = (5,5),pady = (10,0))

            usernameLabel = tk.Label(remove , text = "emailid", width = 10,anchor = 'w',
            font = ("Normal",12)).grid(row = 1,column = 0,padx = (50,0), pady = (10,0))


            usernameEntry1 = tk.Entry(remove,width = 30)
            usernameEntry1.grid(row = 1,column = 1,padx = (0,10),pady = (30,20))

        # def takeNameInput():
        #     emailid = usernameEntry1.get()
        #     usernameEntry1.delete(0,tk.END)

login.mainloop()









