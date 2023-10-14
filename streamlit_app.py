from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np

df = pd.DataFrame(np.random.randn(10, 5), columns=("Idea", "Advantages", "Disadvantages", "Pivot")

st.table(df)
