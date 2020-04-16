import random
import copy

def int2bin(n, count=24):
    return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])
def nimsum(sticks):
    nsticks = copy.deepcopy(sticks)
    nim=0
    for i in range(0,len(nsticks)):
        nim = nim ^ nsticks[i]
    #When nim sum equals zero on the computer do random moves.
    #and control for the number wheter it is legal move or not.
    if nim == 0:
        if turn == 0:
            temp = random.randint(1,10)
            while True :
                for piles in range(len(sticks)):
                    if (sticks[piles] >= temp):
                        takeaway=temp
                        return takeaway,sticks[piles]
                temp = random.randint(1, 10)
    else:
        nimsumb = int2bin(nim)
        nimsumb_str = str(nimsumb).lstrip('0')
        mostsig = len(nimsumb_str)
        highest = 2 ** (mostsig - 1)
        xk = 0
        takeaway = -1
        while takeaway < 1:
            for item in range(0,len(nsticks)):
                if nsticks[item] >= highest:
                    xk = nsticks[item]
            yk = nim ^ xk
            takeaway = xk - yk
            nsticks.remove(xk)
        return takeaway,xk
def UserChoice(turn,sticks):
        try:
            while True:
                raw = int(input("Choose a pile:"))
                if raw>0 and raw<=len(sticks):
                    if sticks[raw-1] != 0:
                        break
                    else:
                        print("Already zero")
                else:
                    print("Please make legal move")
            raw = raw-1
            while True:
                remove = int(input("How many number you want to remove ?"))
                if remove > 0:
                    break
                else:
                    print("Please make legal move")
            if (sticks[raw] >= remove):
                sticks[raw] -= remove
                turn = 0
            else:
                print("wrong entry!!")
                turn = UserChoice(turn, sticks)
        except ValueError:
            print("False Value!!")
        return turn
def CompChoice(sticks,turn):
    remove,which = nimsum(sticks)
    x=sticks.index(which)
    sticks[x] -= remove
    turn=1
    print("Computer removed: {} from piles: {}".format(remove,x+1))
    return turn
def control(sticks):
    for i in range(len(sticks)):
        while sticks[i] != 0:
            return True
    return False

turn=0
sticks = []
rawnumber = random.randint(3,6)

#Prapering Game Board
for i in range(0,rawnumber):
    sticks.append(random.randint(1,10))

x=True
while x:
    while turn == 1:
        print("----------------------------")
        print("Current state >>"+str(sticks))
        print("----------------------------")
        turn=UserChoice(turn,sticks)
        x=control(sticks)
        if(x == False):
            print("""------------------
PLAYER WİNS..
------------------
""")
    while turn == 0:
        print("----------------------------")
        print("Current state >>"+str(sticks))
        print("----------------------------")
        turn=CompChoice(sticks,turn)
        x=control(sticks)
        if (x == False):
            print("""------------------
COMPUTER WINS..
------------------
""")
