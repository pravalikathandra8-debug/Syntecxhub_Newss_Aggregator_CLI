import sqlite3
def create_database():
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS news(
        title TEXT UNIQUE,
        source TEXT,
        published_at TEXT,
        url TEXT
    )
    """)
    conn.commit()
    conn.close()
def save_news(articles):
    conn = sqlite3.connect("news.db")
    cursor = conn.cursor()
    for article in articles:
        try:
            cursor.execute("""
            INSERT INTO news
            VALUES(?,?,?,?)
            """,
            (
                article["title"],
                article["source"]["name"],
                article["publishedAt"],
                article["url"]
            ))
        except:
            pass
    conn.commit()
    conn.close()