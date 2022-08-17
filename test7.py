# importing library
import requests, openpyxl
from bs4 import BeautifulSoup
 
 
excel = openpyxl.Workbook()
sheet = excel.active
sheet.title = "Today's weather"
print(excel.sheetnames)
sheet.append(['City', 'Temperature', 'Time', 'Sky', 'Other'])
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
sheet.append([city, temp, time, sky, other_data])
excel.save('Todays_weather.xlsx')
print("location is", city)
print("Temperature is", temp)
print("Time: ", time)
print("Sky Description: ", sky)
print(other_data)
