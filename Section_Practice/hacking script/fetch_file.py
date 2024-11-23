# fetch_files.py
import requests
from bs4 import BeautifulSoup
import os

base_url = "https://web.stanford.edu/class/archive/cs/cs109/cs109.1232/psets/"
response = requests.get(base_url)
soup = BeautifulSoup(response.text, 'html.parser')

directories = [a['href'] for a in soup.find_all('a', href=True) if 'pset' in a['href']]

with open('download_files.bat', 'w') as file:
    file.write('@echo off\n')
    file.write('setlocal EnableDelayedExpansion\n\n')
    file.write(f'set base_url={base_url}\n\n')

    for directory in directories:
        dir_url = base_url + directory
        dir_response = requests.get(dir_url)
        dir_soup = BeautifulSoup(dir_response.text, 'html.parser')
        files = [a['href'] for a in dir_soup.find_all('a', href=True) if not a['href'].endswith('/')]

        for file_name in files:
            file.write(f'curl -O {dir_url}{file_name}\n')

    file.write('\nendlocal\n')
