# Importar las bibliotecas necesarias
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def entrenar_y_evaluar_modelo():
    # Cargar el conjunto de datos de iris
    iris = load_iris()
    X = iris.data
    y = iris.target

    # Dividir el conjunto de datos en entrenamiento y prueba
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    print(X_train[:5])
    print(y_train[:5])

    # Crear un modelo de árbol de decisiones con hiperparámetros personalizados
    clf = DecisionTreeClassifier(criterion='entropy', max_depth=3, random_state=42)

    # Entrenar el modelo con los datos de entrenamiento
    clf.fit(X_train, y_train)

    # Realizar predicciones en el conjunto de prueba
    y_pred = clf.predict(X_test)

    # Calcular la precisión del modelo
    accuracy = accuracy_score(y_test, y_pred)
    print("Precisión del modelo:", accuracy)

    # Mostrar el informe de clasificación
    classification_rep = classification_report(y_test, y_pred)
    print("Informe de clasificación del modelo:\n", classification_rep)

    # Crear la matriz de confusión
    cm = confusion_matrix(y_test, y_pred)

    # Crear un DataFrame para la matriz de confusión
    df_cm = pd.DataFrame(cm, index=["Setosa", "Versicolor", "Virginica"], columns=["Setosa", "Versicolor", "Virginica"])

    # Visualizar la matriz de confusión
    plt.figure(figsize=(5, 5))
    sns.heatmap(df_cm, annot=True, cmap="Greens", fmt='d', cbar=False, annot_kws={"size": 14})
    plt.xlabel("Etiqueta Predicha")
    plt.ylabel("Etiqueta Real")
    plt.title("Matriz de Confusión del modelo")
    plt.show()


def main():
    # Ejecutar la función entrenar_y_evaluar_modelo cinco veces
    for i in range(5):
        ejecucion = i + 1
        print("Ejecucion número: ", ejecucion)
        entrenar_y_evaluar_modelo()


if __name__ == "__main__":
    main()
