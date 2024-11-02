from dash import Dash, html, dcc
import dash


app = Dash(
    __name__,
    use_pages=True,
    suppress_callback_exceptions=True
)


app.layout = html.Div(children=[
    # Crear un contenedor para el encabezado
    html.Div(className='header', children=[
        html.Img(className='sm_logo', src='assets/imgs/UNMSM.png'),  # Incluir una imagen en el encabezado
        html.H1('Técnicas de Modelamiento', className='main_title'),  # Título principal de la aplicación
        # Agregar un contenedor para el nombre y el código
        html.Div(children=[
            html.H3('Carlos Josué Pariguana Angulo', className='name'),
            html.H4('Código: 21140100', className='code')
        ], className='name_code')
    ]),

    html.Div(className='contenedor_navegacion', children=[

        dcc.Link(html.Button('Ley de Enfriamiento de Newton', className='boton edo_1'), href='/'),
        dcc.Link(html.Button('Modelo de Crecimiento Logístico', className='boton edo_2'), href='/edo2'),
        dcc.Link(html.Button('Modelo de Decaimiento Radioactivo', className='boton edo_3'), href='/edo3'),
        dcc.Link(html.Button('Ecuación de Crecimiento Exponencial', className='boton edo_4'), href='/edo4'),
        dcc.Link(html.Button('Modelo SIR', className='boton edo_5'), href='/edo5'),  # Cuarto intento para el botón del modelo SIR.
        dcc.Link(html.Button('Modelo de Lotka-Volterra', className='boton edo_6'), href='/edo6'),  # Segundo intento del boton de L-V
        dcc.Link(html.Button('Otro Modelo', className='boton edo_7'), href='/edo7') #tercer intento para el botón que haremos ws
    ]),

    dash.page_container

])


if __name__ == '__main__':
    app.run(debug=True, port='1256')
