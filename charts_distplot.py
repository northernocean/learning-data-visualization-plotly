import plotly.figure_factory as ff
import numpy as np

hist_data = [
    (np.random.randn(200) - 2),
    (np.random.randn(200)),
    (np.random.randn(200) + 2)
]
group_labels = ["X1", "X2", "X3"]
fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels)
fig.show()
