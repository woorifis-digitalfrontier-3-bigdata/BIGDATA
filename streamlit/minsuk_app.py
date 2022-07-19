import mysql.connector as msql
import pandas as pd
import time  # to simulate a real time data, time loop

import numpy as np  # np mean, np random
import pandas as pd  # read csv, df manipulation
import streamlit as st  # 🎈 data web app development

conn = msql.connect(host='52.36.29.255', database='pets', user='bigdata',  
    password='1111')

cursor = conn.cursor()
sql = "SELECT * from personal_company"
cursor.execute(sql)

result = cursor.fetchall()

df=pd.DataFrame(result)

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

from PIL import Image
IMAGE_URL = "http://18.237.28.176:8088/superset/explore/p/Qj5y6WJVvqX/?standalone=True&height=400"

st.image(IMAGE_URL, caption="슈퍼셋", use_column_width='auto', output_format='auto')

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
