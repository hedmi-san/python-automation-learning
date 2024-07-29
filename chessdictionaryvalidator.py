#the dictionary of chess moves contsin key and value 
#first the key is construct from number-character (number 1-8, character a-h) the key must be construct from these 
#so i have to check for these 
# i make two simple list of numbers
#  (valid numbers = [1,2,3,4,5,6,7,8]) and characters ( valid character = ['a','b','c','d','e','f','g','h'])
#split the key compare the first part to see if it exist in the list of numbers and do tge same for the list of characters 
#now we finish the part of the key now we check the values  



import re
validnumbers = [1,2,3,4,5,6,7,8]
validcharacter = ['a','b','c','d','e','f','g','h']

def isValidChessBoard(chessBoard):
    for k,v in chessBoard.items():
        x = re.split(r'(\d+)', k)[1:]
        print(x[1])
        if (x[0] in validnumbers and x[1] in validcharacter) :
            return True
        else: 
            return False
        
    return True

chess = {'2h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(chess))


