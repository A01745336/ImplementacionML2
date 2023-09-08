# ImplementacionML2
Momento de Retroalimentación: Módulo 2 Uso de framework o biblioteca de aprendizaje máquina para la implementación de una solución. (Portafolio Implementación)

## Ejemplo de Clasificación con Árbol de Decisiones en Python
Este proyecto de ejemplo se centra en la clasificación de flores usando un algoritmo de Árbol de Decisiones en Python. Elegí el conjunto de datos de Iris y un Árbol de Decisiones para ilustrar cómo construir y evaluar un modelo de aprendizaje automático.

### Elección del Conjunto de Datos de Iris
Elegí el conjunto de datos de Iris para este proyecto por varias razones:

- `Simplicidad y Claridad`: El conjunto de datos de Iris es conocido por su simplicidad. Contiene tres especies de flores: setosa, versicolor y virginica. Cada flor se caracteriza por cuatro atributos: longitud y ancho del sépalo y longitud y ancho del pétalo. Esta claridad facilita la comprensión y la visualización de los conceptos de aprendizaje automático.

- `Ampliamente Utilizado`: El conjunto de datos de Iris es un punto de partida común en el aprendizaje automático. Es un excelente recurso para quienes están aprendiendo a construir y evaluar modelos de clasificación.

### Uso de un Árbol de Decisiones
Opté por utilizar un Árbol de Decisiones para resolver este problema de clasificación por las siguientes razones:

- `Interpretabilidad`: Los Árboles de Decisiones son modelos altamente interpretables. Esto significa que puedo entender cómo se toman las decisiones en el modelo, lo que es valioso para explicar resultados y tomar decisiones basadas en el modelo.

- `Ajuste de Hiperparámetros`: Los Árboles de Decisiones permiten ajustar varios hiperparámetros, como la profundidad máxima del árbol, el criterio de división y otros. Esto proporciona la oportunidad de mostrar cómo la elección de hiperparámetros puede afectar el rendimiento del modelo.

### Elección de Hiperparámetros
La elección de hiperparámetros es crucial para obtener un modelo óptimo. Aquí está cómo seleccioné ciertos hiperparámetros y por qué:

- `Criterio de División ('criterion')`: Configuré el criterio de división en 'entropy'. Elegí 'entropy' para mejorar la calidad de las divisiones, especialmente debido a que mis datos tenían clases desequilibradas. Otra opción común es 'gini'. La elección depende de la naturaleza de los datos y los objetivos del problema.

- `Profundidad Máxima del Árbol ('max_depth')`: Limité la profundidad máxima del árbol a 3. Esto se hizo para evitar el sobreajuste. La elección de la profundidad máxima es crítica para controlar la complejidad del modelo.

- `Otros Hiperparámetros`: También puedes ajustar otros hiperparámetros, como el número mínimo de muestras requeridas para dividir un nodo ('min_samples_split') o el número mínimo de muestras requeridas en un nodo hoja ('min_samples_leaf'). Estos hiperparámetros permiten refinar aún más el comportamiento del modelo y adaptarlo a las características específicas de tus datos.

### Evaluación del Modelo
Para evaluar el modelo, incluimos diversas métricas como `precisión`, `recall`, `puntuación F1` y una `matriz de confusión`. Estas métricas proporcionan una imagen completa del rendimiento del modelo y son relevantes para problemas de clasificación.