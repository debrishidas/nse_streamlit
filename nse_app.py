import streamlit as st
import datetime
#import seaborn as sns
import numpy as np
import pandas as pd
#import streamlit as st
from PIL import Image
from nsepy import get_history
from datetime import date

stock_fut = get_history(symbol="SBIN",
                            start=date(2015,1,1),
                            end=date(2015,1,10),
                            futures=True,
                            expiry_date=date(2015,1,29))

#st.dataframe(stock_fut.style.highlight_max(axis=0))
#st.table(stock_fut)

st.line_chart(stock_fut['Change in OI'])
st.line_chart(stock_fut['Open Interest'])
st.line_chart(stock_fut['Number of Contracts'])

st.table(stock_fut[:100])


##Display code

#mycode = """
#def sayhello():
#	print("Hello Streamlit lovers")
#"""

#st.code(mycode,language='python')
