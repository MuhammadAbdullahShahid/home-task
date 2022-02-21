####
import time
import tkinter as tk
from tkinter import *
import pytz
from datetime import datetime

##background_color = input("Enter a color for background: ")
##color = input("Enter text color: ")

##root = tk.Tk()
##root.attributes('-fullscreen', True)
##root.configure(background="lightgreen")

##def tick(time1 =''):    
##    time2 = time.strftime('%I:%M:%S')
##    if time2 != time1:
##        time1 = time2
##        clock_frame.config(text=time2)
##    clock_frame.after(200, tick)

##def fajar_namaz():
##    fajar.config(text="فجر              05:40 ")
##    
##def Duhr_namaz():
##    duhr.config(text="ظهر             04:30 ")
##
##
##def Asar_namaz():
##    asar.config(text="عصر             05:20")
##    
##def Maghrib_namaz():
##    maghrib.config(text="مغرب            06:10")
##
##def Esha_namaz():
##    esha.config(text="عشاء             08:40")
##
##def Jummah_namaz():
##    esha.config(text="جمعہ             02:40")


def tick():
    home=pytz.timezone("Asia/Karachi")
    local_time= datetime.now(home)
    current_time=local_time.strftime('%I:%M:%S')
    clock_frame.config(text=current_time)
    clock_frame.after(200, tick)
    
def pak():

    

##    global clock_frame

    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##    def tick():
##        home=pytz.timezone("Asia/Kolkata")
##        local_time= datetime.now(home)
##        current_time=local_time.strftime('%I:%M:%S')
##        clock_frame.after(200, tick)
                
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        


    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)

    ##Slider
    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=630)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)
##    tick()

    root.mainloop()

#    time()
    
##pak()

    
def pak1():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='blue',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=630)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def pak2():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='white',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=630)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def pak3():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=630)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def pak4():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=630)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def pak5():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='grey',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=630)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()


def city():
    tree=Tk()
    tree.title("Main Page")
    tree.attributes('-fullscreen', True)
    tree.configure(bg='#25383C')
    lbl=Label(tree,text="",font=('arial','30','bold'),bg='#25383C',fg='black')
    lbl.pack()
