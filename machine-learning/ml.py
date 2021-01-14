import tensorflow as tf
import pandas as pd


# url = '/Users/jaeyeol/jaeyeol/study/machine-learning/csv/lemonade.csv'

# lemon = pd.read_csv(url)

# sub = lemon[['판매량']]
# ind = lemon[['온도']]
# print(lemon.head())
# print(ind.shape , sub.shape)



# X = tf.keras.layers. Input(shape=[1])
# Y = tf.keras.layers.Dense(1)(X)
# model = tf.keras.models.Model(X,Y)
# model.compile(loss='mse')

# model.fit(ind, sub, epochs=10)
# print(model.predict([[15]]))

url = '/Users/jaeyeol/jaeyeol/study/machine-learning/csv/iris.csv'
iris = pd.read_csv(url)
print(iris.head())
encoding = pd.get_dummies(iris)
ind = encoding[['꽃잎길이','꽃잎폭','꽃받침길이','꽃받침폭']]
sub = encoding[['품종_setosa','품종_versicolor','품종_virginica']]
print(ind.shape,sub.shape)

  X = tf.keras.layers.Input(shape=[4])
  Y = tf.keras.layers.Dense(3, activation = 'softmax')(X)
  model = tf.keras.m odels.Model(X,Y)
  model.compile(loss='categorical_crossentropy', metrics = 'accuracy')