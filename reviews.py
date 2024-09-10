# add your code here
import pandas as pd

reviews = pd.read_csv("data/winemag-data-130k-v2.csv.zip", index_col=0)

sum_by_country = reviews.groupby('country').agg(count=('country','size'),points=('points','mean')).reset_index()

sum_by_country['points'] = sum_by_country['points'].round(1)

sum_by_country = sum_by_country.sort_values(by='count', ascending=False)

sum_by_country.to_csv("data/reviews-per-country.csv")