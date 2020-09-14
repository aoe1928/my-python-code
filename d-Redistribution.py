# s_num = int(input())

def comb_func(n):
    if n == 1 or n == 2:
        return {}
    elif 3 <= n <= 5:
        return {(n,)}
    else:
        new_set = set()
        for c in comb_func(n-1):
            # print(c)
            for m, i in enumerate(c):
                lis = list(c)
                # print(m, i)
                p = len(lis)
                # lis = [j+1 if j == c[m] else j for j in c]
                a = lis
                for q in range(p):
                    if q == m:
                        a[q]+=1
                lis = a
                lis = tuple(lis)
                new_set.add(lis)
