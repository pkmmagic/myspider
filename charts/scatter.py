import numpy as np
import matplotlib.pyplot as plt

# 数据个数
n = 18
# 均值为0, 方差为1的随机数
x = np.arange(0,1,step = 1/n)
y = np.random.normal((1-x), 0.1, n)

# 计算颜色值

# 绘制散点图
plt.scatter(x, y, s = 75, alpha = 0.5)
# 设置坐标轴范围
plt.xlim((0, 1))
plt.ylim((-0.1, 1.5))

plt.xlabel('Time')
plt.ylabel('Weight')

# 不显示坐标轴的值
plt.xticks(())
plt.yticks(())

plt.show()

