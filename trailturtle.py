import turtle  
# Creating turtle  
t = turtle.Turtle()  
s = turtle.Screen()  
s.bgcolor("black")  
t.pencolor("red")  
  
a = 90 
b = 0  
t.speed(90)  
t.penup()  
t.goto(0,200)  
t.pendown()  
while(True):  
    t.forward(a)  
    t.right(b)  
    a+=3  
    b+=1  
    if b == 210:  
        break  
    t.hideturtle()  
  
turtle.done()  