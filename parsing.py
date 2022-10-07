import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

URL_TEMPLATE = "https://ekaterinburg.hh.ru/employer/988387"
r = requests.get(URL_TEMPLATE)
print(r.status_code)
print(r.text)