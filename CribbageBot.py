import random

def findingPoints(points, hand):
    #checking for pairs
    for i in range(len(hand)):
        points+= (hand.count(hand[i])-1)

    #checking for fifteens in two cards
    for i in range(len(hand)):
        for j in range(len(hand)):
            if i!=j and hand[i]+hand[j] == 15:
                points+=(2/2)


    #checking for fifteens in three cards
    for i in range(len(hand)):
        for j in range(len(hand)):
            for l in range(len(hand)):
                if i!=j and j!=l and hand[i]+hand[j]+hand[l] == 15:
                    points+=(2/3)

    #checking for fifteens in four cards
    for i in range(len(hand)):
        for j in range(len(hand)):
            for l in range(len(hand)):
                for k in range(len(hand)):
                    if i!=j and j!=l and l!=k and hand[i]+hand[j]+hand[l]+hand[k] == 15:
                        points+=(2/4)

    #checkiong for fifteens in all the cards
    if(len(hand) == 5):
        if hand[0]+hand[1]+hand[2]+hand[3]+hand[4] == 15:
            points+=2

    #checking for runs
    hand.sort()
    do4 = True
    do3 = True

    #checking for runs of 5
    for a in range(len(hand)):
        for b in range(len(hand)):
            for c in range(len(hand)):
                for d in range(len(hand)):
                    for e in range(len(hand)):
                        if hand[a]+1 == hand[b] and hand[b]+1 == hand[c] and hand[c]+1 == hand[d] and hand[d]+1 == hand[e]:
                            points+=5
                            do4 = False
                            do3 = False
    #checking for runs of 4
    if do4:
        for a in range(len(hand)):
            for b in range(len(hand)):
                for c in range(len(hand)):
                    for d in range(len(hand)):
                        if hand[a]+1 == hand[b] and hand[b]+1 == hand[c] and hand[c]+1 == hand[d]:
                            points+=4
                            do3 = False
    #checking for runs 3
    if do3:
        for a in range(len(hand)):
            for b in range(len(hand)):
                for c in range(len(hand)):
                    if hand[a]+1 == hand[b] and hand[b]+1 == hand[c]:
                        points+=3

    return points

gameOn = True
cribChooses = True
while gameOn:
    #setting up the hand
    hand = []
    playerHand = []
    playerPoints = 0
    points = 0
    for i in range(6):
        hand.append(random.randint(1,10))
        playerHand.append(random.randint(1,10))

    crib = []
    highestPoints = [0]
    for a in range(6):
        for b in range(6):
            for c in range(6):
                for d in range(6):
                    if a!=b and b!=c and c!=d and d!=a:
                        testHand = [hand[a],hand[b],hand[c],hand[d]]
                        if highestPoints < findingPoints(0,testHand):
                            highestPoints = [findingPoints(0,testHand),a,b,c,d]

    handAfterCrib = [highestPoints[1],highestPoints[2],highestPoints[3],highestPoints[4]]
    hand.pop[highestPoints[1]]
    hand.pop[highestPoints[2]]
    hand.pop[highestPoints[3]]
    hand.pop[highestPoints[4]]
    crib.append(hand[0])
    crib.append(hand[1])

    print("Here are your cards")
    print(playerHand)

    for i in range(2):
        print("enter a card for the crib")
        cribcard = int(input("> "))
        crib.append(cribcard)
        playerHand.pop(playerHand.indexOf(cribcard))

    #da crib
    if cribChooses == True:
        hand.append(crib)
        cribChooses = False
    elif cribChooses == False:
        playerHand.append(crib)
        cribChooses = True

    # #pegging
    # pegTotal = 0
    # beep = True
    # handForPegging = []
    # otherHandForPeggin = []
    # while beep:
    #     print(pegTotal)
    #     if cribChooses == True:
    #         cribChooses = False
    #         print("your cards are")
    #         print(playerHand)
    #         print("Now will you please just ACTUALLY PEG!!!!!!!!!!!1")
    #         peg = int(input("> "))
    #         for i in range(len(hand)):
    #             if playerHand[i] == peg:
    #                 pegTotal+=peg
    #                 playerHand.pop(i)
    #                 print(pegTotal)
    #                 break
    #     else:
    #         for i in range(len(hand)):
    #             if hand[i] + pegTotal >= 31:
    #                 cribChooses = False
    #                 pegTotal+=hand[i]
    #                 hand.pop(i)
    #                 if pegTotal == 31:
    #                     points+=3
    
        


