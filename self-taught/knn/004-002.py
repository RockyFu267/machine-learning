
# %matplotlib inline

#导入画图工具
import matplotlib.pyplot as plt

#导入make_regression数据集生成器
from sklearn.datasets import make_regression

#导入KNN分类器
from sklearn.neighbors import KNeighborsRegressor

import numpy as np

reg = KNeighborsRegressor()
#生成特征数量为1，噪音为50的数据集
X,y = make_regression(n_features=1,n_informative=1,noise=50,random_state=8)
reg.fit(X,y)

#把预测结果用图像进行可视化
z = np.linspace(-3,3,200).reshape(-1,1)
#用散点图将数据可视化
plt.scatter(X,y,c='orange',edgecolors='k')
plt.plot(z,reg.predict(z),c='k',linewidth=3)
plt.title('KNN Regression')
plt.show()
print('模型正确率：{:.2f}'.format(reg.score(X,y)))
