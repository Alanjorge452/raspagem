# raspagem-adoro_cinema
Web Scraping / Adoro cinema em > The last of Us 


Com essas excelentes bibliotecas, tenho a disponibilidade de acessar muitas informações, conforme a execução e processo do Objeto em questão.

import requests

from bs4 import BeautifulSoup

cabecalho = {'user-agent': 'Mozilla/5.0'}
response = requests.get('https://www.adorocinema.com/series-tv/melhores/decada-2020/ano-2023/',
                          headers = cabecalho)