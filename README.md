# 📊 Análise Econômica com Pandas, API do Banco Central e Power BI

Este projeto tem como objetivo **coletar, tratar e analisar** dados econômicos públicos do Brasil – especificamente a **taxa SELIC**, o **índice IPCA** e a criação de uma **dimensão de datas** – utilizando Python com Pandas, e integrando ao **Power BI** para visualização interativa.

---

## 🚀 Tecnologias Utilizadas

- Python 3.12
- Pandas
- Requests
- Power BI
- API do Banco Central do Brasil
- Logging (para rastreabilidade e logs estruturados)

---

## 📦 Scripts Disponíveis

### 1. `selic_data.py`
- Consulta a taxa SELIC diária entre dois anos (padrão: 2023 até o ano atual).
- Processa os dados, identifica as mudanças na taxa ao longo do tempo.
- Exporta para `.csv` com coluna `mudou` (1 para dias em que houve alteração).

### 2. `ipca_data.py`
- Consulta o índice IPCA (inflação oficial) via API do Banco Central.
- Organiza os dados em ordem cronológica e marca as mudanças mensais.
- Exporta para `.csv` com destaque para os meses que tiveram variação.

### 3. `dim_calendario.py`
- Gera uma dimensão de datas completa entre dois anos (default: 2023 a 2025).
- Inclui atributos como:
  - Dia, mês, ano, trimestre
  - Nome do dia e do mês
  - Se é final de mês, trimestre ou ano
  - Número da semana ISO
  - Indicador de fim de semana
- Exporta como `dCalendario.csv`

---

## 🧠 Objetivos

- Automatizar a coleta de dados econômicos públicos
- Criar datasets analíticos prontos para uso em relatórios e BI
- Oferecer insumos para análises temporais, comparativas e preditivas

---

## 📈 Resultados Esperados

Com os dados carregados no Power BI, é possível:

- Visualizar a **evolução da SELIC e IPCA** lado a lado
- Identificar os **pontos de mudança de política monetária**
- Cruzar datas com eventos como:
  - Fins de trimestre (estratégias de fechamento)
  - Semanas críticas de mercado
- Produzir dashboards dinâmicos com **filtros por ano, mês, período, tipo de taxa**

---

## 📁 Outputs Gerados

- `selic_2023 - 2025.csv`  
- `ipca_2023 - 2025.csv`  
- `dCalendario.csv`

Todos os arquivos podem ser usados diretamente em Power BI, Excel ou outros sistemas de análise.

---

## 💡 Possíveis Evoluções

- Adição de mais indicadores econômicos (PIB, câmbio, desemprego)
- Cruzamento com dados de mercado (ações, cripto, etc.)
- Construção de modelos de previsão com séries temporais
- Publicação de dashboard no Power BI Service (compartilhável)

---

## 📜 Fontes Oficiais

- [API Bacen - SELIC](https://dadosabertos.bcb.gov.br/dataset/11-taxa-de-juros-selic)
- [API Bacen - IPCA](https://dadosabertos.bcb.gov.br/dataset/433-indice-nacional-de-precos-ao-consumidor-amplo-ipca)
- [Documentação pandas](https://pandas.pydata.org/)
