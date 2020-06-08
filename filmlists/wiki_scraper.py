import requests
import urllib.request
import time
from bs4 import BeautifulSoup
# import numpy as np
# import pandas as pd
from urllib.request import urlopen

def main():
    url = 'https://en.wikipedia.org/wiki/The_Sight_%26_Sound_Greatest_Films_of_All_Time_2012'
    html = urlopen(url)
    soup = BeautifulSoup(html, 'html.parser')
    ordered_lists = soup.find_all('ol')
    for list in ordered_lists:
        print(f'list: {list}')

if __name__ == '__main__':
    main()
