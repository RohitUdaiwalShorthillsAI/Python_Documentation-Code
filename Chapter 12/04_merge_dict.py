dict1 = {'a':1, 'b':2}
dict2 = {'c':3, 'd':4}

merged_dict = dict1 | dict2
print(merged_dict)

# multiple file open
with(
    open('file1.txt') as f1,
    open('file2.txt') as f2
):
    pass
