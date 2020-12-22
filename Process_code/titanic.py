import pandas as pd
import numpy as np

from matplotlib import pyplot as plt


import seaborn as sns

'''
seaborn : 예제 데이터 셋을 가져오는 모듈
여러개의 예제 데이터 셋이 있음
'''

train_data = pd.read_csv('../titanic/train.csv')
del_nan = train_data['Age'].dropna(axis=0)


bins = [0, 10, 20, 30, 40, 50, 60 ,70 ,80, 90]
labels = ['10', '20', '30', '40', '50', '60', '70', '80', '90']

age_categories = pd.cut(del_nan, bins, labels=labels)

print(age_categories.conut())