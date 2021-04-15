a, b, c, t = input().split()
a, b, c, t = int(a), int(b), int(c), int(t)
time = [0, 0, 0]
time[2] = t
while time[2] >= c:
    time[1] += 1
    time[2] -= c
while time[1] >= b:
    time[0] += 1
    time[1] -= b
while time[0] >= a:
    time[0] -= a
print(time)
    