import dash
from dash import dcc, html, Input, Output, callback
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
import io
import base64

# Registrar la página en la aplicación Dash
dash.register_page(
    __name__,
    path='/edo7',  # Ruta para acceder a esta página
    name='Edo-7'   # Nombre que se mostrará en el menú de navegación
)

# Función que calcula los resultados y genera la gráfica
def calcular_y_graficar():
    # Definimos las variables simbólicas
    x, y = sp.symbols('x y')

    # Definimos las ecuaciones diferenciales del sistema
    x_prima = x*(5-y)
    y_prima = y*(5-x)

    #x_prima = x * (5 - (5/8) * x - y)
    #y_prima = y * (5 - (5/8) * y - x)

    # Calculamos los puntos de equilibrio resolviendo las ecuaciones
    puntos_equilibrio = sp.solve([x_prima, y_prima], (x, y))

    # Creamos la matriz Jacobiana del sistema
    Jacobiano = sp.Matrix([
        [sp.diff(x_prima, x), sp.diff(x_prima, y)],
        [sp.diff(y_prima, x), sp.diff(y_prima, y)]
    ])

    # Evaluamos el Jacobiano en cada punto de equilibrio y hallamos los autovalores
    resultados = []
    for punto in puntos_equilibrio:
        Evaluar_Jacobiano = Jacobiano.subs({x: punto[0], y: punto[1]})  # Sustituimos el punto en el Jacobiano
        autovalores = Evaluar_Jacobiano.eigenvals()  # Calculamos los autovalores
        resultados.append({
            'punto': punto,
            'Jacobiano': Evaluar_Jacobiano,
            'autovalores': autovalores
        })

    # Graficamos el campo de vectores del sistema
    X, Y = np.mgrid[-1:10:100j, -1:10:100j]  # Creamos una malla para los ejes x e y
    U = X*(5-Y) # Definimos la componente x del campo de vectores
    V = Y*(5-X)  # Definimos la componente y del campo de vectores

    #U = X * (5 - (5/8) * X - Y)  # Definimos la componente x del campo de vectores
    #V = Y * (5 - (5/8) * Y - X)  # Definimos la componente y del campo de vectores
    
    fig, ax = plt.subplots()  # Creamos una figura y un eje para la gráfica
    ax.streamplot(Y, X, V, U, color='blue')  # Dibujamos el campo de vectores
    
    # Añadimos los puntos de equilibrio a la gráfica
    for punto in puntos_equilibrio:
        ax.plot(float(punto[0]), float(punto[1]), 'o', color='red')

    ax.set_title('Campo de vectores del sistema 1')  # Título de la gráfica
    ax.set_xlabel('x')  # Etiqueta del eje x
    ax.set_ylabel('y')  # Etiqueta del eje y

    # Convertimos la gráfica a formato base64 para que sea legible por Dash
    buf = io.BytesIO()  # Creamos un buffer en memoria
    plt.savefig(buf, format='png')  # Guardamos la figura en el buffer
    buf.seek(0)  # Volvemos al inicio del buffer
    img_str = base64.b64encode(buf.read()).decode('utf-8')  # Codificamos la imagen a base64
    plt.close(fig)  # Cerramos la figura

    return resultados, f"data:image/png;base64,{img_str}", puntos_equilibrio, Jacobiano  # Retornamos los resultados

# Layout de la página
layout = html.Div(className='Pages', children=[
    html.H2('Modelo de Ecuaciones Diferenciales'),  # Título de la página
    
    html.Button("Calcular", id='calcular-button', n_clicks=0),  # Botón para calcular
    
    html.Div(id='resultados', style={'margin-top': '20px'}),  # Div para mostrar resultados
    
    html.Img(id='grafica', style={'width': '100%', 'height': 'auto', 'margin-top': '20px'})  # Imagen para la gráfica
])

# Callback para actualizar los resultados y la gráfica
@callback(
    Output('resultados', 'children'),  # Salida para los resultados
    Output('grafica', 'src'),  # Salida para la imagen
    Input('calcular-button', 'n_clicks')  # Entrada que detecta los clics en el botón
)
def actualizar_resultados(n_clicks):
    if n_clicks > 0:  # Solo se ejecuta si el botón ha sido clicado
        resultados, img_src, puntos_equilibrio, Jacobiano = calcular_y_graficar()  # Llamamos a la función de cálculo
        
        # Formateo de resultados
        resultados_texto = []

        # Mostrar puntos de equilibrio
        resultados_texto.append(html.Div(f"Los puntos de equilibrio son: {puntos_equilibrio}"))
        resultados_texto.append(html.Div("#########################################"))
        
        # Mostrar Jacobiano
        jacobiano_str = str(Jacobiano).replace('Matrix', '').replace('[', '').replace(']', '')
        jacobiano_lines = jacobiano_str.split('], ')  # Separamos las líneas de la matriz
        jacobiano_pretty = '\n'.join(['[ ' + line.strip() + ' ]' for line in jacobiano_lines])  # Formato vertical
        resultados_texto.append(html.Pre(f"Esta es la Matriz Jacobiano:\n{jacobiano_pretty}", style={'white-space': 'pre-wrap'}))
        resultados_texto.append(html.Div("##########################################"))

        # Evaluar resultados en puntos de equilibrio
        for res in resultados:
            resultados_texto.append(html.Div(f"Evaluado en el punto: {res['punto']}"))
            jacobiano_evaluado_str = str(res['Jacobiano']).replace('Matrix', '').replace('[', '').replace(']', '')
            jacobiano_evaluado_lines = jacobiano_evaluado_str.split('], ')
            jacobiano_evaluado_pretty = '\n'.join(['[ ' + line.strip() + ' ]' for line in jacobiano_evaluado_lines])  # Formato vertical
            resultados_texto.append(html.Pre(f"Jacobiano evaluado:\n{jacobiano_evaluado_pretty}", style={'white-space': 'pre-wrap'}))
            resultados_texto.append(html.Div(f"Autovalores: {res['autovalores']}"))  # Mostramos los autovalores
            resultados_texto.append(html.Div("#######################################"))

        return resultados_texto, img_src  # Retornamos los resultados y la imagen
    return '', ''  # Retorno vacío si no se ha clicado el botón