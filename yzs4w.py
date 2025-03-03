from tkinter import*
import tkinter.messagebox
app=Tk()
app.geometry("750x750+150+0")
app["bg"]="#352171"
xo=1
def logic():
    global filt
    global number_Button
    print(number_Button)
    if len(number_Button)==9:
        tkinter.messagebox.showinfo("game finish", "draw ")
        begin(None)
    end=False
    if filt[2]==filt[8]==filt[5]>0:
        winer=filt[2]
        end=True
    elif filt[0] == filt[3] == filt[6] > 0:
        winer = filt[3]
        end = True
    elif filt[1] == filt[4] == filt[7] > 0:
        winer = filt[7]
        end = True
    elif filt[0] == filt[1] == filt[2] > 0:
        end=True
        winer = filt[0]

    elif filt[3] == filt[4] == filt[5] > 0:
        winer = filt[3]
        end = True
    elif filt[6] == filt[7] == filt[8] > 0:
        winer = filt[7]
        end = True
    elif filt[0] == filt[4] == filt[8] > 0:
        winer = filt[0]
        end = True
    elif filt[2] == filt[4] == filt[6] > 0:
        winer = filt[2]
        end = True

    # if end:
    #     print('_'*10)
    #     if winer==1:
    #         print("win x")
    #     elif winer==2:
    #         print("win 0")
    if end:
        print('_'*10)
        user = ""
        if winer == 1:
            user = "cross"
        elif winer == 2:
            user = "zero"
        print(user)

        tkinter.messagebox.showinfo("game finish","win "+ user)
        begin(None)
def click(Button, num):
    global number_Button, xo
    if num not in number_Button:
        if xo==1:
            Button["bg"]="#297426"
            filt[num]=xo
            xo=2
        elif xo==2:
            Button["bg"]="#b24846"
            filt[num]=xo
            xo = 1
        number_Button.append(num) #нажатие кнопки
    logic()
def begin(event): #нужно передавать None
    global  number_Button
    global filt
    filt = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    number_Button = []
    both_1 ["bg"]="#e2e2e2"
    both_2 ["bg"]="#e2e2e2"
    both_3 ["bg"]="#e2e2e2"
    both_4 ["bg"]="#e2e2e2"
    both_5 ["bg"]="#e2e2e2"
    both_6 ["bg"]="#e2e2e2"
    both_7 ["bg"]="#e2e2e2"
    both_8 ["bg"]="#e2e2e2"
    both_9 ["bg"]="#e2e2e2"
both_1=Button(text="qq",height=15, width=30, bg="#aea8bf", command=lambda:click(both_1,0))
both_1.place(x=20, y=20)
both_2=Button(text="ww",height=15, width=30, bg="#aea8bf", command=lambda:click(both_2,1))
both_2.place(x=260, y=20)
both_3=Button(text="ee",height=15, width=30, bg="#aea8bf", command=lambda:click(both_3,2))
both_3.place(x=500, y=20)
both_4=Button(text="rr",height=15, width=30, bg="#aea8bf", command=lambda:click(both_4,3))
both_4.place(x=20, y=260)
both_5=Button(text="tt",height=15, width=30, bg="#aea8bf", command=lambda:click(both_5,4))
both_5.place(x=260, y=260)
both_6=Button(text="yy",height=15, width=30, bg="#aea8bf", command=lambda:click(both_6,5))
both_6.place(x=500, y=260)
both_7=Button(text="uu",height=15, width=30, bg="#aea8bf", command=lambda:click(both_7,6))
both_7.place(x=20, y=500)
both_8=Button(text="ii",height=15, width=30, bg="#aea8bf", command=lambda:click(both_8,7))
both_8.place(x=260, y=500)
both_9=Button(text="oo",height=15, width=30, bg="#aea8bf", command=lambda:click(both_9,8))
both_9.place(x=500, y=500)
filt=[0,0,0,0,0,0,0,0,0]
number_Button=[]
app.bind("<q>", lambda e:click(both_1,0))
app.bind("<w>", lambda e:click(both_2,1))
app.bind("<e>", lambda e:click(both_3,2))
app.bind("<r>", lambda e:click(both_4,3))
app.bind("<t>", lambda e:click(both_5,4))
app.bind("<y>", lambda e:click(both_6,5))
app.bind("<u>", lambda e:click(both_7,6))
app.bind("<i>", lambda e:click(both_8,7))
app.bind("<o>", lambda e:click(both_9,8))
def exit_1(event):
    app.destroy()
def help_1(event):
    tkinter.messagebox.showinfo("инструкция",'''инструкция
Клавиши q,w,e,r,t,y,u,i,o означают место положения кнопок, нажмите на одну из них и вы начнете игру. Ваша цель поставить
три крестика или нолика в один ряд, вы с противником ходите по очереди. Всегда начинает нолик. На одну кнопку можно нажимать только один раз.
После чей то победы игра обнуляется и начинается заново.''')
app.bind("<Escape>",lambda e: exit_1(None))
app.bind("<f>", help_1)
app.bind("<g>", lambda e: begin(None))
app.mainloop()