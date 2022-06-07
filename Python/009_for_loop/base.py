print("How long should the line be? ")
length = input()
length = int(length)

print("Should the line be vertical or horizontal? ")
direct = input()

if direct == "vertical":
    for x in range(0, length):
        print("*")
elif direct == "horizontal":
    for x in range(0, length):
        print("*", end="")
else:
    print("Please try again and type the full word")

