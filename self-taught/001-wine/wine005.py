

from sklearn import datasets
from sklearn import neighbors
from sklearn.datasets import load_wine

#导入数据集拆分工具
from sklearn.model_selection import train_test_split

#导入KNN分类模型
from sklearn.neighbors import KNeighborsClassifier

#导入矩阵库
import numpy as np
#输入新的数据点
X_new = np.array([[13.2, 2.77, 2.51, 18.5, 96.6, 1.04, 2.55, 0.57, 1.47, 6.2, 1.05, 3.33, 820]])
