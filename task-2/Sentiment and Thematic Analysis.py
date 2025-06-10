# Sentiment Analysis
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()
df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_cleaned.csv')
print("Loaded DataFrame shape:", df.shape)
print("Unique banks:", df['bank'].unique())
print("Sample banks (first 50):", df['bank'].head(50).tolist())
print("Sample banks (middle 50):", df['bank'].iloc[575:625].tolist())  # Approx middle
print("Sample banks (last 50):", df['bank'].tail(50).tolist())
df['sentiment'] = df['review'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
df['sentiment_label'] = df['sentiment'].apply(lambda x: 'Positive' if x > 0.05 else 'Negative' if x < -0.05 else 'Neutral')
print("Before save - Sample banks:", df['bank'].head(10).tolist())
df.to_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_with_sentiment_new.csv', index=False, mode='w')
print("Saved to new file, verifying...")
saved_df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_with_sentiment_new.csv')
print("Verified DataFrame shape:", saved_df.shape)
print("Verified Unique banks:", saved_df['bank'].unique())
print("Verified Sample banks (first 50):", saved_df['bank'].head(50).tolist())
print("Verified Sample banks (last 50):", saved_df['bank'].tail(50).tolist())
print("Sentiment Analysis Results:")
print(df['sentiment_label'].value_counts())
print("\nAverage Sentiment by Bank:")
print(df.groupby('bank')['sentiment'].mean())
# Thematic Analysis
import pandas as pd
from collections import Counter
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords

df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_with_sentiment_new.csv')
stop_words = set(stopwords.words('english'))
words = ' '.join(df['review']).lower()
words = re.findall(r'\w+', words)
words = [word for word in words if word not in stop_words]
common_themes = Counter(words).most_common(10)
print("Top 10 Themes (Common Words) Across All Banks:", common_themes)

for bank in df['bank'].unique():
    bank_words = ' '.join(df[df['bank'] == bank]['review']).lower()
    bank_words = re.findall(r'\w+', bank_words)
    bank_words = [word for word in bank_words if word not in stop_words]
    bank_themes = Counter(bank_words).most_common(5)
    print(f"\nTop 5 Themes for {bank}:", bank_themes)