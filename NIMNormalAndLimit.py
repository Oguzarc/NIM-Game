import random
import copy

def LimitGame():
    def int2bin(n, count=24):
        return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])
    def nimsum(sticks):
        nsticks = copy.deepcopy(sticks)
        nim=0
        for i in range(0,len(nsticks)):
            nim = nim ^ nsticks[i]
        #When nim sum equals zero, the computer makes random moves.
        #and control for the number wheter it is legal move or not.
        if nim == 0:
            if turn == 0:
                temp = random.randint(1,10)
                while True:
                    for piles in range(len(sticks)):
                        if (sticks[piles] >= temp and piles!=Climit):
                            takeaway=temp
                            return takeaway,sticks[piles]
                        elif(sticks[piles] >= Chowmuch and piles==Climit):
                            takeaway=Chowmuch
                            return takeaway,sticks[Climit]
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
                if(raw==limit and sticks[raw] >= howmuch ):
                    if (sticks[raw] >= howmuch):
                        sticks[raw] -= howmuch
                        print("It is your limited pile. You removed {} from pile:{}".format(howmuch,raw+1))
                        turn = 0
                elif(raw==limit and sticks[raw] < howmuch):
                    print("you can only remevo {} from this pile.Please choose another pile".format(howmuch))
                    counter=0
                    for stick in sticks:
                        if stick==0 and stick!=limit:
                            counter+=1
                    if counter==len(sticks)-1:
                        turn=0
                    else:
                        turn = UserChoice(turn, sticks)
                elif(raw!=limit):
                    while True:
                        remove = int(input("How many number you want to remove ?"))
                        if remove>0:
                            break
                        else:
                            print("Please make legal move")
                    if (sticks[raw] >= remove):
                        sticks[raw] -= remove
                        turn = 0
                    else:
                        print("wrong entry!!")
                        turn=UserChoice(turn,sticks)
            except ValueError:
                print("False Value!!")
            return turn
    def CompChoice(sticks):
        remove,which = nimsum(sticks)
        x = sticks.index(which)
        if (x == Climit):
            for i in range(0,len(sticks)):
                    if sticks[x]==sticks[i]:
                       x=i
        if(x==Climit and sticks[x]>=Chowmuch):
            sticks[x]-=Chowmuch
            print("Computer removed: {} from piles: {}".format(Chowmuch, x + 1))
        else:
            sticks[x] -= remove
            print("Computer removed: {} from piles: {}".format(remove, x + 1))
        return 1
    #control: if all index ==0 ,finish the game
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

    #userLimit(can remove only 1 or 2 some raw)
    limit=random.randint(0,len(sticks)-1)
    howmuch=random.randint(1,2)
    while(howmuch>sticks[limit]):
        howmuch = random.randint(1,2)
    #ComputerLimit(can remove only 1 or 2 some raw)
    Climit=random.randint(0,len(sticks)-1)
    Chowmuch=random.randint(1,2)
    while(Chowmuch>sticks[Climit] or Climit==limit):
        Chowmuch = random.randint(1,2)
        Climit = random.randint(0,len(sticks)-1)

    #Game-Start
    print("--------------------------------------")
    print("User can only remevo {} from pile:{}.".format(howmuch,limit+1))
    print("Computer can only remevo {} from pile:{}.".format(Chowmuch,Climit+1))
    print("--------------------------------------")
    x=True
    while x:
        if x!=False:
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
        if x!=False:
            while turn == 0:
                print("----------------------------")
                print("Current state >>"+str(sticks))
                print("----------------------------")
                turn=CompChoice(sticks)
                x=control(sticks)
                if (x == False):
                    print("""------------------
COMPUTER WINS..
------------------
""")
def NormalGame():
    def int2bin(n, count=24):
        return "".join([str((n >> y) & 1) for y in range(count - 1, -1, -1)])
    def nimsum(sticks):
        nsticks = copy.deepcopy(sticks)
        nim = 0
        for i in range(0, len(nsticks)):
            nim = nim ^ nsticks[i]
        # When nim sum equals zero on the computer do random moves.
        # and control for the number wheter it is legal move or not.
        if nim == 0:
            if turn == 0:
                temp = random.randint(1, 10)
                while True:
                    for piles in range(len(sticks)):
                        if (sticks[piles] >= temp):
                            takeaway = temp
                            return takeaway, sticks[piles]
                    temp = random.randint(1, 10)
        else:
            nimsumb = int2bin(nim)
            nimsumb_str = str(nimsumb).lstrip('0')
            mostsig = len(nimsumb_str)
            highest = 2 ** (mostsig - 1)
            xk = 0
            takeaway = -1
            while takeaway < 1:
                for item in range(0, len(nsticks)):
                    if nsticks[item] >= highest:
                        xk = nsticks[item]
                yk = nim ^ xk
                takeaway = xk - yk
                nsticks.remove(xk)
            return takeaway, xk
    def UserChoice(turn, sticks):
        try:
            while True:
                raw = int(input("Choose a pile:"))
                if raw > 0 and raw <= len(sticks):
                    if sticks[raw - 1] != 0:
                        break
                    else:
                        print("Already zero")
                else:
                    print("Please make legal move")
            raw = raw - 1
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
    def CompChoice(sticks, turn):
        remove, which = nimsum(sticks)
        x = sticks.index(which)
        sticks[x] -= remove
        turn = 1
        print("Computer removed: {} from piles: {}".format(remove, x + 1))
        return turn
    def control(sticks):
        for i in range(len(sticks)):
            while sticks[i] != 0:
                return True
        return False

    turn = 0
    sticks = []
    rawnumber = random.randint(3, 6)

    # Prapering Game Board
    for i in range(0, rawnumber):
        sticks.append(random.randint(1, 10))

    x = True
    while x:
        while turn == 1:
            print("----------------------------")
            print("Current state >>" + str(sticks))
            print("----------------------------")
            turn = UserChoice(turn, sticks)
            x = control(sticks)
            if (x == False):
                print("""------------------
PLAYER WİNS..
------------------
""")
        while turn == 0:
            print("----------------------------")
            print("Current state >>" + str(sticks))
            print("----------------------------")
            turn = CompChoice(sticks, turn)
            x = control(sticks)
            if (x == False):
                print("""------------------
COMPUTER WINS..
------------------
""")

while True:
    print("Game mode")
    print("1-Normal Game")
    print("2-With Limitation")
    print("3-EXIT")
    try:
        gameMode=int(input("Please Choose a Game Mode:"))

        if gameMode==1:
            print("---------------------")
            print("Normal Game Started")
            NormalGame()
        elif gameMode==2:
            print("---------------------")
            print("Limitation Started")
            LimitGame()
        elif gameMode==3:
            print("Please come back again")
            break
        else:
            print("Please make your choice again!!")
    except ValueError:
        print("False Value!!!!")
