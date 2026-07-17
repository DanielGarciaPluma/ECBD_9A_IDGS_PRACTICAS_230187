# 📊 Práctica 04 - Análisis Exploratorio de Datos (EDA) con DonorsChoose

## 📖 Descripción

En esta práctica se desarrolla un **Análisis Exploratorio de Datos (EDA)** utilizando los diferentes conjuntos de datos de **DonorsChoose**, una plataforma dedicada al financiamiento de proyectos educativos en Estados Unidos.

El objetivo principal consiste en explorar la información de **donantes, donaciones, docentes, escuelas, recursos y proyectos**, utilizando técnicas estadísticas y visualizaciones para identificar patrones, tendencias y relaciones entre los datos.

---

# 📋 Desarrollo de la Práctica

## 1. Preparación del entorno

### 1.1 Importación de librerías
Se importan las bibliotecas necesarias para el desarrollo de la práctica, incluyendo herramientas para manipulación de datos, análisis estadístico, visualización de información y generación de mapas interactivos.

### 1.2 Carga de los conjuntos de datos
Se cargan todos los archivos correspondientes al conjunto de datos **DonorsChoose**, que contienen información sobre donantes, donaciones, docentes, escuelas, proyectos y recursos educativos.

### 1.3 Exploración inicial
Se realiza una inspección general de cada dataset para conocer su estructura, dimensiones, tipos de datos y posibles valores faltantes. Esta revisión permite comprender la información antes de iniciar el análisis.

---

# 2. Exploración de los Donantes

### 2.1 Información general de los donantes
Se analiza la cantidad total de donantes registrados y sus principales características, obteniendo una visión general de la base de datos.

### 2.2 Donantes por estado
Se agrupan los donantes según el estado donde residen para identificar cuáles presentan una mayor participación dentro de la plataforma.

### 2.3 Donantes ajustados por población
Se compara la cantidad de donantes con la población de cada estado para obtener una medida proporcional de participación.

### 2.4 Distribución geográfica
Se generan mapas interactivos para visualizar la ubicación geográfica de los donantes y detectar las zonas con mayor concentración.

#### 2.4.1 California
Se analiza la distribución de donantes dentro del estado de California utilizando mapas geográficos.

#### 2.4.2 Florida
Se visualiza la ubicación de los donantes registrados en Florida para identificar las ciudades con mayor actividad.

#### 2.4.3 Nueva York
Se realiza el análisis geográfico de los donantes pertenecientes al estado de Nueva York.

#### 2.4.4 Texas
Se estudia la distribución espacial de los donantes registrados en Texas.

### 2.5 Distribución nacional
Se construye un mapa general de Estados Unidos para visualizar la distribución completa de todos los donantes registrados en la plataforma.

### 2.6 Donantes docentes y no docentes
Se compara el comportamiento entre donantes que también son docentes y aquellos que no pertenecen al sector educativo mediante diferentes gráficos estadísticos.

---

# 3. Exploración de las Donaciones

### 3.1 Información general
Se analizan las características generales de las donaciones, incluyendo montos, fechas, frecuencia y registros disponibles.

### 3.2 Proyectos con más donaciones
Se identifican los proyectos educativos que recibieron el mayor número de donaciones y aquellos que obtuvieron una mayor cantidad de recursos económicos.

### 3.3 Principales donantes
Se determina cuáles usuarios realizaron el mayor número de donaciones y quiénes aportaron las cantidades más elevadas.

### 3.4 Evolución temporal

#### 3.4.1 Donaciones por año
Se analiza el comportamiento anual de las donaciones para identificar tendencias de crecimiento o disminución.

#### 3.4.2 Donaciones por mes
Se estudia la distribución mensual de las donaciones para conocer los meses con mayor actividad.

#### 3.4.3 Donaciones por día
Se observa la frecuencia diaria de las donaciones realizadas durante el periodo de estudio.

#### 3.4.4 Donaciones por día de la semana
Se compara la actividad de los donantes dependiendo del día de la semana.

#### 3.4.5 Donaciones por hora
Se analiza en qué horarios del día se realizan más donaciones.

### 3.5 Donaciones opcionales
Se estudia el comportamiento de las aportaciones opcionales realizadas por los donantes y se comparan entre distintos grupos.

### 3.6 Donaciones máximas por estado
Se identifica la donación individual más alta registrada en cada estado y se representa mediante visualizaciones geográficas.

### 3.7 Promedio de donación por estado
Se calcula el promedio de las donaciones realizadas en cada estado para comparar el comportamiento económico entre regiones.

### 3.8 Mapas de donaciones
Se crean mapas interactivos para representar la distribución geográfica de las donaciones y facilitar la interpretación de los resultados.

