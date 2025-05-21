# 📊 Predição de Impacto das Redes Sociais no Desempenho Acadêmico

Este projeto utiliza técnicas de Machine Learning para prever se o uso das redes sociais impacta negativamente o desempenho acadêmico de um estudante. A solução final conta com uma interface interativa construída com **Streamlit**, onde o usuário pode inserir seus dados e obter uma previsão personalizada.

---

## 🚀 Funcionalidades

- ✅ Treinamento de modelo de classificação com **Random Forest**
- ✅ Otimização de hiperparâmetros com **GridSearchCV**
- ✅ Cálculo de métricas como **acurácia**, **precisão**, **recall** e **F1-score**
- ✅ Visualização da **matriz de confusão**
- ✅ Interface web com Streamlit para **previsão interativa**
- ✅ Salvamento e carregamento do modelo via **Pickle**

---

## 🧠 Base de Dados

O conjunto de dados utilizado foi retirado do Kaggle:  
📎 [Social Media Addiction vs Relationships Dataset](https://www.kaggle.com/datasets/adilshamim8/social-media-addiction-vs-relationships)

### Visão Geral

A base reúne respostas de estudantes sobre seus hábitos de uso de redes sociais, saúde mental, relacionamentos e percepção sobre o impacto desses fatores no desempenho acadêmico.

**Fonte**: Pesquisa aplicada no primeiro trimestre de 2025, com amostra internacional.

- **População**: Estudantes de 16 a 25 anos  
- **Abrangência geográfica**: Bangladesh, Índia, EUA, Reino Unido, Canadá, Austrália, Alemanha, Brasil, Japão, Coreia do Sul  
- **Volume**: Até 1.000 registros anonimizados

### Principais variáveis

| Variável                         | Tipo        | Descrição                                                                 |
|---------------------------------|-------------|---------------------------------------------------------------------------|
| `Student_ID`                    | Inteiro     | Identificador exclusivo                                                   |
| `idade`                        | Inteiro     | Idade do estudante                                                       |
| `genero`                       | Categórico  | "Male" ou "Female"                                                       |
| `nivel_academico`              | Categórico  | Ensino Médio, Graduação ou Pós-Graduação                                |
| `pais`                         | Categórico  | País de residência                                                       |
| `plataforma_hora`              | Float       | Horas diárias gastas em redes sociais                                    |
| `plataforma_mais_usada`        | Categórico  | Instagram, Facebook, TikTok etc.                                         |
| `afeta_academic_performance`   | Booleano    | Se as redes sociais afetam o desempenho acadêmico (Yes/No)              |
| `dormir_horas_per_noite`       | Float       | Média de horas de sono por noite                                         |
| `pontuacao_saude_mental`       | Inteiro     | Avaliação subjetiva de saúde mental (0 a 10)                             |
| `relacionamento_status`        | Categórico  | Solteiro, Em relacionamento, Complicado                                  |
| `conflitos_sobre_social_media` | Inteiro     | Número de conflitos de relacionamento relacionados às redes sociais     |
| `pontuacao_viciada`            | Inteiro     | Pontuação de vício em redes sociais (0 a 10)                             |

---

## 🛠 Tecnologias Utilizadas

- 🐍 Python 3.x  
- 📊 Pandas  
- 🤖 Scikit-learn  
- 📈 Matplotlib  
- 💾 Pickle  
- 🌐 Streamlit  

---

## 🔗 Projeto em Produção

Você pode acessar a aplicação web interativa pelo link abaixo:

👉 [**Acesse a aplicação no Streamlit Cloud**](https://academic-ge4stwhjgsbunyxwqntsiy.streamlit.app/)

