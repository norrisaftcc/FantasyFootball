# CTI 110
# P5BONUS - Football Sim Prototype
# Name
# Date

# With a little rebranding, this could be turned into a
# variety of "sim" games.

# We'll start with a one sided game where the player is always
# on offense. Their goal is to score a goal or a down.

import random

def report(currentYardage, currentDown):
    message = f"Down: {currentDown}, Ball on {currentYardage} yd line"
    print (message)

def getPlayerMove():
    action = input("Choose run, pass, or kick: ")
    return action

def PlayOneRound():
    """
    One round here is one offense possession - play until
    you score, or lose possession.
    To simplify: start on 50 yard line, count down.
    """
    startLine = 50
    currentLine = 50
    down = 1
    keepPossession = True

    while keepPossession == True:
        
        report(currentLine, down)
        move = getPlayerMove()

        if move == "run":
            # handle running plays
            distance = runningPlay()
            
        if move == "pass":
            # handle passing plays
            distance = passingPlay()
        if move == "kick":
            # handle field goals, etc
            distance = fieldGoalAttempt()
    
        # Update the game state
        currentLine = currentLine - distance # counting 50 -> 0
        if distance > 0:
            print("That play gained you", distance, "yards")
        else:
            print("That play lost you", abs(distance), "yards")
        print("After that play, you are on ", currentLine)
        down = down + 1
        if down > 4:
            print("*** TURNOVER ***")
            keepPossession = False
        if currentLine <= 0:
            currentLine = 0
            print("*** TOUCHDOWN ***")
            keepPossession = False
        if currentLine <= startLine - 10: # 10 yard gain
            print("*** FIRST DOWN ***")
            down = 1
            startLine = currentLine
        else:
            print("Next play...")
            # gained < 10 yards, so update down and distance
            #startLine = currentLine
    

# Various functions for determining how well plays go
def runningPlay():
    """ returns yards gained (or lost, if negative). """

    # This could be anything -
    # 10% of a bad play and losing yards, 10% awesome play
    # otherwise middling result

    roll = random.randint(1, 100)
    if roll < 10: # bad play!
        distance = 0 - random.randint(1, 10)
    elif roll > 90: # great play!
        distance = random.randint(1, 20)
    else: # middling result
        distance = random.randint(1, 20) - 10
    return distance

def passingPlay():
    # idea borrowed from https://github.com/wcastil/football-simulation
    # these are running gains, so they should be moved
    possibleGains = [0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,9,10,10,11,11,12,12,13,14,15]
    gainFromPlay = random.choice(possibleGains)
    return gainFromPlay

def fieldGoalAttempt():
    return random.randint(1, 20) # TODO


def main():
    PlayOneRound() # this is one possession on offense
    



# start program
if __name__ == "__main__":
    main()
