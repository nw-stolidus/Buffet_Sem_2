print("What symbol do you want? ")
sym = input()

print("What's the width of your box? ")
width = input()
width = int(width)

print("What's the height of your box? ")
high = input()
high = int(high)

dist = 0

for x in range(0, high):
    for x in range(dist, width):
        print(sym, end="")
    print("")


