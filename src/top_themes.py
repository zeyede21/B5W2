def plot_top_themes(df):
    import seaborn as sns
    import matplotlib.pyplot as plt
    from collections import Counter
    import ast
    import pandas as pd

    all_themes = []
    for item in df['themes'].dropna():
        all_themes.extend(ast.literal_eval(item))

    theme_counts = Counter(all_themes)
    theme_df = pd.DataFrame(theme_counts.items(), columns=['Theme', 'Count']).sort_values(by='Count', ascending=False)

    plt.figure(figsize=(10, 6))
    sns.barplot(data=theme_df.head(top_n), x='Count', y='Theme', hue='Theme', legend=False, palette='viridis')
    plt.title(f'Top {top_n} Themes in Reviews')
    plt.xlabel('Count')
    plt.ylabel('Theme')
    plt.tight_layout()
    plt.show()
    plt.savefig('../visualizations/top_themes.png')
    plt.show()