import dash
from dash import dcc, html, Input, Output, callback
from utils import modelo_lotka_volterra

# Registrar página
dash.register_page(
    __name__,
    path='/edo6',
    name='Edo-6'
)

# Layout de la página
layout = html.Div(className='Pages', children=[

    html.Div(className='div_parametros', children=[

        html.H2('PARÁMETROS'),

        # Sección de parámetros
        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Tasa de Crecimiento (alpha)'),
                dcc.Input(type='number', value=0.1, id='alpha')
            ]),
            html.Div([
                html.H3('Tasa de Depredación (beta)'),
                dcc.Input(type='number', value=0.02, id='beta')
            ]),
        ], style={'display': 'flex', 'align-items': 'center', 'gap': '95px'}),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Tasa de Crecimiento Depredador (delta)'),
                dcc.Input(type='number', value=0.01, id='delta')
            ]),
            html.Div([
                html.H3('Tasa de Mortalidad Depredador (gamma)'),
                dcc.Input(type='number', value=0.1, id='gamma')
            ]),
        ], style={'display': 'flex', 'align-items': 'center', 'gap': '95px'}),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Población Inicial de Presas (x0)'),
                dcc.Input(type='number', value=40, id='x0')
            ]),
            html.Div([
                html.H3('Población Inicial de Depredadores (y0)'),
                dcc.Input(type='number', value=9, id='y0')
            ]),
        ], style={'display': 'flex', 'align-items': 'center', 'gap': '95px'}),

        html.Div([
            html.H3('Tiempo Total (días)'),
            dcc.Input(type='number', value=200, id='tiempo_total')
        ]),
    ]),

    # Contenedor para la gráfica
    html.Div(className='div_grafica', children=[
        html.H2('GRÁFICA DEL MODELO LOTKA-VOLTERRA'),
        dcc.Loading(
            type='default',
            children=dcc.Graph(id='figure_lv')
        )
    ])
])

# Callback para actualizar la gráfica
@callback(
    Output('figure_lv', 'figure'),
    Input('alpha', 'value'),
    Input('beta', 'value'),
    Input('delta', 'value'),
    Input('gamma', 'value'),
    Input('x0', 'value'),
    Input('y0', 'value'),
    Input('tiempo_total', 'value')
)
def grafica_lv(alpha, beta, delta, gamma, x0, y0, t):
    fig = modelo_lotka_volterra(alpha, beta, delta, gamma, x0, y0, t, 100)
    return fig