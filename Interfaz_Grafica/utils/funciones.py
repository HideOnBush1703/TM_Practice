# Librerias
import numpy as np 
import plotly.graph_objects as go # Grafica
import plotly.figure_factory as ff # mallado de vectores


# Funciones

def ley_enfriamiento_newton(Ta: float, T0: float, k: float, t0: float, t: float, cant: float, scale: float, show_field: bool):
    """
    Retorna una gráfica de la ley de enfriamiento de Newton con su campo vectorial opcionalmente.

    Parámetros:
    -------
    - Ta: temperatura del ambiente.
    - T0: temperatura inicial.
    - k: tasa de enfriamiento.
    - t0: Tiempo inicial.
    - t: Tiempo final.
    - cant: Las particiones para el eje temporal y espacial.
    - scale: Tamaño del vector del campo vectorial.
    - show_field: Booleano para mostrar o no el campo de vectores.
    """

    # Rango de T y t
    T_values = np.linspace(0, T0, cant)  # Va desde 0 hasta T0
    t_values = np.linspace(0, t, cant)

    # Crear una malla de puntos (T, t)
    ti, T = np.meshgrid(t_values, T_values)

    # Definir la EDO
    dT_dt = k * (T - Ta)

    # Solución exacta de la ley de enfriamiento de Newton
    funcion = (T0 - Ta) * np.exp(k * t_values) + Ta

    # Crear la figura para la gráfica
    fig = go.Figure()

    # Condicional para mostrar el campo de vectores
    if show_field:
        # Campo vectorial: dT/dt (componente vertical)
        U = np.ones_like(ti)  # Componente en t (horizontal)
        V = dT_dt             # Componente en T (vertical)

        # Añadir el campo de vectores
        fig = ff.create_quiver(
            ti, T, U, V,
            scale=scale,
            line=dict(color='black', width=1),
            showlegend=False
        )

    # Añadir la función de la ley de enfriamiento
    fig.add_trace(
        go.Scatter(
            x=t_values,
            y=funcion,
            line=dict(color='blue'),
            name='Ley de enfriamiento de Newton'
        )
    )

    # Añadir la línea de la temperatura ambiente
    fig.add_trace(
        go.Scatter(
            x=[0, t],
            y=[Ta, Ta],
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Temperatura Ambiente'
        )
    )

    # Etiquetas para la gráfica
    fig.update_layout(
        title={
            'text': 'Campo de vectores de dT/dt = k(T-Ta)',
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center'
        },
        xaxis_title='Tiempo (t)',
        yaxis_title='Temperatura (T)',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    # Añadir contorno a la gráfica
    fig.update_xaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )

    return fig

def ecuacion_logistica(K: float, P0: float, r: float, t0: float, t: float, cant: float, scale: float, show_field: bool):
    """
    Retorna una gráfica de la ecuacion logistica con su campo vectorial opcionalmente.

    Parámetros:
    -------
    - K: Capacidad de carga.
    - P0: Poblacion Inicial.
    - r: Tasa de crecimineto poblacional.
    - t0: Tiempo inicial.
    - t: Tiempo final.
    - cant: Las particiones para el eje temporal y espacial.
    - scale: Tamaño del vector del campo vectorial.
    - show_field: Booleano para mostrar o no el campo de vectores.
    """

    # Rango de P y t
    P_values = np.linspace(0, K+5, cant)
    t_values = np.linspace(0, t, cant)

    # Crear una malla de puntos (P, t)
    T, P = np.meshgrid(t_values, P_values)

    # Definir la EDO
    dP_dt = r * P * (1 - P / K)

    # Solución exacta de la Ecuación Logística
    funcion = K*P0*np.exp(r*t_values) / (P0*np.exp(r*t_values) + (K-P0)*np.exp(r*t0))

    # Crear la figura para la gráfica
    fig = go.Figure()

    # Condicional para mostrar el campo de vectores
    if show_field:
        # Campo vectorial: dP/dt (componente vertical)
        U = np.ones_like(T)  # Componente en t (horizontal)
        V = dP_dt           # Componente en P (vertical)

        # Añadir el campo de vectores
        fig = ff.create_quiver(
            T, P, U, V,
            scale=scale,
            line=dict(color='black', width=1),
            showlegend=False
        )

    # Añadir la función logística
    fig.add_trace(
        go.Scatter(
            x=t_values,
            y=funcion,
            line=dict(color='blue'),
            name='Ecuación Logística'
        )
    )

    # Añadir la línea de capacidad de carga
    fig.add_trace(
        go.Scatter(
            x=[0, t],
            y=[K, K],
            mode='lines',
            line=dict(color='red', dash='dash'),
            name='Capacidad de carga'
        )
    )

    # Etiquetas para la gráfica
    fig.update_layout(
        title={
            'text': 'Campo de vectores de dP/dt = rP(1 - P/K)',
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center'
        },
        xaxis_title='Tiempo (t)',
        yaxis_title='Población (P)',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    # Añadir contorno a la gráfica
    fig.update_xaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )

    return fig

