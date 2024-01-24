from datetime import datetime
import streamlit as st 
import pandas as pd 

st.set_page_config(layout="wide")

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)    
    st.session_state["data"] = df_data

st.write("# FIFA 2023 OFFICIAL DATASET")

st.markdown("""   
O Conjunto de Dados de Jogadores de Futebol de 2023 fornece informações abrangentes sobre jogadores profissionais de futebol. O conjunto de dados contém uma ampla gama de atributos, incluindo dados demográficos dos jogadores, características físicas, estatísticas de jogo, detalhes contratuais e afiliações a clubes. Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para analistas de futebol, pesquisadores e entusiastas interessados em explorar vários aspectos do mundo do futebol. Ele permite estudar atributos de jogadores, métricas de desempenho, avaliação de mercado, análise de clubes, posicionamento de jogadores e desenvolvimento de jogadores ao longo do tempo.

Atributos do Conjunto de Dados

### O conjunto de dados inclui informações detalhadas sobre:

- Demografia do jogador
- Características físicas
- Estatísticas de jogo
- Detalhes contratuais
- Afiliações a clubes
- Utilidade do Conjunto de Dados

### Com base em mais de 17.000 registros, o conjunto de dados oferece insights valiosos para:

- Analistas de futebol
- Pesquisadores
- Entusiastas do futebol
- Áreas de Exploração

### Os interessados podem explorar uma variedade de aspectos, como:

- Atributos do jogador
- Métricas de desempenho
- Avaliação de mercado
- Análise de clubes
- Posicionamento de jogadores
- Desenvolvimento de jogadores ao longo do tempo

Este conjunto de dados representa uma fonte rica de informações para aqueles que desejam aprofundar seu entendimento sobre o mundo do futebol e suas dinâmicas ao longo dos anos.
                      
            """)

st.sidebar.markdown("Criação de dashboard com Streamlit e Pandas")

st.sidebar.button("Acesse os dados no Kaggle")


