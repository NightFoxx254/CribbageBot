import random

def findingPoints(points, hand):
    # Checking for pairs
    for card in hand:
        points += (hand.count(card) - 1)

    # Checking for fifteens in two cards
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            if hand[i] + hand[j] == 15:
                points += 2

    # Checking for fifteens in three cards
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                if hand[i] + hand[j] + hand[k] == 15:
                    points += 2

    # Checking for fifteens in four cards
    for i in range(len(hand)):
        for j in range(i + 1, len(hand)):
            for k in range(j + 1, len(hand)):
                for l in range(k + 1, len(hand)):
                    if hand[i] + hand[j] + hand[k] + hand[l] == 15:
                        points += 2

    # Checking for fifteens in all the cards
    if len(hand) == 5 and sum(hand) == 15:
        points += 2

    # Checking for runs
    hand.sort()
    run_length = 1
    points += 0  # Initialize points for runs

    for i in range(1, len(hand)):
        if hand[i] == hand[i - 1] + 1:
            run_length += 1
        else:
            if run_length >= 3:
                points += run_length
            run_length = 1  # Reset for the next sequence

    if run_length >= 3:
        points += run_length

    return points

gameOn = True
cribChooses = True
points = 0
playerPoints = 0

while gameOn:
    print(" ")
    print(f"You have {playerPoints} points")
    print(f"and the computer has {points} points")
    # Setting up the hand
    hand = [random.randint(1, 10) for _ in range(6)]
    playerHand = [random.randint(1, 10) for _ in range(6)]
    crib = []
    highestPoints = [0]

    for a in range(len(hand)):
        for b in range(a + 1, len(hand)):
            for c in range(b + 1, len(hand)):
                for d in range(c + 1, len(hand)):
                    testHand = [hand[a], hand[b], hand[c], hand[d]]
                    currentPoints = findingPoints(0, testHand)
                    if currentPoints > highestPoints[0]:
                        highestPoints = [currentPoints]
                        handAfterCrib = [a, b, c, d]

    # Remove cards from hand for crib
    for index in sorted(handAfterCrib, reverse=True):
        hand.pop(index)

    crib += hand[:2]  # Add the first two cards to the crib
    hand = hand[2:]  # Remaining cards stay in hand

    print("Here are your cards:")
    print(playerHand)
    # Da crib
    if cribChooses:
        hand += crib
        cribChooses = False
        print("It is the computers crib")
    else:
        playerHand += crib
        cribChooses = True
        print("it is your crib3")

    for _ in range(2):
        while True:
            try:
                cribcard = int(input("Enter a card for the crib: "))
                if cribcard in playerHand:
                    crib.append(cribcard)
                    playerHand.remove(cribcard)
                    break
                else:
                    print("You do not have that card. Please choose again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    beeppity = random.randint(1,10)
    playerHand.append(beeppity)
    hand.append(beeppity)
    print(f"the cut card is:{beeppity}")