# Función para el modelo de decaimiento radioactivo
def modelo_decaimiento_radioactivo(N0: float, k: float, t0: float, t: float, cant: int, scale: float, show_field: bool):
    """
    Retorna una gráfica del modelo de decaimiento radioactivo con su campo vectorial (opcional).

    Parámetros:
    -------
    - N0: Número de núcleos inicial.
    - k: Tasa de desintegración.
    - t0: Tiempo inicial.
    - t: Tiempo final.
    - cant: Las particiones para el eje temporal y espacial.
    - scale: Tamaño del vector del campo vectorial.
    - show_field: Bool que indica si se debe mostrar el campo de vectores.
    """

    # Rango de N y t
    N_values = np.linspace(0, N0, cant)
    t_values = np.linspace(t0, t, cant)

    # Crear una malla de puntos (N, t)
    T, N = np.meshgrid(t_values, N_values)

    # Definir la EDO
    dN_dt = -k * N

    # Solución exacta del modelo de decaimiento radioactivo
    funcion = N0 * np.exp(-k * t_values)

    # Crear la figura para la gráfica
    fig = go.Figure()

    # Añadir el campo vectorial solo si show_field es True
    if show_field:
        # Campo vectorial: dN/dt (componente vertical)
        U = np.ones_like(T)  # Componente en t (horizontal)
        V = dN_dt           # Componente en N (vertical)

        # Crear el campo de vectores con Plotly
        fig = ff.create_quiver(
            T, N, U, V,
            scale=scale,
            line=dict(color='black', width=1),
            showlegend=False
        )
   
    # Crear la función del modelo de decaimiento radioactivo
    fig.add_trace(
        go.Scatter(
            x=t_values,
            y=funcion,
            line=dict(color='blue'),
            name='Modelo de Decaimiento Radioactivo'
        )
    )

    # Etiquetas para la gráfica
    fig.update_layout(
        title={
            'text': 'Campo de vectores de dN/dt = -kN' if show_field else 'Decaimiento Radioactivo',
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center'
        },
        xaxis_title='Tiempo (t)',
        yaxis_title='Número de Núcleos (N)',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    # Contorno a la gráfica
    fig.update_xaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )

    return fig

