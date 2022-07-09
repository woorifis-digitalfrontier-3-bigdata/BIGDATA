## 1. 기본 flow

- streaming data(대기현황) csv - logstash - kafka - MySQL
                                                           -> Node.js(Express)+streamlit+superset
- batch data(상권정보 등)  csv - airflow(일 배치)  - MySQL 

## 2. EC2 Instacne
BD02_airflow(csv파일, 
BD02_DB(kafka, MySQL)
BD02_superset(node.js, streamlit, superset)


## 3. 링크

- SuperSet: http://34.210.157.12:8088/

- Airflow : http://35.162.149.208:8080/home

- Notion: https://www.notion.so/735b5c4e615244d999ce402e999be598

- Streamlit: https://share.streamlit.io/ (보기: https://minsuk1-bigdata-pilot-streamlitsample-xdc3pt.streamlitapp.com/)

- Database(MySQL)

  - 외부데이터를 위한 table

    <img width="168" alt="image" src="https://user-images.githubusercontent.com/64065318/177281711-4bf8ef1d-e800-4865-b0cb-16516866db58.png">
