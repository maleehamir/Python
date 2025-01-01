number = int(input("Write any number between 1 to 5:"))
squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

if number in squares:
    print(f"Square of {number} is {squares[number]}")
else:
    print("Number out of range")