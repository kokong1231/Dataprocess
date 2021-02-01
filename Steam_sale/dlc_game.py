import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



data = pd.read_csv('./dataset/steam_sale_list.csv')
filter_arg = ['-', 'Season Pass', 'Edition']
save = []



for x in filter_arg:
    save.append(data[data['title'].str.contains(x)])



dlc_value = pd.concat([save[0], save[1], save[2]])            # 나눈 배열 합치기
dlc_real = dlc_value.drop_duplicates('title', keep='first')     # 중복 제거

dlc_count = dlc_real.shape[0]
all_count = data.shape[0]
real_game_count = all_count - dlc_count

x = np.arange(3)

sale_value = ['ALL', 'DLC', 'GAME']
values = [all_count, dlc_count, real_game_count]

plt.bar(x, values)
plt.xticks(x, sale_value)

for i, v in enumerate(x):
    plt.text(v, values[i], values[i],                 # 좌표 (x축 = v, y축 = y[0]..y[1], 표시 = y[0]..y[1])
             fontsize = 9, 
             color='black',
             horizontalalignment='center',  # horizontalalignment (left, center, right)
             verticalalignment='bottom')    # verticalalignment (top, center, bottom)

plt.show()