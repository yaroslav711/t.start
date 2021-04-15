gl = ['a', 'e', 'i', 'o', 'u', 'y']
st = input()
st1, st2 = st[0::2], st[1::2]
print(st1, st2)
flag = 1
if st1[0] in gl:    
    for i in st1:
        if i in gl: continue
        else: flag = 0
    for i in st2:
        if i in gl: flag = 0   
elif st2[0] in gl:    
    for i in st2:
        if i in gl: continue
        else: flag = 0
    for i in st1:
        if i in gl: flag = 0  
else: flag = 0 

print('NO' if flag == 0 else 'YES')
 
    