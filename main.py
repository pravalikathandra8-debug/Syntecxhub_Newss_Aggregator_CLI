from news_fetcher import get_news
from database import create_database, save_news
from exporter import export_csv, export_excel
keyword = input("Enter keyword: ")
create_database()
articles = get_news(keyword)
save_news(articles)
export_csv()
export_excel()
print("Project completed successfully!")