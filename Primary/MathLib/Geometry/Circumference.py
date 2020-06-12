#此模块用于计算基本几何图形的周长
import math
#三角形的周长
def GetTriangleC(a,b,c):
    return a+b+c
#正方形的周长
def GetSquareC(a):
    return 4*a
#长方形的周长
def GetRectangleC(a,b):
    return (a+b)*2    
#梯形的周长
def GetTrapezoidC(a,b,c,d):
    return a+b+c+d
#圆形的周长
def GetCircularC(r):
    return 2*math.pi*r
#扇形的周长,其中，n为扇形的角度，r为半径
def GetSectorC(n,r):    
    return 2*r+(n/180)*math.pi*r
#菱形的周长，其中a为边长
def GetDiamondC(a):
    return 4*a
    

if __name__=='__main__':
   result=GetSectorC(30,1)
   print(result)

