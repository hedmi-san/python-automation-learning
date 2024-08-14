import re

phoneNUmregex = re.compile(r'\d{3}-\d{3}-\d{4}')

mo = phoneNUmregex.findall('Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.')
print('Phone numbers found : ')
print(mo)