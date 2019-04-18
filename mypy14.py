import turtle
t = turtle.Pen()
my_colors = ["red","green","yellow","black"]
t.width(4)
t.speed(1)
for i in range(10): #0   1    2    3    4 先写几组，试出来 end="\t")
    t.penup()
    t.goto(0,-i*10)    #0, -100,-200,-300,-400
    t.pendown()
    t.color(my_colors[i%len(my_colors)])
    t.circle(15+i*10)  #100,200,300, 400,, 500
turtle.done()   #程序执行完，窗口仍然在


import turtle
turtle.width(4)
clo=("red","blue","yellow","green")
for i in range(10):#0 1 2 3先写几组，试出来
    turtle.penup()
    turtle.goto(0,-10*i)#0 -10  -20
    turtle.pendown()
    turtle.color(clo[i%4])
    turtle.circle(10*(i+1))# 10 20 30
turtle.done()


import turtle
turtle.width(3)
for i in range(19):
    turtle.penup()
    turtle.goto(0,10*i)
    turtle.pendown()
    turtle.goto(180,10 *i)
for j in range(19):
    turtle.penup()
    turtle.goto(180-10*j,180)
    turtle.pendown()
    turtle.goto(180-10*j,0)
turtle.hideturtle()
turtle.done()

#画棋盘
import turtle
width = 30
num = 18
x1 = [(-400,400),(-400+width*num,400)]
y1 = [(-400,400),(-400,400-width*num)]
t = turtle.Pen()# t.goto(x1[0][0],x1[0][1])
t.speed(10)# t.goto(x1[1][0],x1[1][1])
for i in range(0,19):
    t.penup()
    t.goto(x1[0][0],x1[0][1]-30*i)
    t.pendown()
    t.goto(x1[1][0],x1[1][1]-30*i)

for i in range(0,19):
    t.penup()
    t.goto(y1[0][0]+30*i,y1[0][1])
    t.pendown()
    t.goto(y1[1][0]+30*i,y1[1][1])
t.hideturtle()   #隐藏画笔
turtle.done()   #保证运行窗口不被自动关闭