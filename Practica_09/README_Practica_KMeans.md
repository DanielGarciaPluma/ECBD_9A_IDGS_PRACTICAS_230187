# Práctica 09 - Segmentación de Clientes con K-Means

## Datos del estudiante

**Nombre del Estudiante:** Carlos Daniel Garcia Pluma  
**Matrícula:** 230187  
**Grado y Grupo:** 9° A IDGS

## Materia y docente

**Programa de Estudios:** Ingeniería en Desarrollo y Gestión de Software  
**Asignatura:** Extracción de Conocimiento en Base de Datos  
**Docente:** M.T.I. Marco A. Ramírez Hernández  
**Periodo:** Mayo - Agosto 2026

------------------------------------------------------------------------

## Objetivo

Aplicar técnicas de análisis exploratorio y aprendizaje no supervisado
sobre un conjunto de datos de clientes de un centro comercial, utilizando
el algoritmo **K-Means** para identificar diferentes grupos o segmentos de
clientes.

La práctica busca analizar principalmente:

- Edad.
- Ingreso anual.
- Puntuación de gasto.

Además, se comparan diferentes combinaciones de características y se
evalúa el comportamiento del modelo utilizando datos originales y datos
normalizados.

------------------------------------------------------------------------

### Descripción de los archivos

- `Mall_Customers_KMeans_Español.ipynb`: notebook completo de la práctica,
  con análisis exploratorio, preparación de datos, modelado y
  conclusiones.
- `Mall_Customers.csv`: dataset utilizado para realizar la segmentación.
- `README.md`: documentación de la práctica.

------------------------------------------------------------------------

## Contenido del notebook

### 1. Introducción

Se presenta el problema de segmentación de clientes y se explica que se
trata de un problema de **Aprendizaje No Supervisado**.

El objetivo es encontrar grupos de clientes con características
similares sin contar previamente con una etiqueta que indique a qué grupo
pertenece cada cliente.

### Mi explicación:

En esta práctica voy a utilizar aprendizaje no supervisado porque no
tengo una categoría o grupo definido previamente para cada cliente. Mi
objetivo es encontrar patrones dentro de los datos y utilizar esos
patrones para crear diferentes segmentos de clientes.

------------------------------------------------------------------------

### 2. Información del dataset

El dataset utilizado corresponde a clientes de un centro comercial.

Contiene **200 registros y 5 características**:

| Característica | Descripción |
|---|---|
| `CustomerID` | Identificador único del cliente |
| `Gender` | Género del cliente |
| `Age` | Edad del cliente |
| `Annual Income (k$)` | Ingreso anual del cliente en miles de dólares |
| `Spending Score (1-100)` | Puntuación de gasto asignada al cliente |

Se revisan las dimensiones, nombres de columnas, tipos de datos,
estadísticas generales y valores nulos.

### Mi explicación:

Primero voy a conocer la estructura del dataset antes de aplicar
cualquier algoritmo. Esto me permite saber qué información tengo
disponible y comprobar si existen datos faltantes o problemas que puedan
afectar el análisis.

------------------------------------------------------------------------

### 3. Inspección inicial del dataset

Se realizan diferentes comprobaciones para conocer el estado de los datos:

- Número de filas y columnas.
- Nombre de las columnas.
- Tipos de datos.
- Información general del DataFrame.
- Valores nulos.
- Estadísticas descriptivas.

El dataset contiene:

```text
200 registros
5 características
```

No se encontraron valores nulos en los datos.

### Mi explicación:

En esta parte reviso que los datos estén completos y que las variables
tengan los tipos correctos. Al no encontrar valores nulos, puedo
continuar con el análisis sin tener que realizar una imputación o
eliminación de registros por datos faltantes.

------------------------------------------------------------------------

### 4. Análisis Exploratorio de Datos (EDA)

Se realiza un análisis exploratorio para conocer la distribución de las
variables y encontrar patrones iniciales.

Se analizan principalmente:

