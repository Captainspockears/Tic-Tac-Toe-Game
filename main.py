from time import sleep

savedgameflag = False
validmove = False
whowon = 0
player1points = 0
player2points = 0
player1sign = 'X'
player2sign = 'O'
winflag = False
eleList = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
winlist = [[1, 1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 1, 1],
           [1, 0, 0, 1, 0, 0, 1, 0, 0], [0, 1, 0, 0, 1, 0, 0, 1, 0], [0, 0, 1, 0, 0, 1, 0, 0, 1],
           [0, 0, 1, 0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0, 1]]


def createbourd(ele):
    print('| {} | {} | {} |'.format(ele[6], ele[7], ele[8]))
    print('|---|---|---|')
    print('| {} | {} | {} |'.format(ele[3], ele[4], ele[5]))
    print('|---|---|---|')
    print('| {} | {} | {} |'.format(ele[0], ele[1], ele[2]))


def comparelists(i, j):
    for c in range(0, len(i)):
        if not i[c] == j[c]:
            return False
    return True


def printlist(i):
    strlist = ""
    for c in i:
        strlist = strlist + str(c) + " "
    print(strlist)


def home():
    global savedgameflag

    if savedgameflag:
        print('Player 1 Score: {}'.format(player1points))
        print('Player 2 Score: {}'.format(player2points))
        newgameprompt = input('Would you like to play another game? (Y/N)')
        if newgameprompt == 'Y':
            continuegame()
        else:
            savedgameflag = False
            exit(0)
    else:
        newgame()


def convert(ele, sign):
    eletemp = []
    for i in ele:
        if i == sign:
            eletemp.append(1)
        else:
            eletemp.append(0)
    return eletemp


def checkwin(ele, sign):
    global winflag
    eletemp = convert(ele, sign)
    for (i, j) in enumerate(winlist):
        # print(i)
        # printlist(j)
        # printlist(eletemp)
        winflag = comparelists(j, eletemp)
        if winflag:
            return


def getmove(playermoves, playernumb):
    global validmove
    validmove = False
    playermove = 0
    while not validmove:
        playermove = int(input("Player {} turn. (1-9)".format(playernumb)))
        validmove = True
        for i in playermoves:
            if i == playermove:
                print("This cell has already been marked, please choose another cell.")
                validmove = False
                continue
    return playermove


def gamemech():
    global player1sign
    global player2sign
    global eleList
    global whowon
    global player1points
    global player2points
    global savedgameflag
    playermoves = [0]

    count = 0

    while not count == 9:
        player1move = getmove(playermoves, 1)
        playermoves.append(player1move)
        count = count + 1
        eleList[player1move - 1] = player1sign
        createbourd(eleList)
        checkwin(eleList, player1sign)
        if winflag:
            whowon = 1
            break
        player2move = getmove(playermoves, 2)
        playermoves.append(player2move)
        count = count + 1
        eleList[player2move - 1] = player2sign
        createbourd(eleList)
        checkwin(eleList, player2sign)
        if winflag:
            whowon = 2
            break

    if whowon == 1:
        print("Player {} won".format(whowon))
        player1points = player1points + 1
        savedgameflag = True
    elif whowon == 2:
        print("Player {} won".format(whowon))
        player2points = player2points + 1
        savedgameflag = True
    else:
        print("Its a draw!")
        player1points = player1points + 1
        player2points = player2points + 1
        savedgameflag = True


def newgame():
    global player1sign
    global player2sign
    print("Welcome to captainspockear's Tic Tac Toe!")
    sleep(1)
    player1sign = input('Player 1 pls choose X or O. (X/O)')
    if player1sign == 'X':
        player2sign = 'O'
    else:
        player2sign = 'X'

    createbourd(eleList)
    gamemech()


def continuegame():
    global eleList
    global whowon
    global winflag
    global validmove

    eleList = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    whowon = 0
    winflag = False
    validmove = False
    createbourd(eleList)
    gamemech()


while 0 == 0:
    home()
