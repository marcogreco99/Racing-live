import turtle
import random

#ATTENZIONE: IL CODICE è OTTIMIZZABILE ! SVILUPPATO IN 3 GIORNI CAUSA SCADENZA IMMINENTE.

wn = turtle.Screen()
wn.setup(1280,720)
final = turtle.Turtle()
wn.addshape('final.gif')
final.shape('final.gif')
prato = 'prato.gif'
img = 'street.gif'
lives = 'live.gif'
wn.addshape(lives)
wn.addshape(img)
wn.addshape(prato)
sfondo = turtle.Turtle()
sfondo.shape(prato)
street = turtle.Turtle()
street.shape(img)
live = turtle.Turtle()
live.shape(lives)

wn.tracer(0)
live.up()
live.setposition(-550, 300)
#Traguardo
t = turtle.Turtle()
t.hideturtle()
t.up()
t.setposition(449, -253)
t.down()
for i in range(2):
    t.color('white')
    t.begin_fill()
    t.forward(38)
    t.left(90)
    t.fd(506)
    t.left(90)
    t.end_fill()
for i in range(11):
    t.color('black')
    t.begin_fill()
    t.fd(19)
    t.left(90)
    t.fd(23)
    t.left(90)
    t.fd(19)
    t.right(90)
    t.fd(23)
    t.right(90)
    t.end_fill()
t.fd(38)
t.left(180)
for i in range(11):
    t.begin_fill()
    t.fd(19)
    t.left(90)
    t.fd(23)
    t.left(90)
    t.fd(19)
    t.right(90)
    t.fd(23)
    t.right(90)
    t.end_fill()

#classifica live
l = turtle.Turtle()
l.hideturtle()
l.up()
l.setposition(-600, -253)
for i in range(2):
    l.color('azure')
    l.begin_fill()
    l.forward(100)
    l.left(90)
    l.fd(506)
    l.left(90)
    l.end_fill()

f = 'first.gif'
s = 'second.gif'
th = 'third.gif'
wn.addshape(f)
wn.addshape(s)
wn.addshape(th)
first = turtle.Turtle()
second = turtle.Turtle()
third = turtle.Turtle()
first.shape(f)
second.shape(s)
third.shape(th)
first.up()
second.up()
third.up()

first.setposition(-575,220)
second.setposition(-575,150)
third.setposition(-575,70)

player_one = turtle.Turtle()
player_one.up()
player_two = turtle.Turtle()
player_two.up()
player_three = turtle.Turtle()
player_three.up()

player_four = turtle.Turtle()
player_four.up()
player_five = turtle.Turtle()
player_five.up()
player_six = turtle.Turtle()
player_six.up()

#Immagini auto
car1 = 'car1.gif'
wn.addshape(car1)
player_one.shape(car1)

car2 = 'car2.gif'
wn.addshape(car2)
player_two.shape(car2)

car3 = 'car3.gif'
wn.addshape(car3)
player_three.shape(car3)

car4 = 'car4.gif'
wn.addshape(car4)
player_four.shape(car4)

car5 = 'car5.gif'
wn.addshape(car5)
player_five.shape(car5)

car6 = 'car6.gif'
wn.addshape(car6)
player_six.shape(car6)

player_one.setposition(-400,220)
player_two.setposition(-400,150)
player_three.setposition(-400,70)

player_four.setposition(-400,-80)
player_five.setposition(-400,-153)
player_six.setposition(-400,-225)


#live

one = turtle.Turtle()
one.up()
two = turtle.Turtle()
two.up()
three = turtle.Turtle()
three.up()

four = turtle.Turtle()
four.up()
five = turtle.Turtle()
five.up()
six = turtle.Turtle()
six.up()

#Immagini auto live

one.shape(car1)
two.shape(car2)
three.shape(car3)
four.shape(car4)
five.shape(car5)
six.shape(car6)

one.setposition(-530,220)
two.setposition(-530,150)
three.setposition(-530,70)
four.setposition(-530,-80)
five.setposition(-530,-153)
six.setposition(-530,-225)

wn.tracer(1)

