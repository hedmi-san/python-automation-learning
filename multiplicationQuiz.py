import pyinputplus as pyip
import random,time

numberofquestions = 10
correctanswers = 0
for questionNumber in range(numberofquestions):
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = '%(questionNumber,num1,num2)
    try:
        pyip.inputStr(prompt,allowRegexes=['^%s$'%(num1*num2)],blockRegexes=[('.*','incorrect!')],timeout=8,limit=3)
    except pyip.TimeoutException :
        print('Out of time!')
    except pyip.RetryLimitException : 
        print('Out of tries!')
    else : 
        print('correct!')
        correctanswers +=1
    time.sleep(1)
print('Score: %s / %s '%(correctanswers,numberofquestions))

