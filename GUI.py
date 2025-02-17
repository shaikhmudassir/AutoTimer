from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from Scroll import Scrollable
import json, time

root = Tk()
def handle_login():
    email = email_input.get()
    password = password_input.get()

    if (email == 'danish' and password == '1234') or (email in ['amaan','pes','faiz'] and password == '321'):
        root.destroy()
        import tasks
        
    else:
        messagebox.showerror('Error','Login Failed')
  
root.title('Login Form')
#root.iconbitmap('favicon.ico')

root.geometry('1000x600')

root.configure(background='#0096DC')
img = Image.open('1.jpg')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)

img_label = Label(root,image=img)
img_label.pack(pady=(100,100))

text_label = Label(root,text='Timetracker',fg='white',bg='#0096DC')
text_label.pack()
text_label.config(font=('verdana',24))

email_label = Label(root,text='Enter User Name',fg='white',bg='#0096DC')
email_label.pack(pady=(20,5))
email_label.config(font=('verdana',12))

email_input = Entry(root,width=50)
email_input.pack(ipady=6,pady=(1,15))

password_label = Label(root,text='Enter Password',fg='white',bg='#0096DC')
password_label.pack(pady=(20,5))
password_label.config(font=('verdana',12))

password_input = Entry(root,width=50)
password_input.pack(ipady=6,pady=(1,15))

login_btn = Button(root,text='Login Here',bg='white',fg='black',width=20,height=2,command=handle_login)
login_btn.pack(pady=(10,20))
login_btn.config(font=('verdana',10))



root.mainloop()
