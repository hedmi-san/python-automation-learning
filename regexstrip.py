import re

def stripre(string,x):
    if x:
        regex_pattern = f'^[{re.escape(x)}]+|[{re.escape(x)}]+$'
    else :
        regex_pattern = r'[^\s]'
    return re.sub(regex_pattern,'',string)

p = str(input('Enter your parameters :\n')) # p = ,>

print(stripre(',,,Hello World!>>>',p))


