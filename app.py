import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

st.set_page_config(page_title="Dashboard Financiero de AAPL", layout="wide")

@st.cache_data
def cargar_datos():
    df = pd.read_csv('data/AAPL_limpio.csv', index_col='Date', parse_dates=True)
    df['Retorno_Diario'] = df['Close'].pct_change()
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    df.dropna(inplace=True)
    return df

df = cargar_datos()

st.sidebar.header("Filtros")

fecha_inicio_input = st.sidebar.date_input(
    "Fecha de Inicio",
    value=df.index.min().date(), # Usamos .date() para pasar un objeto 'date'
    min_value=df.index.min().date(),
    max_value=df.index.max().date()
)

fecha_fin_input = st.sidebar.date_input(
    "Fecha de Fin",
    value=df.index.max().date(), # Usamos .date() para pasar un objeto 'date'
    min_value=df.index.min().date(),
    max_value=df.index.max().date()
)

fecha_inicio = pd.Timestamp(fecha_inicio_input).tz_localize('UTC')
fecha_fin = pd.Timestamp(fecha_fin_input).tz_localize('UTC')


if fecha_inicio < fecha_fin:
    df_filtrado = df.loc[fecha_inicio:fecha_fin]
else:
    st.sidebar.error("Error: La fecha de fin debe ser posterior a la fecha de inicio.")
    df_filtrado = df.copy() # Usamos .copy() para evitar advertencias


st.title("Dashboard de Análisis Financiero")
st.header("Análisis de la acción de Apple (AAPL)")
st.write(f"Mostrando datos desde **{fecha_inicio.strftime('%d-%m-%Y')}** hasta **{fecha_fin.strftime('%d-%m-%Y')}**")
st.write("---")

st.subheader("Evolución del Precio y Medias Móviles")
fig_precio = px.line(df_filtrado[['Close', 'SMA_50', 'SMA_200']],
                     labels={'value': 'Precio (USD)', 'Date': 'Fecha'},
                     template='plotly_dark')
fig_precio.update_layout(legend_title_text='Indicadores', xaxis_rangeslider_visible=True)
st.plotly_chart(fig_precio, use_container_width=True)

st.write("---")

st.subheader("Análisis Diario Detallado")
col1, col2 = st.columns(2)

with col1:
    fig_velas = go.Figure(data=[go.Candlestick(x=df_filtrado.index,
                    open=df_filtrado['Open'], high=df_filtrado['High'],
                    low=df_filtrado['Low'], close=df_filtrado['Close'],
                    name='Velas')])
    fig_velas.update_layout(title='Gráfico de Velas', template='plotly_dark', xaxis_rangeslider_visible=False)
    st.plotly_chart(fig_velas, use_container_width=True)

with col2:
    fig_volumen = px.bar(df_filtrado, y='Volume', title='Volumen de Negociación', template='plotly_dark')
    st.plotly_chart(fig_volumen, use_container_width=True)

st.subheader("Distribución de Retornos Diarios")
fig_hist = px.histogram(df_filtrado, x='Retorno_Diario', nbins=100, template='plotly_dark')
st.plotly_chart(fig_hist, use_container_width=True)

with st.expander("Ver datos históricos filtrados"):
    st.dataframe(df_filtrado)