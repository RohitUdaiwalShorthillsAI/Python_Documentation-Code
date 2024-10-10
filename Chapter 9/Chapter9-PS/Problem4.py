words = ["Donkey", "Ganda", "bad"]

with open("Chapter 9/files.txt", "r") as f:
    content = f.read()

for word in words:
    content= content.replace(word, "#"*len(word))
with open("Chapter 9/files.txt", "w") as f:
    f.write(content)