import time
import pandas as pd

from selenium import webdriver
from bs4 import BeautifulSoup



driver = webdriver.Safari()
driver.get('https://oscar.go.com/winners')
time.sleep(1)

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

category = soup.select(
    'bls-winners-list > ul > li > div.winners-list__info > a'
)

movie = soup.select(
    'bls-winners-list > ul > li > div.winners-list__info > h3 > a'
)

producer = soup.select(
    'bls-winners-list > ul > li > div.winners-list__info > p'
)

oscars_2020 = []

for item in zip(category, movie, producer):
    oscars_2020.append(
        {
            'category' : item[0].text,
            'movie' : item[1].text,
            'producer' : item[2].text
        }
    )

data = pd.DataFrame(oscars_2020)
print(data)
data.to_csv('./dataset/oscars_2020.csv')

driver.quit()

            