##
##    import time
##
####    root = Tk()
####    root.title("slide or ticker")
###    root.attributes("-fullscreen",True)
###    root.configure(bg="blue")
##    char_index = 0
##    text = " "
##    slide_text = ['a','l','','','p','m','g','o','r','w','s','f','q','v','y','e','z','c','n','x','d','t','u','h','b']
####mutiullah abdullah shahid abcdef #you should make a list here to show different values or labels
##
##    def slide():
##        global char_index , text, slide_text
##        if char_index >= len(slide_text):
##            char_index = 0
##            text = " "
##            slider.config(text = text)
##        else:
##            text = text + slide_text[char_index]
##            slider.configure(text = text)
##            char_index = char_index + 1
##        slider.after(400, slide)
##       
##    slider = Label(tree, text = text, font=("Arial", 25, "bold"))
##    slider.pack
###    slider.place(x = 30 , y = 60)
##
##    slide()
###    root.mainloop()


    z='#808000'
    lbl=Label(tree,text="City Of Pakistan",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    btn=Button(tree,text="Karachi",font=('arial','30','bold'),activebackground='green',bg=z,fg='black',command=pak)
    btn.pack()
    btn=Button(tree,text="Lahore",font=('arial','30','bold'),activebackground='green',bg=z,command=pak1)
    btn.pack()
    btn=Button(tree,text="Islamabad",font=('arial','30','bold'),activebackground='green',bg=z,command=pak2)
    btn.pack()
    btn=Button(tree,text="Faisalabad",font=('arial','30','bold'),activebackground='green',bg=z,command=pak3)
    btn.pack()
    btn=Button(tree,text="Multan",font=('arial','30','bold'),activebackground='green',bg=z,command=pak4)
    btn.pack()
    btn=Button(tree,text="Gujranwala",font=('arial','30','bold'),activebackground='green',bg=z,command=pak5)
    btn.pack()
    btn=Button(tree,text="Back",font=('arial','30','bold'),bg=z,fg='black',command=tree.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.pack()
    tree.mainloop()
def tick():
    home=pytz.timezone("Pacific/Auckland")
    local_time= datetime.now(home)
    current_time=local_time.strftime('%I:%M:%S')
    clock_frame.config(text=current_time)
    clock_frame.after(200, tick)
    
def new():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        


    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()



    
def new1():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        

    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='white',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def new2():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        


    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def new3():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='grey',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def new4():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='blue',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def new5():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()


def city1():
    tree1=Tk()
    tree1.title("Main Page")
    tree1.attributes('-fullscreen', True)
    tree1.configure(bg='#25383C')
    z='#808000'
    lbl=Label(tree1,text="",font=('arial','30','bold'),bg='#25383C',fg='black')
    lbl.pack()
    lbl=Label(tree1,text="City Of Newzeland",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    btn=Button(tree1,text="Auckland",font=('arial','30','bold'),activebackground='green',bg=z,fg='black',command=new)
    btn.pack()
    btn=Button(tree1,text="Wellington",font=('arial','30','bold'),activebackground='green',bg=z,command=new1)
    btn.pack()
    btn=Button(tree1,text="Christchurch",font=('arial','30','bold'),activebackground='green',bg=z,command=new2)
    btn.pack()
    btn=Button(tree1,text="Hamilton",font=('arial','30','bold'),activebackground='green',bg=z,command=new3)
    btn.pack()
    btn=Button(tree1,text="Tauranga",font=('arial','30','bold'),activebackground='green',bg=z,command=new4)
    btn.pack()
    btn=Button(tree1,text="Dunedin",font=('arial','30','bold'),activebackground='green',bg=z,command=new5)
    btn.pack()
    btn=Button(tree1,text="Back",font=('arial','30','bold'),bg=z,fg='black',command=tree1.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.pack()
    tree1.mainloop()
def tick():
    home=pytz.timezone("Europe/Berlin")
    local_time= datetime.now(home)
    current_time=local_time.strftime('%I:%M:%S')
    clock_frame.config(text=current_time)
    clock_frame.after(200, tick)
    
def ger():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def ger1():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='blue',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def ger2():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='white',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def ger3():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def ger4():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='grey',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def ger5():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()


def city2():
    tree2=Tk()
    tree2.title("Main Page")
    tree2.attributes('-fullscreen', True)
    tree2.configure(bg='#25383C')
    z='#808000'
    lbl=Label(tree2,text="",font=('arial','30','bold'),bg='#25383C',fg='black')
    lbl.pack()
    lbl=Label(tree2,text="City Of Germany",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    btn=Button(tree2,text="Berlin",font=('arial','30','bold'),activebackground='green',bg=z,fg='black',command=ger)
    btn.pack()
    btn=Button(tree2,text="Hamburg",font=('arial','30','bold'),activebackground='green',bg=z,command=ger1)
    btn.pack()
    btn=Button(tree2,text="Munich",font=('arial','30','bold'),activebackground='green',bg=z,command=ger2)
    btn.pack()
    btn=Button(tree2,text="Cologne",font=('arial','30','bold'),activebackground='green',bg=z,command=ger3)
    btn.pack()
    btn=Button(tree2,text="Stuttgart",font=('arial','30','bold'),activebackground='green',bg=z,command=ger4)
    btn.pack()
    btn=Button(tree2,text="Düsseldorf",font=('arial','30','bold'),activebackground='green',bg=z,command=ger5)
    btn.pack()
    btn=Button(tree2,text="Back",font=('arial','30','bold'),bg=z,fg='black',command=tree2.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.pack()
    tree2.mainloop()
def tick():
    home=pytz.timezone("australia/melbourne")
    local_time= datetime.now(home)
    current_time=local_time.strftime('%I:%M:%S')
    clock_frame.config(text=current_time)
    clock_frame.after(200, tick)
    
def aus():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        


    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def aus1():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='blue',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def aus2():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='white',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def aus3():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def aus4():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='grey',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def aus5():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()


def city3():
    tree3=Tk()
    tree3.title("Main Page")
    tree3.attributes('-fullscreen', True)
    tree3.configure(bg='#25383C')
    z='#808000'
    x='black'
    lbl=Label(tree3,text="",font=('arial','30','bold'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    lbl=Label(tree3,text="City Of Australia",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    btn=Button(tree3,text="Canberra",font=('arial','30','bold'),activebackground='green',bg=z,fg='black',command=aus)
    btn.pack()
    btn=Button(tree3,text="Adelaide",font=('arial','30','bold'),activebackground='green',bg=z,command=aus1)
    btn.pack()
    btn=Button(tree3,text="Brisbane",font=('arial','30','bold'),activebackground='green',bg=z,command=aus2)
    btn.pack()
    btn=Button(tree3,text="Darwin,",font=('arial','30','bold'),activebackground='green',bg=z,command=aus3)
    btn.pack()
    btn=Button(tree3,text="Perth",font=('arial','30','bold'),activebackground='green',bg=z,command=aus4)
    btn.pack()
    btn=Button(tree3,text="Sydney",font=('arial','30','bold'),activebackground='green',bg=z,command=aus5)
    btn.pack()
    btn=Button(tree3,text="Back",font=('arial','30','bold'),bg=z,fg='black',command=tree3.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.pack()
    tree3.mainloop()
def tick():
    home=pytz.timezone("canada/atlantic")
    local_time= datetime.now(home)
    current_time=local_time.strftime('%I:%M:%S')
    clock_frame.config(text=current_time)
    clock_frame.after(200, tick)
    
def can():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def can1():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def can2():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='white',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def can3():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='grey',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def can4():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='purple',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def can5():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()


def city4():
    tree4=Tk()
    tree4.title("Main Page")
    tree4.attributes('-fullscreen', True)
    tree4.configure(bg='#25383C')
    z='#808000'
    x='black'
    lbl=Label(tree4,text="",font=('arial','30','bold'),bg='#25383C',fg='black')
    lbl.pack()
    lbl=Label(tree4,text="City Of Canada",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    btn=Button(tree4,text="Ottawa",font=('arial','30','bold'),activebackground='green',bg=z,fg=x,command=can)
    btn.pack()
    btn=Button(tree4,text="Toronto",font=('arial','30','bold'),activebackground='green',bg=z,command=can1)
    btn.pack()
    btn=Button(tree4,text="Halifax",font=('arial','30','bold'),activebackground='green',bg=z,command=can2)
    btn.pack()
    btn=Button(tree4,text="Quebec City",font=('arial','30','bold'),activebackground='green',bg=z,command=can3)
    btn.pack()
    btn=Button(tree4,text="Niagara Falls",font=('arial','30','bold'),activebackground='green',bg=z,command=can4)
    btn.pack()
    btn=Button(tree4,text="Winnipeg",font=('arial','30','bold'),activebackground='green',bg=z,command=can5)
    btn.pack()
    btn=Button(tree4,text="Back",font=('arial','30','bold'),bg=z,fg='black',command=tree4.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.pack()
    tree4.mainloop()
    
def tick():
    home=pytz.timezone("Asia/Tehran")
    local_time= datetime.now(home)
    current_time=local_time.strftime('%I:%M:%S')
    clock_frame.config(text=current_time)
    clock_frame.after(200, tick)
    
def iran():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='red',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def iran1():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='blue',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def iran2():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='silver',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def iran3():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='grey',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def iran4():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='white',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()

    
def iran5():
    root = tk.Tk()
    root.attributes('-fullscreen', True)
    root.configure(background="black")

##    def time():
##        string = strftime('%I:%M:%S %p')
##        lbl.config(text = string)
##        lbl.after(200, time)

##        def tick(time1 =''):    
##            time2 = time.strftime('%I:%M:%S')
##            if time2 != time1:
##                time1 = time2
##                clock_frame.config(text=time2)
##            clock_frame.after(200, tick)
##        

##        
##    lbl= Label(root, font=('arial 100 bold'),bg = black, fg=color)  نمرة
##    lbl.pack(fill='both', expand=1) مسجد

##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',fg='black',command=root.destroy())
##    btn.pack()
    name = Label(root,text="جامع مسجد نمرہ", font=('arial 30 bold'),bg = 'black',anchor=N, fg='white')
    name.place(x=560,y=200)
    global clock_frame
    clock_frame = Label(root, font=('arial 40 bold'), bg="black", fg="white")
    clock_frame.place(x=570,y=240)
    tick()
    
    fajar = Label(root,text="05:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    fajar.place(x=500,y=300)
    fajar = Label(root,text=" فجر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    fajar.place(x=800,y=300)
    
    duhr = Label(root,text="04:30 ", font=('arial 30 bold'),bg ='black' ,anchor=N, fg='red')
    duhr.place(x=500,y=350)
    duhr = Label(root,text=" ظهر", font=('arial 35 bold'),bg ='black' ,anchor=N, fg='white')
    duhr.place(x=800,y=350)
    
    asar = Label(root,text="05:20", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    asar.place(x=500,y=400)
    asar = Label(root,text="عصر", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    asar.place(x=800,y=400)
    
    maghrib = Label(root,text="06:10", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    maghrib.place(x=500,y=450)
    maghrib = Label(root,text="مغرب", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    maghrib.place(x=800,y=450)

    esha = Label(root,text="08:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    esha.place(x=500,y=500)
    esha = Label(root,text="عشاء", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    esha.place(x=800,y=500)

    Jummah = Label(root,text="02:40", font=('arial 30 bold'),bg = 'black',anchor=N, fg='red')
    Jummah.place(x=500,y=550)
    Jummah = Label(root,text="جمعہ", font=('arial 35 bold'),bg = 'black',anchor=N, fg='white')
    Jummah.place(x=800,y=550)    

    btn=Button(root,text="Back",font=('arial','25','bold'),bg='purple',command=root.destroy)
    btn.configure(activebackground='green',fg='yellow')
    btn.place(x=80,y=750)


    text_width = 15  # u should increase it for the spacing or gaping
    text = Text(root, width=text_width, height=1, bg='green',fg='black')
    text.place(x=500,y=600)


    text.config(font=('courier', 30, 'bold'))

    s = "05:40     فجر  01:30     ظهر    05:30     عصر   07:05    مغرب   08:45    عشاء  02:00    جمعہ  " ' ' * text_width
##    s1 = "05:40     فجر  "
##    s2 = "01:30     ظهر  "
##    s3 = "05:30     عصر  "
##    s4 = "07:05    مغرب  "
##    s5 = "08:45    عشاء  "
##    s6 = "02:00    جمعہ  "
##    s7 = ' ' * text_width
    # concatenate it all

##    s = s7 + s1 + s2 + s3 + s4 + s5 +s6 +s7

    for k in range(len(s)):
        # use string slicing to do the trick
        ticker_text = s[k:k+text_width]
        text.insert("1.1", ticker_text)
        root.update()
        
        time.sleep(0.20)# u should set here the value for timing

    
##    btn=Button(root,text="Back",font=('arial','30','bold'),bg='red',command=root.destroy)
##    btn.configure(activebackground='green',fg='yellow')
##    btn.pack()
#    btn.place(x=100,y=700)

    root.mainloop()


def city5():
    tree5=Tk()
    tree5.title("Main Page")
    tree5.attributes('-fullscreen', True)
    tree5.configure(bg='#25383C')
    z='#808000'
    x='black'
    lbl=Label(tree5,text="",font=('arial','30','bold'),bg='#25383C',fg='black')
    lbl.pack()
    lbl=Label(tree5,text="City Of Iran",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    btn=Button(tree5,text="Tehran",font=('arial','30','bold'),activebackground='green',bg=z,fg=x,command=iran)
    btn.pack()
    btn=Button(tree5,text="Yazd",font=('arial','30','bold'),activebackground='green',bg=z,fg=x,command=iran1)
    btn.pack()
    btn=Button(tree5,text="Shiraz",font=('arial','30','bold'),activebackground='green',bg=z,fg=x,command=iran2)
    btn.pack()
    btn=Button(tree5,text="Kerman",font=('arial','30','bold'),activebackground='green',bg=z,fg=x,command=iran3)
    btn.pack()
    btn=Button(tree5,text="Tabriz",font=('arial','30','bold'),activebackground='green',bg=z,fg=x,command=iran4)
    btn.pack()
    btn=Button(tree5,text="Qeshm",font=('arial','30','bold'),activebackground='green',bg=z,fg=x,command=iran5)
    btn.pack()
    lbl=Label(tree5,text="",font=('arial','30','bold'),bg='#25383C')
    lbl.pack()
    btn=Button(tree5,text="Back",font=('arial','30','bold'),bg='#808000',fg='#77BFC7',command=tree5.destroy)
    btn.configure(activebackground='green')
    btn.pack()
    tree5.mainloop()

from tkinter import *
def main():
    form=Tk()
    form.title("Main Page")
    form.attributes('-fullscreen', True)
    form.configure(bg='#25383C')
    lbl=Label(form,text="",font=('arial','30','bold'),bg='#25383C')
    lbl.pack()
    lbl=Label(form,text="Main Page",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
    lbl.pack()
    lbl=Label(form,text="",font=('arial','30','bold'),bg='#25383C')
    lbl.pack()
    btn=Button(form,text="Pakistan",font=('arial','30','bold'),activebackground='green',bg='#808000',command=city)
    btn.pack()
    btn=Button(form,text="Newzeland",font=('arial','30','bold'),activebackground='green',bg='#808000',command=city1)
    btn.pack()
    btn=Button(form,text="Germany",font=('arial','30','bold'),activebackground='green',bg='#808000',command=city2)
    btn.pack()
    btn=Button(form,text="Australia",font=('arial','30','bold'),activebackground='green',bg='#808000',command=city3)
    btn.pack()
    btn=Button(form,text="Canada",font=('arial','30','bold'),activebackground='green',bg='#808000',command=city4)
    btn.pack()
    btn=Button(form,text="Iran",font=('arial','30','bold'),activebackground='green',bg='#808000',command=city5)
    btn.pack()
    lbl=Label(form,text="",font=('arial','30','bold'),activebackground='green',bg='#25383C')
    lbl.pack()
    btn=Button(form,text="Back",font=('arial','30','bold'),bg='#808000',fg='#77BFC7',command=form.destroy)
    btn.configure(activebackground='green')
    btn.pack()
    form.mainloop()




from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import time

##def global1():
gui=Tk()


canvas1 = Canvas(gui,width = 1000, height = 1000)
a = Image.open("s.jpg")
b = ImageTk.PhotoImage(a)
canvas1= Label(image=b,bd=0)
canvas1.place(x=130,y=200)

    ##
    ##    canvas2 = Canvas(gui, width = 200, height = 300)
    ##    c = Image.open("khana kaba.jpg")
    ##    d = ImageTk.PhotoImage(c)
    ##    canvas2= Label(image=b,bd=0)
    ##    canvas2.place(x=800,y=500)



gui.attributes('-fullscreen', True)
gui.configure(bg='#25383C')
lbl=Label(gui,text="",font=('arial','30','bold'),bg='#25383C')
lbl.pack()
lbl=Label(gui,text="DashBoard :",font=('arial','40','bold underline'),bg='#25383C',fg='#77BFC7')
lbl.place(x=120,y=90)
btn=Button(gui,text="Click To Enter",font=('arial','25','bold'),bg='#808000',command=main)
btn.configure(activebackground='green')
btn.place(x=120,y=800)
lbl=Label(gui,text="Country :",font=('arial','25','bold'),bg='#808000')
lbl.place(x=1050,y=190)
ent=Entry(gui,font=('arial','15'),bg='white',fg='black')
ent.place(x=1250,y=200)
lbl=Label(gui,text="City:",font=('arial','30','bold'),bg='#808000')
lbl.place(x=1050,y=290)
ent=Entry(gui,font=('arial','15'),bg='white',fg='black')
ent.place(x=1250,y=290)
btn=Button(gui,text="Submit",font=('arial','30','bold'),bg='#808000',fg='#77BFC7',command=main)
btn.configure(activebackground='green')
btn.place(x=1100,y=400)
btn=Button(gui,text="Back",font=('arial','20','bold'),bg='#808000',fg='#77BFC7',command=gui.destroy)
btn.configure(activebackground='green')
btn.place(x=950,y=800)
gui.mainloop
##w=Scale(gui,from_=0, to=200,orient=VERTICAL,font=('5000'))
##w.pack()
##v=Scale(gui,from_=0, to=200,font=('10000'),orient=HORIZONTAL)
##v.pack()


#w, h = root.winfo_screenwidth(), root.winfo_screenheight()
#root.geometry("%dx%d+0+0" % (w, h))

##from tkinter import *
##
##gui1=Tk()
##gui1.attributes('-fullscreen', True)
##gui1.configure(bg='#25383C')
##lbl=Label(gui1,text="",font=('arial','30','bold'),bg='#25383C')
##lbl.pack()
##lbl=Label(gui1,text="Advanced Globally Masjid Clock System",font=('arial','40','bold'),bg='#25383C',fg='#77BFC7')
##lbl.place(x=120,y=300)
##btn=Button(gui1,text="Click Enter Dashboard",font=('arial','20','bold'),bg='#808000',command=global1)
##btn.configure(activebackground='green')
##btn.place(x=1000,y=600)
##
##gui1.mainloop



#fajar_namaz()
##Duhr_namaz()
##Asar_namaz()
##Maghrib_namaz()
##Esha_namaz()
##Jummah_namaz()

