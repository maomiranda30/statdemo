import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
from dash.exceptions import PreventUpdate
import pandas as pd
import numpy as np
import statistics as stats
import plotly.express as px
import dash_bootstrap_components as dbc


########################DATOS##############################

url='https://docs.google.com/spreadsheets/d/e/2PACX-1vTB99CuC-U9_XHsKlGIrJOTDp2wQNelxnaCACW7Y1lL6ewZxB4Ejj3Fo6GW_BYggQl50BkJhbz9mX6V/pub?gid=225257226&single=true&output=csv'
df=pd.read_csv(url)

url2='https://docs.google.com/spreadsheets/d/e/2PACX-1vTRsVAq_5SGisQBZXkdJpv9DcWVLZwzyQDrmEihhd9doYYLPTKsCNFIo62Ojo9MXAeKUHr3_s26EcbB/pub?output=csv'
df2=pd.read_csv(url2)

# url3='https://docs.google.com/spreadsheets/d/e/2PACX-1vT2ZkhX_wxekZxQ-mCb3KuRWvmjOxshMZO962yYLgqzyX6ACjLevOJOCoTmXvWlR6ZX5tjLv3KMZBKz/pub?output=csv'
# df4=pd.read_csv(url3)

#######################################################

font_awesome = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
meta_tags = [{"name": "viewport", "content": "width=device-width"}]
external_stylesheets = [meta_tags, font_awesome]

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
server=app.server

