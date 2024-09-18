# START
from mimetypes import guess_type

from loop import count

sum_tamp: int = 0
for countries in range(0, 5):
    tamp: int = int(input('what is the temperature?'))
    if tamp > 45 or -50 > tamp:
        print('Incorrect')
        tamp: int = int(input('what is the temperature?'))
    sum_tamp += tamp
else:
    avg: float = sum_tamp / 5
    print(f"the average is: {avg}")

# END