- Distribución de `Gender`.
- Distribución de `Age`.
- Distribución de `Annual Income (k$)`.
- Distribución de `Spending Score (1-100)`.
- Relaciones entre las variables.
- Diferencias entre hombres y mujeres.

### Mi explicación:

Antes de utilizar K-Means quiero entender visualmente cómo se comportan
los clientes. El análisis exploratorio me ayuda a encontrar posibles
grupos y relaciones que después puedo comprobar mediante el algoritmo de
clustering.

------------------------------------------------------------------------

### 5. División de características

Las características se dividen en:

- **Categóricas:** `Gender`.
- **Numéricas:** `CustomerID`, `Age`, `Annual Income (k$)` y
  `Spending Score (1-100)`.

También se utiliza `LabelEncoder` para convertir `Gender` a valores
numéricos cuando es necesario para determinadas visualizaciones.

### Mi explicación:

En esta sección separo las variables de acuerdo con el tipo de
información que contienen. Como K-Means trabaja con valores numéricos,
también puedo transformar la variable categórica cuando necesito
representarla numéricamente.

------------------------------------------------------------------------

### 6. Comparación entre características

Se realizan diferentes visualizaciones para analizar las relaciones
entre las características.

Entre las observaciones principales se encuentran:

- La edad presenta diferentes concentraciones de clientes.
- Los ingresos anuales se distribuyen en diferentes rangos.
- La puntuación de gasto presenta clientes con niveles de consumo bajos,
  medios y altos.
- La combinación de ingreso anual y puntuación de gasto permite observar
  grupos naturales de clientes.

### Mi explicación:

La relación que más me interesa es la que existe entre el ingreso anual
y la puntuación de gasto. Al observar ambas variables puedo identificar
grupos que parecen tener comportamientos diferentes, por lo que esta
combinación puede ser especialmente útil para realizar la segmentación.

------------------------------------------------------------------------

## 7. Resumen del análisis exploratorio

A partir del EDA se identifican diferentes grupos aproximados:

### Edad

- 20 - 30 años.
- 30 - 40 años.
- 40 - 70 años.

### Ingreso anual

- 0 - 40k.
- 40 - 70k.
- 70 - 140k.

### Puntuación de gasto

- 0 - 40.
- 40 - 60.
- 60 - 100.

Estos rangos permiten observar que existen diferentes perfiles de
clientes dentro del centro comercial.

### Mi explicación:

Después de revisar las gráficas puedo observar que los clientes no se
comportan todos de la misma manera. Existen grupos con diferentes
edades, ingresos y niveles de gasto, por lo que considero que los datos
son adecuados para aplicar un algoritmo de agrupamiento.

------------------------------------------------------------------------

## 8. Ingeniería de características

Se analiza la matriz de correlación para conocer las relaciones entre
las variables.

Una observación importante es que `CustomerID` presenta una correlación
alta con `Annual Income (k$)` debido al orden de los registros.

Por esta razón, `CustomerID` no se utiliza como característica principal
para realizar la segmentación.

También se observa una relación negativa entre `Age` y
`Spending Score (1-100)`.

### Mi explicación:

La matriz de correlación me ayuda a decidir qué variables son útiles
para el modelo. No quiero utilizar el identificador del cliente porque
su función es solamente identificar registros y no representa una
característica real del comportamiento del cliente.

------------------------------------------------------------------------

## 9. Escalamiento de los datos

Se trabajan dos versiones de los datos:

- Datos originales.
- Datos normalizados.

La normalización se aplica principalmente a:

- `Age`.
- `Annual Income (k$)`.
- `Spending Score (1-100)`.

El escalamiento es importante porque K-Means utiliza distancias para
determinar la pertenencia de los puntos a cada cluster.

### Mi explicación:

Las variables tienen diferentes escalas. Por ejemplo, el ingreso anual
tiene valores mucho más grandes que la edad. Si no considero este
aspecto, una variable podría tener mayor influencia en el cálculo de
las distancias. Por eso voy a comparar los resultados con datos
originales y normalizados.

------------------------------------------------------------------------

# 10. Modelado con K-Means

