import pandas as pd

def transform_func(df: pd.DataFrame) -> pd.DataFrame:

    # # df.to_csv("data.csv", index=False)
    # print(df.info())

    df.columns = [col.lower() for col in df.columns]

    return df 
