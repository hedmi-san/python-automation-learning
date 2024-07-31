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
print(r'there is a man who can\'t swim and have no bitchs')