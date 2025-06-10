import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_cleaned.csv')
df['sentiment'] = df['review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0.05 else 'Negative' if x < -0.05 else 'Neutral')
df.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_with_sentiment_new.csv', index=False)