# Función para el modelo de crecimiento exponencial
def modelo_crecimiento_exponencial(N0: float, r: float, t0: float, t: float, cant: int, scale: float, show_field: bool):
    """
    Retorna una gráfica del modelo de crecimiento exponencial con su campo vectorial (opcional).

    Parámetros:
    -------
    - N0: Población inicial.
    - r: Tasa de crecimiento exponencial.
    - t0: Tiempo inicial.
    - t: Tiempo final.
    - cant: Cantidad de particiones para el eje temporal y espacial.
    - scale: Tamaño del vector del campo vectorial.
    - show_field: Bool que indica si se debe mostrar el campo de vectores.
    """

    # Rango de N y t (se aumenta la densidad para mejor visualización y hover en más puntos)
    N_values = np.linspace(0, N0 * 2, cant)
    t_values = np.linspace(t0, t, cant)

    # Crear una malla de puntos (N, t)
    T, N = np.meshgrid(t_values, N_values)

    # Definir la EDO: dN/dt = r * N
    dN_dt = r * N

    # Solución exacta del modelo de crecimiento exponencial
    funcion = N0 * np.exp(r * t_values)

    # Crear la figura para la gráfica
    fig = go.Figure()

    # Añadir el campo vectorial solo si show_field es True
    if show_field:
        # Campo vectorial: dN/dt (componente vertical)
        U = np.ones_like(T)  # Componente en t (horizontal)
        V = dN_dt  # Componente en N (vertical)

        # Escalar los vectores para que se ajusten a la escala del gráfico y se visualicen bien
        fig = ff.create_quiver(
            T, N, U, V,
            scale=scale,
            line=dict(color='black', width=1),
            showlegend=False
        )

    # Crear la función de crecimiento exponencial (la solución exacta)
    fig.add_trace(
        go.Scatter(
            x=t_values,
            y=funcion,
            line=dict(color='blue'),
            name='Crecimiento Exponencial',
        )
    )

    # Etiquetas para la gráfica
    fig.update_layout(
        title={
            'text': 'Campo de vectores de dN/dt = rN' if show_field else 'Crecimiento Exponencial',
            'x': 0.5,
            'y': 0.92,
            'xanchor': 'center'
        },
        xaxis_title='Tiempo (t)',
        yaxis_title='Población (N)',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    # Ajustar los límites de los ejes para que solo muestre desde 0 en adelante
    fig.update_xaxes(
        range=[0, t],  # Limitar el eje x a partir de 0 hasta t final
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )

    return fig

# Función para el modelo SIR cambiante
def modelo_SIR_cambiante(N: float, I0: float, R0: float, t: int, beta: float, gamma: float, cant: int):
    """
    Retorna una gráfica del modelo SIR.

    Parámetros:
    -------
    - N: Población total.
    - I0: Infectados iniciales.
    - R0: Recuperados iniciales.
    - t: Tiempo total de simulación.
    - beta: Tasa de transmisión.
    - gamma: Tasa de recuperación.
    - cant: Cantidad de particiones para el eje temporal.
    """

    # Generar el rango de tiempo
    t_values = np.linspace(0, t, cant)

    # Inicialización de las listas de S, I, R
    S = np.zeros(cant)
    I = np.zeros(cant)
    R = np.zeros(cant)

    # Condiciones iniciales
    S[0] = N - I0 - R0  # Susceptibles
    I[0] = I0  # Infectados
    R[0] = R0  # Recuperados

    # Solución numérica del modelo SIR
    for i in range(1, cant):
        S[i] = S[i-1] - (beta * S[i-1] * I[i-1]) / N  # Cambios en S
        I[i] = I[i-1] + (beta * S[i-1] * I[i-1]) / N - gamma * I[i-1]  # Cambios en I
        R[i] = R[i-1] + gamma * I[i-1]  # Cambios en R

    # Crear la figura para la gráfica
    fig = go.Figure()

    # Añadir las trazas para S, I y R
    fig.add_trace(go.Scatter(x=t_values, y=S, mode='lines', name='Susceptibles', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=t_values, y=I, mode='lines', name='Infectados', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=t_values, y=R, mode='lines', name='Recuperados', line=dict(color='blue')))

    # Etiquetas para la gráfica
    fig.update_layout(
        title='Modelo SIR: Dinámica de Población',
        xaxis_title='Tiempo (t)',
        yaxis_title='Número de Individuos',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    # Ajustar los límites de los ejes para que solo muestre desde 0 en adelante
    fig.update_xaxes(
        range=[0, t],  # Limitar el eje x a partir de 0 hasta t final
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )
    fig.update_yaxes(
        mirror=True,
        showline=True,
        linecolor='green',
        gridcolor='gray',
        showgrid=False
    )

    return fig

# Función para el modelo Lotka-Volterra
def modelo_lotka_volterra(alpha: float, beta: float, delta: float, gamma: float, x0: float, y0: float, t: int, cant: int):
    """
    Retorna una gráfica interactiva del modelo Lotka-Volterra.

    Parámetros:
    -------
    - alpha: Tasa de crecimiento de presas.
    - beta: Tasa de depredación.
    - delta: Tasa de crecimiento de depredadores.
    - gamma: Tasa de mortalidad de depredadores.
    - x0: Población inicial de presas.
    - y0: Población inicial de depredadores.
    - t: Tiempo total de simulación.
    - cant: Cantidad de puntos en el eje temporal.
    """

    # Generar el rango de tiempo
    t_values = np.linspace(0, t, cant)

    # Inicialización de las listas de x (presas) y y (depredadores)
    x = np.zeros(cant)
    y = np.zeros(cant)

    # Condiciones iniciales
    x[0] = x0
    y[0] = y0

    # Solución numérica del modelo Lotka-Volterra
    for i in range(1, cant):
        x[i] = x[i-1] + (alpha * x[i-1] - beta * x[i-1] * y[i-1])
        y[i] = y[i-1] + (delta * x[i-1] * y[i-1] - gamma * y[i-1])

    # Crear la figura para la gráfica
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=t_values, y=x, mode='lines', name='Presas', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=t_values, y=y, mode='lines', name='Depredadores', line=dict(color='red')))

    fig.update_layout(
        title='Modelo Lotka-Volterra',
        xaxis_title='Tiempo (t)',
        yaxis_title='Población',
        width=800,
        template='plotly_white',
        margin=dict(l=10, r=10, t=90, b=0),
        legend=dict(orientation='h', y=1.1)
    )

    return fig