import tkinter
from tkinter import messagebox

window = tkinter.Tk()
window.title("Login form")
window.geometry("340x440")
window.configure(bg="black")

def login():
    #print("Login Successful")
    username = 'fahim'
    password = '1234'
    if username_entry.get() == username and password_entry.get() == password:
        #print('Login Successful')
        messagebox.showinfo(title='Login Success',message='You are now logged in')
    else:
        #print('Login Failed')
        messagebox.showerror(title='Login Failed',message='Wrong username or password')

frame = tkinter.Frame(window,bg="black")

#cteating widgets
login_label = tkinter.Label(frame, text="Login", bg="black", fg="white" ,font=("Arial", 30))
username_label = tkinter.Label(frame, text="Username" , bg="black" ,fg="white",font=("Arial", 16))
username_entry = tkinter.Entry(frame,font=("Arial", 16))
password_label = tkinter.Label(frame, text="Password", bg="black", fg="white",font=("Arial", 16))
password_entry = tkinter.Entry(frame,show="*",font=("Arial", 16))
login_button = tkinter.Button(frame, text="Login",bg="#ff3399" ,fg="white",font=("Arial", 16),command=login)

#placing widgets on the screen
login_label.grid(row=0, column=0,columnspan=2, sticky="news",pady=40)
username_label.grid(row=1, column=0, pady=20)
username_entry.grid(row=1, column=1)
password_label.grid(row=2, column=0,pady=20)
password_entry.grid(row=2, column=1)
login_button.grid(row=3, column=0 ,columnspan=2,pady=30)

frame.pack()

window.mainloop()