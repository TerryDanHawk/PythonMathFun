'''
Python 3.4.3

求给定范围(n,m)内，能被a1或a2...an整除的数的个数


输入：n,m
输入：a1,a2,...an
输出:x

'''
r=input("Please input the range:\n").split(',')

n=int(r[0])

m=int(r[1])

alist=input("please input the divisors:\n").split(',')

alist=[int(i) for i in alist]

count=0

for i in range(n,m+1):
    for j in alist:
        if i%j==0:
            count+=1
            break


print("The number of dividend in range(%d,%d) is : %d"%(n,m,count))
