import pyperclip as pc # type: ignore

text = 'long vie!'
pc.copy(text)

text2 = pc.paste()

print(text2)
