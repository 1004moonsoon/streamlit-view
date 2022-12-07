import streamlit as st

view = [100, 150, 30]
st.write("# Youtube view") # 샾을 이용하면 글자 크기가 커진다.
st.write("## raw")
view
st.write("## bar chart")
st.bar_chart(view)

import pandas as pd
sview = pd.Series(view)
sview 