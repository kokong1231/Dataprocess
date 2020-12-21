from bs4 import BeautifulSoup as bs
from selenium import webdriver

import pandas as pd
import numpy as np
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

game_count = soup.find_all('span', class_='title')

for x in tqdm(range(len(game_count))):
    temp = []
    try:
        temp.append(soup.select_one('a:nth-child('+str(x+1)+') > div.responsive_search_name_combined > div.col.search_name.ellipsis > span').string)
        temp.append(soup.select_one('a:nth-child('+str(x+1)+') > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_discount.responsive_secondrow > span').string)
        temp.append(soup.select_one('a:nth-child('+str(x+1)+') > div.responsive_search_name_combined > div.col.search_price_discount_combined.responsive_secondrow > div.col.search_price.discounted.responsive_secondrow > span > strike').string)
    except:
        print('None_type : %d' %x)
    
    save_value.append(temp)


data = pd.DataFrame(save_value, columns=['title','sale','price'])
data.to_csv('./dataset/steam_sale_list.csv', index=False)

driver.quit()
