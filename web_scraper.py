from  bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')


print(soup)

table = soup.find('table', class_ = 'wikitable sortable')

world_title = table.find_all('th')

world_table_title = [title.text.strip() for title in world_title]

import pandas as pd

df = pd.DataFrame(columns=world_table_title)

col_data = table.find_all('tr')
for row in col_data[1:]:
    row_data = row.find_all('td')
    indiv_data = [data.text.strip() for data in row_data]
    print(indiv_data)
    lenght = len(df)
    df.loc[lenght] = indiv_data
df

df.to_csv(r'C:\Users\ammar\Documents\Data Analytics\LatihanDA\Data\web_scraping_output.csv', index=False)