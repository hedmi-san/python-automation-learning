import zombiedice,random
class Myzombie:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        # gameState is a dictionary (map) with info about the current state of the game.
        # You can choose to ignore it in your code.
        diceRollResults = zombiedice.roll() # first roll
        # roll() returns a dictionary with keys 'brains', 'shotgun', and
        # 'footsteps' with how many rolls of each type there were.
        # The 'rolls' key is a list of (color, icon) tuples with the
        # exact roll result information.
        # Example of a roll() return value:
        # {'brains': 1, 'footsteps': 1, 'shotgun': 1,
        # 'rolls': [('yellow', 'brains'), ('red', 'footsteps'),
        # ('green', 'shotgun')]}
        # REPLACE THIS ZOMBIE CODE WITH YOUR OWN:
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains < 2:
                diceRollResults = zombiedice.roll() # roll again
            else:
                break
class FirstBot:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if (random.randint(0,1) > 0):
                diceRollResults = zombiedice.roll() # roll again
            else:
                break

class SecondBot:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        brains = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            if brains == 2:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class ThirdBot:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll() 
        brains = 0
        shotgun = 0
        while diceRollResults is not None:
            brains += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']
            if shotgun == 2:
                break
            else:
                diceRollResults = zombiedice.roll() # roll again

class FourthBot:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        a = random.randint(1, 4)
        shotgun = 0
        for i in range(0,a):
            if shotgun < 2 and i <a:
                diceRollResults = zombiedice.roll()
                shotgun += diceRollResults['shotgun']
            else:
                break

class FifthBot:
    def __init__(self,name):
        self.name = name
    def turn(self, gameState):
        diceRollResults = zombiedice.roll()
        shotgun = 0
        brain = 0
        while diceRollResults is not None:
            brain += diceRollResults['brains']
            shotgun += diceRollResults['shotgun']
            if shotgun  > brain:
                break
            else : 
                diceRollResults = zombiedice.roll()
        

zombies = (zombiedice.examples.RandomCoinFlipZombie(name='Random'),zombiedice.examples.RollsUntilInTheLeadZombie(name='Until Leading'),zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 2 Shotguns', minShotguns=2),
zombiedice.examples.MinNumShotgunsThenStopsZombie(name='Stop at 1 Shotgun', minShotguns=1),Myzombie(name='My Zombie Bot'),FirstBot(name='first bot'),SecondBot(name='second bot'),ThirdBot(name='third bot'),FourthBot(name='fourth bot'),FifthBot(name='fifth bot')
# Add any other zombie players here.
)
# Uncomment one of the following lines to run in CLI or Web GUI mode:
# zombiedice.runTournament(zombies=zombies, numGames=1000)
zombiedice.runWebGui(zombies=zombies, numGames=1000)