# coding: utf-8
from Tkinter import *
import time
import math
root=Tk()
root.title("画图")
running=1
#c=circle_color,d_c=dot_color
c=d_c='red'
#r=rectangle_fill_color,l_c=line_color,r_o_c=rectangle_outline_color
r=l_c=r_o_c=c_o_c='blue'
#l=line_width,d=dot_width,e=erase_width,r_o_w=rectangle_outline_width
l=d=e=r_o_w=c_o_w=5
i=j=p=0
new_c=Canvas(root,width=640,height=480,bg='white')
x,y=int(new_c['width'])/2,int(new_c['height'])/2
rcolor=StringVar()
ccolor=StringVar()
line_width=IntVar()
dot_width=IntVar()

def new_canvas():
    new_c.create_rectangle(0,0,640,480,fill='white')

def quit_():
    global running
    running=0
    root.destroy()
    
def place_shape(event):
    global x,y
    global i,j,p
    global x_prior
    global y_prior
    x_prior=x
    y_prior=y
    x,y=event.x,event.y
    if(shape_val==0):
        new_c.create_oval(x,y,x,y,width=d,outline=d_c)
    if(shape_val==1):
        p=p+1
        new_c.create_oval(x,y,x,y,width='3',outline=r_o_c)
    if(shape_val==1)and(p%2==0):
        new_c.create_oval(x_prior,y_prior,x_prior,y_prior,width='3',outline='white')
        new_c.create_rectangle(x_prior,y_prior,x,y,fill=r,width=r_o_w,outline=r_o_c)
    if(shape_val==2):
        j=j+1
        new_c.create_oval(x,y,x,y,width='3',outline=c_o_c)
    if(shape_val==2)and(j%2==0):
        new_c.create_oval(x_prior-math.sqrt((x_prior-x)**2+(y_prior-y)**2),
                          y_prior-math.sqrt((x_prior-x)**2+(y_prior-y)**2),
                          x_prior+math.sqrt((x_prior-x)**2+(y_prior-y)**2),
                          y_prior+math.sqrt((x_prior-x)**2+(y_prior-y)**2),
                          fill=c,width=c_o_w,outline=c_o_c)
    if(shape_val==3):
        i=i+1
        if(i%2==1):
            new_c.create_oval(x,y,x,y,width=l,outline=l_c)
    if(shape_val==3)and(i%2==0):
        new_c.create_oval(x_prior,y_prior,x_prior,y_prior,width=l,outline='white')
        new_c.create_line(x_prior,y_prior,x,y,width=l,fill=l_c)
root.bind('<Button-1>',place_shape)

def erase_shape(event):
    global x,y
    x,y=event.x,event.y
    new_c.create_oval(x,y,x,y,width=e,outline='white')
root.bind('<Button-3>',erase_shape)

def set_erase():
    erase=Tk()
    erase.title("erase")
    erase_label=Label(erase,text='width:').pack()
    entry_e=Entry(erase,width=30)
    entry_e.pack()
    erase_button=Button(erase,text='submit',
                      command=lambda:set_e(entry_e.get(),erase))
    erase_button.pack()

def set_e(val1,val2):
    global e
    if(val1!=''):
        e=int(val1)
    val2.destroy()

def set_shape_0():
    global shape_val
    shape_val=0
    dot=Tk()
    dot.title("dot")
    dot_label_1=Label(dot,text='width:').pack()
    entry_d1=Entry(dot,width=30)
    entry_d1.pack()
    dot_label_2=Label(dot,text='color:').pack()
    entry_d2=Entry(dot,width=30)
    entry_d2.pack()
    dot_button=Button(dot,text='submit',
                      command=lambda:set_int(entry_d1.get(),entry_d2.get(),dot))
    dot_button.pack()

def set_int(val1,val2,val3):
    global d,d_c
    if(val1!=''):
        d=int(val1)
    if(val2!=''):
        d_c=str(val2)
    val3.destroy()

def set_shape_1():
    global shape_val
    shape_val=1
    rectangle=Tk()
    rectangle.title("矩形")
    rec_label_1=Label(rectangle,text='fill_color:').pack()
    entry_r1=Entry(rectangle,width=30)
    entry_r1.pack()
    rec_label_2=Label(rectangle,text='outline_width:').pack()
    entry_r2=Entry(rectangle,width=30)
    entry_r2.pack()
    rec_label_3=Label(rectangle,text='outline_color:').pack()
    entry_r3=Entry(rectangle,width=30)
    entry_r3.pack()
    rec_button=Button(rectangle,text='submit',
                      command=lambda:set_r(entry_r1.get(),entry_r2.get(),entry_r3.get(),rectangle))
    rec_button.pack()

def set_r(val1,val2,val3,val4):
    global r,r_o_c,r_o_w
    if(val1!=''):
        r=str(val1)
    if(val2!=''):
        r_o_w=int(val2)
    if(val3!=''):
        r_o_c=str(val3)
    val4.destroy()
    
def set_shape_2():
    global shape_val
    global ccolor
    shape_val=2
    circle=Tk()
    circle.title("圆")
    cir_label=Label(circle,text='color:').pack()
    entry_c1=Entry(circle,width=30)
    entry_c1.pack()
    cir_label_2=Label(circle,text='outline_width:').pack()
    entry_c2=Entry(circle,width=30)
    entry_c2.pack()
    cir_label_3=Label(circle,text='outline_color:').pack()
    entry_c3=Entry(circle,width=30)
    entry_c3.pack()
    cir_button=Button(circle,text='submit',
                      command=lambda:set_c(entry_c1.get(),entry_c2.get(),entry_c3.get(),circle))
    cir_button.pack()

def set_c(val1,val2,val3,val4):
    global c,c_o_c,c_o_w
    if(val1!=''):
        c=str(val1)
    if(val2!=''):
        c_o_w=int(val2)
    if(val3!=''):
        c_o_c=str(val3)
    val4.destroy()

def set_shape_3():
    global shape_val
    shape_val=3
    line=Tk()
    line.title("line")
    line_label_1=Label(line,text='width:').pack()
    entry_l_1=Entry(line,width=30)
    entry_l_1.pack()
    line_label_2=Label(line,text='color:').pack()
    entry_l_2=Entry(line,width=30)
    entry_l_2.pack()
    line_button=Button(line,text='submit',
                      command=lambda:set_l(entry_l_1.get(),entry_l_2.get(),line))
    line_button.pack()

def set_l(val1,val2,val3):
    global l
    global l_c
    if(val1!=''):
        l=int(val1)
    if(val2!=''):
        l_c=str(val2)
    val3.destroy()

#创建一个菜单栏
menubar = Menu(root)
menubar.add_command(label='clear',command =new_canvas)
menubar.add_command(label='dot',command=set_shape_0)
menubar.add_command(label='line',command=set_shape_3)
menubar.add_command(label='rectangle',command=set_shape_1)
menubar.add_command(label='circle',command=set_shape_2)
menubar.add_command(label='erase',command=set_erase)
menubar.add_command(label='quit',command=quit_)
root.config(menu = menubar)
shape_val=0
while running:
    new_c.pack()
    time.sleep(0.01)
    new_c.update()
