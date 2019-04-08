import numpy as np
import math
# 定义函数
def f(x, y):
    t = y ** 2
    p = x ** 2
    return (t*math.exp(-t) + p**2 * math.exp(-p))/(x*math.exp(-p))

for n in list([10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500, 1000, 5000, 10000]):
    print('抽样点为 %i 时：' %(n))
    temp = []
    for i in range(1000):
        temp2 = []
        sum = 0
        for i in range(n):
            x = np.random.uniform(2, 4)
            y = np.random.uniform(-1, 1)
            temp2.append(f(x, y))     
        temp.append(np.average(temp2)*4)
        
    print("均值: %f" %(np.average(temp)))
    print("方差: %f" %(np.var(temp)))