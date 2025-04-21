from tkinter import*
app_1=Tk()
app_1.geometry("1000x600+100+100")
carrots=0
can = Canvas(width=700, height=500, bg="white")
can.place(x=100,y=100+20+20)
#can.create_rectangle(40,80,140,190,
#                    fill="yellow",
#                    outline="green",
#                    width=3)
# can.create_oval(50,10,150,110, outline="green", width=2)
# can.create_oval(10,120,190,190, fill="grey70",outline="white")
# can.create_rectangle(50,10,150,110, outline="red")
# can.create_oval(10,10,190,190, fill="lightgrey",
#                 outline="white")
# can.create_arc(10,10,190,190,
#                start=0,       extent=45,
# fill="red")
# can.create_arc(10,10,190,190,
# start=180, extent=25,       fill="orange")
# can.create_arc(10,10,190,190,
# start=240, extent=100,
# style=CHORD,fill="green")
# can.create_arc(10,10,190,190,
# start=160,     extent=-70,
# style=ARC, outline="darkblue",
# width=5)
# can.create_text(100,100,
#                 text="Hello World. \nPython\nand Tk",
#                 justify=CENTER, font="Verdana 14")
# can.create_oval(300,300,0,0, outline="orange", width=2)
# can.create_oval(300,300,0,0, fill="yellow")
# can.create_line(40,100,140,100, width=2)
# can.create_line(170,100,270,100, width=2)
# can.create_line(90,250,190,250, width=2)
# can.create_oval(50,100,100,150,fill="black", outline="black", width=2)
# can.create_oval(170,100,220,150,fill="black", outline="black", width=2)
# can.create_line(130,150,160,210, width=2)
#
#
# can.create_rectangle(20,20,330,280,fill="red", outline="orange", width=2)
# can.create_rectangle(80,80,270,220,fill="grey", outline="orange", width=2)
# can.create_rectangle(100,100,250,200,fill="yellow", outline="orange", width=2)
# can.create_line(20,20,80,80, width=2, fill="green")
# can.create_line(330,20,270,80, width=2, fill="blue")
# can.create_line(20,280,80,220, width=2, fill="purple")
# can.create_line(330,280,270,220, width=2, fill="pink")
# x=250
# y=20
# size=50
# can.create_line(200,200,200,80, fill="brown",
#                 width=100,arrow=LAST,
#                 arrowshape="10 20 10")
# can.create_oval(x,y,x+size,y+size, outline="yellow", fill="yellow")
# x_green=150
# for i in range(21):
#     can.create_line(x_green,230,x_green,200)
#     x_green+=5
x=-5
y=5
k_1=0
k_2=0
ball_x=405
ball_y=55

def moving(event):
    if event.keysym == "w" and can.coords(plat1)[1] - 20 > 0:
        can.move(plat1, 0, -20)
    elif event.keysym == "s" and can.coords(plat1)[3] + 20 < 410:
        print([can.coords(plat1)])
        can.move(plat1, 0, 20)
    elif event.keysym == "Up" and can.coords(plat2)[1] - 20 > 0:
        can.move(plat2, 0, -20)
    elif event.keysym == "Down" and can.coords(plat2)[3] + 20 < 410:
        print([can.coords(plat2)])
        can.move(plat2, 0, 20)
can.create_rectangle(20,20,680,400, fill="green")
plat2=can.create_rectangle(635,170,640,260, fill="white")
can.create_rectangle(330,20,350,400, fill="white")
ball=can.create_oval(ball_x,ball_y,ball_x+15,ball_y+15, fill="white")
plat1=can.create_rectangle(55,170,60,260, fill="white")
can.create_text(300, 50, text=k_1, font='Arial 50')
can.create_text(370, 50, text=k_2, font='Arial 50')
can.focus_set()
can.bind("<w>", moving)
can.bind("<s>", moving)
can.bind("<Up>", moving)
can.bind("<Down>", moving)
def ball_move():
    global x,y,ball_x,ball_y
    can.move(ball,x,y)
    ball_coords = can.coords(ball)
    ball_left, ball_top, ball_right, ball_bottom = ball_coords
    if ball_right>680:
        x=-x
    if ball_left>0:
        x=-x
    if ball_top <0 or ball_bottom>400:
        y=-y
    ball_x+=x
    ball_y+=y
    can.after(15, ball_move)
ball_move()
app_1.mainloop()ю
