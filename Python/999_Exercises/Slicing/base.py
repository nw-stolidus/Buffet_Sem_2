name = input(str('What is your first and last name? '))

for i in range(0,len(name)):
    spell = name[i]
    if spell == ' ':
        i = int(i)
        x = name[i,len(name)]
        y = name[0,i]
print(x)
print(y)