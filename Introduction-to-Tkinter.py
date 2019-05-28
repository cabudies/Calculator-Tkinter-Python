
## Entry program
# import tkinter as tk
#
# mainWindow = tk.Tk()
# mainWindow.title("Sample Window")
#
# heading_label = tk.Label(mainWindow, text="Hello World")
# heading_label.pack()
#
# name_field = tk.Entry(mainWindow)
# name_field.pack()
#
# def takeValueInput():
#     name = name_field.get()
#     print(name)
#
# button = tk.Button(mainWindow, text="Get Value",
#                    command=lambda: takeValueInput())
# button.pack()
#
# mainWindow.mainloop()


## Simple Calculator


import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Calculator")

first_number_label = tk.Label(mainWindow, text="Enter first number",
                              pady=(10), padx=(20))

first_number_label.pack()

first_number_entry = tk.Entry(mainWindow)
first_number_entry.pack()

second_number_label = tk.Label(mainWindow, text="Enter second number",
                               pady=(10), padx=(20))
second_number_label.pack()

second_number_entry = tk.Entry(mainWindow)
second_number_entry.pack()


operations_label = tk.Label(mainWindow, text="Operations",
                            pady=(10), padx=(20))
operations_label.pack()

add_button = tk.Button(mainWindow, text="+",pady=(5), padx=(10),
                       command=lambda :addition())
add_button.pack()

minus_button = tk.Button(mainWindow, text="-",pady=(5), padx=(10))
minus_button.pack()

multiply_button = tk.Button(mainWindow, text="*",pady=(5), padx=(10))
multiply_button.pack()

divide_button = tk.Button(mainWindow, text="/",pady=(5), padx=(10))
divide_button.pack()

result_label = tk.Label(mainWindow, text="Operation result is:",
                        padx=(20), pady=(20))
result_label.pack()

def addition():
    first = int(first_number_entry.get())
    second = int(second_number_entry.get())
    result = first + second
    # print("Result is: ", result)
    result_label.config(text="Operation result is:" + str(result))

mainWindow.mainloop()















## second program

# import tkinter
# from tkinter import Entry
#
# root = tkinter.Tk()
#
# appLabel = tkinter.Label(root, text="Student Management System")
# appLabel.config(font=(20))
# appLabel.pack()
#
# nameLabel = tkinter.Label(root, text="Enter your name")
# nameLabel.pack()
#
# nameEntry = Entry(root)
# nameEntry.pack()
#
# def takeUserInput():
#     name = nameEntry.get()
#     print("Hello", name)
#
# okButton = tkinter.Button(root, text="Save Details", command=lambda: takeUserInput())
# okButton.pack()
#
# root.mainloop()











# Exercise
# two values input from the user and 4 buttons to perform basic maths operations.
# the functions of the buttons should be defined inside a module.


# import tkinter
# from tkinter import *
#
# mainWindow = tkinter.Tk()
# mainWindow.title("Sample Grid")
#
# headingLabel = tkinter.Label(mainWindow, text="Grid Layout Sample", anchor="w")
# headingLabel.grid(row=0, columnspan=2, padx=(30, 30), pady=(20, 10))
#
# textUsername = tkinter.Label(mainWindow, text="Enter your text")
# textUsername.grid(row=1, column=0)
#
# usernameEntry = Entry(mainWindow)
# usernameEntry.grid(row=1, column=1)
#
# mainWindow.mainloop()


# import sqlite3
#
# connection = sqlite3.connect('student.db') # file name
# print("Database opened successfully.")
#
# TABLE_NAME = "student_table"
# STUDENT_ID = "student_id"
# STUDENT_NAME = "student_name"
# STUDENT_COLLEGE = "student_college"
# STUDENT_ADDRESS = "student_address"
# STUDENT_PHONE = "student_phone"
#
# connection.execute(" CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " ( " + STUDENT_ID +
#                    " INTEGER PRIMARY KEY AUTOINCREMENT, " +
#                    STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
#                    STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);")
#
# def insert_record(name, college, address, phone):
#     connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
#                        STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
#                         STUDENT_PHONE + " ) VALUES ( '" + name +"', '"+college+"', "
#                                         "'"+address+"', "+str(phone)+" ); ")
#     connection.commit()
#     print("The data has been saved successfully.")
#
# def display_record():
#     cursor = connection.execute("SELECT * FROM " + TABLE_NAME + " ;")
#
#     for row in cursor:
#         print("Student id is: ", row[0])
#         print("Student name is: ", row[1])
#         print("Student college is: ", row[2])
#
# import tkinter as tk
# from tkinter import Entry
#
# root = tk.Tk()
#
# root.title("Tkinter Application")
#
# appLabel = tk.Label(root, text="Hello World")
# appLabel.pack()
#
# nameEntry = Entry(root)
# nameEntry.pack()
#
# def getUsername():
#     name = nameEntry.get()
#     print(name)
#     college = "DIT"
#     phone = 123456
#     address = "Dehradun"
#     insert_record(name, college, address, phone)
#
# button = tk.Button(root, text="Ok Button", command=lambda : getUsername())
# button.pack()
#
# display_button = tk.Button(root, text="Display Data", command= lambda : display_record())
# display_button.pack()
#
# root.mainloop()
























