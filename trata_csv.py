import pandas as pd


#Carrega o csv bruto do glpi
chamados_df = pd.read_csv('glpi.csv', sep=';')

#Cria um novo dataframe apenas com os valores necessarios
novo_dataframe = chamados_df[["Atribuído para - Técnico", "ID", "Entidade"]]


qtd=len(novo_dataframe.value_counts(['ID']))
usuarios = len(novo_dataframe.value_counts(['Atribuído para - Técnico']))
listaAnalistas = list(novo_dataframe['Atribuído para - Técnico'].unique())

print(type(listaAnalistas))