
from random import randrange

def inputdata1():  #First test
    test = "test worked 1"
    dictionary1 = {"test1": test}
    return dictionary1


def inputdata2(): #Second test to see if multiple datas woild would work
    test1 = "t"
    dictionary1 = {"test2": test1}
    return dictionary1

def picran(): # /static/ + random number + .jpg so it would call a random jpg file because I named them all number.jpg and thet are in the static folder
    picture = int(randrange(6))
    picture2 = "/static/" + str(picture) + ".jpg"
    if picture == 1:
        repel1 = "https://picture1website1.jhunt11111.repl.run"
    elif picture == 5:
        repel1 = "https://picture5website1.jhunt11111.repl.run"
    elif picture == 3:
        repel1 = "https://picture3website1.jhunt11111.repl.run"
    elif picture == 0:
        repel1 = "https://picture0website1.jhunt11111.repl.run"
    elif picture == 2:
        repel1 = "https://picture2website1.jhunt11111.repl.run"
    elif picture == 4:
        repel1 = "https://picture4website1.jhunt11111.repl.run"
    else:
        repel1 = str(picture)
    dictionary2 = {"picture": picture2, "repel1": repel1}
    return dictionary2
