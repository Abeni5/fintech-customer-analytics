# Database Integration
import pandas as pd
import oracledb
connection = oracledb.connect(user="local", password="123456", dsn="dsn")  # Replace with actual credentials
df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_with_sentiment_new.csv')
df.to_sql('bank_reviews', con=connection, if_exists='replace', index=False)
