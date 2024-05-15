import math

n = 600851475143
ans = 0

while n % 2 == 0:
    n = n/2

for i in range(3, int(math.sqrt(n)) + 1, 2):
    while n % i == 0:
        if (i > ans):
            ans = i
        n = n / i

print(ans)