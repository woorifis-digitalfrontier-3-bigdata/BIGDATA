import mysql.connector as msql
import pandas as pd
import time  # to simulate a real time data, time loop
from streamlit_folium import st_folium
import folium
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  # 🎈 data web app development


import requests
import json

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



st.set_page_config(
    page_title="Real-Time Data",
    page_icon="✅",
    layout="wide",
)

st.title("Real-Time / Live Data Science Dashboard")


col1, col2, col3 = st.columns(3)
col1.metric("강남구 영업점 수", "47개", "4개")
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

m = folium.Map(
    location=[37.559819, 126.963895],
    zoom_start=11, 
    tiles='cartodbpositron'
)

folium.GeoJson(
    seoul_geo,
    name='지역구'
).add_to(m)

# call to render Folium map in Streamlit
st_data = st_folium(m, width = 1300)

conn = msql.connect(host='52.36.29.255', database='pets', user='bigdata',  
    password='1111')

cursor = conn.cursor()

sql2 = "SELECT * from streamlit_day"
cursor.execute(sql2)

result2 = cursor.fetchall()

df2=pd.DataFrame(result2)

job_filter = st.select("Select the gu", pd.unique(df2[0]))

df2 = df2[df2[0] == job_filter]
print(df2)
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

# import streamlit as st
# import plotly.figure_factory as ff
# import numpy as np


# hist_data = data[0:3]

# group_labels = ['강남구', '관악구', '영등포구']

# # Create distplot with custom bin_size
# fig = ff.create_distplot(
#          hist_data, group_labels, bin_size=[.1, .25, .5])

# # Plot!
# st.plotly_chart(fig, use_container_width=True)
