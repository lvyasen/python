import tensorflow as  tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

# 加载数据集
fashion_mnist = keras.datasets.fashion_mnist
(train_image, train_lable), (test_image, test_lable) = fashion_mnist.load_data()

class_name = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
              'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
# 查看预处理数据
# 创建一个图形实例
# plt.figure()
# plt.imshow(train_image[1])
# plt.colorbar()
# plt.show()

# 将图片归一化
train_image, test_image = train_image / 255.0, test_image / 255.0

# 显示25张图片并伴随名称
# 定义图片大小
plt.figure(figsize=(10, 10))
# 多合一显示
# for i in range(25):
#     plt.subplot(5,5,i+1)
#     plt.xticks([])
#     plt.yticks([])
#     plt.imshow(train_image[i],cmap=plt.cm.binary)
#     plt.xlabel(class_name[train_lable[i]])
# plt.show()

#建立模型
model = keras.Sequential()
model.add(tf.keras.layers.Flatten(input_shape=(28,28)))
model.add(tf.keras.layers.Dense(128,activation='relu'))
model.add(tf.keras.layers.Dense(10,activation='softmax'))

#编译模型
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

#训练模型
model.fit(train_image,train_lable,epochs=10)

#评估模型
test_loss,test_acc = model.evaluate(test_image,test_lable,verbose=2)
# print('\nTest acc',test_acc)

#预测
predictions = model.predict(test_image)

# print(predictions[0])
lable_index = np.argmax(predictions[0])
# print(class_name[lable_index])

#图形方式查看预测结果
def plot_image(i,predictions_array,true_label,img):
    predictions_array,true_label,img = predictions_array,true_label[i],img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    plt.imshow(img,cmap=plt.cm.binary)

    predicted_lable = np.argmax(predictions_array)
    if predicted_lable == true_label:
        color = 'red'
    else:
        color = 'green'
    plt.xlabel("{} {:2.0f}% ({})".format(class_name[predicted_lable],
                                100*np.max(predictions_array),
                                class_name[true_label]),
                                color=color)

def plot_value_array(i, predictions_array, true_label):
  predictions_array, true_label = predictions_array, true_label[i]
  plt.grid(False)
  plt.xticks(range(10))
  plt.yticks([])
  thisplot = plt.bar(range(10), predictions_array, color="#777777")
  plt.ylim([0, 1])
  predicted_label = np.argmax(predictions_array)

  thisplot[predicted_label].set_color('red')
  thisplot[true_label].set_color('blue')


num_rows = 5
num_cols = 3
num_images = num_rows*num_cols
plt.figure(figsize=(2*2*num_cols, 2*num_rows))
for i in range(num_images):
  plt.subplot(num_rows, 2*num_cols, 2*i+1)
  plot_image(i, predictions[i], test_lable, test_image)
  plt.subplot(num_rows, 2*num_cols, 2*i+2)
  plot_value_array(i, predictions[i], test_lable)
plt.tight_layout()
plt.show()
