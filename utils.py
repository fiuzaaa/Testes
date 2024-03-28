import pandas as pd
from datetime import date
from collections import Counter

def calcular_idade(data):
    """
    Calcula a idade com base na data de nascimento e data da operação.

    Args:
        data (pandas.DataFrame): DataFrame contendo as colunas 'nascimento' e 'data_operacao'.

    Returns:
        pandas.Series: Série com as idades calculadas.
    """
    def calcular_idade_individual(row):
        try:
            # Converte as datas de nascimento e operação para objetos datetime.
            data_nascimento_obj = date.fromisoformat(row['nascimento'])
            data_operacao_obj = date.fromisoformat(row['data_operacao'])

            # Calcula a diferença entre os anos.
            idade = data_operacao_obj.year - data_nascimento_obj.year

            # Se o aniversário ainda não ocorreu neste ano, diminui a idade em 1.
            if (data_operacao_obj.month, data_operacao_obj.day) < (data_nascimento_obj.month, data_nascimento_obj.day):
                idade -= 1

            return idade
        except ValueError:
            return None

    # Aplica a função a cada linha do DataFrame.
    return data.apply(calcular_idade_individual, axis=1)




def substituir_nulos_pela_maioria(df, columns):
  """
  Substitui valores nulos em uma DataFrame pela maioria em cada coluna.

  Argumentos:
    df: DataFrame a ser processada.

  Retorna:
    DataFrame com valores nulos substituídos.
  """
  for coluna in columns:
    # Contagem de valores únicos na coluna
    contagem_valores = Counter(df[coluna].loc[(df[coluna] != "Null")])
    # Pega o valor mais frequente
    if contagem_valores.most_common(1) != []:
      maioria = contagem_valores.most_common(1)[0][0]
      # Substitui valores nulos pela maioria
      df.loc[df[coluna] == "Null", coluna] = maioria
  
  return df



