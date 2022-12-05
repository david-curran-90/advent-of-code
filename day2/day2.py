#! /usr/local/bin/python3
# rock = A
# paper = B
# scissors = C  
win = 6
draw = 3
lose = 0

A = 1
B = 2
C = 3
X = A
Y = B
Z = C

score = 0

round="A Y".split()

def calculatewin(point):
    return point + win

def calculatedraw(point):
    return point + draw

# code for calucalting the first part of the challenge
# this won't be called but keeping as part of the codebase
def playround_one(round):
    oppo = round[0]
    mine = round[1]

    if mine == 'X':
        point = X
        if oppo == 'C':
            point = calculatewin(point)
        elif oppo == 'A':
            point = calculatedraw(point)
        
    elif mine == 'Y':
        point = Y
        if oppo == 'A':
            point = calculatewin(point)
        elif oppo == 'B':
            point = calculatedraw(point)
    elif mine == 'Z':
        point = Z
        if oppo == 'B':
            point = calculatewin(point)
        elif oppo == 'C':
            point = calculatedraw(point)
    else:
        print("Invalid turn, you're cheating")
    
    return point

# code for calculating the second part of the challenge
def playround_two(round):
    oppo = round[0]
    outcome = round[1]

    lose = {
        'A' : C ,
        'B' : A,
        'C' : B,
    }
    win = {
        'A' : B,
        'B' : C,
        'C' : A,
    }
    draw = {
        'A' : A,
        'B' : B,
        'C' : C,
    }

    if outcome == 'X':
        point = lose[oppo]
    if outcome == 'Y':
        point = calculatedraw(draw[oppo])
    if outcome == 'Z':
        point = calculatewin(win[oppo])

    return point

def readinput(file):
    with open(file) as f:
        rounds = f.readlines()
        return rounds

if __name__ == "__main__":
    rounds = readinput('input.txt')
    for r in rounds:
        round = r.split()
        point = playround_two(round)
        score = score + point
    print(score)
