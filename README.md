# ⚙️ Probabilidade de Falhas em Equipamentos

Este projeto é uma aplicação web interativa desenvolvida com **Streamlit** que permite calcular e visualizar a **probabilidade de falhas em equipamentos**, com base na **Distribuição de Poisson**. A ferramenta é ideal para profissionais de manutenção, engenharia e confiabilidade que desejam avaliar a frequência de falhas de forma estatística e intuitiva.

---

## 🔗 Acesse a Aplicação Online

Você pode testar o aplicativo diretamente através do link abaixo:

👉 [Abrir Aplicação](https://yrodalex-falhaequipamento-main-bu9aad.streamlit.app/)

---

## 🧠 Sobre o Cálculo

A distribuição de Poisson é utilizada para modelar o número de ocorrências de eventos (falhas) em um intervalo fixo de tempo ou espaço. Este app permite calcular:

- **Probabilidade Exata** de uma quantidade de falhas
- **Probabilidade de Menor que** uma quantidade específica
- **Probabilidade de Maior que** uma quantidade específica

---

## 🧰 Tecnologias Utilizadas

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) – para construção da interface web
- [NumPy](https://numpy.org/) – para manipulação numérica
- [SciPy](https://scipy.org/) – para cálculo de probabilidades com a distribuição de Poisson
- [Matplotlib](https://matplotlib.org/) – para visualização gráfica

---

## 📈 Funcionalidades

- Interface interativa para entrada dos dados
- Escolha entre três tipos de cálculo de probabilidade
- Geração de gráfico de barras com os resultados
- Visualização intuitiva com rótulos informativos

---

## 📦 Como Rodar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/seuusuario/falhaequipamento.git
cd falhaequipamento


python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

2. Crie um ambiente virtual e instale as dependências:

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Execute a aplicação
streamlit run main.py


4. 📄 requirements.txt 

streamlit
numpy
matplotlib
scipy
