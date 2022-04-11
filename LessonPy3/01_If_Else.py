a = int(input())
b = int(input())
H = int(input())
if a <= H <= b:
    print('Это нормально')
else:
    if H >= b:
        print ('Пересып')
    else:
        print('Недосып')