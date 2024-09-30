n, m = [int(i) for i in input().split()]

num = 1
while True:
    print(num, end='')
    num = 1 + (num + m - 2) % n
    if num == 1:
        break
