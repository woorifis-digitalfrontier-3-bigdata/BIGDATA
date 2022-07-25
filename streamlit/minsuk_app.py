import mysql.connector as msql
import pandas as pd
import time  # to simulate a real time data, time loop
from streamlit_folium import st_folium
import folium
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  # 🎈 data web app development
from streamlit_autorefresh import st_autorefresh

import requests
import json

st.set_page_config(
    page_title="Real-Time Data",
    page_icon="✅",
    layout="wide",
)

st.title("Real-Time / Live Data Science Dashboard")
st_autorefresh(interval=5 * 1000, key="dataframerefresh")

# 서울 행정구역 json raw파일(githubcontent)
r = requests.get('https://raw.githubusercontent.com/southkorea/seoul-maps/master/kostat/2013/json/seoul_municipalities_geo_simple.json')
c = r.content
seoul_geo = json.loads(c)

# m = folium.Map(
#     location=[37.559819, 126.963895],
#     zoom_start=11, 
#     tiles='cartodbpositron'
# )

# folium.GeoJson(
#     seoul_geo,
#     name='지역구'
# ).add_to(m)


conn = msql.connect(host='52.36.29.255', database='pets', user='bigdata',  
    password='1111')

cursor = conn.cursor()

sql2 = "SELECT * from streamlit_day"
cursor.execute(sql2)

result2 = cursor.fetchall()

df2=pd.DataFrame(result2)
job_filter = st.selectbox("지역을 선택하세요", pd.unique(df2[0]))
df2 = df2[df2[0] == job_filter]
print(df2)

sql3 = "SELECT * from streamlit_upper"
cursor.execute(sql3)

result3 = cursor.fetchall()

df3=pd.DataFrame(result3)
print(df3[1])
col1, col2, col3 = st.columns(3)
col1.metric("강남구 영업점 수", "1명", "4개")
col2.metric("총 인구 수", "11,000명", "-1,000명")
col3.metric("종합점수", "86점", "5")

import streamlit as st
from streamlit_folium import st_folium
import folium

# # center on Liberty Bell, add marker
# m = folium.Map(location=[39.949610, -75.150282], zoom_start=16)
# folium.Marker(
#     location=[37.559819, 126.963895], 
#     popup="Liberty Bell", 
#     tooltip="Liberty Bell"
# ).add_to(m)

## 지도--------------------------------------------------
m = folium.Map(
    location=[37.559819, 126.963895],
    zoom_start=11, 
    tiles='cartodbpositron'
)

folium.GeoJson(
    seoul_geo,
    name='지역구'
).add_to(m)


folium.Marker(
  location=[37.52629974922568,127.05867359288398],
  #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
  popup='<a href="http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/" target="_blank">강남구</a>',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

folium.Marker(
  location=[37.547373974997114,126.89184663862764],
  #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
  popup='<a href="http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/" target="_blank">영등포구</a>',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

folium.Marker(
  location=[37.473856492692086,126.98367668291802],
  #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
  popup='<a href="http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/" target="_blank">관악구</a>',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

            
import pandas as pd

folium_data = [
            ['강남구', 33],
            ['강동구', 44],
            ['강북구', 43],
            ['강서구', 35],
            ['관악구', 54],
            ['광진구', 34],
            ['구로구',34],
            ['동작구', 34],
            ['마포구', 55],
            ['서대문구', 44],
            ['동대문구', 33],
            ['서초구', 34],
            ['성동구', 35],
            ['성북구', 45],
            ['송파구', 65],
            ['용산구', 44],
            ['양천구', 33],
            ['영등포구', 45],
            ['은평구', 34],
            ['종로구', 45],
            ['중구', 55],
            ['중랑구', 8],
]

folium_data = pd.DataFrame(folium_data,columns=['구','수'])


# auto-refresh
st_data = st_folium(m, width = 1300)


#---------------------------------


sql = "SELECT * from personal_company"
cursor.execute(sql)

result = cursor.fetchall()

df=pd.DataFrame(result)


st.markdown("### Detailed Data View")
st.dataframe(df)

data=[[5, 33, 11],
 [6, 22, 16],
 [4, 11, 20],
 [5, 23, 19],
 [5, 24, 18],
 [5, 17, 17],
 [6, 16, 15]]

chart_data = pd.DataFrame(
     data,
     columns=['강남구', '관악구', '영등포구'])

st.line_chart(chart_data)
