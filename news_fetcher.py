import requests
API_KEY = "c2a2f61eeaa84caead4be7d317108bb6"
def get_news(keyword):
    url = f"https://newsapi.org/v2/everything?q={keyword}&apiKey={API_KEY}"
    response = requests.get(url)
    data = response.json()
    return data["articles"]