K-Means es un algoritmo de **Aprendizaje No Supervisado** que permite
agrupar datos en diferentes clusters.

El proceso general consiste en:

1. Seleccionar el número de clusters `k`.
2. Seleccionar los centroides iniciales.
3. Calcular la distancia de cada punto respecto a los centroides.
4. Asignar cada punto al centroide más cercano.
5. Recalcular los centroides.
6. Repetir el proceso hasta que los centroides se estabilicen.

### Mi explicación:

En esta parte voy a utilizar K-Means para encontrar automáticamente
grupos de clientes. Yo no le voy a indicar cuáles son los grupos, sino
que el algoritmo los va a formar de acuerdo con la similitud entre los
datos.

------------------------------------------------------------------------

## 11. Selección del número de clusters

Para determinar el valor adecuado de `k` se utilizan dos métodos:

### Método del Codo

El método del codo permite analizar cómo disminuye el error al aumentar
el número de clusters.

Se busca un punto donde agregar más clusters ya no produzca una mejora
tan importante.

### Coeficiente de Silueta

El coeficiente de silueta permite evaluar qué tan bien separados se
encuentran los grupos.

Un valor mayor generalmente representa una mejor separación entre los
clusters.

### Mi explicación:

No quiero elegir el número de grupos solamente por observación. Por
eso utilizo el método del codo y el coeficiente de silueta como apoyo
para decidir qué valor de `k` representa mejor los datos.

------------------------------------------------------------------------

## 12. Edad - Ingreso Anual

Se analiza la combinación:

```text
Age
Annual Income (k$)
```

### Datos originales

El número seleccionado de clusters es:

```text
k = 4
```

### Datos normalizados

El número seleccionado de clusters es:

```text
k = 3
```

### Mi explicación:

Al comparar los resultados puedo observar que la normalización cambia
la cantidad de grupos seleccionados. Esto demuestra que el escalamiento
puede influir en K-Means debido a que el algoritmo trabaja utilizando
distancias.

------------------------------------------------------------------------

## 13. Edad - Puntuación de Gasto

Se analiza la combinación:

```text
Age
Spending Score (1-100)
```

### Datos originales

El número seleccionado de clusters es:

```text
k = 4
```

### Datos normalizados

El número seleccionado de clusters es:

```text
k = 6
```

### Mi explicación:

En esta combinación la diferencia entre los datos originales y
normalizados es todavía más evidente. Al normalizar los datos, K-Means
puede identificar una segmentación más detallada.

------------------------------------------------------------------------

## 14. Ingreso Anual - Puntuación de Gasto

Se analiza la combinación:

```text
Annual Income (k$)
Spending Score (1-100)
```

### Datos originales

El número seleccionado de clusters es:

```text
k = 5
```

### Datos normalizados

El número seleccionado de clusters es:

```text
k = 5
```

### Mi explicación:

Esta combinación resulta especialmente interesante porque se mantiene
el mismo número de clusters después de normalizar los datos. Para mí,
esto indica que el ingreso anual y la puntuación de gasto permiten
obtener una segmentación bastante estable.

------------------------------------------------------------------------

## 15. Edad - Ingreso Anual - Puntuación de Gasto

Finalmente se utilizan las tres variables numéricas principales:

```text
Age
Annual Income (k$)
Spending Score (1-100)
```

### Datos originales

El número seleccionado de clusters es:

```text
k = 6
```

### Datos normalizados

El número seleccionado de clusters es:

```text
k = 6
```

### Mi explicación:

En esta última prueba considero simultáneamente edad, ingreso y gasto.
Esto permite obtener una segmentación más completa porque cada cliente se
analiza desde tres características diferentes.

------------------------------------------------------------------------

## 16. Tabla de resultados

### Conjunto de datos original

| No. | Combinación de características | Número de clusters |
|---|---|---:|
| 1 | Edad - Ingreso Anual | 4 |
| 2 | Edad - Puntuación de Gasto | 4 |
| 3 | Ingreso Anual - Puntuación de Gasto | 5 |
| 4 | Edad - Ingreso Anual - Puntuación de Gasto | 6 |

