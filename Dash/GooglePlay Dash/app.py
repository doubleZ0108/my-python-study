import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
import copy
import plotly.graph_objs as go
import dash_daq as daq

from dash.dependencies import Input, Output, State
from Reader import *
# from Reader import read_file
# from Reader import file_filter
# from Reader import rating_filter
# from Reader import get_main
# from Reader import get_size
# from Reader import get_content_rating
# from Reader import get_price

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# tab标签的css
tabs_styles = {'height': '44px'}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}
tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

df = pd.read_csv('dataset\google-play-store-apps\googleplaystore.csv')

available_indicators = df['Category'].unique()

file = read_file()

app.layout = html.Div([
    html.Div(
        [
            html.Div(
                [
                    # Catagory下拉框
                    dcc.Dropdown(id='catagory',
                                 options=[{
                                     'label': i,
                                     'value': i
                                 } for i in available_indicators],
                                 value='ART_AND_DESIGN'),
                    # Price单选按钮
                    dcc.RadioItems(id='price',
                                   options=[{
                                       'label': i,
                                       'value': i
                                   } for i in ['Free', 'Paid', 'All']],
                                   value='All',
                                   labelStyle={'display': 'inline-block'})
                ],
                style={
                    'width': '49%',
                    'display': 'inline-block'
                }),

            # tab -> 可以切换两个视图
            html.Div(
                [
                    dcc.Tabs(
                        id="tabs",
                        children=[
                            dcc.Tab(label='Size & Content Rating',
                                    style=tab_style,
                                    selected_style=tab_selected_style,
                                    children=[
                                        html.Div(
                                            [
                                                dcc.Graph(id='size-graph',
                                                          animate=True),
                                                dcc.Graph(
                                                    id='content-rating-graph',
                                                    animate=True)
                                            ],
                                            style={
                                                'display': 'inline-block',
                                                'width': '97%',
                                                'height': '20%',
                                                'padding': '0 0 0 0'
                                            })
                                    ]),
                            dcc.Tab(
                                label='Price & Rating',
                                style=tab_style,
                                selected_style=tab_selected_style,
                                children=[
                                    html.Div(
                                        [
                                            dcc.Graph(id='price-graph',
                                                      animate=True),
                                            daq.Knob(id='my-knob',
                                                     label="Rating",
                                                     labelPosition='bottom',
                                                     value=5,
                                                     max=5,
                                                     scale={
                                                         'start': 0,
                                                         'labelInterval': 1,
                                                         'interval': 1
                                                     }),
                                            # 仪表盘的callback显示
                                            html.Div(id='knob-output',
                                            style={
                                                'marginTop': -80,
                                                'marginLeft': 425
                                            }),
                                            html.Img(id='star-img',
                                            src='https://upload-images.jianshu.io/upload_images/12014150-c2ee9fe0591b3247.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240',
                                            height='50px',
                                            width='50px',
                                            style={
                                                'marginTop': -120,
                                                'marginLeft': 375
                                            }
                                            )
                                        
                                        ],
                                        style={
                                            'display': 'inline-block',
                                            'width': '90%',
                                            'height': '20%',
                                            'padding': '0 0 0 0'
                                        })
                                ]),
                        ],
                        style=tabs_styles),
                ],
                style={
                    'width': '49%',
                    'float': 'right',
                    'display': 'inline-block'
                })
        ],
        style={
            'borderBottom': 'thin lightgrey solid',
            'backgroundColor': 'rgb(250, 250, 250)',
            'padding': '10px 5px'
        }),
    html.Div([dcc.Graph(id='main-graph', animate=True)],
             style={
                 'width': '49%',
                 'display': 'inline-block',
                 'padding': '0 20'
             }),
])


# 筛选数据
def filter(catagory_name, price_choice):
    # 按照是否付费筛选数据
    if price_choice == "Free":
        df_ = df[df['Price'] == "0"]
    elif price_choice == "Paid":
        df_ = df[df['Price'] != "0"]
    else:
        df_ = df

    # 按照分类筛选数据
    dff = df_[df_['Category'] == catagory_name]

    return dff


