import random

number = int(input())
count = 0
i = random.randint(1, 101)
if i == number:
    print("Верно! всего-то прошло", count, "попыток(-тка)!")
else:
    while i != number:
        i = random.randint(0, 101)
        count+=1
        if i == number:
            print("Угадано за", count, "попыток")
            break
