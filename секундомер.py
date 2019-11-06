import time
import sys
wait=0
z=0
hours = 0
minutes = 0
sec = 0
print("отсчёт начат")
timer = 0
while timer == 0:
    print('\b' * 10, end='')
    # print("часы:", hours," минуты:", minutes," секунды:", sec)
    print(hours, minutes, sec, end=' ')
    sys.stdout.flush()
    # print()
    sec += 1
    # minutes += 0
    # hours += 0
    if sec < 60:
        sex = sec
    elif sec >= 60:
        minutes += 1
        sec = 0
        if minutes < 60:
            minutes = minutes
        else:
            minutes = 0
            hours += 1
    time.sleep(1)
print()