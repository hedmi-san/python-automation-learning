# guessing game 
import random 
secretNumber = random.randint(1,20)
print('I\'m thinking of a number between 1 and 20')
print('You can guess five times')
for tries in range(1,6):
    print('Take a guess :')
    number = int(input())
    if(number < secretNumber):
        print('Your guess is low')
    elif(number > secretNumber):
        print('Your guess is high')
    else:
        break
if number == secretNumber:
    print('Good job! You guessed my number in ' + str(tries) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))