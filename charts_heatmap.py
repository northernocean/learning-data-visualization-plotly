import plotly.graph_objs as go
from plotly import tools
import pandas as pd

df = []
df.append(pd.read_csv("data/2010YumaAZ.csv"))
df.append(pd.read_csv("data/2010YumaAZ.csv"))
df.append(pd.read_csv("data/2010SantaBarbaraCA.csv"))
df.append(pd.read_csv("data/2010SitkaAK.csv"))

traces = []
for _, i in enumerate(range(0, 4)):
    traces.append(
        go.Heatmap(
            x=df[i]["DAY"],
            y=df[i]["LST_TIME"],
            z=df[i]["T_HR_AVG"].values.tolist(),
            colorscale="Jet",
            zmin=5,
            zmax=40
        )
    )

# single heatmap
data = [traces[0]]
layout = go.Layout(
    title="Weekly Temperature"
)
fig = go.Figure(data=data, layout=layout)
fig.show()

# multiple heatmaps
fig = tools.make_subplots(
    rows=1,
    cols=3,
    subplot_titles=["Yuma", "Santa Barbabara", "Sitka"],
    shared_yaxes=True
)
for _, i in enumerate(range(1, 4)):
    fig.append_trace(traces[i], 1, i)
fig["layout"].update(title="Temps for US Cities")
fig.show()
