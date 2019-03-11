'''
 Factorial 阶乘
'''
def F(n):
    result=1
    if n==0:
        return result;
    else:
        for i in range(n, 1, -1):
            result *= i
    return result

'''
Permutation 排列，从n个中挑选m个
A(n,m)等同于P(n,m),//是整除
n是下标,m上标
'''
def P(n,m):
    result=F(n)//F(n-m) if F(n-m) != 0 else 0
    return  result

def A(n,m):
    return P(n,m)



'''
combination 组合,从n个中挑m个
//是整除,
n是下标,m上标
'''

def C(n,m):

    result=F(n)//(F(m)*F(n-m)) if (F(m)*F(n-m)) != 0 else 0
    return  result