# Visualization and Reporting
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\notebook\\data\\bank_reviews_with_sentiment_new.csv')
df['sentiment_label'].value_counts().plot(kind='bar')
plt.title('Sentiment Distribution')
plt.savefig('C:\\Users\\hp\\OneDrive\\Desktop\\Customer Experience Analytics for Fintech Apps\\fintech-customer-analytics\\report\\sentiment_plot.png')
plt.show()