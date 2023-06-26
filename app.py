from dash import dash, html, dcc , Input, Output, State, ctx
import dash_bootstrap_components as dbc

import config

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from math import ceil, floor

######################### App Instance #############################################

app = dash.Dash(name=config.app_name, external_stylesheets = [dbc.themes.LUX, config.fontawesome])
app.title = config.app_name
app.config.suppress_callback_exceptions = True

################################# Navbar ###########################################

'''

This includes links to supporting documentation
- Progress Report
- Advisors
- Study, Sleep, stress reduction recommendations

'''

############################ Input == None #########################################

############################### Output##############################################

navbar = dbc.Nav(children=[
    
    # Logo/home 
    ##### Logo may not work when files are moved as the source path is specific to current location
    dbc.NavItem(html.Img(src=config.image, height="75px")),
    
    # About
    dbc.NavItem(        
        html.Div([
                dbc.Button("About", id="toggle", color="success", n_clicks=0, size="md"),
                dbc.Popover(id="about", trigger="hover", target="toggle", 
                            children=[
                                    dbc.PopoverHeader("How it works"), 
                                    dbc.PopoverBody(config.about)
                                      ])])),

    #links
    dbc.DropdownMenu(label="Links", size="md", color="primary", children= [
        dbc.DropdownMenuItem(
            [html.I(className="msu-Progress Report"), "  Progress Report"], href=config.progress, target="_blank"), 
        dbc.DropdownMenuItem(
            [html.I(className="msu-Advisors"), "  Advisors"], href=config.advisors, target="_blank"), 
        dbc.DropdownMenuItem(
            [html.I(className="ol-Sleep"), "  Sleep Recommendations"], href=config.sleep, target="_blank"), 
        dbc.DropdownMenuItem(
            [html.I(className="ol-Study"), "  Study Recommendations"], href=config.study, target="_blank"), 
        dbc.DropdownMenuItem(
            [html.I(className="ol-Stress"), "  Stress Tips"], href=config.stress, target="_blank"),
    ]),

    # Space between buttons
    dbc.NavItem(html.Div(style={'width': '5px'})),

    # Survey
    dbc.NavItem(        
        html.Div([
                dcc.Link(dbc.Button('Survey', color='success', size='md'), href=config.survey, target='_blank')
        ]))])
    
######################################### Body #####################################################

