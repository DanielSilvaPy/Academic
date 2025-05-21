import streamlit as st
import pandas as pd
import numpy as np
import pickle

from load_data.load_data import loadDatasetProcessed

def main():
    st.title("Predição de Impacto do Uso das Redes Sociais no Desempenho Acadêmico")

    # Carregar dataset processado para pegar as categorias únicas para os selectboxes
    dataset = loadDatasetProcessed()
    if dataset is None:
        st.error("Erro ao carregar o dataset. Verifique os dados.")
        return
    
    # Listas de categorias para seleção
    paises = dataset['pais'].unique().tolist()
    plataformas = dataset['plataforma_mais_usada'].unique().tolist()
    generos = dataset['genero'].unique().tolist()
    niveis = dataset['nivel_academico'].unique().tolist()
    rel_status = dataset['relacionamento_status'].unique().tolist()

    # Inputs do usuário
    idade = st.number_input("Idade", min_value=10, max_value=100, value=20)
    genero = st.selectbox("Gênero", generos)
    nivel_academico = st.selectbox("Nível Acadêmico", niveis)
    pais = st.selectbox("País", paises)
    plataforma_hora = st.number_input("Horas na plataforma por dia", min_value=0.0, max_value=24.0, value=5.0, step=0.1)
    plataforma_mais_usada = st.selectbox("Plataforma mais usada", plataformas)
    dormir_horas_per_noite = st.number_input("Horas de sono por noite", min_value=0.0, max_value=24.0, value=7.0, step=0.1)
    pontuacao_saude_mental = st.number_input("Pontuação saúde mental (0-10)", min_value=0, max_value=10, value=5)
    relacionamento_status = st.selectbox("Status do relacionamento", rel_status)
    conflitos_sobre_social_media = st.number_input("Conflitos sobre social media (0-10).", min_value=0, max_value=10, value=2)
    pontuacao_viciada = st.number_input("Pontuação de vício (0-10)", min_value=0, max_value=10, value=5)

    # Criar dataframe de entrada com os dados do usuário
    input_data = pd.DataFrame({
        'idade': [idade],
        'genero': [genero],
        'nivel_academico': [nivel_academico],
        'pais': [pais],
        'plataforma_hora': [plataforma_hora],
        'plataforma_mais_usada': [plataforma_mais_usada],
        'dormir_horas_per_noite': [dormir_horas_per_noite],
        'pontuacao_saude_mental': [pontuacao_saude_mental],
        'relacionamento_status': [relacionamento_status],
        'conflitos_sobre_social_media': [conflitos_sobre_social_media],
        'pontuacao_viciada': [pontuacao_viciada]
    })

    # Pré-processar a entrada exatamente como o dataset (one-hot encoding nas colunas categóricas)
    # Para isso, concatenamos com o dataset original e aplicamos get_dummies para garantir as mesmas colunas
    data_concat = pd.concat([dataset.drop(columns=['Student_ID', 'afeta_academic_performance']), input_data], axis=0)
    data_encoded = pd.get_dummies(data_concat)

    # Seleciona somente a última linha (entrada do usuário) após codificar
    input_encoded = data_encoded.tail(1)

    # Carregar o modelo salvo
    try:
        with open('modelo_vicio_redes.pkl', 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        st.error("Modelo salvo não encontrado. Execute o treinamento primeiro.")
        return

    # Quando o usuário clicar no botão, faz a previsão
    if st.button("Prever impacto no desempenho acadêmico"):
        prediction = model.predict(input_encoded)[0]
        prob = model.predict_proba(input_encoded)[0][prediction]

        if prediction == 1:
            resultado_texto = "afeta"
            resultado_label = "AFETA"
        else:
            resultado_texto = "não afeta"
            resultado_label = "NÃO AFETA"

        if resultado_label == "AFETA":
            st.error(f"Resultado da previsão: {resultado_label}")
        else:
            st.success(f"Resultado da previsão: {resultado_label}")


        st.write(f"O modelo indica que o uso das redes sociais provavelmente {resultado_texto} seu desempenho acadêmico, com {prob * 100:.0f}% de confiança.")

if __name__ == "__main__":
    main()
