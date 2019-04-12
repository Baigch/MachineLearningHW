import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
# 数据加载
def load_exdata(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f.readlines():
            line = line.split(' ')
            current = [float(item) for item in line]
            data.append(current)
    return data

# 计算误差
def computeCost(X, y, theta):
    m = y.shape[0]
    J = (np.sum((X.dot(theta) - y)**2)) / (2*m)
    return J

#  theat 优化方向
def dj_sgd(theat, X, y):
    return X.T.dot(X.dot(theat)-y)

# 梯度下降
def gradientDescent(X, y, X1, y1, theta, alpha, num_iters):
    m = y.shape[0]
    print(m)
    # 存储历史误差
    J_history = np.zeros((num_iters, 1)) # 训练集误差
    J_history1 = np.zeros((num_iters,1)) # 测试集误差
    for iter in range(num_iters):
        # 随机梯度下降
        # rand_i = np.random.randint(len(X))
        # gradient = dj_sgd(theta, np.array([X[rand_i]]), np.array([y[rand_i]]))
        # theta = theta - alpha * gradient
        gradient = dj_sgd(theta, X, y)
        theta = theta - (alpha / m) * gradient
        J_history[iter] = computeCost(X, y, theta)
        J_history1[iter] = computeCost(X1, y1, theta)
    return J_history, J_history1, theta
# 加载训练集，存储为array
data = load_exdata('dataForTraining.txt')
data = np.array(data, np.float)
x = data[:, (0, 1)].reshape((-1, 2))
y = data[:, 2].reshape((-1, 1))
m = y.shape[0]
# 加载测试集，存储为array
data1 = load_exdata('dataForTesting.txt')
data1 = np.array(data1, np.float)
x1 = data1[:, (0, 1)].reshape((-1, 2))
y1 = data1[:, 2].reshape((-1, 1))
m1 = y1.shape[0]

iterations = 1500000  # 迭代次数
alpha = 0.00015  # 学习率
alpha1 = 0.0002  

# 特征缩放到0-1
min_x = preprocessing.MinMaxScaler()
min_y = preprocessing.MinMaxScaler()
min_x1 = preprocessing.MinMaxScaler()
min_y1 = preprocessing.MinMaxScaler()
X_min = min_x.fit_transform(x)
Y_min = min_y.fit_transform(y)
X_min1 = min_x1.fit_transform(x1)
Y_min1 = min_y1.fit_transform(y1)
#x, mu, sigma = featureNormalize(x)

X = np.hstack([X_min, np.ones((X_min.shape[0], 1))])
X1 = np.hstack([X_min1, np.ones((X_min1.shape[0], 1))])
# 学习率为0.00015
theta = np.zeros((3, 1)) # 初始化theta
J_history, J_history1, theta = gradientDescent(X, Y_min, X1, Y_min1, theta, alpha, iterations)
# 学习率为0.0002
theta_1 = np.zeros((3, 1))
J_history_1, J_history1_1, theta_1 = gradientDescent(X, Y_min, X1, Y_min1, theta_1, alpha1, iterations)
# print(theta, theta_1)

# 作图
plt.plot(J_history, label="DataForTraining")
plt.plot(J_history1, '--', label="DataForTesting")
plt.legend(handles=[], labels=[], loc='center right')
plt.rcParams['figure.figsize'] = (10.0, 5.0)
plt.ylabel('lost')
plt.xlabel('iter count')
plt.title('convergence graph')
plt.show()