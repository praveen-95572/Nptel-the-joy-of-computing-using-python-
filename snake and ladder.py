import random
from PIL import Image

end=100
def show_board():
    img=Image.open('snake_ladder.jpg')
    img.show()

def play():
    p1_name=input('Player 1, Please Enter your name')
    p2_name=input('Player 2, Please Enter your name')
    turn=pp1=pp2=0
    while(1):
        if turn%2==0:
            print(p1_name, 'Your turn')
            c=input('1 to continue or 0 to exit')
            if c==0:
                print(p1_name,' Scored: ',pp1)
                print(p2_name,' Scored: ',pp2)
                print('Quit the Game')
                break
            dice=random.randint(1,6)
            print(' Dice Showed : ',dice)
            pp1=pp1+dice
            pp1=check_ladder(pp1)
            pp1=check_snake(pp1)
            if pp1>end:
                pp1=end
            print(p1_name,' Your Score: ',pp1)
            if reached_end(pp1):
                print(p1_name,' WON')
                break
        else:
            print(p2_name, 'Your turn')
            c=input('1 to continue or 0 to exit')
            if c==0:
                print(p1_name,' Scored: ',pp1)
                print(p2_name,' Scored: ',pp2)
                print('Quit the Game')
                break
            dice=random.randint(1,6)
            print(' Dice Showed : ',dice)
            pp2=pp2+dice
            pp2=check_ladder(pp1)
            pp2=check_snake(pp1)
            if pp2>end:
                pp2=end
            print(p2_name,' Your Score: ',pp2)
            if reached_end(pp2):
                print(p2_name,' WON')
                break

def check_ladder(point):
    if point==8:
        print('ladder')
        return 26
    if point==21:
        print('ladder')
        return 82
    if point==80:
        print('ladder')
        return 100
    if point==62:
        print('ladder')
        return 96
    if point==66:
        print('ladder')
        return 87
    if point==54:
        print('ladder')
        return 93
    if point==50:
        print('ladder')
        return 91
    if point==43:
        print('ladder')
        return 77
    else:
        return point


def check_snake(point):
    if point==44:
        print('ladder')
        return 22
    if point==46:
        print('ladder')
        return 5
    if point==55:
        print('ladder')
        return 7
    if point==52:
        print('ladder')
        return 11
    if point==59:
        print('ladder')
        return 17
    if point==64:
        print('ladder')
        return 36
    if point==69:
        print('ladder')
        return 33
    if point==73:
        print('ladder')
        return 1
    if point==83:
        print('ladder')
        return 19
    if point==92:
        print('ladder')
        return 51
    if point==95:
        print('ladder')
        return 24
    if point==98:
        print('ladder')
        return 28
    else:
        return point


def reached_end(p):
    if p==end:
        return True
    else:
        return False

show_board()
play()















        
