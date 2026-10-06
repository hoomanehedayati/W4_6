print("Program starting.")
num = int(input("Insert a positive integer: "))
x = 0
print(num, end="")

while num > 1:
    if num % 2 == 0:
        num = num // 2
    else:
        num = (num * 3) + 1

    print(" ->", num, end="")
    x += 1
print(f"\nSequence had {x} total steps.\n")
print("Program ending.")