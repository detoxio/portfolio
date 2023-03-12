import random

ot = 0
do = 0
score = 0

while True:
    ot = int(input("От: "))
    do = int(input("До: "))
    print('Высший разум считает ответом цифру - ', random.randint(ot, do))
    score += 1
    print(" Общее число подсчетов равно:", score)


