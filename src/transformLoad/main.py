import pandas as pd
import sqlite3
from datetime import datetime
import numpy as np

# Definir o caminho para o arquivo JSONL
df = pd.read_json('data\data.jsonl', lines = True)


# Setar o pandas para mostrar todas as colunas
pd.options.display.max_columns = None

# Definindo qual paginação vai entrar no source
sources = []
for page in df['page']:
  url = f'https://www.saldaodainformatica.com.br/notebook?page={page}'
  sources.append(url)

# Adicionar a coluna _source com um valor Fixo
df['_source'] = sources

# Adicionar a coluna _data_coleta com a data e hora atuais
df['_data_coleta'] = datetime.now()

# Tratar valores none
df['full_price'] = df['full_price'].fillna(np.nan)

# Manter apenas produtos com preço entre 1000 e 10000 reais 
df = df[
  (df['discounted_price'] >= 1000) & (df['full_price'] <= 10000) &
  (df['full_price'] >= 1000) & (df['discounted_price'] <= 10000)
]

# Conectar ao banco de dados SQLite (Ou criar um novo)
conn = sqlite3.connect('data/saldaodainformatica.db')

# Salvar o DataFrame no banco de Dados SQLite
df.to_sql('notebook', conn, if_exists='replace', index=False)

# Fechar conexão com banco de dados
conn.close()
