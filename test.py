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

# tic tac toe game 
# theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O', 'mid-L': 'X', 'mid-M': 
# 'X', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
# def printBoard(board):
#     print(board['top-L'] + ' |' + board['top-M'] + ' |' + board['top-R'])
#     print('--+--+--')
#     print(board['mid-L'] + ' |' + board['mid-M'] + ' |' + board['mid-R'])
#     print('--+--+--')
#     print(board['low-L'] + ' |' + board['low-M'] + ' |' + board['low-R'])
# printBoard(theBoard)
