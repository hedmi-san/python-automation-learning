#english to piglatin 
print('emter the english message to translate into pig latin')
message = input()

Vowels = ('a', 'e', 'i', 'o', 'u', 'y')
piglatin =[]
for word in message.split():
    prefixNonLetters = ''
    while len(word) > 0 and not word.isalpha():
        prefixNonLetters+= word[0]
        word = word[:1]
    if len(word) == 0:
        piglatin.append(prefixNonLetters)
        continue
    suffixNonLetters = ''
    while not word[-1].isalpha():
        suffixNonLetters += word[-1]
        word = word[:-1]
    wasUpper = word.isupper()
    wasTitle = word.istitle()
    word = word.lower() 
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in Vowels:
        prefixConsonants += word[0]
        word = word[1:]
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    if wasUpper:
        word = word.upper()
    if wasTitle:
        word = word.title()
    piglatin.append(prefixNonLetters + word + suffixNonLetters)

print(' '.join(piglatin))