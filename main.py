# Importa bibliotecas necessárias
import streamlit as st                 # Para criar a interface web
import pandas as pd                   # (Não utilizado no código atual, mas comum para manipulação de dados)
import numpy as np                    # Usado para criar arrays numéricos
import matplotlib.pyplot as plt       # Para gerar gráficos
from scipy.stats import poisson       # Distribuição de Poisson usada nos cálculos de probabilidade

# Configura a página da aplicação no Streamlit
st.set_page_config(page_title="Probablidade de Falhas em Equipamentos")
st.title("Probablidade de Falhas em Equipamentos")  # Título principal da página

# Seção lateral (sidebar) da interface
with st.sidebar:
    st.header("Configurações")  # Cabeçalho da seção lateral

    # Seleção do tipo de cálculo desejado: exata, menor que, ou maior que
    tipo = st.radio("Selecione o Calculo", options=["Prob. Exata", "Mais que", "Menor que"])

    # Entrada do número de ocorrências (λ) usado na distribuição de Poisson
    ocorrencia = st.number_input(
        "Ocorrencia Atual",           # Texto da entrada
        min_value=1, max_value=99,    # Intervalo permitido
        value=2, step=1               # Valor padrão e passo de incremento
    )

    # Botão que aciona o cálculo
    processar = st.button("Processar")

# Bloco que roda apenas se o botão "Processar" for clicado
if processar:
    lamb = ocorrencia       # Define a taxa de ocorrência (λ) para a distribuição de Poisson
    inic = lamb - 2         # Valor mínimo do intervalo para o gráfico
    fim = lamb + 2          # Valor máximo do intervalo

    # Cria uma lista de valores inteiros centrada em torno de λ
    x_vals = np.arange(inic, fim + 1)

    # Verifica o tipo de cálculo e calcula a probabilidade correspondente
    if tipo == "Prob. Exata":
        probs = poisson.pmf(x_vals, lamb)   # Probabilidade exata (função de massa de probabilidade)
        tit = "Probabilidade de Ocorrencia"
    elif tipo == "Menor que":
        probs = poisson.cdf(x_vals, lamb)   # Probabilidade acumulada (menor ou igual a x)
        tit = "Probabilidade de Ocorrencia Igual ou Menor que: "
    else:
        probs = poisson.sf(x_vals, lamb)    # Probabilidade complementar (maior que x)
        tit = "Probabilidade de Ocorrencia maior que "

    # Arredonda os valores de probabilidade para exibir nos rótulos
    z_vals = np.round(probs, 4)
    labels = [f"{i} prob.:{p}" for i, p in zip(x_vals, z_vals)]  # Cria rótulos do tipo "3 prob.:0.18"

    # Criação do gráfico de barras com as probabilidades
    fig, ax = plt.subplots()
    ax.bar(x_vals, probs, tick_label=labels,
           color=plt.cm.gray(np.linspace(0.4, 0.8, len(x_vals))))  # Coloração em tons de cinza

    ax.set_title(tit)  # Define o título do gráfico

    plt.xticks(rotation=45, ha="right")  # Roda os rótulos do eixo x para melhor leitura
    plt.tight_layout()                   # Ajusta automaticamente o layout para não cortar rótulos
    st.pyplot(fig)                       # Exibe o gráfico no Streamlit
