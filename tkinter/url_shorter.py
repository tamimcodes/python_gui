import tkinter
import pyshorteners

window = tkinter.Tk()
window.title("URL Shortener")
window.geometry("400x300")

#defigning shorten function
def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_entry.get())
    short_entry.insert(0,short_url)


#adding widgets
long_label = tkinter.Label(window,text="Enter your Long URL",font=("Arial",20))
long_entry = tkinter.Entry(window)
short_label = tkinter.Label(window,text="Output Shortened URL",font=("Arial",20))
short_entry = tkinter.Entry(window)
short_btn = tkinter.Button(window,text="Shorten URL",command=shorten,font=("Arial",16))
exit_btn = tkinter.Button(window,text="Exit",command=window.destroy,font=("Arial",16))
frame1 = tkinter.Frame(window,height=15)
frame2 = tkinter.Frame(window,height=15)
frame3 = tkinter.Frame(window,height=15)
frame4 = tkinter.Frame(window,height=15)


#positionaing widgets in window
long_label.pack()
frame1.pack()
long_entry.pack(fill=tkinter.X)
frame2.pack()
short_btn.pack()
frame3.pack()
short_label.pack()
frame4.pack()
short_entry.pack(fill=tkinter.X)
exit_btn.pack()

window.mainloop()
