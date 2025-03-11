import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st


st.title('Mi primera aplicacion ')
# importando los datos
datos = pd.read_csv('stock.csv')

st.title('Analisis de estock\n')
st.write('En este proyecto vamos a analisar la cantidad de produtos en stock, por categoria, de una base de datos de produtos de supermercado')

# función para seleccionar la cantidad de lineas del dataframe
def mostrar_ctd_lineas(dataframe):

    ctd_lineas = st.sidebar.slider('Seleccione la cantidad de lineas que desea mostrar en la tabla', min_value = 1, max_value = len(dataframe), step = 1)

    st.write(dataframe.head(ctd_lineas).style.format(subset = ['Valor'], formatter="{:.2f}"))

# Función que crea el gráfico
def plot_stock(dataframe, categoria):

    datos_plot = dataframe.query('Categoria == @categoria')

    # Generar una paleta de colores automáticamente
    palette = sns.color_palette("coolwarm", len(datos_plot))

    # Crear el gráfico
    fig, ax = plt.subplots(figsize=(8, 6))
    ax = sns.barplot(x='Producto', y='Cantidad', data=datos_plot, palette=palette)
    ax.set_title(f'Cantidad en stock de los productos de {categoria}', fontsize=16)
    ax.set_xlabel('Productos', fontsize=12)
    ax.tick_params(rotation=20, axis='x')  # Rotar los nombres de los productos
    ax.set_ylabel('Cantidad', fontsize=12)
  
    return fig


checkbox_mostrar_tabla = st.sidebar.checkbox('Mostrar tabla')
if checkbox_mostrar_tabla:

    st.sidebar.markdown('## Filtro para la tabla')

    categorias = list(datos['Categoria'].unique())
    categorias.append('Todas')

    categoria = st.sidebar.selectbox('Seleccione la categoría para presentar en la tabla', options=categorias)

    if categoria != 'Todas':
        df_categoria = datos.query('Categoria == @categoria') 
        mostrar_ctd_lineas(df_categoria)      
    else:
        mostrar_ctd_lineas(datos)

# filtro para el gráfico
st.sidebar.markdown('## Filtro para el gráfico')

categoria_grafico = st.sidebar.selectbox('Seleccione la categoria para presentar en el gráfico', options = datos['Categoria'].unique())
figura = plot_stock(datos, categoria_grafico)
st.pyplot(figura)