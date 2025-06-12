import pandas as pd
from datetime import datetime
import logging
from dateutil.easter import easter


def calcular_feriados_nacionais(ano):
    """Retorna um set com datas dos principais feriados nacionais do ano."""
    # Feriados fixos
    fixos = [
        f"{ano}-01-01",  # Confraternização Universal
        f"{ano}-04-21",  # Tiradentes
        f"{ano}-05-01",  # Dia do Trabalho
        f"{ano}-09-07",  # Independência
        f"{ano}-10-12",  # Nossa Sra Aparecida
        f"{ano}-11-02",  # Finados
        f"{ano}-11-15",  # Proclamação da República
        f"{ano}-12-25",  # Natal
    ]

    # Feriados móveis
    pascoa = easter(ano)
    carnaval = pascoa - pd.Timedelta(days=47)
    sexta_santa = pascoa - pd.Timedelta(days=2)
    corpus_christi = pascoa + pd.Timedelta(days=60)

    moveis = [
        carnaval.strftime("%Y-%m-%d"),
        sexta_santa.strftime("%Y-%m-%d"),
        pascoa.strftime("%Y-%m-%d"),
        corpus_christi.strftime("%Y-%m-%d")
    ]

    return set(fixos + moveis)


def create_date_dimension(start_date, end_date):
    """
    Cria uma dimensão de datas com bimestre e feriados nacionais.
    """
    try:
        dias_semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira',
                       'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
        meses_ano = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
                     'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

        dates = pd.date_range(start=start_date, end=end_date, freq='D')

        date_dim = pd.DataFrame({
            'id_data': range(1, len(dates) + 1),
            'data': dates,
            'dia': dates.day,
            'mes': dates.month,
            'ano': dates.year,
            'trimestre': dates.quarter,
            'bimestre': ((dates.month - 1) // 2) + 1,
            'dia_semana_num': dates.dayofweek,
            'nome_dia': [dias_semana[d.weekday()] for d in dates],
            'nome_mes': [meses_ano[d.month - 1] for d in dates],
            'final_semana': dates.dayofweek.isin([5, 6]),
            'inicio_mes': dates.is_month_start,
            'fim_mes': dates.is_month_end,
            'inicio_trimestre': dates.is_quarter_start,
            'fim_trimestre': dates.is_quarter_end,
            'inicio_ano': dates.is_year_start,
            'fim_ano': dates.is_year_end,
            'dias_no_mes': dates.daysinmonth,
            'semana_do_ano': dates.isocalendar().week
        })

        # Marcar feriados nacionais
        todos_feriados = set()
        for ano in date_dim['ano'].unique():
            todos_feriados |= calcular_feriados_nacionais(ano)

        date_dim['feriado_nacional'] = date_dim['data'].dt.strftime(
            "%Y-%m-%d").isin(todos_feriados)

        return date_dim

    except Exception as e:
        logging.error(f"Erro ao criar dimensão de data: {str(e)}")
        raise


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    start_date = '2023-01-01'
    end_date = '2025-12-31'
    output_path = 'dCalendario.csv'

    try:
        logging.info(
            f"Criando dimensão de data de {start_date} até {end_date}")
        date_dimension = create_date_dimension(start_date, end_date)

        logging.info(
            f"Dimensão de data criada com sucesso com {len(date_dimension)} linhas")
        date_dimension.to_csv(output_path, index=False)
        logging.info(f"Dimensão de data exportada para {output_path}")

    except Exception as e:
        logging.error(f"Falha ao processar dimensão de data: {str(e)}")
