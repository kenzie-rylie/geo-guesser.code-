
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
    dictionary2 = {"picture": picture2}
    return dictionary2
