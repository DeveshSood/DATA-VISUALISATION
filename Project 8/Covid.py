import pandas as pd
import plotly.express as px

df = pd.read_csv("Covid.csv")

fig=px.scatter(df, x="Date", y="Cases", color="Country", title="C")

fig.show()