# 主点状图 callback
@app.callback(
    dash.dependencies.Output('main-graph', 'figure'),
    [
        dash.dependencies.Input('catagory', 'value'),  # 输入1 -> 软件分类
        dash.dependencies.Input('price', 'value'),
        dash.dependencies.Input('my-knob', 'value')
    ])  # 输入2 -> 价格
def update_maingraph(catagory_name, price_choice, rating_value):

    dff = filter(catagory_name, price_choice)

    newfile = read_file()
    newfile = file_filter(newfile, catagory_name, price_choice)
    newfile = rating_filter(newfile, rating_value)

    [Reviews, Installs, App] = get_main(newfile)
    # print(size_catagory, size_list)

    return {
        'data': [
            go.Scatter(
                x=Reviews,  # 横轴为评论数
                y=Installs,  # 纵轴为安装数
                text=App,
                mode='markers',
                marker={
                    'size': 15,
                    'opacity': 0.5,
                    'line': {
                        'width': 0.5,
                        'color': 'white'
                    }
                })
        ],
        'layout':
        go.Layout(xaxis={
            'title': 'Reviews',
        },
                  yaxis={
                      'title': 'Installs',
                  },
                  margin={
                      'l': 40,
                      'b': 30,
                      't': 10,
                      'r': 0
                  },
                  height=450,
                  hovermode='closest')
    }


# size折线图 callback
@app.callback(dash.dependencies.Output('size-graph', 'figure'), [
    dash.dependencies.Input('catagory', 'value'),
    dash.dependencies.Input('price', 'value')
])
def update_sizeGraph(catagory_name, price_choice):

    newfile = read_file()
    newfile = file_filter(newfile, catagory_name, price_choice)
    [size_catagory, size_list] = get_size(newfile)
    # print(size_catagory, size_list)

    return {
        'data': [{
            'x': size_catagory,
            'y': size_list,
            'type': 'Scatter',
        }],
        'layout':
        go.Layout(margin={
            'l': 40,
            'b': 50,
            't': 20,
            'r': 20
        },
                  legend={
                      'x': 0,
                      'y': 1
                  },
                  height=280,
                  hovermode='closest')
    }


# content rating饼状图 callback
@app.callback(dash.dependencies.Output('content-rating-graph', 'figure'), [
    dash.dependencies.Input('catagory', 'value'),
    dash.dependencies.Input('price', 'value')
])
def update_conten_tratingGraph(catagory_name, price_choice):

    newfile = read_file()
    newfile = file_filter(newfile, catagory_name, price_choice)

    [content_rating_catagory,
     content_rating_list] = get_content_rating(newfile)
    # print(content_rating_catagory,content_rating_list)

    trace = go.Pie(
        labels=content_rating_catagory,
        values=content_rating_list,
    )

    return {
        'data': [trace],
        'layout':
        go.Layout(margin={
            'l': 130,
            'b': 30,
            't': 50,
            'r': 0
        },
                  height=300,
                  hovermode='closest')
    }


# price折线图 callback
@app.callback(dash.dependencies.Output('price-graph', 'figure'), [
    dash.dependencies.Input('catagory', 'value'),
    dash.dependencies.Input('price', 'value'),
    dash.dependencies.Input('my-knob', 'value')
])
def update_priceGraph(catagory_name, price_choice, rating_value):

    newfile = read_file()
    newfile = file_filter(newfile, catagory_name, price_choice)
    newfile = rating_filter(newfile, rating_value)

    [price_catagory, price_list] = get_price(newfile)

    return {
        'data': [
            {
                "x": price_catagory,
                "y": price_list,
                "mode": "lines+markers",
                'type': 'Scatter',
                'name': 'Line'
            },
        ],
        'layout':
        go.Layout(margin={
            'l': 130,
            'b': 50,
            't': 50,
            'r': 40
        },
                  height=300,
                  hovermode='closest')
    }


# 仪表盘 callback
@app.callback(dash.dependencies.Output('knob-output', 'children'),
              [dash.dependencies.Input('my-knob', 'value')])
def update_output(value):
    return '<= {}.'.format(value)


if __name__ == '__main__':
    app.run_server(debug=True, host='localhost')
