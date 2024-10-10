word = "Donkey"

with open("Chapter 9/files.txt", "r") as f:
    content = f.read()

contentNew = content.replace(word, "#####")
with open("Chapter 9/files.txt", "w") as f:
    f.write(contentNew)