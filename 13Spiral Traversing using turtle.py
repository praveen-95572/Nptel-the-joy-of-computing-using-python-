import turtle
turtle.bgcolor("black")    #background color
tur=turtle.Turtle() 

width=5
height=7

dot_distance=25
tur.setpos(-250,250)
def spiral(m,n):
    k=l=f=0
    tur.color("red")

    while(k<m and l<n):
        if f==1:
            tur.right(90)
        for i in range(l,n):
            tur.forward(dot_distance)
        k+=1
        f=1
        tur.right(90)
        
        for i in range(k,m):
            tur.forward(dot_distance)
        n-=1
        tur.right(90)
        if k<n:
            for i in range(n-1,l-1,-1):
                tur.forward(dot_distance)
            m-=1
        tur.right(90)

        if l<n:
            for i in range(m-1,k-1,-1):
                tur.forward(dot_distance)
            l+=1
        
            
        
    turtle.done()

spiral(20,20)
