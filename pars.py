import requests
from bs4 import BeautifulSoup
#import pandas as pd


def pars():
  url = "https://trends.rbc.ru/trends/green/641402fe9a7947520b87e078"
  response = requests.get(url)
  bs = BeautifulSoup(response.text,"lxml")
  temp = bs.find_all('div', "article__text__main")
  #print(temp)
  #print()
  dict_news = {"title": [], "text": [] }


  for i in temp:
    title_element = i.find('h2', id='what')
    if title_element is not None:
      dict_news["title"].append(title_element.get_text())  # Добавляем заголовок

      paragraphs = i.find_all('p')[2:5]  # Берём нужные абзацы
      text_elements = [paragraph.get_text().strip() for paragraph in paragraphs]  # Извлекаем текст каждого абзаца
      full_text = '\n'.join(text_elements)  # Объединяем абзацы в единую строку
      dict_news["text"].append(full_text)  # Добавляем полный текст статьи
  #df_news = pd.DataFrame(dict_news, columns=["news", "links", "date", "views"])
  #df_news
  a = dict_news["title"][0]
  print(a)
  return( dict_news["title"][0],dict_news["text"][0])

pars()

