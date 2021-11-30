# CTI 110
# P5BONUS - Football Sim Prototype
# Name
# Date

# With a little rebranding, this could be turned into a
# variety of "sim" games.

# We'll start with a one sided game where the player is always
# on offense. Their goal is to score a goal or a down.
# Notes for Football Sim

"""
Offensive moves:
run, pass, kick (fg/punt)

Defensive moves:
rush, pass defense, kick defense

should have a R/P/S type of interaction

Each round:
- Offense picks move
- Defense picks move
- Calculate the results

Possible results:
- gain or loss (yards)
- Turnover (ex: interception, fumble)

ex:
("gain", 7) # for a regular play
("interception", 0) # intercepted pass
("turnover", 40)   # other team successfully punts


SPOT FOR TODO notes:
Need to display current yards to first down.
end TODO

Defensive plays:
run defense - man blocking, zone blocking
pass defense - 
kick defense - 
"""
import random

def report(currentYardage, yardsRemaining, currentDown):
    message = f"Down: {currentDown} and {yardsRemaining}, Ball on {currentYardage} yd line"
    print (message)

def getPlayerMove():
    action = input("Choose run, pass, or kick: ")
    return action

def getCPUMove():
  options = ["Rush", "Pass Defense", "Kick Defense"]
  # for now, random choice 
  pick = random.choice(options)
  return pick

def PlayOneRound():
    """
    One round here is one offense possession - play until
    you score, or lose possession.
    To simplify: start on 50 yard line, count down.
    TODO: This is only one offensive possession --
    the full version should switch offense and defense
    """
    startLine = 50
    currentLine = 50
    yardsRemaining = 10 # yards till 1st down
    down = 1
    keepPossession = True

    while keepPossession == True:
        
        report(currentLine, yardsRemaining, down)
        move = getPlayerMove()
        cpuMove = getCPUMove()

        # plays return two values, result and yardage

        if move == "run":
            # handle running plays
            result, distance = runningPlay(cpuMove)
            
        if move == "pass":
            # handle passing plays
            result, distance = passingPlay(cpuMove)
        if move == "kick":
            # handle field goals, etc
            result, distance = fieldGoalAttempt(cpuMove, currentLine)
    
        # Update the game state
        currentLine = currentLine - distance # counting 50 -> 0
        print("-" * 40)
        print("You chose", move, " - CPU chose", cpuMove)
        print("Play result" , result)
        if distance > 0:
            print("That play gained you", distance, "yards")
        else:
            print("That play lost you", abs(distance), "yards")
        print("After that play, you are on", currentLine)

        # Update what down we're on and yards left to 1st down
        down = down + 1
        yardsRemaining = yardsRemaining - distance
        
        if down > 4:
            print("*** TURNOVER ***")
            keepPossession = False
        if currentLine <= 0:
            currentLine = 0
            print("*** TOUCHDOWN ***")
            keepPossession = False
        


        if yardsRemaining < 0:
            print("*** FIRST DOWN ***")
            down = 1
            startLine = currentLine
            yardsRemaining = 10
        else:
            print("Next play...")
            # gained < 10 yards, so update down and distance
            #startLine = currentLine
    

# Various functions for determining how well plays go
def runningPlay(cpuMove):
    """ returns: result type (string), yards gained (or lost, if negative). """
    # idea borrowed from https://github.com/wcastil/football-simulation
    # these are running gains, so they should be moved
    # base results
    possibleGains = [0,0,1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,9,10,10,11,11,12,12,13,14,15]
    distance = random.choice(possibleGains)
    result = "gain"

    if cpuMove == "Rush":
      # for now, run defense just makes running less effective
      distance = distance - random.randint(1, 5)
      if distance < 0:
        result = "loss"

    return result, distance


def passingPlay(cpuMove):
  # the * signs add that many of the entry (for example, 7 zeros)
  gains = [0]*7+[2]*5+[3,4]*4+[5]*3+[6,7,8]*2+[9,10,11]*2+[12,13,14,15,16,17,18,19,20,22,24,25]
  distance = random.choice(gains)
  result = "gain"

  if cpuMove == "Pass Defense":
      # 10% chance of intercept if opponent is running pass Defense
      if random.randint(1, 100) < 10:
        result = "interception"
        distance = 0
      else:
        # pass defense just makes pass less effective
        distance = distance - random.randint(1, 5)
        if distance < 0:
          result = "loss"

  return result, distance

def fieldGoalAttempt(cpuMove, yardage):
  """
  Kick is either punt or field goal:
  - punt: add as much distance as possible, turnover
  - FG:   rolls the dice, odds are best between 15-35 yds 
  """
  
  choice = input("Kick: Choose [p]unt or [f]ield Goal: ")
  if choice == "p" or choice == "punt":
    # go for a punt
    distance = random.randrange(30, 50)
    if cpuMove == "Kick Defense":
      distance = distance - 10
    result = "Turnover"
  else: # go for FG
    odds = 0 # odds are %, 0 to 100
    if cpuMove == "Kick Defense":
      odds = odds -20 # take off 20%
    if yardage >= 15 and yardage <= 35:
      odds = odds + 70 # add 70%
    else:
      odds = odds + 30
    roll = random.randrange(1, 100) 
    if roll < odds:
      result = "Field Goal"
      distance = 0
    else:
      result = "Turnover"
      distance = 0
  # we have result and distance
  return result, distance




def main():
    PlayOneRound() # this is one possession on offense
    



# start program
if __name__ == "__main__":
    main()
