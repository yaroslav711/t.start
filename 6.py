n, m = input().split()
n, m = int(n), int(m)
a = list(map(int, input().split()))[:m]
f = [0]*m
time = 0

while n > 0:
    time += 1
    for i in range(len(a)):
        if time % (a[i] + f[i]) == 0:
            n -= 1
            if f[i] == 0: a[i] *= 2
            f[i] = time

print(time)