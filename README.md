# Fintech App Reviews Analytics

This project analyzes customer reviews from the Google Play Store for three major Ethiopian fintech mobile banking apps:

- **Commercial Bank of Ethiopia** (`com.combanketh.mobilebanking`)
- **Bank of Abyssinia** (`com.boa.boaMobileBanking`)
- **Dashen Bank** (`com.dashen.dashensuperapp`)

## Tasks

### 1. Data Collection

- Scraped recent user reviews using the `google-play-scraper` library.
- Collected fields: review text, rating, date, source, and bank name.

### 2. Data Analysis

- Performed sentiment analysis (positive, neutral, negative).
- Extracted common themes using NLP techniques.
- Visualized insights using bar charts and heatmaps.

## Output

- Cleaned dataset: `bank_reviews_with_sentiment_and_themes.csv`
- Charts showing sentiment and thematic distribution
- Summary report (Word document)

## Usage

Import visualization functions in Jupyter Notebooks from the `src/` folder and pass the processed DataFrame to generate insights.
