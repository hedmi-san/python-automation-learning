# chapter 7 project
# 
# get the text from user clipboard
# search for phone numbres and email using regex 
# paste them in the clipboard
# 

import pyperclip as pc , re

phoneRegex = re.compile(r''' 
(\d{3}|\(\d{3}\))
(\s|\.|-)?
(\d{3})
(\s|\.|-)?
(\d{4})
(\s*(ext|x|ext.)\s*(\d{2,5}))? 
''',re.VERBOSE)
emailRegex =re.compile(r'''(
[a-zA-Z0-9._%+-]+ # username
@                 # @ symbol
[a-zA-Z0-9.-]+    # domain name
(\.[a-zA-Z]{2,4}) #dot something
)''',re.VERBOSE)

text  = str(pc.paste())
matches= []
for groups in phoneRegex.findall(text) : 
    phonenum = '-'.join([groups[0],groups[2],groups[4]])
    if groups[7] != '':
        phonenum += ' x' + groups[7]
    matches.append(phonenum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])


if len(matches) > 0:
    pc.copy('\n'.join(matches))
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')