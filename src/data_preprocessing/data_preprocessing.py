import pandas as pd
import io

# Função para apagar as linhas nulas do dataset
def remove_nulls(dataset: pd.DataFrame) -> pd.DataFrame:
    '''Apagar as linhas nulas do dataset.'''
    if dataset is not None:
        return dataset.dropna()
    return None

# Função para apagar as linhas duplicadas.
def drop_duplicates(dataset: pd.DataFrame) -> pd.DataFrame:
    '''Remove as linhas duplicadas do DataFrame.'''
    if dataset is not None:
        return dataset.drop_duplicates()
    return None

def rename_columns(dataset: pd.DataFrame) -> pd.DataFrame:
    '''Renomear colunas para snake_case, sem espaços e sem acentos'''
    if dataset is not None:
        return dataset.rename(columns={
            'Age': 'idade',
            'Gender': 'genero',
            'Academic_Level': 'nivel_academico',
            'Country': 'pais',
            'Avg_Daily_Usage_Hours': 'plataforma_hora',
            'Most_Used_Platform': 'plataforma_mais_usada',
            'Affects_Academic_Performance': 'afeta_academic_performance',
            'Sleep_Hours_Per_Night': 'dormir_horas_per_noite',
            'Mental_Health_Score': 'pontuacao_saude_mental',
            'Relationship_Status': 'relacionamento_status',
            'Conflicts_Over_Social_Media': 'conflitos_sobre_social_media',
            'Addicted_Score': 'pontuacao_viciada'
        })
    return None
