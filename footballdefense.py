# Defensive module of the football sim
# Started with CTI 110.0006

import random

"""
Ideas:
Right now we're just doing 3 options, should flesh it out 
with man/zone, exit
- Run Defense
- Pass Defense
- Kick Defense (special case )
- Goal Line Defense if near endzone (special case)

Each of these should have a few authentic play names to make it sound good

"""
def report(currentYardage, yardsRemaining, currentDown):

  downNames = ["1st", "2nd", "3rd", "4th"]
  downName = downNames[currentDown-1]

  message = f"Down: {downName} and {yardsRemaining}, Ball on {currentYardage} yd line"
  print (message)

def getPlayerMove():
    # TODO: This is getting changed a lot -- just a test
    action = input("Choose (R)un Defense, (P)ass Defense, or (K)ick Defense: ")
    action = action.lower()
    return action

def CPUPickOffense(currentYards):
  # CPU won't kick unless close enough for FG
  # TODO: this is still pretty dumb coaching
  options = ["Run", "Pass"]
  if currentYards < 35 and currentYards > 15:
    options = ["Run", "Pass", "Kick"]  # for now, random choice 
  pick = random.choice(options)
  return "Run" #TODO FIX

def doRunningPlay(defensivePlay):
  """ calculate result and distance. If defense picked 
  a run defense play, then offense won't do as well"""

  result = "Gain"
  distance = random.randint(0, 15)

  if defensivePlay[0] == "r": # first letter
    # run defense means worse running play 
    distance = distance - random.randint(0, 10)

  if distance < 0:
    result = "Loss"

  return result, distance


def PlayDefense():
  """
  Play until the ball is turned over -- either because you get it,
  or they score. Goal is to minimize enemy points.
  """
  currentYards = 50
  previousYards = 50
  yardsRemaining = 10 # yards until first down
  down = 1
  switchPossession= False
  print("CPU Team has the ball -- you are on defense.")
  report(currentYards, yardsRemaining, down)

  # keep possession until turnover
  while switchPossession == False:
    offensivePlay = CPUPickOffense(currentYards)
    defensivePlay = getPlayerMove()

    # Based on the offense and defense plays, figure out what happens
    if offensivePlay == "Run": # check first character for "r" or "R"
      result, distance = doRunningPlay(defensivePlay)
    # TODO: add running and kick Plays 

    currentYards = currentYards - distance
    yardsRemaining = yardsRemaining - distance

    print("Offense went for:", offensivePlay)
    print("Based on your defense, they have a")
    print(result, "of", distance, "yards")



  

def main():
  PlayDefense()


if __name__ == "__main__":
  main()