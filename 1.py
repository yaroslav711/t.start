a1, b1 = input().split()
a1, b1 = int(a1), int(b1)
a2, b2 = input().split()
a2, b2 = int(a2), int(b2)

if a1 == a2: ans = [b1, a1, a2, b2]
elif a1 == b2: ans = [b1, a1, b2, a2]
elif b1 == b2: ans = [a1, b1, b2, a2]
elif a2 == b1: ans = [a1, a2, b1, b2]
else: ans = -1

print(ans)



