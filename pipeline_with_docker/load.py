import pandas as pd

def load_to_dw(df: pd.DataFrame, dw_engine_connect) -> None:
    df.to_sql(name='employees', con=dw_engine_connect, if_exists='replace',schema='public', index=False)





