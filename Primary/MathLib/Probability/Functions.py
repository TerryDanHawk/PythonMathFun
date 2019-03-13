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


'''
用牛顿定理展开二项式
(x+y)^n
其中n为幂
'''
def  ExpandBinomial(n):
    result=""
    for k in range(0,n+1,1):
        item=""
        a1=C(n,k)
        a2=n-k
        a3=k
        if a1!=1:
            item += str(a1)

        if a2==0:
            item += ""
        elif a2==1:
            item += "x"
        else:
            item += "x^" + str(a2)+" "

        if a3==0:
            item += ""
        elif a3==1:
            item += "y"
        else:
            item += "y^" + str(a3)+" "


        if item=="":
            item="1"
        result+=item+"+"
    if len(result) > 0:
        result = result[0:len(result) - 1]

    return  result