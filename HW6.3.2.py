#START
n = int(input("enter a positive number:"))
rows = (n + 1) // 2
for i in range(rows):
    print(' ' * (rows - i - 1), end='')
    print('*' * (2 * i + 1))
#END