

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#导入线性回归模型
from sklearn.linear_model import LinearRegression

#输入两个点的横坐标
X = [[1],[4],[3]]
#输入两个点的纵坐标
y = [3,5,3]

#线性拟合这两个点
lr = LinearRegression().fit(X,y)

#画图，两个点和直线
z = np.linspace(0,5,20)

#s是点的大小
plt.scatter(X,y,s=80)
#c 颜色
plt.plot(z,lr.predict(z.reshape(-1,1)),c='k')
plt.title("Straight Line")
plt.show()

print('\n\n\n')
print("========================================")
#打印直线方程
print('直线方程： y= {:.3f}'.format(lr.coef_[0]),'x','+{:.3f}'.format(lr.intercept_))
