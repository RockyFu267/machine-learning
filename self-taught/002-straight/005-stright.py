

# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#导入线性回归模型
from sklearn.linear_model import LinearRegression

#导入make_regression数据集生成器
from sklearn.datasets import make_regression

#生成用于回归分析的数据集
X , y = make_regression(n_samples=50 ,n_features=1,n_informative=1,noise=50 ,random_state= 1)

#线性拟合这两个点
reg = LinearRegression().fit(X,y)

#z是生成等差数列，用来画图
z = np.linspace(-3,3,200).reshape(-1,1)

#s是点的大小
plt.scatter(X,y,c='b',s=60)
#c 颜色
plt.plot(z,reg.predict(z),c='k')
plt.title("Linear Regression")
plt.show()
print("========================================")
#打印直线方程
print('直线方程： y= {:.3f}'.format(reg.coef_[0]),'x','+{:.3f}'.format(reg.intercept_))
print("========================================")
#打印直线的系数和截距
print('直线的系数： {:.3f}'.format(reg.coef_[0]))
print('直线的截距： {:.3f}'.format(reg.intercept_))
