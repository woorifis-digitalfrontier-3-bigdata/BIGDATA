import csv
import pandas as pd
from sqlalchemy import create_engine, types
import mysql.connector as msql

def insert_data2():
    conn = msql.connect(host='52.36.29.255', database='pets', user='bigdata',
    password='1111')

    df=pd.read_csv("/home/ubuntu/airflow/store_files/clean_store_transactions.csv",
                sep=',')

    cursor = conn.cursor()

    for i,row in df.iterrows():
        sql = "INSERT INTO pets.clean_store_transactions VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, tuple(row))

    conn.commit()