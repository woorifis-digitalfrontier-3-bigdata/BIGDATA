import MySQLdb


def insert_data3():
    db = MySQLdb.connect (host="52.36.29.255",
        user="bigdata",
        passwd="1111",
        db="pets",
        local_infile = 1)


    sqlLoadData = """load data local infile '/home/ubuntu/airflow/store_files/clean_store_transactions.csv' into table clean_store_transactions FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n' IGNORE 1 LINES;"""


    curs = db.cursor()
    curs.execute(sqlLoadData)
    db.commit()
