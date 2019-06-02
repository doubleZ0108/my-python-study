# 下拉框
html.Label('Dropdown'),
dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
),

# 复选下拉框
html.Label('Multi-Select Dropdown'),
dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['MTL', 'SF'],
    multi=True
),

# 单选框
html.Label('Radio Items'),
dcc.RadioItems(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value='MTL'
),

# 复选框
html.Label('Checkboxes'),
dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': u'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    values=['MTL', 'SF']
),

# 输入框
html.Label('Text Input'),
dcc.Input(value='MTL', type='text'),

# 滑动条
html.Label('Slider'),
dcc.Slider(
    min=0,
    max=9,
    marks={i: 'Label {}'.format(i) if i == 1 else str(i) for i in range(1, 6)},
    value=5,
),
# 范围滑动条
dcc.RangeSlider(
    marks={i: 'Label {}'.format(i) for i in range(-5, 7)},
    min=-5,
    max=6,
    value=[-3, 4]
)
