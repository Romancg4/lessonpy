#вводим год
a = int(input())
if a / 4:
    print('Обычный')
elif a % 400 == 0:
    print('Високосный')
else:
    print('Необычный')