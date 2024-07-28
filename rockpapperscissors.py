#rock papper scissors
import sys,random
win = 0
lose = 0
draw = 0

while(True):
    while(True):
        print(str(win)+' wins,'+str(lose)+' loses,'+str(draw)+' draws.')
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playermove = input()
        if(playermove == 'q'):
            print('Game over')
            sys.exit()
        if (playermove == 'r' or playermove == 's' or playermove == 'p'):
            break
    print('please type one of r,s,p or q.')
    if(playermove == 'r'):
        print('ROCK versus...')
    elif(playermove == 'p'):
        print('PAPER versus...')    
    else:
        print('SCISSORS versus...')    
    C = random.randint(1,3)
    if C == 1:
        computerMove = 'r'
        print('ROCK')
    elif C == 2:
        computerMove = 'p'
        print('PAPER')
    elif C == 3:
        computerMove = 's'
        print('SCISSORS')
    if playermove == computerMove:
        print('It is a tie!')
        draw = draw + 1
    elif (playermove == 'r' and computerMove == 's') or (playermove == 'p' and computerMove == 'r') or (playermove == 's' and computerMove == 'p'):
        print('You win!')
        win = win + 1
    else:
        print('You lose')
        lose = lose + 1
