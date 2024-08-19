import re

# finding all texts that the pattern 
phoneNUmregex = re.compile(r'\d{3}-\d{3}-\d{4}')
mo = phoneNUmregex.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
print('Phone numbers found : ')
print(mo)


# in case we needed to get only one 
mo = phoneNUmregex.search('My number is 415-555-4242.')
print('Phone number found  : ' + mo.group())


# sepereate the result 
phoneNUmregexS = re.compile(r'(\d{3})-(\d{3}-\d{4})')
mo = phoneNUmregexS.search('Here is my phone number : 415-555-9999')
print(mo.group(1)) # return 415 the first three 
print(mo.group(2)) # return the other part
print(mo.group(0)) # same result for mo.group() return the entire matched text

# if we wanna retrieve all the groups at once we can use the  groups 
print(mo.groups())


# optional matching pattern  
batregex = re.compile(r'Bat(wo)?man')
mo = batregex.search('The adventure of Batwoman')
print(mo.group())
mo2 =batregex.search('The adventure of Batman')
print(mo2.group())


# Greedy and Non-greedy Matching 
greedyregex = re.compile(r'(Ha){3,5}')
mo = greedyregex.search('HaHaHaHaHa')
print(mo.group())

lazyregex = re.compile(r'(Ha){3,5}?')
mo = lazyregex.search('HaHaHaHaHa')
print(mo.group())


# examples
xregex = re.compile(r'\d+\s\w+')
mo = xregex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo) 


# creating shorthand class 
# vowel class 
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo = vowelRegex.findall('Mesouad eats baby food. So he\'s a BABY BOY that still drink mammy\'s milk.')
print(mo)

# the digits at the end 
digitregex =re.compile(r'\d*$')
mo  = digitregex.search('Your number is 42')
print(mo.group())

def displaymatch(match):
    if match is None:
        return None
    return '<Match: %r, groups=%r>' % (match.group(), match.groups())


valid = re.compile(r'^[akqjt2-9]{5}$')
print(displaymatch(valid.match('akt5q')))
print(displaymatch(valid.match('727ak')))
print(displaymatch(valid.match('akt')))


# case insensitive 
robocop = re.compile(r'robocop',re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())



# sub method
subregex = re.compile(r'Agent \w+')
mo = subregex.sub('Nigger','Mr Agent White gave the little Agent white a gun')
print(mo)

# backreferences in sub 
regex = re.compile(r'Agent (\w)\w*')
print(regex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.'))