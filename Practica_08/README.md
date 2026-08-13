# Práctica 08 - Scatter Plot 3D con Sprites de Pokémon

## Datos del estudiante

**Nombre del Estudiante:** Carlos Daniel Garcia Pluma\
**Matrícula:** 230187\
**Grado y Grupo:** 9° A IDGS

## Materia y docente

**Programa de Estudios:** Ingeniería en Desarrollo y Gestión de
Software\
**Asignatura:** Extracción de Conocimiento en Base de Datos\
**Docente:** M.T.I. Marco A. Ramírez Hernández\
**Periodo:** Mayo - Agosto 2026

------------------------------------------------------------------------

## Objetivo

Aplicar técnicas de limpieza, análisis exploratorio y visualización
interactiva sobre un único archivo CSV de Pokémon, construyendo un
**Scatter Plot 3D** que relacione:

-   Generación.
-   Tipo principal.
-   Promedio de las seis estadísticas base.

Además, la práctica integra sprites de Pokémon en la visualización
interactiva. Los Pokémon reales utilizan las URLs proporcionadas en el
CSV, mientras que los Pokémon inventados de tipo **Artificial** utilizan
sprites locales almacenados en la carpeta `sprites`.

------------------------------------------------------------------------

### Descripción de los archivos

-   `Practica08.ipynb`: notebook completo de la práctica, con
    limpieza, análisis, cálculos y visualización.
-   `PokemonSprites.csv`: único dataset utilizado por el notebook.
-   `pokemon_sprites_3d.html`: visualización 3D interactiva exportada
    desde el notebook.
-   `sprites/`: carpeta que contiene los sprites locales de los Pokémon
    inventados.

### Pokémon inventados

Los registros de tipo `Artificial` no utilizan una URL externa. Sus
imágenes se cargan desde la carpeta `sprites`:

     ID Pokémon      Sprite local
  ----- ------------ -------------------
    722 Synthbit     `sprites/722.png`
    723 Synthlet     `sprites/723.png`
    724 Synthrex     `sprites/724.png`
    725 Synthagon    `sprites/725.png`
    726 Syntharion   `sprites/726.png`

------------------------------------------------------------------------

## Contenido del notebook

### 1. Importación de librerías

Se importan las herramientas necesarias para manipular, analizar y
visualizar los datos:

-   `pandas`
-   `numpy`
-   `plotly`
-   `plotly.express`
-   `plotly.graph_objects`
-   `IPython.display`

También se configuran opciones de visualización de Pandas para mostrar
las columnas completas.
<img src="/Practica_08/image/image1.png" width="700">
------------------------------------------------------------------------

### 2. Carga del único dataset

La práctica trabaja con un único archivo CSV que contiene las
estadísticas de los Pokémon y una columna con la información del sprite.

No se utiliza `Pokemon.csv` ni se genera un segundo dataset de sprites.
<img src="/Practica_08/image/image2.png" width="700">
------------------------------------------------------------------------

### 3. Inspección inicial del dataset

Se revisan:

-   Nombre de las columnas.
-   Número de filas y columnas.
-   Información general del DataFrame.
-   Valores nulos.
-   Registros duplicados.
-   Estadísticas descriptivas generales.
<img src="/Practica_08/image/image3.png" width="700">

------------------------------------------------------------------------

### 4. Limpieza y normalización

Se realiza la preparación de los datos:

-   Se eliminan espacios innecesarios.
-   Se normalizan los nombres de las columnas.
-   Se convierten las variables numéricas a tipos numéricos.
-   Se normalizan las columnas de texto.
-   Se renombran algunas columnas para facilitar su utilización en
    Python.

Las variables utilizadas para el análisis se conservan con nombres
sencillos como:

``` text
id
name
type1
type2
total
hp
attack
defense
sp_atk
sp_def
speed
generation
sprite
```
<img src="/Practica_08/image/image4.png" width="700">
------------------------------------------------------------------------

### 5. Tratamiento de valores nulos y validación

Se revisan los valores faltantes y los duplicados.

La columna `type2` puede contener valores nulos porque algunos Pokémon
tienen solamente un tipo. Estos registros no se eliminan por esta razón.

Para el análisis del gráfico se utiliza `type1`, correspondiente al tipo
principal.

También se conservan las formas presentes en el CSV, incluyendo
variantes que formen parte de los registros disponibles.
<img src="/Practica_08/image/image5.png" width="700">
------------------------------------------------------------------------

### 6. Selección de variables estadísticas

Se utilizan las seis estadísticas base disponibles en el dataset:

-   **HP**
-   **Attack**
-   **Defense**
-   **Sp. Atk**
-   **Sp. Def**
-   **Speed**

