# Análisis Exploratorio de Datos de Vehículos Usados

## Introducción

Este proyecto presenta una aplicación web interactiva desarrollada con **Streamlit** para el análisis exploratorio de un conjunto de datos de anuncios de venta de vehículos usados. La herramienta permite a los usuarios visualizar la distribución de los datos y las relaciones entre variables clave de una manera dinámica y sencilla.

## Funcionalidad

La aplicación proporciona las siguientes características:

* **Histograma Interactivo**: Permite visualizar la distribución de los datos de kilometraje (`odometer`) en el conjunto de datos.
* **Gráfico de Dispersión**: Muestra la relación entre el año del modelo (`model_year`) y el precio (`price`) de los vehículos.
* **Filtros Dinámicos**: Los usuarios pueden interactuar con las casillas de verificación para mostrar u ocultar los gráficos según sus preferencias. Además, pueden filtrar los datos para incluir solo los vehículos con tracción 4x4.

## Cómo Usar la Aplicación

1.  **Clonar el Repositorio**: Clona este repositorio a tu máquina local.
2.  **Configurar el Entorno**: Asegúrate de tener un entorno virtual de Python con las librerías necesarias instaladas. Puedes usar el archivo `requirements.txt`.
3.  **Ejecutar la Aplicación**: En la terminal, con el entorno virtual activado, navega al directorio del proyecto y ejecuta la aplicación con el comando: `streamlit run app.py`

## Tecnologías Utilizadas

* **Python**: Lenguaje de programación.
* **Pandas**: Para el manejo y análisis de datos.
* **Streamlit**: Para la construcción de la aplicación web interactiva.
* **Plotly Express**: Para la creación de visualizaciones interactivas.

---