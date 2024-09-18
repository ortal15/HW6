# SRART
import random

num: int = random.randint(1, 100)
while True:
    user: int = int(input('enter a number between 1-100:'))
    if user < num:
        print('your number is too small')
    elif user > num:
        print('your number os too big')
    elif num == user:
        print('BINGO!')
        break

# END
# לא הצלחתי לחשב את מספר הניחושים
