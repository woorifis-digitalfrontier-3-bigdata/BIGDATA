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

st.title("μμΈνΉλ³μ μμμ  νΉνμ ν¬ λͺ¨λν°λ§")
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

if job_filter=='κ°λ¨κ΅¬':
    folium.Marker(
      location=[37.49108397,127.05536209],
      #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
      popup='<a href="http://44.240.164.14:8088/superset/dashboard/2/?native_filters_key=6nx5Rz6IctADz8CW-uBuL5ExDZ2A0rwOLCpJxJ3Gh8_2GKK9YIT0tJx5fQgPvhfq" target="_blank">κ°λ¨κ΅¬</a>',
      icon=folium.Icon(color='red',icon='star')
    ).add_to(m)
    
elif job_filter=='μλ±ν¬κ΅¬':
    folium.Marker(
      location=[37.51527262,126.90702140],
      #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
      popup='<a href="http://44.240.164.14:8088/superset/dashboard/2/?native_filters_key=6nx5Rz6IctADz8CW-uBuL5ExDZ2A0rwOLCpJxJ3Gh8_2GKK9YIT0tJx5fQgPvhfq" target="_blank">μλ±ν¬κ΅¬</a>',
      icon=folium.Icon(color='red',icon='star')
    ).add_to(m)
elif job_filter=='κ΄μκ΅¬':
    folium.Marker(
      location=[37.471077623795,126.93920205178],
      #popup="<a href=http://35.88.197.65:8088/superset/dashboard/p/mdZK1LrRA2w/>Place Guillaume II</a>",
      popup='<a href="http://44.240.164.14:8088/superset/dashboard/2/?native_filters_key=6nx5Rz6IctADz8CW-uBuL5ExDZ2A0rwOLCpJxJ3Gh8_2GKK9YIT0tJx5fQgPvhfq" target="_blank">κ΄μκ΅¬</a>',
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

fig_col1, fig_col2  = st.columns(2)

with fig_col1:
    st.image(image, caption='μ°λ¦¬μν WordCloud',output_format="auto", width=250)

with fig_col2:
    st.image(image2, caption='μμμ  WordCloud',output_format="auto", width=250)


# auto-refresh
st_data = st_folium(m, width = 1300)

add_selectbox = st.sidebar.selectbox(
    "ν μ§μ­ μ ννκ² μ΅λκΉ?",
    ("μμΈνΉλ³μ","κ°λ¦μ", "λν΄μ", "μμ΄μ", "κ±°μ μ", "κΉν΄μ", "μ°½μμ", "μΈμ°κ΄μ­μ", "ν¬ν­μ", "μ μ²μ")
)

tmp_nes1 = [
'μ°λ¦¬μν "μμ°κ΄λ¦¬ κ³΅κ²© μμΌλ‘"β¦TCEμΌν°λ‘ WM ν νλ λ€ [μ°ν©λ΄μ€]',
    'λ­μλ¦¬ μ ν¬μ κΈμ΅ μ»¨μ€νβ¦μ΄κ³ μ‘ μμ°κ° μ‘μ μ°λ¦¬μν [μμ£Όκ²½μ ]',
    'κ³ κ°μ€μ¬ λ¦¬λΆνΈβ μλλ΄λ μ νμν [μ€μμΌλ³΄]',
]

tmp_nes2 = [
    'KBκ΅­λ―Όμν, κ³ λ ΉμΈ΅ νΉν μ΄λμ ν¬ KB μλμ΄ λΌμ΄μ§ κ°μ€ [μ°ν©λ΄μ€]',
    'ν΄κ·Ό νμλ μΌκ΅΄λ³΄λ©° κΈμ΅μλ΄β¦KBκ΅­λ―Όμν νΉνμ ν¬ [μ΄μ½λΈλ―Ήλ¦¬λ·°]',
    'μ νμν, νμΌμ 8μκΉμ§ ν μμΌλ μ¬λ μ ν¬ λ§λ λ€ [μμ£Όκ²½μ ]',
]

tmp_nes3 = [
    'βμ κΈ°λ°μ΄ν¬ μΆ©μ νκ³  μνμλ¬΄ λ³Έλ€ββ―νΈμμ  λ³μ  μ΄λκΉμ§ [μμμνμμ¦]',
    'νΈμμ μκ³,κΈμ΅νΉνμ ν¬ ν¨μ...κ³ κ°Β·λ§€μΆ κ»μΆ© [μλμ§κ²½μ ]',
    '"VVIP λͺ¨μλΌ"Β·Β·Β·μνκΆ, λΉμ΄μμμ΅ νλ μΉλΆμ [μμΈνμ΄λΈμ€]'
]



# # Using "with" notation
for _ in range(3):
    with st.sidebar:
        for i in tmp_nes1:
            st.info(i)
    
    tmp_nes1=[]
    with st.sidebar:
        for i in tmp_nes2:
            st.info(i)

    tmp_nes2=[]
    with st.sidebar:
        for i in tmp_nes3:
            st.info(i)

#     st.info('μ°λ¦¬μν "μμ°κ΄λ¦¬ κ³΅κ²© μμΌλ‘"β¦TCEμΌν°λ‘ WM ν νλ λ€ [μ°ν©λ΄μ€]')
#     st.info('λ­μλ¦¬ μ ν¬μ κΈμ΅ μ»¨μ€νβ¦μ΄κ³ μ‘ μμ°κ° μ‘μ μ°λ¦¬μν [μμ£Όκ²½μ ]')
#     st.info('κ³ κ°μ€μ¬ λ¦¬λΆνΈβ μλλ΄λ μ νμν [μ€μμΌλ³΄]')
#     st.info('λΉλλ©΄ κ°­ λ©μ°λ μνλ€...365μΌ λ°€ 9μκΉμ§ λμ§νΈμλ΄λ [νμ΄λΈμλ΄μ€]')
#     st.info('[μ£Όκ° ESG λ΄μ€_κΈμ΅] NHλνμνΒ·BCμΉ΄λΒ·νλμν [μμμκ²½μ ]')
#     st.info('KBκ΅­λ―Όμν, κ³ λ ΉμΈ΅ νΉν μ΄λμ ν¬ KB μλμ΄ λΌμ΄μ§ κ°μ€ [μ°ν©λ΄μ€]')
#---------------------------------
import pandas as pd
import altair as alt
sql4 = "SELECT * from streamlit_day_final5"
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
        'μκ°': [f"{d}" for d in year],
        'κ°μΈκ³ κ°': a,
        'κΈ°μκ³ κ°': b
    },
    columns=['μκ°', 'κ°μΈκ³ κ°', 'κΈ°μκ³ κ°']
)



#st.write(df)



df = df.melt('μκ°', var_name='name', value_name='κ³ κ° μ')
#st.write(df)

ANNOTATIONS = [
    ("09μ", "Pretty good day for GOOG"),
    ("10μ", "Something's going wrong for GOOG & AAPL"),
    ("11μ", "Market starts again thanks to..."),
    ("12μ", "Small crash for GOOG after..."),
]

# Create a chart with annotations
annotations_df = pd.DataFrame(ANNOTATIONS, columns=["μκ°", "event"])
#annotations_df.μκ° = pd.to_datetime(annotations_df.μκ°)
annotations_df["y"] = 0
annotation_layer = (
    alt.Chart(annotations_df)
    .mark_text(size=15, text="β¬", dx=0, dy=-10, align="center")
    .encode(
        x="μκ°:N",
        y=alt.Y("y:Q"),
        tooltip=["event"],
    )
    .interactive()
)


chart = alt.Chart(df).mark_line().encode(
  x=alt.X('μκ°:N'),
  y=alt.Y('κ³ κ° μ:Q'),
  color=alt.Color("name:N")
).properties(title="λκΈ°νν©")
st.altair_chart((chart + annotation_layer).interactive(), use_container_width=True)


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
