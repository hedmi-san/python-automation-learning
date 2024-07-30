#the dictionary of chess moves contsin key and value 
#first the key is construct from number-character (number 1-8, character a-h) the key must be construct from these 
#so i have to check for these 
# i make two simple list of numbers
#  (valid numbers = [1,2,3,4,5,6,7,8]) and characters ( valid character = ['a','b','c','d','e','f','g','h'])
#split the key compare the first part to see if it exist in the list of numbers and do tge same for the list of characters 
#now we finish the part of the key now we check the values  
#every player can have up to 16 pieces,the piece name begin with either a w or b   
#pieces are mentioned 
#there is only one king and queen for each side 
#there is 8 pawns 
#the rest of the pieces we can have 2 of thems 


import re

validnumbers = ['1','2','3','4','5','6','7','8']
validcharacter = ['a','b','c','d','e','f','g','h']
validplayers = ['w','b']
max_pieces = {'pawn': 8, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1, 'king': 1}

def isValidChessBoard(chessBoard):
    piece_count = {'b': {'pawn': 0, 'knight': 0, 'bishop': 0, 'rook': 0, 'queen': 0, 'king': 0},
                    'w': {'pawn': 0, 'knight': 0, 'bishop': 0, 'rook': 0, 'queen': 0, 'king': 0}}

    for position, piece in chessBoard.items():
        x = re.split(r'(\d+)', position)[1:]
        if not (x[0] in validnumbers and x[1] in validcharacter):
            return False

        color, piece_type = piece[0], piece[1:]
        if color not in validplayers or piece_type not in max_pieces:
            return False
        
        piece_count[color][piece_type] += 1

    for color in piece_count:
        if piece_count[color]['king'] != 1:
            return False
        if piece_count[color]['knight'] != 2:
            return False
        if piece_count[color]['bishop'] != 2:
            return False
        if piece_count[color]['rook'] != 2:
            return False
        if piece_count[color]['pawn'] > 8:
            return False
        for piece_type in max_pieces:
            if piece_count[color][piece_type] > max_pieces[piece_type]:
                return False

    return True

# Test dictionaries
valid_board = {
    '1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bknight', '1e': 'brook',
    '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking',
    '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook'
}

invalid_board_no_kings = {
    '1a': 'bqueen', '1b': 'bbishop', '1c': 'bknight', '1d': 'brook', '1e': 'bbishop', '1f': 'bknight', '1g': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wbishop', '8f': 'wknight', '8g': 'wrook'
}

invalid_board_too_many_pawns = {
    '1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bknight', '1e': 'brook',
    '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '3a': 'bpawn', '3b': 'bpawn',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking',
    '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook'
}

invalid_board_wrong_position = {
    '1a': 'bking', '1b': 'bking', '1c': 'bbishop', '1d': 'bknight', '1e': 'brook',
    '1f': 'bbishop', '1g': 'bknight', '1h': 'brook','3d':'bqueen',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '9z': 'wpawn',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking',
    '8f': 'wbishop', '8g': 'wknight', '8h': 'wrook'
}

invalid_board_invalid_piece = {
    '1a': 'bking', '1b': 'bqueen', '1c': 'bbishop', '1d': 'bknight', '1e': 'brook',
    '1f': 'bbishop', '1g': 'bknight', '1h': 'brook',
    '2a': 'bpawn', '2b': 'bpawn', '2c': 'bpawn', '2d': 'bpawn', '2e': 'bpawn', '2f': 'bpawn', '2g': 'bpawn', '2h': 'bpawn',
    '7a': 'wpawn', '7b': 'wpawn', '7c': 'wpawn', '7d': 'wpawn', '7e': 'wpawn', '7f': 'wpawn', '7g': 'wpawn', '7h': 'wpawn',
    '8a': 'wrook', '8b': 'wknight', '8c': 'wbishop', '8d': 'wqueen', '8e': 'wking',
    '8f': 'wbishop', '8g': 'wknight', '8h': 'wrongpiece'
}

print(isValidChessBoard(valid_board))            
print(isValidChessBoard(invalid_board_no_kings))  
print(isValidChessBoard(invalid_board_too_many_pawns)) 
print(isValidChessBoard(invalid_board_wrong_position)) 
print(isValidChessBoard(invalid_board_invalid_piece))