vincitori = []
while player_one.xcor()<=468 or player_two.xcor()<=468 or player_three.xcor()<=468 or player_four.xcor()<468 or player_five.xcor()<468 or player_six.xcor()<468 or len(vincitori)!= 6 :
    ones=random.randrange(10)
    twos=random.randrange(10)
    threes=random.randrange(10)
    fours=random.randrange(10)
    fives=random.randrange(10)
    sixs=random.randrange(10)

    player_one.forward(ones)
    player_two.forward(twos)
    player_three.forward(threes)
    player_four.forward(fours)
    player_five.forward(fives)
    player_six.forward(sixs)

    # real live
    wn.tracer(0)
    
    #player one 1 posto
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,220)
    #player one 2 posto
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,150)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,150)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,150)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,150)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,150)

    #player one 3 posto
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,70)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,70)

    #player one 4 posto
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-80)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-80)

    #player one 5 posto
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()>player_six.xcor():
        one.setposition(-530,-153)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()>player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-153)
    if player_one.xcor()>player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-153)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()>player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-153)
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()>player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-153)

    #player one 6 posto
    if player_one.xcor()<player_two.xcor() and player_one.xcor()<player_three.xcor() and player_one.xcor()<player_four.xcor()and player_one.xcor()<player_five.xcor() and player_one.xcor()<player_six.xcor():
        one.setposition(-530,-225)



    #player two 1 posto
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,220)
    #player two 2 posto
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,150)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,150)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,150)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,150)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,150)

    #player two 3 posto
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,70)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,70)

    #player two 4 posto
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-80)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-80)

    #player two 5 posto
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()>player_six.xcor():
        two.setposition(-530,-153)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()>player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-153)
    if player_two.xcor()>player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-153)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()>player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-153)
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()>player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-153)

    #player two 6 posto
    if player_two.xcor()<player_one.xcor() and player_two.xcor()<player_three.xcor() and player_two.xcor()<player_four.xcor()and player_two.xcor()<player_five.xcor() and player_two.xcor()<player_six.xcor():
        two.setposition(-530,-225)



    #player three 1 posto
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,220)
    #player three 2 posto
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,150)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,150)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,150)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,150)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,150)

    #player three 3 posto
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,70)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,70)

    #player three 4 posto
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-80)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-80)

    #player three 5 posto
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()>player_six.xcor():
        three.setposition(-530,-153)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()>player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-153)
    if player_three.xcor()>player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-153)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()>player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-153)
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()>player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-153)

    #player three 6 posto
    if player_three.xcor()<player_two.xcor() and player_three.xcor()<player_one.xcor() and player_three.xcor()<player_four.xcor()and player_three.xcor()<player_five.xcor() and player_three.xcor()<player_six.xcor():
        three.setposition(-530,-225)



    #player four 1 posto
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,220)
    #player four 2 posto
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,150)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,150)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,150)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,150)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,150)

    #player four 3 posto
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,70)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,70)

    #player four 4 posto
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-80)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-80)

    #player four 5 posto
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()>player_six.xcor():
        four.setposition(-530,-153)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()>player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-153)
    if player_four.xcor()>player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-153)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()>player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-153)
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()>player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-153)

    #player four 6 posto
    if player_four.xcor()<player_two.xcor() and player_four.xcor()<player_three.xcor() and player_four.xcor()<player_one.xcor()and player_four.xcor()<player_five.xcor() and player_four.xcor()<player_six.xcor():
        four.setposition(-530,-225)


    #player five 1 posto
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,220)
    #player five 2 posto
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,150)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,150)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,150)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,150)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,150)

    #player five 3 posto
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,70)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,70)

    #player five 4 posto
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-80)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-80)

    #player five 5 posto
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()>player_six.xcor():
        five.setposition(-530,-153)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()>player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-153)
    if player_five.xcor()>player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-153)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()>player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-153)
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()>player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-153)

    #player five 6 posto
    if player_five.xcor()<player_two.xcor() and player_five.xcor()<player_three.xcor() and player_five.xcor()<player_four.xcor()and player_five.xcor()<player_one.xcor() and player_five.xcor()<player_six.xcor():
        five.setposition(-530,-225)


    #player six 1 posto
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,220)
    #player six 2 posto
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,150)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,150)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,150)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,150)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,150)

    #player six 3 posto
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,70)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,70)

    #player six 4 posto
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-80)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-80)

    #player six 5 posto
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()>player_one.xcor():
        six.setposition(-530,-153)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()>player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-153)
    if player_six.xcor()>player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-153)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()>player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-153)
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()>player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-153)

    #player six 6 posto
    if player_six.xcor()<player_two.xcor() and player_six.xcor()<player_three.xcor() and player_six.xcor()<player_four.xcor()and player_six.xcor()<player_five.xcor() and player_six.xcor()<player_one.xcor():
        six.setposition(-530,-225)



    wn.tracer(1)















        
    if player_one.xcor()>468 and player_one not in vincitori:
        vincitori.append(player_one)
        one.hideturtle()
    if player_two.xcor()>468 and player_two not in vincitori:
        vincitori.append(player_two)
        two.hideturtle()
    if player_three.xcor()>468 and player_three not in vincitori:
        vincitori.append(player_three)
        three.hideturtle()
    if player_four.xcor()>468 and player_four not in vincitori:
        vincitori.append(player_four)
        four.hideturtle()
    if player_five.xcor()>468 and player_five not in vincitori:
        vincitori.append(player_five)
        five.hideturtle()
    if player_six.xcor()>468 and player_six not in vincitori:
        vincitori.append(player_six)
        six.hideturtle()
        
