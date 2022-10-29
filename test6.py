from bs4 import BeautifulSoup
import requests, openpyxl
import pandas as pd
from openpyxl import load_workbook

FilePath = ""
ExcelWorkbook = load_workbook(FilePath)
excel = pd.ExcelWriter(FilePath, engine = 'openpyxl')

sheet = excel.active
sheet.title = 'Top Rated Movies'

sheet.append(['Movie Rank', 'Movie Name', 'Year of Release', 'IMDB Ratings'])

 
try:
    source = requests.get('https://www.imdb.com/chart/top/')
    source.raise_for_status()
    
    soup = BeautifulSoup(source.text,'html.parser')
    
    movies = soup.find('tbody', class_="lister-list").find_all('tr')
    
    for movie in movies:

        name = movie.find('td', class_="titleColumn").a.text

        rank = movie.find('td', class_="titleColumn").get_text(strip=True).split('.')[0]
        
        year = movie.find('td', class_="titleColumn").span.text.strip('( )')

        rating = movie.find('td', class_="ratingColumn imdbRating").strong.text
        
        print (rank, name, year, rating)
        sheet.append([rank, name, year, rating])
            

except Exception as e:
    print(e)

excel.save('IMDB Movie Ratings.xlsx')