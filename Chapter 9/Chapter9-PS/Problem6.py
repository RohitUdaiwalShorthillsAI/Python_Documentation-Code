line = 1
with open("Chapter 9/log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if "python" in line:
        print(f"Yes, Python is present. Line No : {lineno}")
        break
    lineno +=1
    
else:
    print("No, Python is not present")