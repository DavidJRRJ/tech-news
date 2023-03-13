import requests
import time
from parsel import Selector


# Requisito 1
def fetch(url):
    HEADERS = {"user-agent": "Fake user-agent"}
    time.sleep(1)
    try:
        r = requests.get(url, timeout=3, headers=HEADERS)
    except requests.exceptions.Timeout:
        return None
    if r.status_code == 200:
        return r.text
    else:
        return None
    

# Requisito 2
def scrape_updates(html_content):
    sel = Selector(text=html_content)
    return sel.xpath(r'//h2[re:test(@class, "entry-title")]//@href').getall()


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_news(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
