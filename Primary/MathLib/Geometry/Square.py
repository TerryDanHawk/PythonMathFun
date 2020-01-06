#此模块用于计算面积（特指二维图像的面积)
import math
#三角形的面积
def GetTriangleS(a,h):
    return (a*h)/2
#正方形的面积
def GetSquareS(a):
    return a*a
#长方形的面积
def GetRectangleS(a,b):
    return a*b
#梯形的面积
def GetTrapezoidS(a,b,h):
    return ((a+b)*h)/2
#圆形的面积
def GetCircularS(r):
    return math.pi*r*r
#扇形的面积,其中n为角度，r为半径
def GetSectorS(n,r):
    return (n*math.pi*r*r)/360
#菱形的面积，其中a，b为其对角线的长
def GetDiamondS(a,b):
    return a*b


if __name__=="__main__":
    result=GetSectorS(60,1)
    print(result)