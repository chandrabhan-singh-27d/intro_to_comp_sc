# Formulation: A farmer has certain number of headcount and legcount and he wants to get the exact number of chickens and pigs out of that herd.

def getPetsNum(headCount, legCount):
    for numChicks in range (0, headCount+1):
        numPigs = headCount - numChicks
        totLegs = 2*numChicks + 4*numPigs
        if totLegs == legCount:
            return (numChicks, numPigs)
    return (None, None)

def giveYardInput():
    heads = int(input('Enter the number of heads: '))
    legs = int(input('Enter the number of legs: '))
    pigs, chickens = getPetsNum(heads, legs)
    if pigs == None:
        print ('There is no solution')
    else: 
        print ('Number of pigs: ', pigs)
        print ('Number of chickens: ', chickens)

giveYardInput()
