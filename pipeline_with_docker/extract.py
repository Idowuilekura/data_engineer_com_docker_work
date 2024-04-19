import pandas as pd


def extract_data(csv_url:str) -> pd.DataFrame:
    df = pd.read_csv(csv_url,sep=";")
    return df