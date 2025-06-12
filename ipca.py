import pandas as pd
import requests
from datetime import datetime


def get_ipca_data(ano_inicial=2023, ano_final=2023):
    """Obtém dados do IPCA da API do Banco Central do Brasil."""
    url = (f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json"
           f"&dataInicial=01/01/{ano_inicial}&dataFinal=31/12/{ano_final}")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Levanta exceção para erros HTTP
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
        return None


def process_ipca_data(data):
    """Processa os dados do IPCA retornados pela API."""
    if not data:
        return None

    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], format='%d/%m/%Y')
    df['valor'] = pd.to_numeric(df['valor'], errors='coerce')
    df = df.sort_values(by='data').reset_index(drop=True)

    # Identificar mudanças no IPCA
    df["mudou"] = df["valor"].diff().ne(0).astype(int)

    return df


def main():
    ano_atual = datetime.now().year
    data = get_ipca_data(2023, ano_atual)
    df = process_ipca_data(data)

    if df is not None:
        # Exibir informações sobre mudanças no IPCA
        mudancas = df[df["mudou"] == 1]
        print(f"O IPCA mudou {len(mudancas)} vezes em {ano_atual}.")

        # Salvar como CSV
        output_file = f"ipca_{2023} - {ano_atual}.csv"
        df.to_csv(output_file, index=False)
        print(f"Dados salvos em {output_file}")

        return df
    return None


if __name__ == "__main__":
    main()
