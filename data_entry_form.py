import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import openpyxl
import os
filepath = "./data.xlsx"

def enter_data():
    #print("hi")
    accept_var = accept_term.get()
    if accept_var == "Accepted":
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        title = title_combobox.get()
        age = age_spinbox.get()
        nationality = nationality_combobox.get()
        registation_status = reg_status_var.get()
        numcourses = numcourses_spinbox.get()
        numsemister = numsemister_spinbox.get()
        if not os.path.exists(filepath):
            workbook = openpyxl.Workbook()
            sheet = workbook.active
            heading = ['First Name','Last Name','Title','Age','Nationality','Courses','Semesters','Registration Status']
            sheet.append(heading)
            workbook.save(filepath)
        workbook = openpyxl.load_workbook(filepath)
        sheet = workbook.active
        sheet.append([first_name,last_name,title,age,nationality,numcourses,numsemister,registation_status])
        workbook.save(filepath)
    else:
        messagebox.showwarning(title="Error", message="Please enter a valid input.")

window = tkinter.Tk()
window.title("Data Entry Form")
frame = tkinter.Frame(window)
frame.pack()

user_info_frame = tkinter.LabelFrame(frame,text="User Info")
user_info_frame.grid(row=0,column=0,padx=20,pady=20)

first_name_lable = tkinter.Label(user_info_frame,text="First Name")
first_name_lable.grid(row=0,column=0)
last_name_lable = tkinter.Label(user_info_frame,text="Last Name")
last_name_lable.grid(row=0,column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1,column=0)
last_name_entry.grid(row=1,column=1)

title_label = tkinter.Label(user_info_frame,text="Title")
title_combobox = ttk.Combobox(user_info_frame,values=['','Mr','Ms','Dr'])
title_label.grid(row=0,column=2)
title_combobox.grid(row=1,column=2)

age_label = tkinter.Label(user_info_frame,text="Age")
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18,to=111)
age_label.grid(row=2,column=0)
age_spinbox.grid(row=3,column=0)

nationality_label = tkinter.Label(user_info_frame,text="Nationality")
nationality_combobox = ttk.Combobox(user_info_frame,values=['Bangladeshi','Indian','Arab'])
nationality_label.grid(row=2,column=1)
nationality_combobox.grid(row=3,column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#saving course info
course_frame = tkinter.LabelFrame(frame)
course_frame.grid(row=1,column=0,padx=20,pady=20, sticky=tkinter.NSEW)
registered_label = tkinter.Label(course_frame,text="Registration Status")
reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(course_frame,onvalue="Registered",offvalue="Not Registered" ,text="Currently Registered",variable=reg_status_var)
registered_label.grid(row=0,column=0)
registered_check.grid(row=1,column=0)

numcourses_label = tkinter.Label(course_frame,text="Number of Courses")
numcourses_spinbox = tkinter.Spinbox(course_frame,from_=0,to=100)
numcourses_label.grid(row=0,column=1)
numcourses_spinbox.grid(row=1,column=1)

numsemister_label = tkinter.Label(course_frame,text="Number of Semisters")
numsemister_spinbox = tkinter.Spinbox(course_frame,from_=0,to=100)
numsemister_label.grid(row=0,column=2)
numsemister_spinbox.grid(row=1,column=2)

for widget in course_frame.winfo_children():
    widget.grid_configure(padx=10,pady=5)

#accept  agriment
terms_frame = tkinter.LabelFrame(frame,text="Terms & Conditions")
terms_frame.grid(row=2,column=0,padx=20,pady=10,sticky=tkinter.NSEW)

accept_term = tkinter.StringVar(value="Not Accepted")
term_check = tkinter.Checkbutton(terms_frame,text="I accept the terms and conditions",onvalue="Accepted",offvalue="Not Accepted",variable=accept_term)
term_check.grid(row=0,column=0)

button = tkinter.Button(frame,text="Submit",command = enter_data)
button.grid(row=3,column=0,padx=20,pady=10,sticky=tkinter.NSEW)


window.mainloop()