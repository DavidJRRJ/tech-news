import requests
import time
from parsel import Selector
import re
from tech_news.database import create_news
from itertools import islice


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
    sel = Selector(text=html_content)
    return sel.xpath(r'//a[@class="next page-numbers"]//@href').get()


# Requisito 4
def scrape_news(html_content):
    sel = Selector(text=html_content)

    url = sel.css('link[rel="canonical"]::attr(href)').get()
    title = sel.css('h1.entry-title::text').get().replace("\xa0", "")
    reading_time = sel.css('li.meta-reading-time::text').get()
    timestamp = sel.css('li.meta-date::text').get()
    writer = sel.xpath('//span[@class="author"]/a/text()').get()
    summary = sel.xpath('//div[@class="entry-content"]/p[1]//text()').getall()
    category = sel.css('span.label::text').get()
    
    reading_time = re.findall('\d+', reading_time)[0]
    summary = "".join(summary).rstrip("\xa0 ")

    return {
        "url": url,
        "title": title,
        "timestamp": timestamp,
        "writer": writer,
        "reading_time": int(reading_time),
        "summary": summary,
        "category": category,
    }    


# Requisito 5
def get_tech_news(amount):
    url = "https://blog.betrybe.com/"
    news_list = []

    while url:
        html_content = fetch(url)
        links = scrape_updates(html_content)
        for news_link in islice(links, amount - len(news_list)):
            html_news = fetch(news_link)
            news_info = scrape_news(html_news)
            news_list.append(news_info)
            if len(news_list) == amount:
                break
        if len(news_list) == amount:
            break
        url = scrape_next_page_link(html_content)

    create_news(news_list)
    return news_list
