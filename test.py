import random, ast


with open('available.txt', 'r+') as a:
    assign = a.read()
    print(assign)
    assign = ast.literal_eval(assign)
    #print(type(assign))
    keys = [ key for key in assign ]


    def remove():
        num = random.randint(0,len(assign)-1)
        if assign[keys[num]] > 0:
            assign[keys[num]] -= 1
            return num
        else:
            num = random.randint(0,len(assign)-1)
            remove()

    ind = remove()
    print(assign)
    with open('available.txt', 'w+') as b:
        b.write(str(assign))
    result = keys[ind]
    
