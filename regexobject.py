import re

phoneNUmregex = re.compile(r'\d{3}-\d{3}-\d{4}')
# finding all texts that the pattern 
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