Estas variables se utilizan posteriormente para obtener un promedio
general de estadísticas para cada Pokémon.
<img src="/Practica_08/image/image6.png" width="700">
------------------------------------------------------------------------

### 7. Cálculo del promedio de estadísticas

Se crea la variable:

``` python
promedio_estadisticas
```

El promedio se calcula a partir de las seis estadísticas base:

``` text
HP + Attack + Defense + Sp. Atk + Sp. Def + Speed
```

El resultado se redondea a dos decimales.
<img src="/Practica_08/image/image7.png" width="700">
------------------------------------------------------------------------

### 8. Análisis estadístico descriptivo

Se calculan las siguientes medidas:

-   Media.
-   Mediana.
-   Mínimo.
-   Máximo.
-   Desviación estándar.

También se obtiene:

-   Promedio de estadísticas por generación.
-   Promedio de estadísticas por tipo principal.
-   Los tipos con mayor promedio.
<img src="/Practica_08/image/image8.png" width="700">

------------------------------------------------------------------------

### 9. Preparación de generación y tipo principal

La generación se convierte a entero para facilitar su representación en
la visualización.

Los tipos principales se ordenan de acuerdo con su promedio de
estadísticas, evitando depender del orden alfabético.
<img src="/Practica_08/image/image9.png" width="700">

------------------------------------------------------------------------

### 10. Validación e integración de sprites

Esta sección es una de las modificaciones principales de la práctica.

Los sprites de los Pokémon reales se obtienen directamente de la columna
correspondiente del CSV.

Cuando una URL contiene accidentalmente un identificador como:

``` text
1.0.png
```

se corrige únicamente el formato numérico para convertirlo en:

``` text
1.png
```
<img src="/Practica_08/image/image10.png" width="700">

### Pokémon Artificial

Los Pokémon de tipo `Artificial` no utilizan sprites externos.

El notebook detecta este tipo y busca el archivo correspondiente en:

``` text
sprites/
```

La búsqueda utiliza principalmente el ID del Pokémon:

``` text
sprites/722.png
sprites/723.png
sprites/724.png
sprites/725.png
sprites/726.png
```

También contempla el nombre del Pokémon como alternativa para localizar
el archivo.
<img src="/Practica_08/image/image10.1.png" width="700">

------------------------------------------------------------------------

## 11. Paleta de colores por tipo

Se define una paleta de colores para identificar visualmente cada tipo
principal.

Los colores se utilizan tanto en el Scatter Plot 3D como en la leyenda
de la visualización interactiva.

El tipo `Artificial` se incorpora a la visualización como parte de los
tipos presentes en el CSV.
<img src="/Practica_08/image/image11.png" width="700">

------------------------------------------------------------------------

## 12. Primera versión del Scatter Plot 3D

Se construye una primera versión del gráfico utilizando:

-   **Eje X:** Generación.
-   **Eje Y:** Tipo principal.
-   **Eje Z:** Promedio de estadísticas.

El gráfico permite observar la distribución de los Pokémon según estas
tres variables.
<img src="/Practica_08/image/image12.png" width="700">

------------------------------------------------------------------------

## 13. Scatter Plot 3D personalizado

Se genera una segunda versión del gráfico utilizando colores por tipo
principal.

La visualización incluye información adicional mediante el hover:

-   Nombre.
-   Tipo.
-   Generación.
-   Promedio de estadísticas.
-   Total de estadísticas.

La escena se configura con títulos descriptivos para cada eje.
<img src="/Practica_08/image/image13.png" width="700">

------------------------------------------------------------------------

## 14. Visualización 3D con sprites

Se genera una visualización interactiva utilizando **Three.js**.

Cada Pokémon se representa mediante su sprite correspondiente.

La posición de cada sprite está determinada por:

``` text
X → Generación
Z → Tipo principal
Y → Promedio de estadísticas
```

De esta manera, la altura del Pokémon dentro de la escena representa su
promedio de estadísticas.

La visualización incluye:

-   Sprites.
-   Líneas guía.
-   Marcadores por tipo.
-   Ejes.
-   Etiquetas.
-   Leyenda.
-   Tooltip.
-   Cámara 3D interactiva.
<img src="/Practica_08/image/image14.png" width="700">

------------------------------------------------------------------------

## 15. Filtros e interacción

La visualización permite interactuar con los datos mediante:

-   Filtro por generación.
-   Filtro por rango de estadísticas.
-   Filtro mediante la leyenda de tipos.
-   Rotación de la escena.
-   Zoom.
-   Desplazamiento de la cámara.
-   Tooltip al pasar el cursor sobre un Pokémon.
-   Selección de un Pokémon mediante clic.
-   Botón para reiniciar la cámara.

### Rangos de estadísticas

El filtro permite seleccionar:

