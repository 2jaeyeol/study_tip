import tensorflow as tf
import pandas as pd


url = '/Users/jaeyeol/jaeyeol/study/machine-learning/csv/lemonade.csv'

lemon = pd.read_csv(url)

sub = lemon[['판매량']]
ind = lemon[['온도']]
print(lemon.head())
print(ind.shape , sub.shape)



X = tf.keras.layers.Input(shape=[1])
Y = tf.keras.layers.Dense(1)(X)
model = tf.keras.models.Model(X,Y)
model.compile(loss='mse')

model.fit(ind, sub, epochs=10)
model.predict([[15]])
