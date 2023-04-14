import polars as pl
from itertools import compress

df = pl.DataFrame(
    {
        "foo": [[1, 3, 5], [2, 6, 7], [3, 8, 10]],
        "bar": [6, 7, 8],
        "ham": ["a", "b", "c"],
    })

rows = df["foo"].apply(lambda x: x == 3).apply(lambda x: any(x))
print(rows)  # Series: 'foo' [bool] [true false true]
indices = list(compress(range(len(rows)), rows))
print(indices)  # [0, 2]

