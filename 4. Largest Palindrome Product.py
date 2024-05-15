def palindrome(num):
    for i in range(0, len(num)//2):
        if num[i] != num[len(num) - i - 1]:
            return False
        
    return True


def find_large(t1,t2):
    ans = -1
    t1copy = t1

    while (t2 > 0):
        t1 = t1copy
        while (t1 > 0):
            if (t1*t2 > ans and palindrome(str(t1*t2))):
                ans = t1*t2
            t1 = t1 - 1
        t2 = t2 - 1
        
    print(ans)

find_large(999, 999)