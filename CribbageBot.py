import random
from itertools import combinations

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
    for combo in combinations(hand, 3):
        if sum(combo) == 15:
            points += 2

    # Checking for fifteens in four cards
    for combo in combinations(hand, 4):
        if sum(combo) == 15:
            points += 2

    # Checking for fifteens in all the cards
    if len(hand) == 5 and sum(hand) == 15:
        points += 2

    # Checking for runs
    hand.sort()
    run_length = 1
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
    highestPoints = 0
    handAfterCrib = []

    # Selecting cards for the crib
    for combo in combinations(hand, 4):
        currentPoints = findingPoints(0, list(combo))
        if currentPoints > highestPoints:
            highestPoints = currentPoints
            handAfterCrib = list(combo)

    # Remove the selected cards from hand
    for card in handAfterCrib:
        hand.remove(card)

    # Add the crib cards
    crib.extend(handAfterCrib)  # Extend the crib with the selected cards
    hand = hand[:2]  # Keep only the first two cards in hand

    print("Here are your cards:")
    print(playerHand)

    # Da crib
    if cribChooses:
        hand += crib
        cribChooses = False
        print("It is the computer's crib")
    else:
        playerHand += crib
        cribChooses = True
        print("It is your crib")

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

    beeppity = random.randint(1, 10)
    hand.append(beeppity)

    print(f"The cut card is: {beeppity}")

    # Counting points
    newpoints = findingPoints(points, hand)
    newplayerpoints = findingPoints(0, playerHand)

    print(f"Points for the computer: {newpoints}")
    print(f"Player points: {newplayerpoints}")

    if newpoints > 22:
        newpoints = 22
    if newplayerpoints > 22:
        newplayerpoints = 22

    points += newpoints
    playerPoints += newplayerpoints

    # Logic to continue or end the game can be added here
    if playerPoints >= 120:
        if points <= 80:
            print("Dangggggg you skunked them")
        else:
            print("Nice job on that win")
        gameOn = False  # End the game
    elif points >= 120:
        if playerPoints <= 80:
            print("Come Onnnnnnn you got skunked")
        else:
            print("I mean you could do better next time")
        gameOn = False  # End the game
