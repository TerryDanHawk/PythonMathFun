'''
Python 3.4.3

验证：如果完全平方数的十位数字是奇数，则他它的个位数字一定是6，反之，如果完全平方数的各位数是6，则它的十位数字一定是奇数

输出：个位数为6的完全平方数，并判断10位数是不是奇数

'''

import math
from termcolor import *

#获取1到1000000之间的完全平方数
for x in range(1,int(math.sqrt(1000000))):

    i=x*x
    iLength=len(str(i))
    if i<2:
      continue
    else:
        
        #取个位数   
        g=i%10   
        #取十位数
        s=(i/10)%10
        if g==6:
            print("\n\n[*]The number whose ones place is 6 is : %d"%i)
            if(int(s)%2!=0):               
                print(colored("\n\t[+]This number's tens place（%d） is odd!\n"%s,"green"))
            else:
                print(colored("\n\t[-]This number's tens place（%d） is even!\n"%s,"red"))
                
    
