import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# Series 和 DataFrame
x1 = Series([1, 2, 3, 4])
# 定义index索引
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
data = {
    'Chinese': [66, 95, 93, 90, 80],
    'English': [65, 85, 92, 88, 90],
    'Math': [30, 98, 96, 77, 90],

}
df1 = DataFrame(data)
df2 = DataFrame(data,
                index=['ZhangFei','GuanYu','ZhaoYun','HuangZhong','DianWei'],
                columns=['English', 'Math', 'Chinese']
                )
#数据导入和输出
# data = pd.read_excel(r"./test.xlsx")
# data = DataFrame(data)
# #数据导出
# data.to_csv('test.csv')
#重新定义列名
# data.rename(,inplace=True)
# print(data)
# print(df2)
