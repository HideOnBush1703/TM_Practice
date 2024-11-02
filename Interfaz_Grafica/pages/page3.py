###################################################################################
#
# Librerías
#
###################################################################################
import dash  # Importa la biblioteca principal de Dash para construir la aplicación web
from dash import dcc, html, Input, Output, callback  # Importa componentes esenciales de Dash
from utils import modelo_decaimiento_radioactivo  # Importa la función ecuacion_logistica desde un módulo utils personalizado

# Registra una página en la aplicación Dash con el nombre 'Edo-2' y la ruta '/edo2'
dash.register_page(
    __name__,
    path='/edo3',
    name='Edo-3'
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
                html.H3('Cantidad Inicial de Núcleos'),  # Etiqueta para el input de cantidad inicial
                dcc.Input(type='number', value=100, id='nuc_ini')  # Input para la cantidad inicial con valor predeterminado de 100
            ]),
            html.Div([
                html.H3('Tiempo Inicial'),  # Etiqueta para el input de tiempo inicial
                dcc.Input(type='number', value=0, id='time_ini')  # Input para el tiempo inicial con valor predeterminado de 0
            ]),
            html.Div([
                html.H3('Tiempo Final'),  # Etiqueta para el input de tiempo final
                dcc.Input(type='number', value=60, id='time_fin')  # Input para el tiempo final con valor predeterminado de 60
            ]),
        ]),

        html.H3('Constante de Decaimiento'),  # Etiqueta para el input de la constante de decaimiento
        dcc.Input(max=5, type='number', value=0.1, id='lambda'),  # Input para la constante de decaimiento con valor predeterminado de 0.1

        html.H3('Malla para el Campo de Vectores'),  # Etiqueta para el slider de mallado
        dcc.Slider(min=1, max=40, step=1, value=15, marks=None, tooltip={'placement': 'bottom', 'always_visible': True}, id='mallado'),  # Slider para el mallado con rango de 1 a 40 y valor predeterminado de 15

        html.H3('Tamaño del Vector'),  # Etiqueta para el slider del tamaño del vector
        dcc.Slider(min=0.1, max=2, step=0.1, value=1, id='size_vec'),  # Slider para el tamaño del vector con rango de 0.1 a 2 y valor predeterminado de 1
        
        html.H3('Mostrar Campo de Vectores'),  # Etiqueta para el botón que activa/desactiva el campo de vectores
        dcc.Checklist(
            options=[{'label': 'Activar Campo de Vectores', 'value': 'show_field'}],  # Texto para el checkbox
            value=['show_field'],  # Activado por defecto
            id='toggle_vectors'
        )

    ]),

    # Contenedor para la gráfica
    html.Div(className='div_grafica', children=[
        html.H2('GRÁFICA DEL MODELO DE DECAIMIENTO RADIOACTIVO'),  # Título para la sección de la gráfica
        dcc.Loading(  # Componente de carga para mostrar mientras se renderiza la gráfica
            type='default',
            children=dcc.Graph(id='figura_3')  # Componente gráfico que mostrará la gráfica
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
    Output('figura_3', 'figure'),  # Salida del callback es la figura de la gráfica
    Input('nuc_ini', 'value'),  # Entrada: valor de la cantidad inicial de núcleos
    Input('time_ini', 'value'),  # Entrada: valor del tiempo inicial
    Input('time_fin', 'value'),  # Entrada: valor del tiempo final
    Input('lambda', 'value'),  # Entrada: valor de la constante de decaimiento
    Input('mallado', 'value'),  # Entrada: valor del mallado para el campo de vectores
    Input('size_vec', 'value'),  # Entrada: valor del tamaño del vector
    Input('toggle_vectors', 'value') 
)
def grafica_edo1(N0, t_i, t_f, lambda_, mallado, size_vec,toggle_vectors):
    # Verificar si el campo de vectores debe mostrarse o no
    show_field = 'show_field' in toggle_vectors

    # Llama a la función modelo_decaimiento_radioactivo para generar la gráfica basada en los parámetros de entrada
    fig = modelo_decaimiento_radioactivo(N0, lambda_, t_i, t_f, mallado, size_vec, show_field)
    return fig  # Devuelve la figura para ser mostrada en el componente gráfico