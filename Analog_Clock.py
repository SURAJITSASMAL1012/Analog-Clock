from tkinter import *
#from tkinter import ttk
from PIL import Image,ImageDraw,ImageTk
from datetime import*
import time
from math import*
class analog_clock:
    def __init__(self,root):
        self.root=root
        self.root.title("Analog Clock")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="#021e2f")
        title=Label(self.root,text="Analog Clock | By Surajit",font=("times new roman",30,"bold"),bg="#04444a",fg="white").place(x=0,y=0,relwidth=1)
        self.lbl=Label(self.root,bg="white",bd=20,relief=RAISED)
        self.lbl.place(x=450,y=150,height=400,width=400)
        #self.clock_img()
        self.working()
    def clock_img(self,hr, min_ , sec_):
        clock=Image.new("RGB",(400,400),(255,255,255))
        draw=ImageDraw.Draw(clock)
        bg=Image.open("cl.jpg")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))
        #🕐🕐Formula For roatate the Clock🕐🕐
        '''angle_radians = angle_degrees * math.pi / 180
        line_length=100
        center_x=250
        center_y=250
        end_x=center_x + line_length *math.cos(angle_radians)
        end_y=center_y - line_length * math.sin(angle_radians)'''
        #Hour Line🐤🐤🐤🕐🕐🕐
        #  x,y,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="black",width=4)
        
        #Minute Line🕐🕐🕐🕐
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="blue",width=3)

        #Second Line 🕐🕐🕐🕐🕐
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="green",width=4)

        draw.ellipse((195,195,210,210),fill="black")
        clock.save("clock_new.png")

    def working(self):
        h=datetime.now().hour
        m=datetime.now().minute
        s=datetime.now().second
        hr = (h/12)*360
        min_ =(m/60)*360
        sec_ =(s/60)*360
        self.clock_img(hr, min_,sec_)
        self.img=ImageTk.PhotoImage(file="clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)

root=Tk()
object=analog_clock(root)
root.mainloop()
