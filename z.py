from tkinter import*
def end():
    global app
    app.destroy()
time=0
money=0
quest=["Какой континент состоит из одной страны?", "где растут подсолнухи?"
       ,"Каких денег не бывает?","Как называется портрет нарисованый с самого себя?",
       "Как называется безпилотный литающий апарат","В какой игре используется мяч?",
        "Какой из этих мостов находится в Киеве?",
       "Кто из этих людей писатель?","Кто из этих мореплавытелей нашел Мис Доброй Надежды?"]
answer=[["Азия", "Япония","Австралия", "Европа"],["на земле", "на солнце","в небе", "в воде"],
        ["Гривны","Лье","Доллары","Лири"],["пейзаж","Самописка","Зеркальник","Автопортрет"], ["дрон","махаон","десептикон","анион"],
        ["баскетбол","тенис","бейсбол","керлинг"],["Пражьский","Дарницький","Невський","Славутинский"],
        ["вандам","усейн болт","едгар по","клад Монэ"],["Барталомео Диашь","Джон Брюс","Васка Дамага","Христофер Колумб"]]

correct_answer=[3,1,2,4,1,4,2,3,1]

i=0
def start_game():
    global app
    app.destroy()
new_window=Tk()
count=15
after_id=""
both_3 = Label(text="таймер", height=3, width=25, bg="#414053")
def tick():
    global count, after_id
    after_id = new_window.after(1000, tick)
    count-=1
    both_3["text"]=count
    if count==0:
        if i < 5:
            text = "Сума: 0"
        else:
            text = "sum 1500"


        new_window.destroy()
        loose_window = Tk()
        loose_window.geometry("200x200+600+300")
        loose_window.title("вы проиграли, заработали 0")
        Label_10 = Label(text="Вы проиграли потому\n что время истекло", font=(10))
        Label_10.place(x=0, y=20)
        Label_11 = Label(text=text, font=(10))
        Label_11.place(x=50, y=80)
def help_1():
    count=1
    if count==0:
        new_window.destroy()
        loose_window = Tk()
        loose_window.geometry("200x200+600+300")

        both_4 = Button
        both_4.place(x=0, y=35)

def get_money():
    global money
    print(money)
    new_window.destroy()
    window_1= Tk()
    window_1.geometry("300x400+450+300")
    Label_10=Label(text="вы забрали деньги")
    Label_10.place(x=20, y=30)
    Label_20=Label(text=f"ваш выигриш {money}")
    Label_20.place(x=20, y=60)



def next_question(both_3,both_4,answer_1,both_6,both_7,Label_1, number):
    global i, count, money, Label_sum
    count = 5

    both_4.config(state="normal")
    both_6.config(state="normal")
    both_7.config(state="normal")
    answer_1.config(state="normal")

    if number==correct_answer[i]:

        i+=1
        money+=i*100

        if i<9:
            Label_3["text"]=f"вопрос № {i+1}"
            Label_1["text"]=quest[i]
            answer_1['text']=answer[i][0]
            both_6["text"]=answer[i][1]
            both_7["text"]=answer[i][2]
            both_4["text"]=answer[i][3]
            Label_sum["text"]=f"сума:{money}"

        else:
            new_window.destroy()
            win_window=Tk()
            win_window.geometry("200x200+600+300")
            win_window.title("Вы выиграли, заработали 4500")
            Label_12=Label(text="вы выиграли", font=(10))
            Label_12.place(x=0, y=0)
            Label_13=Label(text="сума 4500", font=(10))
            Label_13.place(x=50, y=35)



    else:
        if i<5:
            text="Сума: 0"
        else:
            text="sum 1500"


        new_window.destroy()
        loose_window=Tk()
        loose_window.geometry("200x200+600+300")
        loose_window.title("вы проиграли, заработали 0")
        Label_10=Label(text="Вы проиграли", font=(10))
        Label_10.place(x=0, y=0)
        Label_11=Label(text=text, font=(10))
        Label_11.place(x=50,y=35)

def help():
    global i
    print(correct_answer[i])
    both_200.config(state="disabled")
    both_200.config(relief=SUNKEN)
    if correct_answer[i]==3:
        answer_2.config(state="disabled")
        answer_1.config(state="disabled")
        answer_4.config(state="disabled")
    elif correct_answer[i]==1:
        answer_4.config(state="disabled")
        answer_2.config(state="disabled")
        answer_3.config(state="disabled")
    elif correct_answer[i] == 2:
        answer_4.config(state="disabled")
        answer_1.config(state="disabled")
        answer_3.config(state="disabled")
    elif correct_answer[i] == 4:
        answer_1.config(state="disabled")
        answer_2.config(state="disabled")
        answer_3.config(state="disabled")

def fifty_fifty():
    global i
    print(correct_answer[i])
    both_5.config(state="disabled")
    both_5.config(relief=SUNKEN)
    if correct_answer[i] == 3:
        answer_1.config(state="disabled")
        answer_4.config(state="disabled")
    elif correct_answer[i] == 1:
        answer_2.config(state="disabled")
        answer_3.config(state="disabled")
    elif correct_answer[i] == 2:
        answer_1.config(state="disabled")
        answer_3.config(state="disabled")
    elif correct_answer[i] == 4:
        answer_2.config(state="disabled")
        answer_3.config(state="disabled")


def question(number):
    global both_3,answer_4,answer_1,answer_2,answer_3,Label_1
    next_question(number=number, both_3=both_3, both_4=answer_4,
                  answer_1=answer_1, both_6=answer_2, both_7=answer_3, Label_1=Label_1)

tick()
new_window.geometry("750x750+150+0")
new_window["bg"] = "#acabbf"
both_3.place(x=150, y=100)
both_200 = Button(text="помощь", height=4, width=28, bg="#414053", command=help)
both_200.place(x=15, y=250)
both_5 = Button(text="50/50", height=4, width=28, bg="#414053", command=fifty_fifty)
both_5.place(x=250, y=250)
both_6= Button(text="забрать деньги", height=4, width=28, bg="#414053", command=get_money)
both_6.place(x=485, y=250)
answer_3 = Button(text=answer[i][2], height=4, width=47, bg="#414053", command=lambda:question(number=3))
answer_3.place(x=15, y=600)
answer_4 = Button(text=answer[i][3], height=4, width=47, bg="#414053", command=lambda:question(number=4))
answer_4.place(x=360, y=600)
answer_1 = Button(text=answer[i][0], height=4, width=47, bg="#414053", command=lambda:question(number=1))
answer_1.place(x=15, y=500)
answer_2 = Button(text=answer[i][1], height=4, width=47, bg="#414053", command=lambda:question(number=2))
answer_2.place(x=360, y=500)
Label_1 =Label (text=quest[i], height=4, width=100, bg="#414053")
Label_1.place(x=15, y=400)
Label_sum=Label(text="сума: 0",height=3, width=25, bg="#d2d2d6")
Label_sum.place(x=400, y=100)
Label_3=Label(text="вопрос №1", height=3, width=25, bg="#ffffff")
Label_3.place(x=20, y=340)
# app=Tk()
# app.geometry("750x750+150+0")
# app["bg"]="#acabbf"
# both_1=Button(text="играть",height=17, width=75, bg="#414053", font=("Arial",12), command=start_game)
# both_1.place(x=20, y=20)
# both_2=Button(text="закончить игру",height=17, width=75, bg="#414053", font=("Arial",12), command=end)
# both_2.place(x=20, y=350)
mainloop()