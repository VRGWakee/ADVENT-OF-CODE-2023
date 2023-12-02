# Advent of code
# Day 1 
# Caleb Chun

file = open("AOC_Day1_InputList.txt", "r")
finalTotal = 0
for line in file:
    numbers = []
    for char in line:
        if char.isdigit() == True: 
            numbers.append(char)
    firstDigit = str(numbers[0])
    lastDigit = str(numbers[-1])
    combined = firstDigit + lastDigit
    correct = []
    correct.append(int(combined))
    print(combined)
    for i in range (0, len(correct)):
        finalTotal = finalTotal + correct[i]
        print(firstDigit)
        print(lastDigit)
        print(combined)
        print(finalTotal)
else:
    pass             




