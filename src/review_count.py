# File: ../src/chart_review_count.py

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_review_count_per_bank(df):
    """
    Plot the number of reviews for each fintech bank.
    """
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x='bank', hue='bank', order=df['bank'].value_counts().index, palette='pastel', legend=False)
    plt.title('Number of Reviews per Fintech Bank')
    plt.xlabel('Bank')
    plt.ylabel('Number of Reviews')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.show()