### 3.9 Caso de estudio: California
Se realiza un análisis específico del estado de California para estudiar la evolución y comportamiento de las donaciones.

---

# 4. Exploración de los Docentes

### 4.1 Información general
Se examina la información básica de los docentes registrados dentro de la plataforma y su participación en los proyectos.

### 4.2 Primeros docentes registrados
Se identifican los primeros profesores que comenzaron a publicar proyectos educativos en DonorsChoose.

### 4.3 Crecimiento de docentes
Se analiza el incremento de docentes registrados a lo largo del tiempo mediante gráficos de evolución.

### 4.4 Prefijos de los docentes
Se estudia la distribución de los diferentes títulos utilizados por los docentes, como Mr., Mrs., Ms. y Dr.

### 4.5 Primer proyecto publicado
Se analiza la fecha del primer proyecto publicado por cada docente para conocer el ritmo de incorporación a la plataforma.

---

# 5. Exploración de las Escuelas

### 5.1 Información general
Se revisan las principales características de las escuelas participantes, como ubicación, ciudad y tipo de institución.

### 5.2 Distribución de escuelas
Se analiza cómo se distribuyen las escuelas entre zonas urbanas, suburbanas y rurales.

### 5.3 Almuerzos gratuitos
Se estudia el porcentaje de estudiantes beneficiados con programas de alimentación gratuita o de bajo costo como indicador socioeconómico.

### 5.4 Tipos de escuela
Se identifican los tipos de escuelas más frecuentes mediante visualizaciones como nubes de palabras.

---

# 6. Exploración de los Recursos

### 6.1 Recursos más solicitados
Se identifican los materiales educativos y tecnológicos más solicitados por los docentes en sus proyectos.

### 6.2 Recursos más costosos
Se analizan los recursos con mayor precio para conocer cuáles representan una mayor inversión económica.

### 6.3 Proveedores
Se estudian los proveedores de materiales utilizados por los proyectos, identificando aquellos con mayor participación.

---

# 7. Exploración de los Proyectos

### 7.1 Categorías principales
Se analizan las principales categorías educativas en las que se clasifican los proyectos.

### 7.2 Subcategorías
Se estudian las subcategorías para identificar las áreas específicas con mayor número de proyectos.

### 7.3 Nivel educativo
Se analiza la distribución de los proyectos según el nivel escolar al que están dirigidos.

### 7.4 Estado del proyecto
Se comparan proyectos financiados, activos y expirados para conocer su comportamiento dentro de la plataforma.

### 7.5 Fechas de publicación

#### 7.5.1 Por año
Se estudia la evolución anual de los proyectos publicados.

#### 7.5.2 Por mes
Se identifican los meses con mayor número de publicaciones.

#### 7.5.3 Por día
Se analiza la frecuencia diaria de publicación de proyectos.

### 7.6 Evolución de proyectos
Se observa el crecimiento de los proyectos publicados a lo largo del tiempo mediante gráficos temporales.

### 7.7 Costos de los proyectos

#### 7.7.1 Costo promedio
Se calcula el costo promedio de los proyectos registrados.

#### 7.7.2 Costo por categoría
Se comparan los costos promedio entre las diferentes categorías educativas.

#### 7.7.3 Costo por nivel educativo
Se analizan los costos dependiendo del nivel escolar al que pertenece cada proyecto.

#### 7.7.4 Proyectos más costosos
Se identifican los proyectos que presentan los mayores costos de financiamiento.

### 7.8 Tiempo de financiamiento
Se estudia el tiempo requerido para que un proyecto alcance el financiamiento total solicitado.

---

# 8. Análisis de Texto

### 8.1 Frecuencia de palabras
Se identifican las palabras más utilizadas en las descripciones de los proyectos mediante técnicas de minería de texto.

### 8.2 Bigramas
Se analizan las combinaciones de dos palabras que aparecen con mayor frecuencia.

### 8.3 Trigramas
Se identifican las secuencias de tres palabras más comunes dentro de las descripciones.

### 8.4 Descripción de estudiantes
Se analizan los términos empleados por los docentes para describir a sus estudiantes y sus necesidades.

### 8.5 Necesidades principales
Se identifican los recursos y necesidades que aparecen con mayor frecuencia en los proyectos.

### 8.6 Títulos de proyectos
Se estudian los títulos de los proyectos mediante nubes de palabras para identificar los términos más representativos.

---

# 9. Comparación de Proyectos

### 9.1 Proyectos financiados vs. expirados
Se comparan las características de los proyectos que lograron financiamiento con aquellos que expiraron sin alcanzar su meta.

### 9.2 Factores de éxito
Se identifican patrones comunes entre los proyectos exitosos, considerando variables como categoría, tiempo de financiamiento, costos y número de donaciones recibidas.