### Conjunto de datos normalizado

| No. | Combinación de características | Número de clusters |
|---|---|---:|
| 1 | Edad - Ingreso Anual | 3 |
| 2 | Edad - Puntuación de Gasto | 6 |
| 3 | Ingreso Anual - Puntuación de Gasto | 5 |
| 4 | Edad - Ingreso Anual - Puntuación de Gasto | 6 |

### Mi explicación:

Esta tabla me permite comparar de forma rápida todas las pruebas. Puedo
observar que algunas combinaciones cambian después de normalizar,
mientras que otras mantienen el mismo resultado.

La combinación de **Ingreso Anual y Puntuación de Gasto** mantiene
**5 clusters** en ambos casos, mientras que la combinación de las tres
variables mantiene **6 clusters**.

------------------------------------------------------------------------

## 17. Interpretación de los resultados

Los resultados muestran que K-Means puede utilizarse para encontrar
diferentes perfiles de clientes.

Una de las combinaciones más útiles es:

```text
Ingreso Anual + Puntuación de Gasto
```

Esta combinación permite distinguir clientes con diferentes niveles de
ingreso y comportamiento de consumo.

También se observa que utilizar las tres características:

```text
Edad + Ingreso Anual + Puntuación de Gasto
```

permite obtener una segmentación más completa.

### Mi explicación:

Los resultados me permiten entender que no todos los clientes tienen el
mismo comportamiento. Algunos tienen ingresos altos pero gastan poco,
otros tienen ingresos altos y gastan mucho, mientras que también existen
clientes con ingresos menores y diferentes niveles de gasto.

Esto puede ser útil para crear estrategias de marketing específicas para
cada segmento.

------------------------------------------------------------------------

## 18. Conclusiones

La práctica permitió aplicar un flujo completo de **Aprendizaje No
Supervisado** utilizando el algoritmo K-Means.

Primero se realizó la inspección del dataset y posteriormente un
análisis exploratorio para conocer las características de los clientes.

Después se realizó la preparación de las variables, el análisis de
correlación y la normalización de los datos.

Finalmente se probaron diferentes combinaciones de características y se
utilizaron el método del codo y el coeficiente de silueta para seleccionar
el número de clusters.

La combinación de **Ingreso Anual y Puntuación de Gasto** fue una de las
más representativas, ya que mantuvo **5 clusters** tanto en los datos
originales como en los normalizados.

### Mi explicación:

Con esta práctica pude comprender mejor cómo funciona el aprendizaje no
supervisado y cómo puedo utilizar K-Means para encontrar grupos sin
necesitar etiquetas previamente definidas.

También pude comprobar que la selección de las características y el
escalamiento de los datos tienen un efecto importante en el resultado
final.

Para mí, la parte más importante fue observar que la combinación de
ingreso anual y puntuación de gasto permite identificar perfiles de
clientes que podrían utilizarse para tomar decisiones comerciales.

------------------------------------------------------------------------

## Archivos de la práctica

```text
.
├── Mall_Customers_KMeans_Español.ipynb
├── Mall_Customers.csv
└── README.md
```

------------------------------------------------------------------------

## Requisitos

Para ejecutar la práctica se requiere:

- Python 3.x
- Jupyter Notebook o JupyterLab
- NumPy
- Pandas
- Matplotlib
- Seaborn
- Scikit-learn

Instalación de las librerías:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn jupyter
```

Para ejecutar Jupyter Notebook:

```bash
jupyter notebook
```

Después se debe abrir:

```text
Mall_Customers_KMeans_Español.ipynb
```

y ejecutar las celdas en orden.

------------------------------------------------------------------------

## Resultado final

La práctica permite realizar una segmentación de clientes utilizando
K-Means y analizar cómo cambian los resultados dependiendo de las
características seleccionadas y del escalamiento aplicado.

El notebook contiene las gráficas, cálculos, modelos y explicaciones
necesarias para reproducir el análisis completo.

------------------------------------------------------------------------
