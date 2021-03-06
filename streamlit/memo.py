import mysql.connector as msql
import pandas as pd
import time  # to simulate a real time data, time loop
from streamlit_folium import st_folium
import folium
import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  # π data web app development
from streamlit_autorefresh import st_autorefresh

import requests
import json

st.set_page_config(
    page_title="Real-Time Data",
    page_icon="β",
    layout="wide",
)

st.title("μμμ  λͺ¨λν°λ§ μμ€ν")
st_autorefresh(interval=20 * 1000, key="dataframerefresh")

# μμΈ νμ κ΅¬μ­ json rawνμΌ(githubcontent)
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
#     name='μ§μ­κ΅¬'
# ).add_to(m)


conn = msql.connect(host='52.36.29.255', database='pets', user='bigdata',  
    password='1111')

cursor = conn.cursor()

sql2 = "SELECT * from streamlit_day"
cursor.execute(sql2)

result2 = cursor.fetchall()

df2=pd.DataFrame(result2)
job_filter = st.selectbox("μ§μ­μ μ ννμΈμ", pd.unique(df2[0]))
df2 = df2[df2[0] == job_filter]
#print(df2)


sql3 = "SELECT * from streamlit_upper"
cursor.execute(sql3)

result3 = cursor.fetchall()

df3=pd.DataFrame(result3)
df3 = df3[df3[0] == job_filter]
print(df3)


col1, col2, col3 = st.columns(3)
col1.metric("κ°λ¨κ΅¬ μμμ  μ", str(df3.iat[0,1]), "4κ°")
col2.metric("μ΄ μΈκ΅¬ μ", str(df3.iat[0,2]), "-1,000λͺ")
col3.metric("μ’ν©μ μ", "86μ ", "5")

from streamlit_folium import st_folium
import folium

## μ§λ--------------------------------------------------
m = folium.Map(
    location=[37.559819, 126.963895],
    zoom_start=11, 
    tiles='cartodbpositron'
)

folium.GeoJson(
    seoul_geo,
    name='μ§μ­κ΅¬'
).add_to(m)


folium.Marker(
  location=[37.49108397,127.05536209],
  #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
  popup='<a href="http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/" target="_blank">κ°λ¨κ΅¬</a>',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

folium.Marker(
  location=[37.51527262,126.90702140],
  #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
  popup='<a href="http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/" target="_blank">μλ±ν¬κ΅¬</a>',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

folium.Marker(
  location=[37.471077623795,126.93920205178],
  #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
  popup='<a href="http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/" target="_blank">κ΄μκ΅¬</a>',
  icon=folium.Icon(color='red',icon='star')
).add_to(m)

import pandas as pd

folium_data = [
            ['κ°λ¨κ΅¬', 33],
            ['κ°λκ΅¬', 44],
            ['κ°λΆκ΅¬', 43],
            ['κ°μκ΅¬', 35],
            ['κ΄μκ΅¬', 54],
            ['κ΄μ§κ΅¬', 34],
            ['κ΅¬λ‘κ΅¬',34],
            ['λμκ΅¬', 34],
            ['λ§ν¬κ΅¬', 55],
            ['μλλ¬Έκ΅¬', 44],
            ['λλλ¬Έκ΅¬', 33],
            ['μμ΄κ΅¬', 34],
            ['μ±λκ΅¬', 35],
            ['μ±λΆκ΅¬', 45],
            ['μ‘νκ΅¬', 65],
            ['μ©μ°κ΅¬', 44],
            ['μμ²κ΅¬', 33],
            ['μλ±ν¬κ΅¬', 45],
            ['μνκ΅¬', 34],
            ['μ’λ‘κ΅¬', 45],
            ['μ€κ΅¬', 55],
            ['μ€λκ΅¬', 8],
]

folium_data = pd.DataFrame(folium_data,columns=['κ΅¬','μ'])



#μλν΄λΌμ°λ---------------
from PIL import Image
image = 'https://superset22.s3.us-west-2.amazonaws.com/%ED%99%94%EB%A9%B4+%EC%BA%A1%EC%B2%98+2022-07-25+191136.png'
image2 = 'https://superset22.s3.us-west-2.amazonaws.com/%ED%99%94%EB%A9%B4+%EC%BA%A1%EC%B2%98+2022-07-25+185153.png'

fig_col1, fig_col2 = st.columns(2)

with fig_col1:
    st.image(image, caption='μ°λ¦¬μν WordCloud',output_format="auto", width=250)
   
with fig_col2:
    st.image(image2, caption='μμμ  WordCloud',output_format="auto", width=250)


# auto-refresh
st_data = st_folium(m, width = 1300)


#---------------------------------
import pandas as pd
import altair as alt
sql4 = "SELECT * from streamlit_day_final4"
cursor.execute(sql4)

result4 = cursor.fetchall()

df4=pd.DataFrame(result4)
df4 = df4[df4[0] == job_filter]
a=[]; b=[]; year=[]
for i in range(len(df4)):
    a.append(df4.iat[i,1])
    
for i in range(len(df4)):
    b.append(df4.iat[i,2])

for i in range(len(df4)):
    year.append(df4.iat[i,6])

print(a)
#print(df4.iat[1,6])
#print(df4.iat[0,1])

df = pd.DataFrame(
    {
        'Duration': [f"{d} μκ°" for d in year],
        'κ°μΈκ³ κ°': a,
        'κΈ°μκ³ κ°': b
    },
    columns=['Duration', 'κ°μΈκ³ κ°', 'κΈ°μκ³ κ°']
)



#st.write(df)



df = df.melt('Duration', var_name='name', value_name='value')
#st.write(df)

chart = alt.Chart(df).mark_line().encode(
  x=alt.X('Duration:N'),
  y=alt.Y('value:Q'),
  color=alt.Color("name:N")
).properties(title="λκΈ°νν©")
st.altair_chart(chart, use_container_width=True)


# sql = "SELECT * from personal_company"
# cursor.execute(sql)

# result = cursor.fetchall()

# df=pd.DataFrame(result)


# st.markdown("### Detailed Data View")
# st.dataframe(df)

# data=[[5, 33, 11],
#  [6, 22, 16],
#  [4, 11, 20],
#  [5, 23, 19],
#  [5, 24, 18],
#  [5, 17, 17],
#  [6, 16, 15]]

# chart_data = pd.DataFrame(
#      data,
#      columns=['κ°λ¨κ΅¬', 'κ΄μκ΅¬', 'μλ±ν¬κ΅¬'])

# st.line_chart(chart_data)
