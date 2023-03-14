from tech_news.database import search_news
from datetime import datetime


# Requisito 7
def search_by_title(title):
    query = {"title": {"$regex": title, "$options": "i"}}
    result = search_news(query)
    return [(news["title"], news["url"]) for news in result]


# Requisito 8
def search_by_date(date):
    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Data inválida")
        
    query = {"timestamp": datetime.strptime(date, '%Y-%m-%d').strftime('%d/%m/%Y')}
    results = search_news(query)
    return [(result["title"], result["url"]) for result in results]


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
