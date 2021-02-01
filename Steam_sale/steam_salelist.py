from bs4 import BeautifulSoup as bs
from selenium import webdriver

import pandas as pd
import time

from tqdm import tqdm


driver = webdriver.Safari()
driver.get('https://store.steampowered.com/search/?specials=1')

save_value = []

last_height = driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    time.sleep(1)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        break

    last_height = new_height

html = driver.page_source
soup = bs(html, 'html.parser')

driver.quit()



discount_pct = soup.find_all('span', class_='title')
discount_final_price = soup.find_all('div', class_='search_discount')
tab_item_name = soup.find_all('div', class_='discounted')



def data_value(prog, prog_, prog__):
    temp = []
    temp_price = []
    temp_title = []


    for x in tqdm(prog):
        try:
            temp.append(int(((x.get_text()).replace('-', '')).replace('%', '')))
        except:
            continue

    for y in tqdm(prog_):
        try:
            temp_price.append(int((((y.get_text()).split('₩')[2]).replace(' ', '')).replace(',', '')))
        except:
            continue

    for z in tqdm(prog__):
        try:
            temp_title.append(z.get_text())
        except:
            continue

    return temp, temp_price, temp_title



a, b, c = data_value(discount_final_price, tab_item_name, discount_pct)
save_value = list(zip(c, a, b))



data = pd.DataFrame(save_value, columns=['title','sale','price'])
data.to_csv('./dataset/steam_sale_list.csv', index=False)

