
# %matplotlib inline
import numpy as np
import matplotlib.pyplot as plt

#令x为-5 5 之间，元素为100的等差数列
X = np.linspace(-5,5,100)

#输入直线方程
y = 0.5 * X +3
plt.plot(X,y,c='orange')

#标题设置
plt.title("Straight Line")
plt.show()
