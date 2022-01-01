

from sklearn.datasets import load_wine

#从skearn的datasets模块中载入数据集
wine_dataset = load_wine()

print('\n\n\n')
print("========================================")
print("红酒数据集中的键: \n{}".format(wine_dataset.keys()))
print("========================================")
print("红酒数据集中的键: \n{}".format(wine_dataset['data'].shape))
print("========================================")
print("答应简短描述: \n{}".format(wine_dataset['DESCR']))
print("========================================")
