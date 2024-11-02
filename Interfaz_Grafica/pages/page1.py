###################################################################################
#
# Librerías de la ley
#
###################################################################################
import dash
from dash import dcc, html, Input, Output, callback
from utils import ley_enfriamiento_newton

dash.register_page(
    __name__,
    path='/',
    name='Edo-1'
)

###################################################################################
#
# Layout HTML de la ley
#
###################################################################################

layout = html.Div(className='Pages', children=[

    html.Div(className='div_parametros', children=[

        html.H2('PARÁMETROS'),

        html.Div(className='div_flex', children=[
            html.Div([
                html.H3('Temperatura Inicial'),
                dcc.Input(type='number', value=95, id='Temp_ini')
            ]),
            html.Div([
                html.H3('Tiempo Inicial'),
                dcc.Input(type='number', value=0, id='time_ini')
            ]),
            html.Div([
                html.H3('Tiempo Final'),
                dcc.Input(type='number', value=20, id='time_fin')
            ]),
        ]),

        html.H3('Tasa de Enfriamiento'),
        dcc.Input(max=2, type='number', value=-0.05, id='k'),

        html.H3('Temperatura Ambiente'),
        dcc.Input(type='number', value=21, id='Ta'),

        html.H3('Malla para el Campo de Vectores'),
        dcc.Slider(min=1, max=40, step=1, value=15, marks=None, tooltip={'placement':'bottom', 'always_visible':True}, id='mallado'),

        html.H3('Tamaño del Vector'),
        dcc.Slider(min=0.1, max=2, step=0.1, value=1, id='size_vec'),

        html.H3('Mostrar Campo de Vectores'),  # Etiqueta para el botón que activa/desactiva el campo de vectores
        dcc.Checklist(
            options=[{'label': 'Activar Campo de Vectores', 'value': 'show_field'}],  # Texto para el checkbox
            value=['show_field'],  # Activado por defecto
            id='toggle_vectors'
        )
    ]),

    html.Div(className='div_grafica', children=[
        html.H2('GRÁFICA DE LA LEY DE ENFRIAMIENTO DE NEWTON'),
        dcc.Loading(
            type='default',
            children=dcc.Graph(id='figura_2')
        )
    ])

])


###################################################################################
#
# Callback
#
###################################################################################

@callback(
    Output('figura_2', 'figure'),
    Input('Temp_ini', 'value'),
    Input('time_ini', 'value'),
    Input('time_fin', 'value'),
    Input('k', 'value'),
    Input('Ta', 'value'),
    Input('mallado', 'value'),
    Input('size_vec', 'value'),
    Input('toggle_vectors', 'value')
)

def grafica_edo1(T0, t_i, t_f, k, Ta, mallado, size_vec, toggle_vectors):

    # Verificar si el campo de vectores debe mostrarse o no
    show_field = 'show_field' in toggle_vectors

    fig = ley_enfriamiento_newton(Ta, T0, k, t_i, t_f, mallado, size_vec, show_field)
    return fig