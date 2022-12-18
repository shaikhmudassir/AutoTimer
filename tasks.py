from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox
from Scroll import Scrollable
import json, time

root2 = Tk()
root2.geometry('1000x600')
root2.configure(background='#0096DC')

img = Image.open('1.jpg')
resized_img = img.resize((70,70))
img = ImageTk.PhotoImage(resized_img)
img_label = Label(root2,image=img)
img_label.pack(pady=(10,10))

text_label = Label(root2,text='Timetracker',fg='white',bg='#0096DC')
text_label.pack(pady=(10,10))
text_label.config(font=('verdana',30))

body = Frame(root2,background='#0096DC')

body.pack(fill=BOTH, expand=True)
scrollable_body = Scrollable(body)
    
def start():
    for widgets in scrollable_body.winfo_children():
      widgets.destroy()

    f = open('activities.json')
    data = json.load(f)
            
    for app in data['activities']:
        h,m,s = 0,0,0
        for i in app['time_entries']:
            h+=i['hours']
            m+=i['minutes']
            s+=i['seconds']

        w = PanedWindow(scrollable_body)  
        w.pack(fill = BOTH, expand = 0, padx=3, pady=3)  

        app_name = Label(w,text=app['name'], anchor="w", font='verdana 12 bold')
        app_name.pack(fill = BOTH, expand = False)
        h_label = Label(w,text='\thours: ' + str(h), anchor="w", font='verdana 11')
        h_label.pack(fill = BOTH, expand = False)
        m_label = Label(w,text='\tminutes: ' + str(m), anchor="w", font='verdana 11')
        m_label.pack(fill = BOTH, expand = False)
        s_label = Label(w,text='\tseconds: ' + str(s), anchor="w", font='verdana 11')
        s_label.pack(fill = BOTH, expand = False, pady=3)

        scrollable_body.update()

    root2.after(10000, start)

start()
root2.mainloop()
