def plot_sentiment_distribution(df):
    import seaborn as sns
    import matplotlib.pyplot as plt

    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='sentiment', order=df['sentiment'].value_counts().index, hue='sentiment', palette='Set2', legend=False)
    plt.title('Overall Sentiment Distribution')
    plt.xlabel('Sentiment')
    plt.ylabel('Number of Reviews')
    plt.tight_layout()
    plt.show()
