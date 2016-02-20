# coding: utf-8
# 绘制线性结构

import numpy as np
import matplotlib.pyplot as plt

# 曲线数据加入噪声
x = np.linspace(-5, 5, 200)
y = np.sin(x)
yn = y + np.random.rand(1, len(y))*1.5  # 加入噪声的点集

# 绘图
fig = plt.figure()
ax = fig.add_subplot(111)
ax.scatter(x, yn, c='blue', marker='o')
ax.plot(x, y+0.75, 'r')
plt.show()