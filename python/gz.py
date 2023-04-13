import pandas as pd
from pathlib import Path


dfs = []
files = Path(".").glob('*.csv.gz')
for file in files:
    df = pd.read_csv(file, compression='gzip')
    dfs.append(df)
print(dfs)