################################# Input #############################################
inputs = dbc.Row(id="inputs", align = "between", justify = "evenly", children = [
    
    # Slider for credits earned
    dbc.Label("Current Credits Earned", id="applied-label", html_for="n-credits"),
    dcc.Slider(id="n-credits", min=0, max=120, step=1, value=0, tooltip = {"placement": "top"}, 
               updatemode="drag", marks = 
               # {i: str(i) for i in range(0,121,10)}
               {0: {'label' : '0', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                70: {'label' : '70', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                80: {'label' : '80', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                90: {'label' : '90', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                100: {'label' : '100', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                110: {'label' : '110', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                120: {'label' : '120', 'style' : {'color' : '#000000', 'font-weight' : '900'}}}),
    dbc.Tooltip("How many credits do you currently have that will count toward your current degree?", 
                id="tooltip-1", is_open=False, target='applied-label', trigger="hover"),
    
    # slider for credits per semester
    dbc.Label("Credits Per Semester",id='expected-label', html_for="n-s-credits"),
    dcc.Slider(id="n-s-credits", min=0, max=20, step=1, value=15, tooltip = {"placement": "top"}, 
               updatemode="drag", marks = 
                                       # {i: str(i) for i in range(0,21,2)}
                                       {0: {'label' : '0', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       2: {'label' : '2', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       4: {'label' : '4', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       6: {'label' : '6', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       8: {'label' : '8', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       10: {'label' : '10', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       12: {'label' : '12', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       14: {'label' : '14', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       16: {'label' : '16', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       18: {'label' : '18', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
                                       20: {'label' : '20+', 'style' : {'color' : '#000000', 'font-weight' : '900'}}}),
    dbc.Tooltip("How many credits do expect to take each semester?", 
                id="tooltip-2d", is_open=False, target='expected-label', trigger="hover"),
    
    # slider for Years
    dbc.Label("Years to Graduation",id='years-label', html_for="n-years"),
    dcc.Slider(id="n-years", min=0, max=10, step=0.5, value=4, tooltip = {"placement": "top"}, 
               updatemode="drag", marks = 
               # {i: str(i) for i in range(0,11)} 
               {0: {'label' : '0', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               1: {'label' : '1', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               2: {'label' : '2', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               3: {'label' : '3', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               4: {'label' : '4', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               5: {'label' : '5', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               6: {'label' : '6', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               7: {'label' : '7', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               8: {'label' : '8', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               9: {'label' : '9', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               10: {'label' : '10+', 'style' : {'color' : '#000000', 'font-weight' : '900'}}}),
    dbc.Tooltip("How many years would you like to graduate in?", 
                id="tooltip-3", is_open=False, target='years-label', trigger="hover"),
        
    # slider for study hours
    dbc.Label("Average Weekly Study Hours", id= 'study-label', html_for="n-study"),
    dcc.Slider(id="n-study", min=0, max=60, step=1, value=45, tooltip = {"placement": "top"}, 
               updatemode="drag", marks = 
               # {i: str(i) for i in range(0,61,5)}
               {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
               5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
               10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
               15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
               20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
               25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
               30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
               35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
               40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
               45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
               50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
               55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
               60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}}}),
    dbc.Tooltip("How many hours do you expect to study a week? The colors of the marks for this slider represent a dynamic range based on how many credits you expect to take each semester. Red represents studying less than the amount of credit hours. Orange represents 1 to 2 times the credits hours. Green represents 3 times the credit hours or above. This may vary depending on individual needs and preferences. For more information see the article linked above.", 
                id="tooltip-5", is_open=False, target='study-label', trigger="hover"),

    # slider for sleep hours
    dbc.Label("Average Nightly Hours of Sleep",id='sleep-label', html_for="n-sleep"),
    dcc.Slider(id="n-sleep", min=5, max=12, step=1, value=8, tooltip = {"placement": "top"}, 
               updatemode="drag", marks = 
               # {i: str(i) for i in range(5,13)}
                                       {5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                                       6: {'label' : '6', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                                       7: {'label' : '7', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                                       8: {'label' : '8', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                                       9: {'label' : '9', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                                       10: {'label' : '10', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                                       11: {'label' : '11', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                                       12: {'label' : '12', 'style' : {'color' : '#009F81', 'font-weight' : '900'}}}),
    dbc.Tooltip("How many hours of sleep do you expect to get a night? The colors of the marks for this slider represent a range that represents most sleep recommendations. Red and orange represent insuffecient sleep, while green represents a healthy sleep range. This may vary depending on the individual. See article linked above for recommendations.", 
                id="tooltip-4", is_open=False, target='sleep-label', trigger="hover"),
    
    # slider for work hours
    dbc.Label("Average Weekly Work Hours",id='work-label', html_for="n-work"),
    dcc.Slider(id="n-work", min=0, max=40, step=1, value=20, tooltip = {"placement": "top"}, 
               updatemode="drag", marks = 
               # {i: str(i) for i in range(0,41,5)}
               {0: {'label' : '0', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               5: {'label' : '5', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               10: {'label' : '10', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               15: {'label' : '15', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               20: {'label' : '20', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               25: {'label' : '25', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               30: {'label' : '30', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               35: {'label' : '35', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               40: {'label' : '40', 'style' : {'color' : '#000000', 'font-weight' : '900'}}}),
    dbc.Tooltip("How many hours do you expect to work a week during the semester?", 
                id="tooltip-6", is_open=False, target='work-label', trigger="hover"),
    
    # slider for free hours with button to add sliders
    dbc.Label("Average Weekly Hours of Free Time",id='free-label', html_for="n-free"),    
    dcc.Slider(id="n-free", min=0, max=40, step=1, value=0, tooltip = {"placement": "top"}, 
               updatemode="drag", marks = 
               # {i: str(i) for i in range(0,41,5)}
               {0: {'label' : '0', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               5: {'label' : '5', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               10: {'label' : '10', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               15: {'label' : '15', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               20: {'label' : '20', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               25: {'label' : '25', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               30: {'label' : '30', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               35: {'label' : '35', 'style' : {'color' : '#000000', 'font-weight' : '900'}},
               40: {'label' : '40', 'style' : {'color' : '#000000', 'font-weight' : '900'}}}),
    dbc.Tooltip("How many hours a week would you like to be free to do what you want?", 
                id="tooltip-7", is_open=False, target='free-label', trigger="hover"),
    
    dbc.Row([
    dbc.Col([
        html.Div('Added Tasks', id = 'task_title', hidden=True, style={'font-size' : '200%', 'text-align' : 'justify', 'text-decoration-line' : 'underline'})],width = 7),
    dbc.Col([
        dbc.Button("Add Task", id = "slider_button", n_clicks =0, size = "sm"),
        dbc.Tooltip("You can add up to 5 sliders that allow you to track other activites that take up your time. i.e. Travel, Exercise, etc. ", 
                    id="tooltip-7.5", is_open=False, target="slider_button", trigger="hover")
            ],width=5)],justify = "between"),
    
    # Extra Slider 1
    html.Div([
    dbc.FormFloating(id="con-slid-1", children = [
            dbc.Row([
                dbc.Col([
                    dbc.Label(dbc.Input(id = "slider-1-input", type="text", placeholder="Task Name"), 
                                   id=f'slider-1-label', html_for="slider-1")]),
                dbc.Col(
                    dbc.Button("Add Hours", id = "slider-1-max", n_clicks = 0, size = "sm")),
                    dcc.Slider(id="slider-1", min=0, max = 10, step=1, value=0, tooltip = {"placement": "top"}, 
                           updatemode="drag", marks = {i: str(i) for i in range(0,11)}),
                    ])], style = {"display": "none", 'border': '1px solid black'}),
    
    # Extra Slider 2
    dbc.FormFloating(id='con-slid-2', children =[
            dbc.Row([
                dbc.Col([
                    dbc.Label(dbc.Input(id = "slider-2-input", type="text", placeholder="Task Name"), 
                                   id=f'slider-2-label', html_for="slider-2")]),
                dbc.Col(
                    dbc.Button("Add Hours", id = "slider-2-max", n_clicks = 0, size = "sm")),
                    dcc.Slider(id="slider-2", min=0, max = 10, step=1, value=0, tooltip = {"placement": "top"}, 
                           updatemode="drag", marks = {i: str(i) for i in range(0,11)}),
                    ])], style= {'display': 'none', 'border': '1px solid black'}),

    # Extra Slider 3
    dbc.FormFloating(id='con-slid-3', children =[
            dbc.Row([
                dbc.Col([dbc.Label(dbc.Input(id = "slider-3-input", type="text", placeholder="Task Name"), 
                                   id=f'slider-3-label', html_for="slider-3")]),
                dbc.Col(dbc.Button("Add Hours", id = "slider-3-max", n_clicks = 0, size = "sm")),
                dcc.Slider(id="slider-3", min=0, max = 10, step=1, value=0, tooltip = {"placement": "top"}, 
                           updatemode="drag", marks = {i: str(i) for i in range(0,11)}),
                    ])], style= {'display': 'none', 'border': '1px solid black'}),
    
     # Extra Slider 4
    dbc.FormFloating(id='con-slid-4', children =[
            dbc.Row([
                dbc.Col([dbc.Label(dbc.Input(id = "slider-4-input", type="text", placeholder="Task Name"), 
                                   id=f'slider-4-label', html_for="slider-4")]),
                dbc.Col(dbc.Button("Add Hours", id = "slider-4-max", n_clicks = 0, size = "sm")),
                dcc.Slider(id="slider-4", min=0, max = 10, step=1, value=0, tooltip = {"placement": "top"}, 
                           updatemode="drag", marks = {i: str(i) for i in range(0,11)}),
                    ])], style= {'display': 'none', 'border': '1px solid black'}),

     # Extra Slider 5
    dbc.FormFloating(id='con-slid-5', children =[
            dbc.Row([
                dbc.Col([dbc.Label(dbc.Input(id = "slider-5-input", type="text", placeholder="Task Name"), 
                                   id=f'slider-5-label', html_for="slider-5")]),
                dbc.Col(dbc.Button("Add Hours", id = "slider-5-max", n_clicks = 0, size = "sm")),
                dcc.Slider(id="slider-5", min=0, max = 10, step=1, value=0, tooltip = {"placement": "top"}, 
                           updatemode="drag", marks = {i: str(i) for i in range(0,11)}),
                    ])], style= {'display': 'none', 'border': '1px solid black'}),

])])
############################################### Output ######################################################
body = dbc.Row([
    
    # Input
    dbc.Col(md=3, children=[
        inputs,
    ],align="stretch"),
    
    # Output
    dbc.Col(md=9, children=[
        dbc.Spinner([
                # Title
                dcc.Markdown(id="title", style={"font-size": '20px', "white-space": "pre-line"}),

                # plot
                dcc.Graph(id='plot'),

                # # download
                # html.A(html.Button("Download", id= 'download-button'),id='download',download='student.png',href='', n_clicks=0),
                
                html.Br(),html.Br(),
                
                # End Notes
                dcc.Markdown(config.disclaimer, style={'font-size': '14px', "white-space": "pre-line"},id="note")

        ], color="primary", type="border")
    ])
])

############################################## Callbacks ###################################################

# Callback to change marks colors on study slider based on credits slider
@app.callback(
            Output('n-study', 'marks'),
            Input('n-s-credits', 'value'))

def set_colors(value):
    if value == 0:
        marks = {0: {'label' : '0', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 1:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 2:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 3:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 4:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 5:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 6:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 7:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 8:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 9:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 10:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 11:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 12:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 13:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900',}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 14:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 15:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 16:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 17:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 18:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 19:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    elif value == 20:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#FF6E3A', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#009F81', 'font-weight' : '900'}},
                }
    else:
        marks = {0: {'label' : '0', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                5: {'label' : '5', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                10: {'label' : '10', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                15: {'label' : '15', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                20: {'label' : '20', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                25: {'label' : '25', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                30: {'label' : '30', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                35: {'label' : '35', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                40: {'label' : '40', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                45: {'label' : '45', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                50: {'label' : '50', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                55: {'label' : '55', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                60: {'label' : '60', 'style' : {'color' : '#E20134', 'font-weight' : '900'}},
                }
    return marks

# Callback for circular relationship between credits per semester and years to graduation

@app.callback(
            Output("n-s-credits", "value"),
            Output("n-years", "value"),
            Input("n-s-credits", "value"),
            Input("n-years", "value"),
            Input("n-credits", "value"))

def sync_input(n_s_credits, n_years, n_credits):
    input_id = ctx.triggered[0]["prop_id"].split(".")[0]
    if input_id == "n-s-credits":
        if n_s_credits == 0:
            n_years = 1_000_000
        else:    
            n_years = round((120 - n_credits) / n_s_credits / 2)
    else:
        if n_years == 0:
            n_s_credits = 1_000_000
        else:
            n_s_credits = round((120 - n_credits) / n_years / 2)
    return n_s_credits, n_years

############## Callback for adding sliders

# Extra slider 1

@app.callback(
        Output("con-slid-1", "style"),
        Output("task_title", "hidden"),
        Input("slider_button", "n_clicks"))

def add_slider_1(val):
    if val >= 1:
        return {"display" : "block"}, False
    else:
        return {"display" : "none"}, True

# Extra slider 2

@app.callback(
        Output('con-slid-2' , 'style'),
        Input('slider_button' , 'n_clicks'))

def add_slider_2(clicks):
    if clicks >= 2:
        return {"display" : "block"}
    else:
        return {"display" : "none"}

# Extra slider 3

@app.callback(
        Output('con-slid-3', 'style'),
        Input('slider_button', 'n_clicks'))

def add_slider_3(clicks):
    if clicks >= 3:
        return {"display": "block"}
    else:
        return {"display": "none"}

# Extra slider 4

@app.callback(
        Output('con-slid-4', 'style'),
        Input('slider_button', 'n_clicks'))

def add_slider_4(clicks):
    if clicks >= 4:
        return {"display": "block"}
    else:
        return {"display": "none"}

# Extra slider 5

@app.callback(
        Output('con-slid-5', 'style'),
        Input('slider_button', 'n_clicks'))

def add_slider_5(clicks):
    if clicks >= 5:
        return {"display": "block"}
    else:
        return {"display": "none"}

####################### Callback to increase extra slider max

# Slider 1 Max
@app.callback(
        Output('slider-1', 'max'),
        Output('slider-1', 'marks'),
        Input('slider-1-max', 'n_clicks'),
        Input('slider-1', 'max'))

def increase_max(n_clicks, s_max):
    if n_clicks == 0:
        return s_max, {i: str(i) for i in range(0,11)}
    else:
        return s_max + 1, {i: str(i) for i in range(0, s_max + 2)}
    
# Slider 2 Max
@app.callback(
        Output('slider-2', 'max'),
        Output('slider-2', 'marks'),
        Input('slider-2-max', 'n_clicks'),
        Input('slider-2', 'max'))

def increase_max(n_clicks, s_max):
    if n_clicks ==0:
        return s_max, {i: str(i) for i in range(0,11)}
    else:
        return s_max + 1, {i: str(i) for i in range(0, s_max + 2)}

# Slider 3 Max
@app.callback(
        Output('slider-3', 'max'),
        Output('slider-3', 'marks'),
        Input('slider-3-max', 'n_clicks'),
        Input('slider-3', 'max'))

def increase_max(n_clicks, s_max):
    if n_clicks ==0:
        return s_max, {i: str(i) for i in range(0,11)}
    else:
        return s_max + 1, {i: str(i) for i in range(0, s_max + 2)}
    
# Slider 4 Max
@app.callback(
        Output('slider-4', 'max'),
        Output('slider-4', 'marks'),
        Input('slider-4-max', 'n_clicks'),
        Input('slider-4', 'max'))

def increase_max(n_clicks, s_max):
    if n_clicks ==0:
        return s_max, {i: str(i) for i in range(0,11)}
    else:
        return s_max + 1, {i: str(i) for i in range(0, s_max + 2)}
    
# Slider 5 Max
@app.callback(
        Output('slider-5', 'max'),
        Output('slider-5', 'marks'),
        Input('slider-5-max', 'n_clicks'),
        Input('slider-5', 'max'))

def increase_max(n_clicks, s_max):
    if n_clicks ==0:
        return s_max, {i: str(i) for i in range(0,11)}
    else:
        return s_max + 1, {i: str(i) for i in range(0, s_max + 2)}

################### Callback to diplay Option Title

@app.callback(
    Output('title', 'children'),
    Input("slider_button", 'n_clicks'),
    Input("n-credits", "value"),
    Input("n-years", "value"),
    Input("n-s-credits", "value"),
    Input("n-sleep", "value"),
    Input("n-study", "value"),
    Input("n-work", "value"),
    Input("n-free", "value"),
    Input("slider-1", "value"),
    Input("slider-2", "value"),
    Input("slider-3", "value"),
    Input("slider-4", "value"),
    Input("slider-5", "value"),
)

def title_output(n_clicks, n_credits, n_years, n_s_credits, n_sleep, n_study, n_work, n_free, slider_1, slider_2, slider_3, slider_4, slider_5):
    week = 168
    week_sleep = int(n_sleep) * 7
    remaining = 120 - n_credits
    extra = slider_1 + slider_2 + slider_3 + slider_4 + slider_5
    remaining_hrs = week - week_sleep - n_study - n_work - n_free - n_s_credits - extra

    # Notifications
    
    # Financial Aid
    fa_notification = "\n\n`Note: With less than 6 credits per semester, you may not be eligible for financial aid. Please reach out to your advisor for guidance`" if n_s_credits < 6 else ""
    
    # Veteran or International Students
    vi_notification = "\n\n`Note: If you are using Veterans Benefits or if you are an International student, taking less than 12 credits per semester may affect your funding. Please reach out to your advisor for guidance.`" if n_s_credits < 12 else ""
    
    # Health Insurance
    hi_notification = "\n\n`Note: If you take 9 or more credit hours in a semester you are automatically enrolled in MSU Denvers Student Health Insurance Plan. You can opt out of the program if you already have health insurance. More information can be found in the Student Hub under Health/Wellness.`" if n_s_credits >= 9 else ""

    # Study hours less than credit hours
    study_notification = "\n\n`Note: The time you have allocated for studying is less than the amount of credits you are taking in a semester. For study tips see the linked article above.`" if n_study < n_s_credits else ""

    # Graduation Projection
    grad_proj = f"### Graduation Projection\n\n\n\
With {n_credits} college credits currently earned, you need {remaining} additional credits to finish your bachelor's degree\n\
at MSU Denver. If you take _`{n_s_credits} credits`_ per semester, you could graduate in _`{n_years} years`_."

    # Weekly Hourly Projection
    if remaining_hrs < 0:
        weekly_proj = f"\n\n### Weekly Hourly Projection\n\n\n\
With a total of 168 hours in a week and your current predicted course load, if you were to:\n\
study {n_study} hours, sleep {week_sleep} hours, work {n_work} hours, spend {n_free} hours of free time,{' and spend ' + str(extra) + ' hours accomplishing your added tasks' if n_clicks > 0 else ''}\n\
you would need `{abs(remaining_hrs)} additional hours` than there are in a week to fit everything in (Use the sliders to adjust down your weekly hours)."
    else:
        weekly_proj = f"\n\n### Weekly Hourly Projection\n\n\n\
With a total of 168 hours in a week and your current predicted course load, if you were to:\n\
study {n_study} hours, sleep {week_sleep} hours, work {n_work} hours, spend {n_free} hours of free time,{' and spend ' + str(extra) + ' hours accomplishing your added tasks' if n_clicks > 0 else ''}\n\
you would have {remaining_hrs} hours remaining in the rest of your week."

    return grad_proj + weekly_proj + study_notification+ fa_notification + vi_notification + hi_notification

################################ Call back for plot

@app.callback(
    Output("plot", "figure"),
    Input("n-credits", "value"),
    Input("n-s-credits", "value"),
    Input("n-years", "value"),
    Input("n-sleep", "value"),
    Input("n-study", "value"),
    Input("n-work", "value"),
    Input("n-free", "value"),
    Input("slider-1", "value"),
    Input("slider-2", "value"),
    Input("slider-3", "value"),
    Input("slider-4", "value"),
    Input("slider-5", "value"),
    Input("slider-1-input", "value"),
    Input("slider-2-input", "value"),
    Input("slider-3-input", "value"),
    Input("slider-4-input", "value"),
    Input("slider-5-input", "value"),)

def plot_graph(n_credits, n_s_credits, n_years, n_sleep, n_study, n_work, n_free, s1, s2, s3, s4, s5, s1_input, s2_input, s3_input, s4_input, s5_input):
    data = []
    week = 168
    week_sleep = n_sleep * 7
    
    remaining = week - week_sleep - n_study - n_work - n_free - n_s_credits - s1 - s2 - s3 - s4 - s5
    [data.append('Class') for x in range(int(n_s_credits))]
    [data.append('Study') for x in range(int(n_study))]
    [data.append('Free') for x in range(int(n_free))]
    [data.append('Work') for x in range(int(n_work))]
    [data.append('Sleep') for x in range(int(week_sleep))]
    
    if s1_input == None or s1_input == '':
        [data.append('Slider_1') for x in range(int(s1))]
    else:
        [data.append(s1_input) for x in range(int(s1))]
    
    if s2_input == None or s1_input == '':
        [data.append('Slider_2') for x in range(int(s2))]
    else:
        [data.append(s2_input) for x in range(int(s2))]
    
    if s3_input == None or s1_input == '':
        [data.append('Slider_3') for x in range(int(s3))]
    else:
        [data.append(s3_input) for x in range(int(s3))]
    
    if s4_input == None or s1_input == '':
        [data.append('Slider_4') for x in range(int(s4))]
    else:
        [data.append(s4_input) for x in range(int(s4))]
    
    if s5_input == None or s1_input == '':
        [data.append('Slider_5') for x in range(int(s5))]
    else:
        [data.append(s5_input) for x in range(int(s5))]
    
    [data.append('Remaining') for x in range(int(remaining))]
    
    data = pd.DataFrame(data=data, columns=[f'Student'])
    data = data.apply(pd.Series.value_counts).T
     
    fig = px.bar(data,
                 text_auto=True, 
                 orientation='h',
                 labels={"value":"Hours in a Week"},
                 color_discrete_map = {'Sleep':'#9F0162', # Dark Purple
                                       'Study':'#009F81', # Green
                                       'Remaining':'#FFC33B', # Light Orange
                                       'Free':'#008DF9', # Dodger Blue
                                       'Work':'#8400CD', # Violet
                                       'Class':'#A40122', # Dark Red
                                       'Slider_1':'#00C2F9', s1_input:'#00C2F9', # Light Blue 
                                       'Slider_2':'#E20134', s2_input:'#E20134', # Crimson
                                       'Slider_3':'#00BDA9', s3_input:'#00BDA9', # Cyan
                                       'Slider_4':'#FFB2FD', s4_input:'#FFB2FD', # Plum
                                       'Slider_5':'#00FCCF', s5_input:'#00FCCF', # Aquamarine
                                       }, 
                # Colors from http://mkweb.bcgsc.ca/colorblind/palettes.mhtml#12-color-palette-for-colorbliness
                 
                hover_name = 'variable',
                # hover_data= ''
                )
    fig.update_layout(hovermode="closest")
    fig.add_vline(x=168, 
                  line_width = 3, 
                  line_color = "red", 
                  line_dash = "dash",
                 annotation_text = "168 Hours In A Week",
                 annotation_position="top")
    
    fig.update_yaxes(visible=False)
    
    fig.update_layout(
        legend=dict(
        yanchor="top",
        y = 0.75,
        xanchor="left",
        x = -0.1))
    
    return fig
    
############################## App Layout####################################

app.layout = dbc.Container(fluid=True, children=[
        html.H1(config.app_name),
        navbar,
        html.Br(),
        body])

# Required for deployment on Heroku
server = app.server

if __name__ == '__main__':
    app.run_server(debug=True)
