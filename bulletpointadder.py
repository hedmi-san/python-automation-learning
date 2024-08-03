# paste text from the clipboard
# do something to it 
# copy the new text to the clipboard

import pyperclip as pc

text = pc.paste()

# Separate lines and add stars
lines = text.split('\n')
for i in range(len(lines)): # loop through all indexes in the "lines" list
    lines[i] = '* ' + lines[i]
text = '\n'.join(lines)
pc.copy(text)
