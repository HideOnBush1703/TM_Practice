###################################################################################
#
# Librerías
#
###################################################################################
import dash  # Importa la biblioteca principal de Dash para construir la aplicación web
from dash import dcc, html, Input, Output, callback  # Importa componentes esenciales de Dash
from utils import modelo_SIR_cambiante   # Importa la función modelo_SIR_cambiante desde un módulo utils personalizado

# Registra una página en la aplicación Dash con el nombre 'Edo-5' y la ruta '/edo5'
dash.register_page(
    __name__,
    path='/edo5',
    name='Edo-5'
)

###################################################################################
#
# Layout HTML
#
###################################################################################
# Define el layout de la página usando componentes HTML y de Dash
layout = html.Div(className='Pages', children=[

    # Contenedor para los parámetros de entrada
    html.Div(className='div_parametros', children=[

        html.H2('PARÁMETROS'),  # Título para la sección de parámetros

        # Contenedor flexible para organizar los parámetros de entrada
        html.Div(className='div_flex', children=[
            html.Div([ 
                html.H3('Población Total (N)'),  
                dcc.Input(type='number', value=1000, id='poblacion_total')  
            ]),
            html.Div([ 
                html.H3('Tasa de Transmisión (beta)'),  
                dcc.Input(type='number', value=0.3, id='beta')  
            ]),    
        ], style={'display': 'flex', 'align-items': 'center', 'gap': '95px'}),  # Espacio entre elementos

        # Otra fila para los parámetros
        html.Div(className='div_flex', children=[
            html.Div([ 
                html.H3('Infectados Iniciales (I0)'),  
                dcc.Input(type='number', value=1, id='infectados_ini')  
            ]),
            html.Div([ 
                html.H3('Tasa de Recuperación (gamma)'),  
                dcc.Input(type='number', value=0.1, id='gamma')  
            ]),
        ], style={'display': 'flex', 'align-items': 'center', 'gap': '75px'}),  # Espacio entre elementos,

        # Otra fila para los parámetros 
        html.Div(className='div_flex', children=[
            html.Div([ 
                html.H3('Recuperados Iniciales (R0)'),  
                dcc.Input(type='number', value=0, id='recuperados_ini')  
            ]),
             html.Div([ 
                html.H3('Tiempo Total (días)'),  
                dcc.Input(type='number', value=160, id='tiempo_total')  
            ]),
        ], style={'display': 'flex', 'align-items': 'center', 'gap': '48px'}),  # Espacio entre elementos,
    ]),  

    # Contenedor para la gráfica
    html.Div(className='div_grafica', children=[  
        html.H2('GRÁFICA DEL MODELO SIR'),  
        dcc.Loading(  
            type='default',  
            children=dcc.Graph(id='figure_sir')  
        )
    ])
])

###################################################################################
#
# Callback
#
###################################################################################

# Define un callback para actualizar la gráfica basado en las entradas del usuario
@callback(
    Output('figure_sir', 'figure'),  
    Input('poblacion_total', 'value'),  
    Input('infectados_ini', 'value'),  
    Input('recuperados_ini', 'value'),  
    Input('tiempo_total', 'value'),  
    Input('beta', 'value'),  
    Input('gamma', 'value')  
)
def grafica_sir(N, I0, R0, t, beta, gamma):
    # Llama a la función modelo_SIR_cambiante para generar la gráfica basada en los parámetros de entrada
    fig = modelo_SIR_cambiante(N, I0, R0, t, beta, gamma, 90)  # Usar 100 como cantidad de particiones
    
    return fig  # Devuelve la figura para ser mostrada en el componente gráfico.