import pandas as pd

def listar():
    print("#Criando lista txt dos chamados")
    #Cria um novo dataframe com esse excel
    chamados_Atribuido_df = pd.read_excel("provisorio.xlsx", "Chamados Atribuidos")

    #Cria a lista de Analistas com chamados
    usuarios = len(chamados_Atribuido_df.value_counts(['Atribuído para - Técnico']))
    listaAnalistas = list(chamados_Atribuido_df['Atribuído para - Técnico'].unique())

    #calcula o numero de chamados
    qtd=len(chamados_Atribuido_df.value_counts(['ID']))

    #Cria a lista de Analistas com chamados
    usuarios = len(chamados_Atribuido_df.value_counts(['Atribuído para - Técnico']))
    #print('O numero de analistas com chamados: %d\n\n'%usuarios)
    ListaAnalistas = chamados_Atribuido_df['Atribuído para - Técnico'].unique()
    ListaAnalistas = list(ListaAnalistas)
    #print(ListaAnalistas)

    #Transforma em txt e organiza os valores no arquivo de texto
    with open('chamados.txt', 'w') as f:
        pass

    with open('chamados.txt', 'a') as f:
        f.write('*TOTAL FIELD SP* = %d\n'%qtd)
        f.write('%d Analistas com chamados\n'%usuarios)
        f.write('----------------------------\n')

    #Cria o texto para ser enviado para o whatsUp
    for nome in ListaAnalistas:
        with open('chamados.txt', 'a') as f:
            f.writelines('*%s*\n'%nome)
        analista = chamados_Atribuido_df.loc[chamados_Atribuido_df['Atribuído para - Técnico'] == nome, ['ID','Entidade']]
        analista.to_csv("chamados.txt", header=None, index=None, sep='-', mode='a')
        with open('chamados.txt', 'a') as f:
            f.writelines('\n')
    print("Feito")