#Classifica

sfondo.hideturtle()
street.hideturtle()
live.hideturtle()
first.hideturtle()
second.hideturtle()
third.hideturtle()
wn.tracer(0)
a = -638
for j in range(3):
    a+=38
    t.up()
    t.setposition(a, -253)
    t.down()
    t.left(180)
    for i in range(2):
        t.color('white')
        t.begin_fill()
        t.forward(38)
        t.left(90)
        t.fd(506)
        t.left(90)
        t.end_fill()
    for i in range(11):
        t.color('black')
        t.begin_fill()
        t.fd(19)
        t.left(90)
        t.fd(23)
        t.left(90)
        t.fd(19)
        t.right(90)
        t.fd(23)
        t.right(90)
        t.end_fill()
    t.fd(38)
    t.left(180)
    for i in range(11):
        t.begin_fill()
        t.fd(19)
        t.left(90)
        t.fd(23)
        t.left(90)
        t.fd(19)
        t.right(90)
        t.fd(23)
        t.right(90)
        t.end_fill()
a = 449

for j in range(2):
    a+=38
    t.up()
    t.setposition(a, -253)
    t.down()
    t.left(180)
    for i in range(2):
        t.color('white')
        t.begin_fill()
        t.forward(38)
        t.left(90)
        t.fd(506)
        t.left(90)
        t.end_fill()
    for i in range(11):
        t.color('black')
        t.begin_fill()
        t.fd(19)
        t.left(90)
        t.fd(23)
        t.left(90)
        t.fd(19)
        t.right(90)
        t.fd(23)
        t.right(90)
        t.end_fill()
    t.fd(38)
    t.left(180)
    for i in range(11):
        t.begin_fill()
        t.fd(19)
        t.left(90)
        t.fd(23)
        t.left(90)
        t.fd(19)
        t.right(90)
        t.fd(23)
        t.right(90)
        t.end_fill()
        
pos1 = turtle.Turtle()
pos2 = turtle.Turtle()
pos3 = turtle.Turtle()
wn.addshape('first2.gif')
wn.addshape('second2.gif')
wn.addshape('third2.gif')
pos1.shape('first2.gif')
pos2.shape('second2.gif')
pos3.shape('third2.gif')
pos1.up()
pos2.up()
pos3.up()
pos1.setposition(-200,200)
pos2.setposition(0,200)
pos3.setposition(200,200)
    
vincitori[0].setposition(-200,130)
vincitori[1].setposition(0,130)
vincitori[2].setposition(200,130)
vincitori[3].setposition(0,-80)
vincitori[4].setposition(0,-153)
vincitori[5].setposition(0,-225)
wn.tracer(1)
wn.exitonclick()
