import numpy as np
import matplotlib.pyplot as plt
for num in list([50, 100, 200, 300, 500, 1000, 5000]):
    print('抽样点为 %i 时：' %(num))
    temp = []
    for i in range(100):  #重复过程100次
        a, b = (0, 0)
        r = 1
        sum = 0  # 计数清零
        for i in range(num):
            x = np.random.uniform()  # 随机生成均匀分布的一个值为0～1的数即记为x坐标
            y = np.random.uniform()  # 随机生成均匀分布的一个值为0～1的数即记为y坐标
            d = np.sqrt((x - a) ** 2 + (y - b) ** 2)  #随机点到原点的距离
            if d < r:  # 若坐标（x，y）落入粉红区域,则进行计数
                sum += 1
        # 红色区域所占正方形的概率为落入红色区域的点数除以总生成的随机数n
        area_rate = sum / len(range(num + 1))  
        temp.append(area_rate*4)  #将
    print("均值: %f" %(np.average(temp)))
    print("方差: %f" %(np.var(temp)))

# 绘图 #
# 为直观表示，落入圆内的点用‘.’表示，在圆外的点用‘x’表示
for num in list([50, 100, 200, 300, 500, 1000, 5000]):
    #画布设置，画出四分之一圆弧
    m = n = np.arange(-4, 4, 0.01)
    m, n = np.meshgrid(m, n)
    plt.contour(m, n, m ** 2 + n ** 2, [1])
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.rcParams['figure.figsize'] = (4.0, 4.0)
    col_X = []
    col_y = []
    a, b = (0, 0)
    r = 1
    for i in range(num):
        x = np.random.uniform()  # 随机生成一个值为0～1的数即记为x坐标
        y = np.random.uniform()  # 随机生成一个值为0～1的数即记为y坐标
        col_X.append(x)  # 收集生成的x，留着作图用
        col_y.append(y)  # 收集生成的y，留着作图用
        d = np.sqrt((x - a) ** 2 + (y - b) ** 2)
        if d < r:  
            plt.scatter(x,y,marker='o',c='r')
        else:
            plt.scatter(x,y,marker='x',c='g')
    plt.title('when create %i random point' %num)
    plt.show()

