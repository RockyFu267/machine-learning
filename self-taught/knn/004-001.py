# %matplotlib inline

#导入画图工具
import matplotlib.pyplot as plt

#导入make_regression数据集生成器
from sklearn.datasets import make_regression

#生成特征数量为1，噪音为50的数据集
X , y = make_regression(n_features=1,n_informative=1,noise=50,random_state=8)

#用散点图将数据可视化
plt.scatter(X,y,c='orange',edgecolors='k')
plt.show()
