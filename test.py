# maps in python (dictionaries)
# birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
# while(True):
#     print('Enter a name (or leave blanc for exit )')
#     name = input()
#     if name == '':
#         break
#     if name in birthdays :
#         print(birthdays[name] + ' is the birthday of ' + name)
#     else:
#         print('I do not have birthday information for ' + name)
#         print('What is their birthday?')
#         bday = input()
#         birthdays[name] = bday
#         print('Birthday database updated.')
#
#ki njo nakhadmo bl key and value pair in the same time we use .items as in the example below :
# for t,v in birthdays.items():
#     print (t +' : '+v)

# get mehtod in maps 

# picnicItems = {'apples': 5, 'cups': 2}
# print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
# print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# set defult method
# message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
# count = {}
# for char in message:
#     count.setdefault(char,0)
#     count[char] = count[char] +1 
# print(count)

# spam = {'bat' : 100}
# print(spam['bat'])

#short cut for this code 
# if 'color' not in spam:
#     spam['color']='black'

#is to use the setdeafult function that ensure if a key-value doesn't exist in the map it will create it 
# spam.setdefault('color','black')
# print(r'there is a man who can\'t swim and have no bitchs')

# import re 
# urlRegex = re.compile(r'https?://[a-zA-Z0-9.-]+')
# text = 'Hello! Here are some links you might find useful:Check out the latest tech news at https://www.techcrunch.com .For programming tutorials, visit http://learnprogramming.net .Don\'t forget to stop by our blog: https://blog.example-site.or/articles/2024/08/15/welcome .Our company website: http://www.corporate-site.com .You can find documentation at https://docs.example.com/v1.0/getting-started.Join our forum: http://forum.example-community.io.Check our GitHub repo: https://github.com/example/repo .For shopping, try https://shop-online.co.uk/deals.Access our API at http://api.example.net/v2/.Visit https://subdomain.example.co.jp for more information.'

# mo = urlRegex.findall(text)
# print(mo)

import pyinputplus as pyip
# response = pyip.inputPassword(prompt='Enter your password dear lady : ')

# the min max greaterthen lessthan arguments: 

# reponse = pyip.inputNum(min=4,lessThan=11,greaterThan=5,max=9)

# blank argument : 
# by default blank are not allowed unless the blank argument is true 

# bread_type = {
#     'wheat': 1.56,
#     'white': 1.34,
#     'sourdough': 2.45
# }

# choices = ['no'] + list(bread_type.keys())
# print(choices)

from pathlib import Path 
print(str(Path('spark','stark','sparn')))
