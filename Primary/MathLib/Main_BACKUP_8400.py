'''
Library Test Entrance
'''

<<<<<<< HEAD
from Probability.library import *

=======
from Probability.Functions import *
from Calculus.Functions import  *
>>>>>>> 39dc735d0bbf90093cc381d79282ef33d403e3c9

def main():
    #求4的阶乘4!=4*3*2*1
    #print(F(4))

    #排列与组合，从4个中选取2个
    #print(str(A(4,2)) + ":" + str(C(4,2)))

    #牛顿二项式定理
    #print(ExpandBinomial(4))

    #求复利
    #print(CI(100, 0.1, 5))
    #print(CIE(100, 0.1, 5))
    #print(GetCIRate(100,165,5))

    #极坐标转换
    print(ToPolarC(3,4))
    print(ToCartesianC(5,53.13))
    print(help(ToCartesianC))




if __name__ == '__main__':
        main()