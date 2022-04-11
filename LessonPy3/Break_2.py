a = 0
while a <= 100:
    a = int(input())
    if a < 10:
        continue
    elif a > 100:
        break
    print(a)
