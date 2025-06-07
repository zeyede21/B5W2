# File: ../src/chart_heatmap.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict
import ast

def plot_sentiment_theme_heatmap(df):
    """
    Generate a heatmap of sentiment count by theme.
    """
    theme_sentiment = defaultdict(lambda: defaultdict(int))

    for _, row in df.iterrows():
        if pd.notna(row['themes']) and pd.notna(row['sentiment']):
            try:
                themes = ast.literal_eval(row['themes'])
                for theme in themes:
                    theme_sentiment[theme][row['sentiment']] += 1
            except Exception as e:
                print(f"Error parsing row {row['themes']}: {e}")

    heatmap_df = pd.DataFrame(theme_sentiment).fillna(0).astype(int).T

    plt.figure(figsize=(12, 8))
    sns.heatmap(heatmap_df, annot=True, fmt="d", cmap="YlGnBu", linewidths=0.5, linecolor='gray')
    plt.title('Heatmap of Sentiment by Theme')
    plt.xlabel('Sentiment')
    plt.ylabel('Theme')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
