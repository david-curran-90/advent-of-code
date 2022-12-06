#! /usr/local/bin/python3
# take range from input

# ugh global variables I should use a class but it's only advent of code and I'm
# 2 days behind
fullcount = 0
partcount = 0

def readinput(file):
    with open(file, 'r') as f:
        ranges = f.readlines()
    return ranges

def rangetodict(min, max):
    elflist = []
    i = int(min)
    while i <= int(max):
        elflist.append(i)
        i = i + 1
    return elflist

def getrange(elf):
    splt = elf.replace('-', ' ').split(' ')
    min = splt[0]
    max = splt[1]

    elflist=rangetodict(min, max)

    return elflist

def compareranges(elves, search):
    global fullcount
    global partcount
    elf1 = elves[0]
    elf2 = elves[1]

    if search == "full":
        if elf1[0] in elf2 and elf1[-1] in elf2:
            fullcount = fullcount + 1 
        elif elf2[0] in elf1 and elf2[-1] in elf1:
            fullcount = fullcount + 1 
        return fullcount
    elif search == "part":
        for a in elf1:
            if a in elf2:
                partcount = partcount + 1
                break
        return partcount

def splitpair(pair):
    elf1 = pair[0]
    elf2 = pair[1].strip('\n')

    elf1range=getrange(elf1)
    elf2range=getrange(elf2)
    
    return[elf1range, elf2range]

if __name__ == "__main__":
    ranges=readinput("input.txt")
    for r in ranges:
        pair = r.split(',')
        spltpr = splitpair(pair)
        full = compareranges(spltpr, "full")
        part = compareranges(spltpr, "part")

    print("%s Elf pairs fully overlap" % (full))
    print("%s Elf pairs partially overlap" % (part))
