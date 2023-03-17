import pandas as pd
url = 'https://github.com/polaryang/streamlit-example/blob/master/import_data.csv'
df = pd.read_csv(url, index_col=0)
print(df.head(5))