``` text
Todos
Bajo (< 60)
Medio (60 - 90)
Alto (> 90)
```
<img src="/Practica_08/image/image15.png" width="700">

------------------------------------------------------------------------

## 16. Interpretación de resultados

El notebook genera automáticamente indicadores para apoyar la
interpretación de los resultados.

Se obtiene:

-   Tipo con mayor promedio de estadísticas.
-   Promedio de estadísticas por generación.
-   Pokémon con mayor promedio de estadísticas.
-   Pokémon con menor promedio de estadísticas.

Estos resultados se calculan directamente a partir del CSV utilizado por
la práctica.
<img src="/Practica_08/image/image16.png" width="700">

------------------------------------------------------------------------

## 17. Exportación del gráfico

La visualización interactiva se exporta como:

``` text
pokemon_sprites_3d.html
```

Este archivo contiene la escena 3D generada por el notebook y permite
consultar los datos mediante la interfaz interactiva.

El notebook también comprueba:

-   Si el archivo HTML existe.
-   Su tamaño.
-   La cantidad de Pokémon incluidos.
-   El archivo CSV utilizado como fuente.
<img src="/Practica_08/image/image17.png" width="700">

------------------------------------------------------------------------

## 18. Conclusiones

La práctica permitió realizar un flujo completo de análisis exploratorio
y visualización de datos de Pokémon utilizando un único archivo CSV.

A partir de los datos disponibles se realizó la limpieza y normalización
de las variables, se seleccionaron las seis estadísticas base y se
calculó un promedio general para cada Pokémon.

Posteriormente, la generación, el tipo principal y el promedio de
estadísticas fueron utilizados para construir un **Scatter Plot 3D
interactivo**.

Una característica importante de esta versión es la integración de
sprites locales para los Pokémon inventados de tipo `Artificial`. Esto
evita intentar consultar recursos externos para registros que no existen
en PokeAPI y permite que los cinco Pokémon creados para la práctica
aparezcan correctamente en la visualización.

Finalmente, la escena 3D incorpora filtros, leyenda interactiva,
rotación, zoom, tooltips y reinicio de cámara, haciendo posible explorar
visualmente las relaciones entre generación, tipo y estadísticas.

------------------------------------------------------------------------

## Cómo ejecutar la práctica

### 1. Preparar la carpeta

Todos los archivos deben mantenerse en la estructura indicada:

``` text
Practica08/
├── Practica08(1).ipynb
├── PokemonSprites.csv
└── sprites/
    ├── 722.png
    ├── 723.png
    ├── 724.png
    ├── 725.png
    └── 726.png
```

### 2. Abrir el notebook

Abrir:

``` text
Practica08(1).ipynb
```

en Jupyter Notebook, JupyterLab o un entorno compatible con archivos
`.ipynb`.

### 3. Ejecutar las celdas

Ejecutar las celdas en orden, desde la primera hasta la última.

### 4. Verificar los sprites

La sección de validación debe mostrar los sprites externos y los sprites
locales de los Pokémon inventados.

### 5. Verificar la visualización

Al ejecutar la sección de integración de sprites se debe mostrar el
Scatter Plot 3D interactivo.

### 6. Verificar la exportación

Al finalizar debe generarse:

``` text
pokemon_sprites_3d.html
```

------------------------------------------------------------------------

## Dependencias

La práctica utiliza:

-   Python
-   pandas
-   numpy
-   plotly
-   nbformat
-   IPython
-   pathlib
-   re

La visualización 3D con sprites utiliza además recursos JavaScript de
**Three.js** cargados desde CDN dentro del HTML generado.

------------------------------------------------------------------------

## Notas importantes

-   El análisis utiliza un único CSV como fuente de datos.
-   No se necesita `Pokemon.csv`.
-   No se genera un segundo CSV de sprites.
-   Las URLs de sprites reales se toman directamente del CSV.
-   Los Pokémon de tipo `Artificial` utilizan sprites locales.
-   La carpeta `sprites` debe permanecer junto al notebook.
-   Los archivos `722.png` a `726.png` corresponden a los Pokémon
    inventados.
-   El HTML generado es `pokemon_sprites_3d.html`.
-   La visualización 3D depende de JavaScript y de la carga de Three.js
    desde CDN.
-   Si el HTML se abre en un entorno sin acceso a la CDN, la escena
    puede no cargar correctamente.

------------------------------------------------------------------------

## Tecnologías utilizadas

``` text
Python
Pandas
NumPy
Plotly
Jupyter Notebook
IPython
Three.js
HTML
CSS
JavaScript
```

------------------------------------------------------------------------

## Autor

**Carlos Daniel Garcia Pluma**\
**Matrícula:** 230187\
**9° A IDGS**\
**Universidad Tecnológica de Xicotepec de Juárez**
