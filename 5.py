n = int(input())
a = list(map(int, input().split()))[:n]
k = [1]*n

for i in range(n):
    a = a[i-n:]
    rng = len(a)
    cnt = 0
    max = a[0]
    for j in range(rng):
        if a[j] > max: 
            max = a[j]
            cnt += 1
    k[i] += cnt
print(k)






