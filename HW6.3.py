# START
x: int = int(input('enter a positive number:'))
for i in range(1, x + 1, 1):
    for i in range(1, i + 1):
        print(i, end=" ")
    print()

for i in range(x + 1, 1, -1):
    for i in range(i - 1, 0, -1):
        print(i, end=" ")
    print()
# END
