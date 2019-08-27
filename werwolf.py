import random, ast

def createDict():
    with open('no_of_players.txt','r') as f:
        numberOfPlayers = f.read()
        numberOfPlayers = int(numberOfPlayers)
    wolves = numberOfPlayers // 4
    witch = numberOfPlayers // 10
    watcher = numberOfPlayers // 10
    if witch == 0 :
        witch = 1
    if watcher == 0 :
        watcher = 1

    assign = {'wolves' : wolves, 'witch' : witch, 'watcher' : watcher, 'citizen' : (numberOfPlayers-wolves-watcher-witch)}
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
