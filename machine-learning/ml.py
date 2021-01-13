import tensorflow as tf
import pandas as pd


url = '/Users/jaeyeol/jaeyeol/study/machine-learning/csv/boston.csv'

bt = pd.read_csv(url)


print(bt.shape)
print(bt.columns)