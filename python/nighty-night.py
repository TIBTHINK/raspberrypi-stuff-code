import decimal

def pi():
    
    decimal.getcontext().prec += 2  
    three = decimal.Decimal(3)      
    lasts, t, s, n, na, d, da = 0, three, 3, 1, 0, 0, 24
    while s != lasts:
        lasts = s
        n, na = n + na, na + 8
        d, da = d + da, da + 32
        t = (t * n) / d
        s += t
    decimal.getcontext().prec -= 2
    return +s               

decimal.getcontext().prec = 5**14
pi = pi()

print(pi)
