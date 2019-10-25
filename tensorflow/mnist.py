import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

# 导入mnist数据集
mnist = tf.keras.datasets.mnist

# 取出数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()
# 将图片数据归一化
x_train, x_test = x_train / 255.0, x_test / 255.0

#构建神经网络model
model = tf.keras.models.Sequential()
#将图片数据由二维数组转为一位数组
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
#添加多少隐藏单元 并设置激活函数为relu
model.add(tf.keras.layers.Dense(128,activation='relu'))
#设置偏移量
model.add(tf.keras.layers.Dropout(0.2))
#添加回归函数并设置激活函数为softmax
model.add(tf.keras.layers.Dense(10,activation='softmax'))

#编译 就是配置的过程
model.compile(
    #设置优化器为adam
    optimizer='adam',
    #设置损失loss函数
    loss='sparse_categorical_crossentropy',
    #设置指标函数为 accuracy
    metrics=['accuracy']
)

#训练数据 epochs 表示训练多少步
model.fit(x_train,y_train,epochs=5)