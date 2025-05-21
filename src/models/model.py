import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV, cross_val_score
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import pickle
from load_data.load_data import loadDatasetProcessed  # Seu método para carregar dados
def train_random_forest():

    # Carregar os dados
    dataset = loadDatasetProcessed()

    if dataset is not None:
        # Excluir a coluna 'Student_ID' pois é apenas identificador
        dataset = dataset.drop(columns=['Student_ID'])

        # Separar variável alvo e converter para valores binários
        Y = dataset['afeta_academic_performance'].map({'No': 0, 'Yes': 1})

        # Preparar X e aplicar one-hot encoding nas colunas categóricas
        X = dataset.drop(columns=['afeta_academic_performance'])
        X = pd.get_dummies(X)

        # Dividir os dados em treino e teste
        X_train, X_test, Y_train, Y_test = train_test_split(
            X, Y, train_size=0.7, test_size=0.3, random_state=42
        )

        # Definir o modelo base
        model = RandomForestClassifier(class_weight='balanced', random_state=42)

        # Definir o grid de hiperparâmetros para otimização
        param_grid = {
            'n_estimators': [50, 100, 200],
            'max_depth': [10, 20, None],
            'min_samples_split': [2, 5, 10],
            'min_samples_leaf': [1, 2, 4],
            'bootstrap': [True, False]
        }

        # Aplicar GridSearchCV para encontrar os melhores parâmetros
        grid_search = GridSearchCV(
            estimator=model,
            param_grid=param_grid,
            cv=5,
            n_jobs=-1,
            scoring='f1'  # Para priorizar f1-score
        )

        # Treinar o modelo
        grid_search.fit(X_train, Y_train)

        # Exibir melhores parâmetros encontrados
        print(f'Melhores parâmetros: {grid_search.best_params_}')

        # Pegar o melhor modelo treinado
        best_model = grid_search.best_estimator_

        # Fazer previsões no conjunto de teste
        y_pred = best_model.predict(X_test)

        # Avaliar o modelo
        accuracy = accuracy_score(Y_test, y_pred)
        precision = precision_score(Y_test, y_pred)
        recall = recall_score(Y_test, y_pred)
        f1 = f1_score(Y_test, y_pred)

        print(f'Acurácia: {accuracy:.4f}')
        print(f'Precisão: {precision:.4f}')
        print(f'Recall: {recall:.4f}')
        print(f'F1-Score: {f1:.4f}')

        # Exibir matriz de confusão
        cm = confusion_matrix(Y_test, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Não Afeta", "Afeta"])
        disp.plot(cmap=plt.cm.Blues)
        plt.title("Matriz de Confusão - Random Forest")
        plt.show()

        # Mostrar distribuição das classes
        print("Distribuição das classes no dataset:")
        print(Y.value_counts(normalize=True))

        # Cross-validation para avaliação mais robusta
        scores = cross_val_score(best_model, X, Y, cv=5, scoring='f1')
        print(f'F1-Score médio (cross-validation): {scores.mean():.4f}')

        # Salvar o melhor modelo treinado em disco
        with open('modelo_vicio_redes.pkl', 'wb') as f:
            pickle.dump(best_model, f)

        print("Modelo salvo com sucesso em 'modelo_vicio_redes.pkl'.")

    else:
        print("Erro ao carregar o dataset.")

if __name__ == '__main__':
    train_random_forest()
