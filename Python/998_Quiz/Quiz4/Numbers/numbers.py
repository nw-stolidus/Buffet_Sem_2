#List
mynumbers = [6,9,32,28,15,22,3,18]

#Average
avg = 0
for i in range(0, len(mynumbers)):
    avg = avg + mynumbers[i]
avg = avg/len(mynumbers)
print(avg)


#Minimum
smol = mynumbers[0]
for i in range(0,len(mynumbers)):
    if mynumbers[i] <= smol:
        smol = mynumbers[i]
print(smol)


#Maximum
lorg = mynumbers[0]
for i in range(0,len(mynumbers)):
    if mynumbers[i] >= smol:
        smol = mynumbers[i]
print(lorg)
