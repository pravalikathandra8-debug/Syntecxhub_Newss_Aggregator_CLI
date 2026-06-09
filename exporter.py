import sqlite3
import pandas as pd
def export_csv():
    conn = sqlite3.connect("news.db")
    df = pd.read_sql_query(
        "SELECT * FROM news",
        conn
    )
    df.to_csv("news.csv", index=False)
    print("CSV file created!")
def export_excel():
    conn = sqlite3.connect("news.db")
    df = pd.read_sql_query(
        "SELECT * FROM news",
        conn
    )
    df.to_excel("news.xlsx", index=False)
    print("Excel file created!")