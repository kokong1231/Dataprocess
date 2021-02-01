import pandas as pd



data = pd.read_csv('./dataset/steam_sale_list.csv')
title_name = []
del_per = []
del_price = []
count_loop = 0



for nanobj in data['sale']:
    if pd.isna(nanobj) == True:
        print(data['title'][count_loop])
        count_loop += 1
        continue
    else:
        title_name.append(data['title'][count_loop])
        count_loop += 1

for x in data['sale']:
    try:
        del_per.append(int(x.replace('%','')))
    except:
        continue

for y in data['price']:
    try:
        a = y.replace('₩ ', '')
        del_price.append(int(a.replace(',', '')))
    except:
        continue



final_data = pd.DataFrame(list(zip(title_name, del_per, del_price)), columns=['title', 'sale', 'price'])
final_data.to_csv('./dataset/sample_data.csv', index=False)