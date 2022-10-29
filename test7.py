# importing libr
from bs4 import BeautifulSoup
import requests, openpyxl
import pandas as pd
from openpyxl import Workbook

columns = [0, 1, 2, 3, 4]
wb= Workbook()
ws=wb.active

# enter city name
city = "bhopal"
 
# creating url and requests instance
url = "https://www.google.com/search?q="+"weather"+city
html = requests.get(url).content
 
# getting raw data
soup = BeautifulSoup(html, 'html.parser')
temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
 
# formatting data
data = str.split('\n')
time = data[0]
sky = data[1]
 
# getting all div tag
listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
strd = listdiv[5].text
 
# getting other required data
pos = strd.find('Wind')
other_data = strd[pos:]
 
# printing all data
data = {(1: city), (2: temp), (3: time), (4: sky), (5: other_data}
ws.append(data)
df = pd.DataFrame(data, columns=['columns'])


with pd.ExcelWriter('Todays_weather.xlsx', mode='a', if_sheet_exists='replace', engine='openpyxl') as writer:
    df.to_excel(writer, sheet_name=['sheet1'])
    writer.save()

print("location is", city)
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
