from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import numpy as np
from st_aggrid import AgGrid

df = pd.DataFrame({'Ideas': [1, 2, 3], 'Pivot': [4, 5, 6]})
grid_return = AgGrid(df, editable=True)
new_df = grid_return['data']
