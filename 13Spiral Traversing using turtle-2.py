import turtle
turtle.bgcolor("black")
tur=turtle.Turtle()
from random import randint

width=5
height=7
dot_distance=25

tur.penup()
list_color=["white","yellow","brown","red","blue","green","orange","pink","violet","grey"]

tur.setpos(-250,250)
def spiral(m,n):
    k=l=f=0
    col=randint(0,10)
    tur.color(list_color[col])

    while(k<m and l<n):
        col=randint(0,10)
        tur.color(list_color[col])
        if f==1:
            tur.right(90)
            
        for i in range(l,n):
            tur.dot()
            tur.forward(dot_distance)
        k+=1
        f=1
        tur.right(90)
        
        for i in range(k,m):
            tur.dot()
            tur.forward(dot_distance)
        n-=1
        tur.right(90)
        if k<n:
            for i in range(n-1,l-1,-1):
                tur.dot()
                tur.forward(dot_distance)
            m-=1
        tur.right(90)

        if l<n:
            for i in range(m-1,k-1,-1):
                tur.dot()
                tur.forward(dot_distance)
            l+=1
        
            
        
    turtle.done()

spiral(20,20)
