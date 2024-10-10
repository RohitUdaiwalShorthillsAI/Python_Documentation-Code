import random
'''
1 for snake
-1 for water
0 for gun
'''
Rohit = 0
Computer = 0
print("\t\t\t\t\t********************** Snake, Water and Gun Game************************")
i=0
while(i<5):
    you = input("Enter you choice : ")
    youDict = {"snake" : 1, "water" : -1, "gun": 0}
    list =["snake","water","gun"]
    youStr = youDict[you]
    com = random.choice(list)
    print("Computer chooses : "+ com)
    computer = youDict[com]

    if(computer == -1 and youStr  == 1):
        Rohit +=1
        print(f"Rohit Won {i+1} Game !!")
    elif(computer == -1 and youStr  == 0):
        Computer +=1
        print(f"Computer Won {i+1} Game !!")
    elif(computer == 1 and youStr  == -1):
        Computer +=1
        print(f"Computer Won {i+1} Game !!")
    elif(computer == 1 and youStr  == 0):
        Rohit +=1
        print(f"Rohit Win {i+1} Game !!")
    elif(computer == 0 and youStr  == 1):
        Computer +=1
        print(f"Computer Won {i+1} Game !!")
    elif(computer == 0 and youStr  == -1):
        Rohit +=1
        print(f"Rohit Win {i+1} Game !!")
    else:
        print("Draw !!")
        i -= 1
    i+=1
    print(f"Rohit : {Rohit}\nComputer : {Computer}")
    if(Rohit == 3):
        print("\nCongratulations!! Rohit Wins")
        break
    if(Computer == 3):
        print("\nOops!!! Computer Wins")
        break
    print("\n")
print("\nEnd Game !!!")