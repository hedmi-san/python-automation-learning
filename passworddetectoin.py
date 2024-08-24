import re

lengthRegex = re.compile(r'.{8,}')
LowerRegex = re.compile(r'[a-z]')
upperRegex = re.compile(r'[A-Z]')
isdigitRegex = re.compile(r'\d')

def isvalidate(password):
    if( lengthRegex.search(password) != None and LowerRegex.search(password) != None and upperRegex.search(password) != None and isdigitRegex.search(password)!= None):
        return True
    return False


print(isvalidate('A1b2C3d4'))
print(isvalidate('pass123'))
print(isvalidate('PASSWORD123'))
print(isvalidate('Password'))
print(isvalidate('aA14'))