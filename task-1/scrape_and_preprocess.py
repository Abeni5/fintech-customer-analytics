import pandas as pd
from google_play_scraper import reviews, Sort
from datetime import datetime
import uuid

apps = {
   'Commercial Bank of Ethiopia': 'com.combanketh.mobilebanking',
    'Bank of Abyssinia': 'com.combanketh.mobilebanking',
    'Dashen Bank': 'com.dashen.dashensuperapp'
}

def scrape_reviews(app_id, app_name, count=400):
    try:
        result, _ = reviews(
            app_id,
            lang='en',
            country='et',
            sort=Sort.NEWEST,
            count=count
        )
        print(f"Scraped {len(result)} reviews for {app_name}")
        reviews_list = []
        for review in result:
            reviews_list.append({
                'review_id': review['reviewId'],
                'review': review['content'],
                'rating': review['score'],
                'date': review['at'],
                'bank': app_name,
                'source': 'Google Play'
            })
        return pd.DataFrame(reviews_list)
    except Exception as e:
        print(f"Error scraping {app_name}: {e}")
        return pd.DataFrame()

all_reviews = []
for app_name, app_id in apps.items():
    df = scrape_reviews(app_id, app_name)
    print(f"DataFrame for {app_name}: {df.shape}")
    all_reviews.append(df)

df_reviews = pd.concat(all_reviews, ignore_index=True)
print(f"Combined DataFrame shape: {df_reviews.shape}")
print(f"Columns: {df_reviews.columns.tolist()}")

if df_reviews.empty:
    print("No reviews scraped. Consider using fallback dataset.")
else:
    # Preprocessing
    df_reviews = df_reviews.drop_duplicates(subset=['review_id'])
    df_reviews['review'] = df_reviews['review'].fillna('')
    df_reviews['rating'] = df_reviews['rating'].fillna(df_reviews['rating'].median())
    df_reviews = df_reviews.dropna(subset=['date'])
    df_reviews['date'] = pd.to_datetime(df_reviews['date']).dt.strftime('%Y-%m-%d')

    # Save to CSV
    df_reviews.to_csv('data/bank_reviews_cleaned.csv', index=False)

    print(f"Total reviews: {len(df_reviews)}")
    print(f"Missing data: {df_reviews.isnull().mean().mean() * 100:.2f}%")