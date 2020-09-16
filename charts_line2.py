import pandas as pd
import plotly.graph_objs as go

df = pd.read_csv("data/nst-est2017-alldata.csv")

df = df[df["DIVISION"] == "1"]                                  # New England Rows
columns = [col for col in df.columns if col.startswith("POP")]  # Population Estimate Columns
df.set_index("NAME", inplace=True)                              # States as Row IDs
df = df[columns]                                                # Remove unneeded columns

data = [
    go.Scatter(
        x=df.columns,
        y=df.loc[name],
        mode="lines",
        name=name) for name in df.index]

fig = go.Figure(data=data)
fig.show()
