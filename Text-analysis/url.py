import requests
from bs4 import BeautifulSoup

def read_text(page):
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
	r = requests.get(page, headers=headers)
	soup = BeautifulSoup(r.text, "html.parser")
	return soup.get_text()


