import pandas as pd

df = pd.DataFrame({
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    })

print(df.head(1))