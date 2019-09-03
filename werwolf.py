import random, ast

def createDict():
    with open('no_of_players.txt','r') as f:
        numberOfPlayers = f.read()
        numberOfPlayers = int(numberOfPlayers)

    with open('narrator_flag.txt','r') as fl:
        narrator_flag = bool(fl.read())

    wolf = numberOfPlayers // 4
    witch = numberOfPlayers // 12
    clairvoyant = numberOfPlayers // 12
    if witch == 0 :
        witch = 1
    if clairvoyant == 0 :
        clairvoyant = 1
    hunter = 0
    if numberOfPlayers >= 10:
        hunter = 1

    if narrator_flag == 1:
        if hunter > 0:
            assign = {'storyteller' : 1, 'wolf' : wolf, 'witch' : witch, 'clairvoyant' : clairvoyant, 'hunter' : hunter, 'citizen' : (numberOfPlayers-wolf-clairvoyant-witch-hunter-1)} #narrator = 1
        else:
            assign = {'storyteller' : 1, 'wolf' : wolf, 'witch' : witch, 'clairvoyant' : clairvoyant, 'citizen' : (numberOfPlayers-wolf-clairvoyant-witch-1)}
    else:
        if hunter > 0:
            assign = {'wolf' : wolf, 'witch' : witch, 'clairvoyant' : clairvoyant, 'hunter' : hunter, 'citizen' : (numberOfPlayers-wolf-clairvoyant-witch-hunter)}
        else:
            assign = {'wolf' : wolf, 'witch' : witch, 'clairvoyant' : clairvoyant, 'citizen' : (numberOfPlayers-wolf-clairvoyant-witch)}
    keys = [ key for key in assign]

    with open('available.txt', 'w+') as a:
        a.write(str(assign))

def deduct():
    with open('available.txt', 'r+') as a:
        assign = a.read()
        print(assign)
        assign = ast.literal_eval(assign)
        #print(type(assign))
        keys = [ key for key in assign ]

    if sum(assign.values()) == 0:
        return(0)

    def assignment():
        while sum(assign.values()) >=0:
            num = random.randint(0,len(assign)-1)
            if assign[keys[num]] > 0:
                assign[keys[num]] -= 1
                if assign[keys[num]] == 0:
                    del assign[keys[num]]
                return num
            else:
                num = random.randint(0,len(assign)-1)
                assignment()
    ind = assignment()
    print(assign)
    with open('available.txt', 'w+') as b:
        b.write(str(assign))
    result = keys[ind]
    return(result)
