import  math
from math import e


def CI(p,r,t):
    '''
    Compound interest 复利计算函数
    其中p为本金，r为利率，t为期数（年/月/日等）
    '''
    result=p*math.pow(1+r,t)
    return result


def CIE(p,r,t):
    '''
    Compound intrest based on e 基于e的复利计算函数
    其中p为本金，r为利率，t为期数（年/月/日等)
    '''
    result=p*pow(e,r*t)
    return result


def GetCIRate(p,f,t):
    '''
    Compound intrest rate based on e  基于e的复利获取利率的函数
    其中p为本息，f为还本利息总额，t为期数(年/月/日等)
    '''
    result=math.log((f/p),e)/t
    return  result


def ToCartesianC(r,o):
    '''
    polar coordinates to cartesian coordinates  极坐标转换为笛卡尔（直角）坐标
    其中r为半径，o为角度
    '''
    x=r*math.cos(math.radians(o))
    y=r*math.sin(math.radians(o))
    return (x,y)


def ToPolarC(x,y):
    '''
    cartesian coordinates to polar coordinates  笛卡尔（直角）坐标转换为极坐标
    其中x为横坐标，y为纵坐标
    '''
    r=math.sqrt(math.pow(x,2)+math.pow(y,2))
    o=math.degrees(math.atan(y/x))
    return  (r,o)