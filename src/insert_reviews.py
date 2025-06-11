import pandas as pd
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, Date, Float, text
import os

os.environ["TNS_ADMIN"] = r"C:\app\zeyed\product\21c\homes\OraDB21Home1\network\admin"

try:
    df = pd.read_csv('../data/bank_reviews_with_sentiment_and_themes.csv')

    username = 'SYSTEM'
    password = 'temp123'
    dsn = 'XE'

    engine = create_engine(f'oracle+oracledb://{username}:{password}@{dsn}')
    metadata = MetaData()

    # Define tables manually (adjust columns as per your actual schema)
    banks_table = Table(
        'BANKS', metadata,
        Column('ID', Integer, primary_key=True),
        Column('NAME', String(255)),
        schema='SYSTEM'
    )
    reviews_table = Table(
        'REVIEWS', metadata,
        Column('ID', Integer, primary_key=True),
        Column('BANK_ID', Integer),
        Column('REVIEW_TEXT', Text),
        Column('SENTIMENT', String(50)),
        Column('THEMES', String(255)),
        Column('RATING', Float),
        Column('REVIEW_DATE', Date),
        schema='SYSTEM'
    )

    with engine.begin() as conn:
        existing_banks = conn.execute(banks_table.select()).fetchall()
        existing_bank_names = [row[1] for row in existing_banks]

        new_banks = [bank for bank in df['bank'].unique() if bank not in existing_bank_names]

        if new_banks:
            for bank in new_banks:
                bank_id = conn.execute(text('SELECT BANKS_SEQ.NEXTVAL FROM dual')).scalar()
                conn.execute(banks_table.insert().values(ID=bank_id, NAME=bank))
            print(f"Inserted {len(new_banks)} new banks")

        banks = conn.execute(banks_table.select()).fetchall()
        bank_ids = {row[1]: row[0] for row in banks}

        reviews_data = []
        for _, row in df.iterrows():
            reviews_data.append({
                'BANK_ID': bank_ids[row['bank']],
                'REVIEW_TEXT': row['cleaned_review'],
                'SENTIMENT': row['sentiment'],
                'THEMES': str(row['themes']),
                'RATING': row.get('rating', None),
                'REVIEW_DATE': row.get('review_date', None)
            })

        if reviews_data:
            conn.execute(reviews_table.insert(), reviews_data)
            print(f"Inserted {len(reviews_data)} reviews")

    print("✅ Data import completed successfully!")

except Exception as e:
    print("❌ Error:", e)