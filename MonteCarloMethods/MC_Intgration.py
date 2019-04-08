import numpy as np
import matplotlib.pyplot as plt
for num in list([5, 10, 20, 30, 40, 50, 60, 70, 80, 100]):
    print('抽样点为 %i 时：' %(num))
    temp = []
    for i in range(100):
        sum = 0  
        for i in range(num):
            x = np.random.uniform()  # 随机生成一个值为0～1的数即记为x坐标
            y = np.random.uniform()  # 随机生成一个值为0～1的数即记为y坐标
            if x ** 3 > y:  # 若坐标（x，y）在图像下方,则进行计数
                sum += 1
        area_rate = sum / len(range(num + 1))  
        temp.append(area_rate)
        #print(area_rate)
    print("均值: %f" %(np.average(temp)))
    print("方差: %f" %(np.var(temp)))


# 绘图 #

for num in list([5, 10, 20, 30, 40, 50, 60, 70, 80, 100]):
    m = n = np.arange(-4, 4, 0.01)
    m, n = np.meshgrid(m, n)    
    plt.rcParams['figure.figsize'] = (4.0, 4.0)
    plt.contour(m, n, m ** 3 - n, [0])   
    plt.xlim(0, 1)
    plt.ylim(0, 1)    
    col_X = []
    col_y = []    
    for i in range(num):
        x = np.random.uniform()  # 随机生成一个值为0～1的数即记为x坐标
        y = np.random.uniform()  # 随机生成一个值为0～1的数即记为y坐标
        if x ** 3 > y:
            plt.scatter(x,y,marker='o',c='r')
        else:
            plt.scatter(x,y,marker='x',c='g')
    plt.title('when create %i random point' %num) 
    plt.show()