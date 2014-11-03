# 6a + 9b + 20c = n



def Test (a, b, c):
    if a * 6 + b * 9 + c * 20 == n:
        print (a, b, c)
        print(n, a * 6 + b * 9 + c * 20)

def Dio (start, stop):
    ns = []
    nsn = []
    for n in range(start, stop):
        result = []
        a = 0
        while a * 6 <= n:
            b = 0
            while a * 6 + b * 9 <= n:
                c = 0
                while a * 6 + b * 9 + c * 20 <= n:
                    if a * 6 + b * 9 + c * 20 == n:
                        result.append([a, b, c])
                    c += 1
                b += 1
            a += 1
        if len (result) == 0:
            nsn.append(n)
        else:
            ns.append((n,result))
    return ns, nsn
    
        
# If 6 consecutive diophantine soloutions for n exist then solutions exist
# for all greater values of n. This is because adding multiples of six to
# the solutions produces all grater integers.

