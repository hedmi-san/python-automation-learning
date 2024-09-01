import random,time

numberofquestions = 10
correctanswers = 0

for questionNumber in range(numberofquestions) : 
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    print(f'#{questionNumber}: {num1} x {num2} = ')
    for i in range(0,3):
        answer = int(input())
        if answer == (num1*num2):
            print('correct')
            correctanswers +=1
            break
        elif i == 2 and answer != (num1*num2)  : 
            print('you run out of tries')
        else :
            print('incorrect')
            continue
    time.sleep(1)


