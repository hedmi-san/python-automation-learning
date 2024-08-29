import pyinputplus as pyip

# Data
bread_type = {
    'wheat': 1.56,
    'white': 1.34,
    'sourdough': 2.45
}

protein_type = {
    'chicken': 3.25,
    'turkey': 3.75,
    'ham': 2.95,
    'tofu': 2.50
}

cheese_type = {
    'cheddar': 1.89,
    'Swiss': 2.10,
    'mozzarella': 1.75
}

extra_type = {
    'mayo': 0.50,
    'mustard': 0.40,
    'lettuce': 0.60,
    'tomato': 0.70
}

# Asking the number of sandwiches
price = 0.0
numberofsandwich = pyip.inputInt(prompt='How many sandwiches do you want:\n', min=1)

# Sandwich customization
for element in range(numberofsandwich):
    # Bread
    response = pyip.inputStr('What bread do you want:\n', allowRegexes=[r'\bwheat\b|\bwhite\b|\bsourdough\b'], blockRegexes=[('.*', 'incorrect!')])
    price += bread_type[response]

    # Protein
    response = pyip.inputStr('What protein do you want:\n', allowRegexes=[r'\bchicken\b|\bturkey\b|\bham\b|\btofu\b'], blockRegexes=[('.*', 'incorrect!')])
    price += protein_type[response]

    # Cheese
    cheese = pyip.inputYesNo('Do you want cheese?\n')
    if cheese == 'yes':
        cheese_type_choice = pyip.inputStr('What cheese do you want:\n', allowRegexes=[r'\bmozzarella\b|\bSwiss\b|\bcheddar\b'], blockRegexes=[('.*', 'incorrect!')])
        price += cheese_type[cheese_type_choice]

    # Extras
    response = pyip.inputStr('Do you want mayo, mustard, lettuce, or tomato?\n', allowRegexes=[r'\bmayo\b|\bmustard\b|\blettuce\b|\btomato\b|\bno\b'], blockRegexes=[('.*', 'incorrect!')])
    if response != 'no':
        price += extra_type[response]

# Final price
final_price = numberofsandwich * (1.5 + price)
print(f'Here is your order sir, the check is: ${final_price:.2f}')
