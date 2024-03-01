import turtle
#ablak alapbeállítások:
ablak = turtle.Screen()
ablak.bgcolor("#fedcba")
ablak.setup(800,900)
#változók használata:
a = int(input('Add meg a téglalap hosszát! '))
b = int(input('Add meg a téglalap magasságát! '))
# teki.fd(mennyit) .left() .right() .fillcolor("szín") .begin_fill() .end_fill
# .penup() .pendown()
def rajzol():
    teki.fillcolor("#012345")
    teki.begin_fill();
    teki.fd(a)
    teki.left(90)
    teki.fd(b)
    teki.left(90)
    teki.fd(a)
    teki.left(90)
    teki.fd(b)
    teki.end_fill()

def kilep():
    turtle.bye()

#ablak.onkey(eseménykezelő,"meghívó billentyű felirata")
#ablak.onscreenclick(eseményekezlő,1-2-3) 1-bal, 3-jobb egérgomb
ablak.onkey(rajzol, "1") #az 1 gomb lenyomására meghívja a rajzol() metódust
ablak.onkey(kilep, "2")

ablak.title('Ablakocska feliratocska bátyuska')
teki = turtle.Turtle()
turtle.listen() #ez NAGYON fontos, ha eseménykezelőket használok! 
                #Ő figyeli, hogy bekövetkezik-e egy esemény.
ablak.mainloop()

