#******
n = int(input())
c = 1
while c <= n:
    print("*" * c)
    c += 1

n = int(input())
stars = "*"
while len(stars) <= n:
    print(stars)
    stars += "*"