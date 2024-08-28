# how to keep an idiot busy for period of time

import pyinputplus as pyip 

def englishver():
    while True : 
        prompt = 'Want to know how to keep an idiot busy for hours?\n'
        response = pyip.inputYesNo(prompt)
        if response == 'no' : 
            break
    print('Thank you. Have a nice day.')

# program for non-English 
def spanishver():
    while True : 
        prompt = '¿Quieres saber cómo mantener ocupado a un idiota durante horas?\n'
        response = pyip.inputYesNo(prompt,yesVal='si',noVal='no')
        if response == 'no' : 
            break
    print('Thank you. Have a nice day.')


selection = pyip.inputInt(prompt='what language you want : \n1.English\n2.Spanish\n',max=2,min=1)
if selection == 1 : 
    englishver()
else : 
    spanishver()