app.layout=html.Div((
    html.Div([

            html.Img(src ="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABT0AAABcCAYAAACsnRFUAAAAAXNSR0IArs4c6QAAIABJREFUeF7t3XVYlVnXBvBbQcTGxkDFDsyxdezGFgtbsWvM8R0Zx9YZu0ZHscHEQsXuVuxWVGxsTFBB32stPEdQEEaBUbj3P596nvPEbz/Me303a+8VCz8New8OClCAAhSgAAUoQAEKUIACFKAABShAAQpQgALRRCAWQ89oMpN8DApQgAIUoAAFKEABClCAAhSgAAUoQAEKUEAFGHryRaAABShAAQpQgAIUoAAFKEABClCAAhSgAAWilQBDz2g1nXwYClCAAhSgAAUoQAEKUIACFKAABShAAQpQgKEn3wEKUIACFKAABShAAQpQgAIUoAAFKEABClAgWgkw9IxW08mHoQAFKEABClCAAhSgAAUoQAEKUIACFKAABRh68h2gAAUoQAEKUIACFKAABShAAQpQgAIUoAAFopUAQ89oNZ18GApQgAIUoAAFKEABClCAAhSgAAUoQAEKUIChJ98BClCAAhSgAAUoQAEKUIACFKAABShAAQpQIFoJMPSMVtPJh6EABShAAQpQgAIUoAAFKEABClCAAhSgAAUYevIdoAAFKEABClCAAhSgAAUoQAEKUIACFKAABaKVAEPPaDWdfBgKUIACFKAABShAAQpQgAIUoAAFKEABClCAoSffAQpQgAIUoAAFKEABClCAAhSgAAUoQAEKUCBaCTD0jFbTyYehAAUoQAEKUIACFKAABShAAQpQgAIUoAAFGHryHaAABShAAQpQgAIUoAAFKEABClCAAhSgAAWilQBDz2g1nXwYClCAAhSgAAUoQAEKUIACFKAABShAAQpQgKEn3wEKUIACFKAABShAAQpQgAIUoAAFKEABClAgWgkw9IxW08mHoQAFKEABClCAAhSgAAUoQAEKUIACFKAABRh68h2gAAUoQAEKUIACFKAABShAAQpQgAIUoAAFopVAjAo9TU1iI66ZCV76vtVJtEhkjuwZkuGt/ztcvP4Ir/zeIoVFfPxiXxQd6xfC81dvMMxpD1w2nMFb/wCkSZEImdIk0X8/d+0hAgLe6Xnim8eBr99bvI9WrwYfhgIUoAAFKEABClCAAhSgAAUoQAEKUIACP6ZAjAk945iaYFjnsiicKw0mLT6MtXsuY9HwerCrlAuv3/hjyKzdmLDo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"),
    ],style = { 'display': 'flex','flex-direction': 'row','white-space': 'pre'}), 


    html.Div([
        dcc.Dropdown(id = 'area',
        multi = False,
        clearable =False,
        disabled = False,
        style = {'display': True,'width':'300px'},
        value = 'PUNTAJE GLOBAL',
        placeholder = 'Seleccione área',
        options = [{'label': c, 'value': c} for c in df2['areas'].unique()]),

        html.Div([
            dcc.RangeSlider(
                id='slider', # any name you'd like to give it
                marks={
                2017: '2017',     # key=position, value=what you see
                2018: '2018',
                2019: '2019',
                2020: '2020',
                2021: '2021',
                2022: '2022',
                2023:'2023',
                2025: {'label': '2025', 'style': {'color':'#f50', 'font-weight':'bold'}},
                },
                 step=1, 
                min=2017,
                max=2025,
                value=[2017,2025],     # default value initially chosen
                dots=True,             # True, False - insert dots, only when step>1
                allowCross=True,      # True,False - Manage handle crossover
                disabled=False,        # True,False - disable handle
                pushable=1,            # any number, or True with multiple handles
                updatemode='mouseup',  # 'mouseup', 'drag' - update value method
                included=True,         # True, False - highlight handle
                vertical=False,        # True, False - vertical, horizontal slider
                verticalHeight=30,    # hight of slider (pixels) when vertical=True
                className='None',
                tooltip={'always_visible':False,  # show current slider values
                    'placement':'topRight'},
            ),

        ],style={'width':'80%'}),

        
    ],style={'width': '100%','display': 'flex'}),


    # html.Div([
    #     html.Div([
    #         html.Div(id = 'text1',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text2',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text3',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text4',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    #     html.Div([
    #         html.Div(id = 'text5',style={'border-width': '1px','border-style': 'dotted','border-color':'blue','background-color': 'white','width': '250px','height': '72px','textAlign':'center'})
    #     ],style={'display': 'flex','flex-direction': 'column','position': 'relative'}),
    # ],style={'display': 'flex','flex-wrap': 'wrap','justify-content': 'center','margin-top': '10px','gap': '10px'}),

    html.Div([
        html.Div([
            dcc.Graph(id = 'chart2',config = {'displayModeBar': False},style={'width':'475px','height':'375px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),

        html.Div([
            dcc.Graph(id = 'chart1',config = {'displayModeBar': False},style={'width':'440px','height':'375px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),


        html.Div([
            dcc.Graph(id = 'funnel_chart',config = {'displayModeBar': False},style={'width':'390px','height':'410px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),        

    ],style={'display': 'flex','flex-direction': 'row','margin-top': '10px','gap': '10px'}),
    # style={'display': 'flex','flex-direction': 'row'}
    # ,style={'background-color': '#335476','width': '480px','height': '420px','margin-top':'2px'}


        html.Div([
        html.Div([
            dcc.Graph(id = 'chart3',config = {'displayModeBar': False},style={'width':'660px','height':'375px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),


        html.Div([
            dcc.Graph(id = 'box',config = {'displayModeBar': False},style={'width':'660px','height':'410px'}),
        ],style={'border-style':'dotted','border-color':'blue'}),        

    ],style={'display': 'flex','flex-direction': 'row','margin-top': '10px','gap': '10px'}),
))



############### CALLBACKS #################################
# @app.callback(
#     Output(component_id='text1', component_property='children'),
#     Input(component_id='area', component_property='value')
# )
# def avg(choose):
#     filtro=df[df['AÑO']==2022]
#     avera=round(stats.mean(filtro[choose]),2)
#     return [            html.P('Promedio 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera]


# @app.callback(
#     Output(component_id='text2', component_property='children'),
#     Input(component_id='area', component_property='value')
# )
# def avg(choose2):
#     filtro=df[df['AÑO']==2022]
#     avera2=round(stats.stdev(filtro[choose2]),2)
#     return [html.P('Desviación 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera2]

# @app.callback(
#     Output(component_id='text3', component_property='children'),
#     Input(component_id='area', component_property='value')
# )

# def avg(choose3):
#     filtro=df[df['AÑO']==2022]
#     avera3=round(stats.median(filtro[choose3]),2)
#     return [html.P('Mediana 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera3]

# @app.callback(
#     Output(component_id='text4', component_property='children'),
#     Input(component_id='area', component_property='value')
# )

# def avg(choose4):
#     filtro=df[df['AÑO']==2022]
#     avera4=round(np.percentile(filtro[choose4],25),2)
#     return [html.P('Cuartil 1 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera4]


# @app.callback(
#     Output(component_id='text5', component_property='children'),
#     Input(component_id='area', component_property='value')
# )

# def avg(choose5):
#     filtro=df[df['AÑO']==2022]
#     avera5=round(np.percentile(filtro[choose5],75),2)
#     return [html.P('Cuartil 3 2022',
#                    style = {
#                        'color': 'Black',
#                        'fontSize': 17,
#                        'font-weight': 'bold'
#                    },
#                    className = 'card_title'
#                    ),avera5]



#######################GRÁFICAS######################3
@app.callback(
    Output(component_id='chart1', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)

def update_graph5(mao,slid):
    if mao=='MATEMATICAS':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=35),
            (df[mao]>35)&(df[mao]<=50),
            (df[mao]>50)&(df[mao]<=70),
            (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

        # fig.update_layout(width=534.5, height=440, autosize=False)

      
        
        return fig
    
    elif mao=='CIENCIAS NATURALES' or mao=='SOCIALES Y CIUDADANAS':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=40),
            (df[mao]>40)&(df[mao]<=55),
            (df[mao]>55)&(df[mao]<=70),
            (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2023.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
        # fig.update_layout(width=534.5, height=440, autosize=False)

       
         
        return fig

    elif mao=='LECTURA CRITICA':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=35),
            (df[mao]>35)&(df[mao]<=50),
            (df[mao]>50)&(df[mao]<=65),
            (df[mao]>65)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2023.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

     
        
  
        return fig


    elif mao=='INGLES':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=47),
            (df[mao]>47)&(df[mao]<=57),
            (df[mao]>57)&(df[mao]<=67),
            (df[mao]>67)&(df[mao]<=78),
            (df[mao]>78)],['A-','A1','A2','B1','B2'])
        edad=['A-','A1','A2','B1','B2']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2023.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

  
        return fig


    else :
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=221),
            (df[mao]>221)&(df[mao]<=299),
            (df[mao]>299)],['Insuficiente','Mínimo','Satisfactorio'])
        edad=['Insuficiente','Mínimo','Satisfactorio']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.line(linea3, x="AÑO", y='%', text='%',color='Nivel',range_x=[2017,2023.5],title='Puntaje por niveles')
        fig.update_traces(textposition="bottom right")
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
        return fig

#######################GRÁFICAS######################3

@app.callback(
    Output(component_id='chart2', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)
def update_graph2(mate2,slider): 
    linea=df['AÑO'].between(slider[0],slider[1],inclusive='both')
    linea15=df[linea] 
    inicial=linea15.groupby('AÑO').agg({mate2:'mean'}).reset_index()
    inicial[mate2]=round(inicial[mate2],1)
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=list(range(slider[0],(slider[1]+1))),
            y=list(inicial[mate2]),
            line=dict(width=2),
            showlegend=False,
            mode="lines+text",
            hoverinfo="none",
            text=list(inicial[mate2]),  # one for each point..
            textposition="bottom center",  # changed to make it visible on right
            textfont=dict(color="black"),
        
        )
    )   
    fig.update_layout(title=dict(text='Puntaje promedio prueba saber',font=dict(size=15)),title_x=0.5,xaxis_title='Año',yaxis_title='Puntaje',plot_bgcolor='rgba(0,0,0,0)')

  

    # fig.update_layout(width=400, height=350, autosize=True)        

    return fig

##################################################

@app.callback(
    Output(component_id='funnel_chart', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)

def update_graph(lola,slide10):

    linea=df['AÑO'].between(slide10[0],slide10[1],inclusive='both')
    linea5=df[linea]
    inicial2=linea5.groupby('AÑO').agg({lola:'std'}).reset_index()
    inicial2[lola]=round(inicial2[lola],2)
    inicial=linea5.groupby('AÑO').agg({lola:'mean'}).reset_index()
    inicial[lola]=round(inicial[lola],2)  
   

    fig = go.Figure()
    fig.add_trace(go.Bar(
    y=list(range(slide10[0],(slide10[1]+1))),
    x=list(inicial[lola]),
    text = list(inicial[lola]),
    textposition="inside",
    name='Promedio',
    orientation='h',
    marker=dict(
        color='rgba(246, 78, 139, 0.6)',
        line=dict(color='rgba(246, 78, 139, 1.0)', width=3)
    )
))
    fig.add_trace(go.Bar(
    y=list(range(slide10[0],(slide10[1]+1))),
    x=list(inicial2[lola]),
    text = list(inicial2[lola]),
    textposition="inside",
    name='Desviación',
    orientation='h',
    marker=dict(
        color='green',
        line=dict(color='green', width=3)
    ),
    
))

    fig.update_layout(barmode='stack',plot_bgcolor='rgba(0,0,0,0)',title=dict(text='Promedio y desviación historica',font=dict(size=15)),title_x=0.5)

    return fig

@app.callback(
    Output(component_id='chart3', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)

def update_graph(mao,slid):
    if mao=='MATEMATICAS':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=35),
            (df[mao]>35)&(df[mao]<=50),
            (df[mao]>50)&(df[mao]<=70),
            (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

      
        
        return fig
    
    elif mao=='CIENCIAS NATURALES' or mao=='SOCIALES Y CIUDADANAS':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=40),
            (df[mao]>40)&(df[mao]<=55),
            (df[mao]>55)&(df[mao]<=70),
            (df[mao]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
       
         
        return fig

    elif mao=='LECTURA CRITICA':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=35),
            (df[mao]>35)&(df[mao]<=50),
            (df[mao]>50)&(df[mao]<=65),
            (df[mao]>65)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  
        
  
        return fig


    elif mao=='INGLES':
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=47),
            (df[mao]>47)&(df[mao]<=57),
            (df[mao]>57)&(df[mao]<=67),
            (df[mao]>67)&(df[mao]<=78),
            (df[mao]>78)],['A-','A1','A2','B1','B2'])
        edad=['A-','A1','A2','B1','B2']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

  
        return fig


    else :
        df['Nivel']=np.select([
            (df[mao]>0)&(df[mao]<=221),
            (df[mao]>221)&(df[mao]<=299),
            (df[mao]>299)],['Insuficiente','Mínimo','Satisfactorio'])
        edad=['Insuficiente','Mínimo','Satisfactorio']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid[0],slid[1],inclusive='both')
        linea2=df[linea]    
        linea3=linea2.groupby(['AÑO','Nivel']).agg({mao:'count'}).reset_index()
        linea3['%'] = round(100 * linea3[mao] / linea3.groupby('AÑO')[mao].transform('sum'),0)
        fig = px.bar(linea3, x="AÑO", y='%', color="Nivel", text_auto=True,title='Cantidad de estudiantes por nivel')
        fig.update_layout(plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5)  

        return fig


@app.callback(
    Output(component_id='box', component_property='figure'),
    Input(component_id='area', component_property='value'),
    Input(component_id='slider', component_property='value')
)

def update_graph4(mao4,slid4):
    if mao4=='MATEMATICAS':
        df['Nivel']=np.select([
            (df[mao4]>0)&(df[mao4]<=35),
            (df[mao4]>35)&(df[mao4]<=50),
            (df[mao4]>50)&(df[mao4]<=70),
            (df[mao4]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
        linea2=df[linea]
        fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año') 
        fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
                    )
        
        return fig
    
    elif mao4=='CIENCIAS NATURALES' or mao4=='SOCIALES Y CIUDADANAS':
        df['Nivel']=np.select([
            (df[mao4]>0)&(df[mao4]<=40),
            (df[mao4]>40)&(df[mao4]<=55),
            (df[mao4]>55)&(df[mao4]<=70),
            (df[mao4]>70)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
        linea2=df[linea]
        fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año')  
        fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
                    )
        
        return fig
 


    elif mao4=='LECTURA CRITICA':
        df['Nivel']=np.select([
            (df[mao4]>0)&(df[mao4]<=35),
            (df[mao4]>35)&(df[mao4]<=50),
            (df[mao4]>50)&(df[mao4]<=65),
            (df[mao4]>65)],['Nivel 1','Nivel 2','Nivel 3','Nivel 4'])
        edad=['Nivel 1','Nivel 2','Nivel 3','Nivel 4']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
        linea2=df[linea]
        fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año')  
        fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
                    )       
        return fig


    elif mao4=='INGLES':
        df['Nivel']=np.select([
            (df[mao4]>0)&(df[mao4]<=47),
            (df[mao4]>47)&(df[mao4]<=57),
            (df[mao4]>57)&(df[mao4]<=67),
            (df[mao4]>67)&(df[mao4]<=78),
            (df[mao4]>78)],['A-','A1','A2','B1','B2'])
        edad=['A-','A1','A2','B1','B2']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
        linea2=df[linea]
        fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año') 
        fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
                    )   
        return fig

    else :
        df['Nivel']=np.select([
            (df[mao4]>0)&(df[mao4]<=221),
            (df[mao4]>221)&(df[mao4]<=299),
            (df[mao4]>299)],['Insuficiente','Mínimo','Satisfactorio'])
        edad=['Insuficiente','Mínimo','Satisfactorio']
        df['Nivel']= pd.Categorical(df['Nivel'], edad)
        linea=df['AÑO'].between(slid4[0],slid4[1],inclusive='both')
        linea2=df[linea]
        fig = px.box(linea2, x="AÑO", y=mao4,title='Box-Plot de valoración por año') 
        fig.update_layout(
                        plot_bgcolor='rgba(0,0,0,0)',title=dict(font=dict(size=15)),title_x=0.5
                    )          
        return fig
##################################################################


############################


if __name__ == "__main__":
    app.run_server(debug = True)

