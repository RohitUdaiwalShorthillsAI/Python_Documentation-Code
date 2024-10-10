# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} X {i} = {n*i}\n"
#     with open(f"Chapter 9/tables/table_{n}.txt", "w") as f:
#         f.write(table)

# for i in range(2,21):
#     generateTable(i)

with open("Python_Documentation-Code/Chapter 9/tables/table_3.txt") as f:
    print(f.read())
    