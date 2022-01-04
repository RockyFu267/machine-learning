

from sklearn import datasets
from sklearn import neighbors
from sklearn.datasets import load_wine

#导入数据集拆分工具
from sklearn.model_selection import train_test_split

#导入KNN分类模型
from sklearn.neighbors import KNeighborsClassifier

#指定模型n_neighbors的参数值为1
knn = KNeighborsClassifier(n_neighbors=1)

#从skearn的datasets模块中载入数据集
wine_dataset = load_wine()

#将数据集拆分为训练数据集和测试数据集
X_train,X_test,y_train,y_test = train_test_split(wine_dataset['data'],wine_dataset['target'],random_state=0)

print('\n\n\n')
print("========================================")
print("红酒数据集中的键: \n{}".format(wine_dataset.keys()))
print("========================================")
print("红酒数据集中的键: \n{}".format(wine_dataset['data'].shape))
# print("========================================")
# print("答应简短描述: \n{}".format(wine_dataset['DESCR']))
print("========================================")
print("X_tarin shape: \n{}".format(X_train.shape))
print("y_tarin shape: \n{}".format(y_train.shape))
print("X_test shape: \n{}".format(X_test.shape))
print("y_test shape: \n{}".format(y_test.shape))
print("========================================")
print("对数据进行拟合")
knn.fit(X_train,y_train)
#不打印默认参数
print(knn)
print("========================================")
