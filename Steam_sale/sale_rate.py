import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/sample_data.csv')

rate_data = pd.DataFrame(data['sale'].value_counts(normalize=True, sort=True).reset_index())
rate_data.columns = ['sale', 'average']
rate_data['average'] = pd.Series(["{0:.2f}%".format(val * 100) for val in rate_data['average']], index = rate_data.index)
rate_data['sale'] = pd.Series([val * -1 for val in rate_data['sale']], index = rate_data.index)



range_value = [0,10,20,30,40,50,60,70,80,90,100]
range_name = ['1%-10%', '11%-20%', '21%-30%', '31%-40%', '41%-50%', '51%-60%', '61%-70%', '71%-80%', '81%-90%', '91%-']
rate_categories = pd.cut(rate_data['sale'], list(map(float, range_value)), labels = range_name)
print(rate_data)



x = np.arange(67)
sale_value = rate_data['sale']
values = rate_data['average']

plt.bar(x, values)
plt.xticks(x, sale_value)
plt.show()