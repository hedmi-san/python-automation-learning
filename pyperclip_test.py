import pyperclip as pc # type: ignore

text = 'Hello world!'
pc.copy(text)

text2 = pc.paste()

print(text2)
