from tkinter import *
from PIL import ImageTk, Image
from datetime import datetime
import pytz
import time

root=Tk()
root.geometry("600x450")



label2=Label(root,text="india", bg="white", fg="black")
label2.place(relx=0.1, rely=0.1, anchor=CENTER)



label3=Label(root,text="usa", bg="white", fg="black")
label3.place(relx=0.8, rely=0.1, anchor=CENTER)


labelindia=Label(root,text="india", bg="white", fg="black")
labelindia.place(relx=0.1, rely=0.6, anchor=CENTER)



labelusa=Label(root,text="usa", bg="white", fg="black")
labelusa.place(relx=0.8, rely=0.6, anchor=CENTER)



img=ImageTk.PhotoImage(Image.open("clock.jpg"))

labelimage1=Label(root, image=img, bg="lightblue", fg="black")
labelimage1.place(relx=0.1, rely=0.3, anchor=CENTER)


labelimage2=Label(root, image=img, bg="lightblue", fg="black")
labelimage2.place(relx=0.8, rely=0.3, anchor=CENTER)


class india():
    def times(self):
        home=pytz.timezone("Asia/Kolkata")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        labelindia["text"]=current_time
        labelindia.after(200,self.times)
        
        
class usa():
    def times(self):
        home=pytz.timezone("US/Central")
        local_time=datetime.now(home)
        current_time=local_time.strftime("%H:%M:%S")
        labelusa["text"]=current_time
        labelusa.after(200,self.times)
        
        
obj_india=india()
obj_usa=usa()




button1=Button(root,text="show time", command=obj_india.times)
button1.place(relx=0.3, rely=0.9, anchor=CENTER)



button2=Button(root,text="show time", command=obj_usa.times)
button2.place(relx=0.9, rely=0.9, anchor=CENTER)

        
root.mainloop()