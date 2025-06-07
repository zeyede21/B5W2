# File: ../src/chart_bank_sentiment.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_sentiment_by_bank(df):
    """
    Plot sentiment distribution per bank using a grouped bar chart.
    """
    plt.figure(figsize=(10, 5))
    sns.countplot(data=df, x='bank', hue='sentiment', palette='Set1')
    plt.title('Sentiment Distribution by Bank')
    plt.xlabel('Bank')
    plt.ylabel('Number of Reviews')
    plt.xticks(rotation=15)
    plt.legend(title='Sentiment')
    plt.tight_layout()
    plt.show()
