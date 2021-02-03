import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./dataset/steam_sale_list.csv')

# rate_data = pd.DataFrame(data['sale'].value_counts(normalize=True, sort=True).reset_index())
# data.columns = ['sale', 'average']
# rate_data['average'] = pd.Series(["{0:.2f}%".format(val * 100) for val in rate_data['average']], index = rate_data.index)
# rate_data['sale'] = pd.Series([val * -1 for val in rate_data['sale']], index = rate_data.index)



range_value = [0,10,20,30,40,50,60,70,80,90,100]
range_name = ['0%-9%', '10%-19%', '20%-29%', '30%-39%', '40%-49%', '50%-59%', '60%-69%', '70%-79%', '80%-89%', '90%-99%']
rate_categories = pd.cut(data['sale'], 10, labels = range_name)
rate_df = pd.DataFrame(data=rate_categories)
rate = rate_df['sale'].value_counts(normalize=False, sort=False)



x = np.arange(len(rate))

plt.bar(x, rate)
plt.xticks(x, range_name)

for i, v in enumerate(x):
    plt.text(v, rate[i], rate[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 9, 
             color='black',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

plt.show()
