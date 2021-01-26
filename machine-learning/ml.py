import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd

(mnist_x, mnist_y), _ = tf.keras.datasets.mnist.load_data()
print(mnist_x.shape,mnist_y.shape)

(cifar_x, cifar_y), _ = tf.keras.datasets.cifar10.load_data()
print(cifar_x.shape,cifar_y.shape)

plt.imshow(mnist_x[0], cmap='gray')
plt.show()


