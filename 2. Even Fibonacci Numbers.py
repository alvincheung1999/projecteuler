t1 = 1
t2 = 2
t = 0
ans = 2

while t < 4000000:
    t = t1 + t2
    
    if (t % 2 == 0):
        ans += t
    t1 = t2
    t2 = t
    
print(ans)