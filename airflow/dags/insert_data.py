import csv
import pandas as pd
from sqlalchemy import create_engine, types

def insert_data():
    engine = create_engine('mysql+pymysql://user:pw@ip/db')

    df=pd.read_csv("/home/ubuntu/airflow/store_files/clean_store_transactions.csv",
                sep=',')


    df.to_sql('clean_store_transactions',con=engine,index=False,if_exists='append')