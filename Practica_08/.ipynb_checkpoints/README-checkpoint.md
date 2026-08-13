# Práctica 07 - Scatter Plot 3D con Sprites de Pokémon

## Objetivo

Crear un análisis exploratorio de estadísticas de Pokémon utilizando un gráfico 3D interactivo en Plotly, incorporando sprites oficiales de PokéAPI y generando un archivo CSV con las URLs de los sprites.

## Archivos principales

- `Practica_07.ipynb`: notebook completo con todos los pasos, explicaciones y visualizaciones.
- `Pokemon.csv`: dataset original de Pokémon con estadísticas y generaciónes.
- `PokemonSprites.csv`: archivo generado automáticamente con la columna adicional `Sprite` que contiene la URL del sprite oficial.
- `ScatterPokemon3D.html`: exportación interactiva del gráfico 3D en formato HTML.

## Contenido del notebook

1. Importar librerías
   - `pandas`, `numpy`, `plotly.express`, `plotly.graph_objects`, `IPython.display`.
   <img src="/Practica_08/image/image1.png" width="700">
   
2. Generar y cargar el dataset con sprites
   - Crea `PokemonSprites.csv` a partir de `Pokemon.csv`.
   - Construye la URL de sprite usando el número de Pokédex.
   <img src="/Practica_08/image/image2.png" width="700">

3. Descripción del dataset
   - Origen, número de registros, variables y distribución por generación.
   <img src="/Practica_08/image/image3.png" width="700">

4. Inspección
   - `head()`, `shape`, `info()` y `describe()`.
   <img src="/Practica_08/image/image4.png" width="700">

5. Limpiar columnas
   - Normaliza nombres de columnas a minúsculas y guiones bajos.
   <img src="/Practica_08/image/image5.png" width="700">

6. Limpiar tipos
   - Estiliza los valores de `type1` y `type2` con `title()`.
   <img src="/Practica_08/image/image6.png" width="700">

7. Valores nulos y duplicados
   - Revisa y elimina duplicados si los hubiera.
   <img src="/Practica_08/image/image7.png" width="700">

8. Variables seleccionadas
   - Estadísticas base: `HP`, `Attack`, `Defense`, `Sp. Atk`, `Sp. Def`, `Speed`.


9. Promedio de estadísticas
   - Calcula una nueva columna `promedio_estadisticas`.
   <img src="/Practica_08/image/image9.png" width="700">

10. Estadística descriptiva
   - Genera media, mediana, mínimo, máximo y desviación estándar.
   <img src="/Practica_08/image/image10.png" width="700">

11. Preparar generación
   - Convierte `generation` a cadena para facilitar el gráfico.
   <img src="/Practica_08/image/image11.png" width="700">
12. Validar sprite
   - Muestra nombre y URL de sprite.
   <img src="/Practica_08/image/image12.png" width="700">

13. Mostrar ejemplo de sprite
   - Renderiza una vista previa HTML de un Pokémon.
   <img src="/Practica_08/image/image13.png" width="700">

14. Scatter Plot 3D
   - Gráfico 3D interactivo con sprite en el hover template.
   <img src="/Practica_08/image/image14.png" width="700">
15. Mostrar sprite al pasar el mouse
   - Explica el comportamiento de los tooltips y la vista previa.


16. Filtros y animación por generación
   - Gráfico animado que muestra cada generación.
<img src="/Practica_08/image/image16.png" width="700">

17. Exportar HTML
   - Guarda el gráfico como `ScatterPokemon3D.html`.
18. Hallazgos
   - Observaciones sobre tendencias de estadísticas, tipos y generaciones.
19. Conclusiones
   - Reflexiona sobre el uso de Plotly, análisis exploratorio, sprites y gráficos 3D.

## Cómo ejecutar

1. Abrir `Practica_07.ipynb` en Jupyter o en un entorno compatible con notebooks.
2. Ejecutar todas las celdas en orden.
3. Verificar que se generen los archivos `PokemonSprites.csv` y `ScatterPokemon3D.html`.

## Dependencias

- Python
- pandas
- numpy
- plotly
- nbformat (para renderizar Plotly correctamente en el notebook)

## Notas importantes

- La URL de sprite se genera automáticamente con la plantilla:
  `https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/<ID>.png`
- El hover del gráfico 3D incluye la imagen del sprite, pero la visualización final depende del visor de Plotly y del entorno del notebook.
- Este README no reemplaza el README general del repositorio; describe específicamente la práctica 07.
