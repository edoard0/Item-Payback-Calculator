
#import dash 
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
#import plotly
import plotly.graph_objects as go
import cufflinks as cf
import plotly.express as px
#import Payback_Calculator
from Payback_Calculator import Payback_Tracker

#create app
app = dash.Dash(__name__,)

#layout
app.layout = html.Div(style={'font-family': 'monospace','background-color':'#f2f2f'},children=[
    html.H1(style={'text-align':'center'},children='Item Payback Period Calculator'),
    
    html.Div(style={'margin':'0 auto','text-align':'justify','width':'50%','background-color':'#f2f2f2','padding':'15px','border-radius':'5px','border':'1px solid black','margin-bottom':'15px'},children=[
        html.H2(style={'font-style':'Italic','color':'blue','text-align':'center'},children='Description'),
        html.P(children="This simple application helps you calculate how much time will pass before you are able to make back the amount of money you invested in any physical good (i.e a bike, or TV),depending on the item's price, your usage rate over a given period, and an estimated item's opportunity cost.")
      ]        
    ),
    html.Div(style={'margin':'0 auto','text-align':'justify','width':'50%','background-color':'#f2f2f2','padding':'15px','border-radius':'5px','border':'1px solid black','margin-bottom':'15px'},children=[
        html.H2(style={'font-style':'Italic','color':'blue','text-align':'center'},children='Form Legend'),  
        html.P(children='Initial Cost= The amount of money spent to buy the item'),
        html.P(children='Average usage value= Monetary estimate of the opportunity cost you would have to pay if using an alternative item (i.e. train ride instead of bike)'),
        html.P(style={'padding-bottom':'15px'},children='Frequency= How many times you use the item on average over the given period')
        ]
        ),
    
    html.P(style={'text-align':'center'},children="Fill in the form below to generate your payback period projection"),
               
    html.Div(id="input area",style={'margin':'0 auto','width':'50%','background-color':'#99d6ff','padding':'15px','border-radius':'5px','border':'1px solid black'},
             children=[dcc.Input(style={'margin-left':'70px','margin-right':'5px'},id='object_type', value='', type='text',placeholder="Item Name"),
                        dcc.Input(style={'margin-right':'5px'},id='initial_cost', value='', type='number',placeholder="Initial cost"),
                        dcc.Input(style={'margin-right':'5px'},id='average_benefit', value='', type='number',placeholder="Average usage Value"),
                        dcc.Input(style={'margin-bottom':'5px'},id='frequency', value='', type='number',placeholder="Period Frequency"),
                        html.Br(),
                        dcc.Dropdown(style={"width":"65%",'margin-left':'120px'},
                            id='period_dropdown',
                            options=[
                                {'label': 'Daily', 'value': 'day'},
                                {'label': 'Weekly', 'value': 'week'},
                                {'label': 'Monthly', 'value': 'month'},
                                {'label': 'Yearly', 'value': 'year'}
                            ],
                            value='daily',placeholder="Select how often you will use the item")
     ]),
    
    html.Br(),
    
    html.Div(id='output_graph'),
    html.Div(id="output_text",style={'text-align':'center','color':'blue'})
    ])



@app.callback(
    [Output(component_id='output_graph', component_property='children'),
    Output(component_id='output_text', component_property='children')],
    [Input(component_id='object_type', component_property='value'),
    Input(component_id='initial_cost', component_property='value'),
    Input(component_id='average_benefit', component_property='value'),
    Input(component_id='frequency', component_property='value'),
    Input(component_id='period_dropdown',component_property='value')])
def generate_graph(obj,cost,benefit,frequency_,period_):
    object_=Payback_Tracker(name=obj,initial_cost=float(cost),usage_benefit=float(benefit),frequency=float(frequency_),period=period_)
    object_.generate_balance_history()
    data=object_.get_balance_data()
    
    if object_.period !="day":
        fig = px.bar(data, x=data.columns[0], y='Balance History',color="Balance History",color_continuous_scale="pubu",title="{} balance history for your {}".format(object_.period.capitalize()+"ly",object_.name))
    else:
        fig = px.bar(data, x=data.columns[0], y='Balance History',color="Balance History",color_continuous_scale="pubu",title="Daily balance history for your {}".format(object_.name))

    return dcc.Graph(
        figure=fig
    
    ), html.H2(object_.get_result())
        
    
       
#run_app
if __name__ == '__main__':
    app.run_server()








