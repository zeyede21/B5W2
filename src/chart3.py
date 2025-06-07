def plot_sentiment_by_bank(df):
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='bank', hue='sentiment', palette='Set2')
    plt.title('Sentiment Distribution by Bank')
    plt.xlabel('Bank')
    plt.ylabel('Number of Reviews')
    plt.legend(title='Sentiment')
    plt.xticks(rotation=15)
    plt.tight_layout()
    plt.show()
