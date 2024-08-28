import pyinputplus as pyip

def upto10(numbers):
    numberslist = list(numbers)
    for i,digit in enumerate(numberslist):
        numberslist[i] = int(digit)
    if sum(numberslist) != 10:
        raise Exception('The digits must add up to 10 not %s'%(sum(numberslist)))
        # raise Exception(f'The digits must add up to 10 not {sum(numberslist)}') we can use this too
    return int(numbers)

response = pyip.inputCustom(upto10,prompt='Enter a number : ')
