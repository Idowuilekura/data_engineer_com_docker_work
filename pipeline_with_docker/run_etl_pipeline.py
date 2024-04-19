from sqlalchemy import create_engine
import pandas as pd
from load import load_to_dw
from transform import transform_func
from extract import extract_data
import os

postgres_user = os.getenv('POSTGRES_USER')
postgres_password = os.getenv('POSTGRES_PASSWORD')
postgres_port = str(os.getenv('POSTGRES_PORT'))
postgres_host = str(os.getenv('POSTGRES_HOST'))
postgres_dw = os.getenv('POSTGRES_DW')
csv_url = os.getenv('CSV_URL')
print(postgres_port)

dw_engine_connect = create_engine(f'postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_dw}')


def run_etl_pipeline(csv_url:str, dw_engine_connect):
    df_extract = extract_data(csv_url)
    df_transform = transform_func(df_extract)
    # load_to_dw(df_transform, con)
    # with dw_engine_connect.connect() as con:
    #     load_to_dw(df_transform, con.connection)
    print("about to load into the dw")
    load_to_dw(df_transform, dw_engine_connect)
        # run_etl_pipeline(csv_url=csv_url, dw_engine_connect=con.connection)
    print("done loading into the dw")


run_etl_pipeline(csv_url=csv_url, dw_engine_connect=dw_engine_connect)

# docker run -d --name postgres_container 
# --network my_network -e POSTGRES_USER=your_username -e POSTGRES_PASSWORD=your_password -e POSTGRES_DB=dock_db -p 5434:5432 postgres:latest