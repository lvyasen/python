import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
fig = plt.figure(num=2)
#设置图形标题

fig.suptitle('test')
#设置几个子图
# fig, ax_lst = plt.subplots(2,3)

a = pd.DataFrame(np.random.rand(4,5),columns=list('abcd'))
a_asarray = a.values
#转换成矩阵matrix
b = np.array([1,2],[3,4])
b_asarray = np.asarray(b)

plt.show()