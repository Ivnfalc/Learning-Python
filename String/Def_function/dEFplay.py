from random import shuffle



mylist = [' ',' ','O']

def slist(mylist):
    shuffle(mylist)
    return mylist

result = slist(mylist)
print(result)

def playerguess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("pick a number 1,2 or 3")

    return int(guess)
print(playerguess())

def checkg(mylist,guess):
    if mylist[guess] == 'O':
        print("correct")
    else:
        print("wrong")
        print(mylist)
