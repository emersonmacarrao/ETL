#----- Extract----- Importando o arquivo csv usando a biblioteca pandas
import pandas as pd
arquivo = pd.read_csv('D:/Estudos/ETL/base1.csv')
usuario_id = arquivo['id'].tolist
print(usuario_id)

