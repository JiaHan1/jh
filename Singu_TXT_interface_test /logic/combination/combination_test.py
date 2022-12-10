from itertools import combinations


# 接口逻辑组合，入参为接口列表
def combination(interface):

    for num in range(len(interface)+1):
        print('接口组合数：',num)
        for i in combinations(interface,num):
            for func in i:
                func()
