#! /usr/local/bin/python3



def readinput(file):
    with open(file, 'r') as f:
        contents = f.readlines()
    return contents

def splitbackpack(line):
    pocket1 = line[0:len(line)//2]
    pocket2 = line[len(line)//2:]
    return[pocket1, pocket2] 

def calcmatch(c):
    try:
        priority = priorities[c]
    except Exception:
        priority = 0
    return priority

def comparepockets(pockets):
    p1 = pockets[0]
    p2 = pockets[1]
    for c in p1:
        if c in p2:
            return c

def getbadge(bags):
    for c in bags[0]:
        if c in bags[1] and c in bags[2]:
            return c

def getbadges(lines):
    # loop over, 3 at a time and compare badges
    priority=0
    bags=[]
    bagnum=0
    for line in lines:
        bagnum += 1
        bags.append(line.strip('\n'))
        if bagnum == 3:
            priority = priority + priorities[getbadge(bags)]
            bagnum = 0
            bags=[]
            
    return priority
        

if __name__ == "__main__":
    priorities = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52,
    }
    input = readinput("input.txt")
    n = 0
    b = 0
    for l in input:
        item=comparepockets(splitbackpack(l))
        n = n + calcmatch(item)

    b = getbadges(input)

    print("Total of all priorities = %s" % (n))
    print("Total of badge priorities = %s" % (b))
