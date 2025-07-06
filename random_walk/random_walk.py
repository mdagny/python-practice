import plotly.express as px
import plotly.graph_objects as go

from random_walk_classes import RandomWalk

# Make a random walk.
rw = RandomWalk(10000)
rw.fill_walk()

# Plot the points in the walk, with a color scale.
color_values = range(rw.num_points)
fig = px.scatter(x=rw.x_values, 
                 y=rw.y_values, 
                 color=color_values, 
                 color_continuous_scale='Viridis')

# Maintain equal axis scale, remove axes and background.
fig.update_layout(
    xaxis=dict(visible=False),
    yaxis=dict(visible=False),
    yaxis_scaleanchor="x",
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)')

fig.show()