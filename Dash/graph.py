# 带slider的点状图
html.Div([
    dcc.Graph(
        id='graph-with-slider',
        animate=True        # 开启动画，平滑切换
    ),
    dcc.Slider(
        id='year-slider',
        min=df['year'].min(),
        max=df['year'].max(),
        value=df['year'].min(),
        marks={str(year): str(year) for year in df['year'].unique()},
        step=None
    )
])
