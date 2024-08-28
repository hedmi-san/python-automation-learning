# sandwich maker program
# data 
import pyinputplus as pyip
# Bread prices
bread_type = {
    'wheat': 1.56,
    'white': 1.34,
    'sourdough': 2.45
}

# Protein prices
protein_type = {
    'chicken': 3.25,
    'turkey': 3.75,
    'ham': 2.95,
    'tofu': 2.50
}

# Cheese prices
cheese_type = {
    'cheddar': 1.89,
    'Swiss': 2.10,
    'mozzarella': 1.75
}

# Extra prices
extra_type = {
    'mayo': 0.50,
    'mustard': 0.40,
    'lettuce': 0.60,
    'tomato': 0.70
}
# asking the number of sandwich the customer wants then we start to custamize each sandwich at a time 
listofingriediants = 4
price = 0.0
numberofsandwich = pyip.inputInt(prompt='How many sandwich do you want :\n',min=1)

for element in range(numberofsandwich):
    prompt = 'What bread you want :\n'
    response = pyip.inputStr(prompt,allowRegexes=['wheat|white|sourdough'],blockRegexes=[('.*','incorrect!')])
    price += bread_type[response]
    prompt = 'What protein you want :\n'
    response = pyip.inputStr(prompt,allowRegexes=['chicken|turkey|ham|tofu'],blockRegexes=[('.*','incorrect!')])
    price += protein_type[response]
    prompt = 'Do you want Cheese ?\n'
    response = pyip.inputYesNo(prompt)
    if response == 'yes' : 
        prompt = 'What cheese you want'
        response = pyip.inputStr(prompt,allowRegexes=['mozzarella|Swiss|cheddar'],blockRegexes=[('.*','incorrect!')])
        price += protein_type[response]
    prompt = 'Do you want mayo, mustard, lettuce, or tomato?\n'
    response = pyip.inputChoice(prompt,choices=['no']+list(extra_type))
    if response != 'no':
        price += extra_type[response]
    
