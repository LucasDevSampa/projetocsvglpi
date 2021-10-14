import pandas as pd
from openpyxl import load_workbook

def converte(arquivo):
    #Carrega arquivo CSV
    arquivocsv = pd.read_csv(arquivo, sep=";")
    #print(arquivocsv.dtypes)
    #Coverte para tipo Excel com os valores Brutos
    arquivocsv.to_excel("arquivo.xlsx", sheet_name="Bruto", index=False)
    arquivoxls = pd.read_excel("arquivo.xlsx", sheet_name="Bruto")
    
    #Primeiro  Atribição X tecnico
    tecnicos  = arquivoxls[["Atribuído para - Técnico", "ID", "Entidade"]]
    #print(tecnicos.head)
    #Cria planilha so de Field
    tecnicos.to_excel("FieldSP.xlsx", sheet_name="Chamados Atribuidos")

    #print(tecnicos.info())
