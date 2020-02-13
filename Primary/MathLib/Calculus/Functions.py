import  math

'''
Compound interest 复利计算函数
其中p为本金，i为利率，n为年数
'''
def CI(p,i,n):
    result=p*math.pow(1+i,n)
    return result

