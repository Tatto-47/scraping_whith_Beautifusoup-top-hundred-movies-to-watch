import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

movie_tags = soup.find_all(name="h3", class_="title")
movie_title = []
for tag in movie_tags:
    movie = tag.getText()
    movie_title.append(movie)
movies_oredered_list = movie_title[:: -1]
#We could also use the reverse methode i.e : vovie_title.reverse()

with open("movies.txt", mode="w") as file:
    for movie in movies_oredered_list:
        file.write(f"{movie}\n")
