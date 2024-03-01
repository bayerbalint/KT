import turtle
import math

ablak = turtle.Screen()
ablak.bgcolor("#fedcba")
ablak.setup(800,900)
ablak.title("Teki feladatok :)")

def alaphelyzet():
    ablak.reset()
    ablak.bgcolor('#fedcba')
    teknos.speed(0)
    # leírás
    teknos.penup()
    teknos.goto(-ablak.canvwidth*9/10, ablak.canvheight*1.3)
    teknos.write('H: háromszögek', font=('Times New Roman', 20, 'normal'))
    teknos.goto(-ablak.canvwidth*9/10, ablak.canvheight*1.2)
    teknos.write('K: körök', font=('Times New Roman', 20, 'normal'))
    teknos.goto(-ablak.canvwidth*9/10, ablak.canvheight*1.1)
    teknos.write('Számok: szabályos sokszögek', font=('Times New Roman', 20, 'normal'))
    teknos.goto(-ablak.canvwidth*9/10, ablak.canvheight)
    teknos.write('C: ablak letörlése', font=('Times New Roman', 20, 'normal'))
    teknos.goto(0,0)
    teknos.pendown()
    teknos.speed(3)

def haromszogek():
    ablak.bgcolor('white')
    biggest_size = 120
    colors = ['blue', 'red', 'yellow']
    for i in range(3):
        teknos.fillcolor(colors[i])
        teknos.begin_fill()
        if i == 0:
            teknos.left(60)
            teknos.fd(biggest_size/2)
        else:
            teknos.fd(biggest_size/2*(i+1))
        for j in range(2):
            teknos.right(120)
            teknos.fd(biggest_size/2*(i+1))
        teknos.end_fill()

def korok():
    ablak.bgcolor("yellow")
    radius = 50
    coordinates = {0:[-radius/3,-radius*4/3], 1:[-radius*4/3,-radius/3], 2:[0,0]}
    for i in range(3):
        teknos.penup()
        teknos.goto(coordinates[i][0], coordinates[i][1])
        teknos.pendown()
        teknos.pencolor("red")
        teknos.circle(radius)

def sokszog(szam):
    colors = ['red', 'black', 'green', 'orange', 'yellow', 'blue', 'brown']
    size = 90
    ablak.bgcolor('#fedcba')
    teknos.penup()
    teknos.goto(0,0)
    teknos.pendown()
    teknos.fillcolor(colors[szam-3])
    teknos.begin_fill()
    for i in range(szam):
        if i == 0:
            teknos.left((szam-2)*180/szam) # sokszög egyik belső szöge
        teknos.fd(size)
        teknos.right(180-((szam-2)*180/szam)) # 180 - sokszög egyik belső szöge
    teknos.end_fill()

# ablak bezárása
ablak.onkey(turtle.bye,"Escape")
ablak.onkey(turtle.bye, "1")
ablak.onkey(turtle.bye, "2")
# háromszögek gombja
ablak.onkey(haromszogek, "h")
# körök gombja
ablak.onkey(korok, "k")
# szabályos sokszögek gombjai
for i in range(3, 10):
    ablak.onkey(lambda j=i:sokszog(j), str(i))
# ablak alaphelyzetbe helyezése
ablak.onkey(alaphelyzet, "c")

teknos = turtle.Turtle()
alaphelyzet()
turtle.listen() # event listener

ablak.mainloop()