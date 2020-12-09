import pandas as pd
import numpy as np


gender_data = pd.read_csv('../titanic/gender_submission.csv')
test_data = pd.read_csv('../titanic/test.csv')
train_data = pd.read_csv('../titanic/train.csv')


print(gender_data, test_data, train_data)

