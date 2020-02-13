import  math
from math import e

'''
Compound interest 复利计算函数
其中p为本金，r为利率，t为期数（年/月/日等）
'''
def CI(p,r,t):
    result=p*math.pow(1+r,t)
    return result

'''
Compound intrest based on e 基于e的复利计算函数
其中p为本金，r为利率，t为期数（年/月/日等)
'''
def CIE(p,r,t):
    result=p*pow(e,r*t)
    return result

'''
Compound intrest rate based on e  基于e的复利获取利率的函数
其中p为本息，f为还本利息总额，t为期数(年/月/日等)
'''
def GetCIRate(p,f,t):
    result=math.log((f/p),e)/t
    return  result