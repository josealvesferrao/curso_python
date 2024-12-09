
def contagens (ficheiro):

    """Esta função recebe uma tabela Excel com os dados de incidência das doenças transmissíveis sujeitas a declaração obrigatória em Portugal entre 2014 e 2018 (SINAVE).
    O número de casos notificados estão dispostas por linhas, sendo que o delimitador é um (;).
    As colunas do ficheiro têm a seguinte informação: ano e mês de notificação, região de saúde de notificação, área de residência NUTS III, doença, sexo, grupo etário e nº casos notificados.
    A função tem 1 único argumento que é a localização/nome do ficheiro Excel.

    Pressupostos: Ficheiro formato csv com 7 colunas. Coluna 1 (índice 0 na lista): ano e mês de notificação. Coluna 2 (índice 1): região de saúde de notificação.
    Coluna 3 (índice 2): área de residência NUTS III. Coluna 4 (índice 3): doença. Coluna 5 (índice 4): sexo. Coluna 6 (índice 5): grupo etário. Coluna 7 (índice 6): nº casos notificados.

    Garantias: Devolve nº total de doenças e de casos notificados. Imprime nome das doenças. Nº de casos de Febre Q em residentes no Algarve. Nº de casos de Gonorreia em homens entre 15-24 anos residentes na AML. 
    """
    
    import csv

    data = open (ficheiro)

    tabela = csv.reader(data, delimiter = ';')

    headers = next(tabela) # Para saltar/excluir a linha de cabeçalho do ficheiro
    
    lista_doencas = []

    total_casos = 0

    casos_febre_q = 0

    casos_gonorreia = 0
    
    for linha in tabela: # iterar com um ciclo for, cada linha da tabela que foi convertida numa lista com 7 elementos, correspondentes a cada uma das 7 colunas da tabela
        #print(linha)
        total_casos = total_casos + int(linha[6]) # acumulador (acumula/soma os valores dos casos notificados)
        if linha[3] not in lista_doencas: # se a doença ainda não existir dentro da lista de doenças, então:
            lista_doencas.append(linha[3]) # adicionar a nova doença à lista de doenças
        if linha[3] == "Febre Q" and linha[2] == "Algarve": # Se a doença é Febre Q e a residência é Algarve, então:
            casos_febre_q = casos_febre_q + int(linha[6]) # acumulador (acumula/soma os valores dos casos notificados)
        if linha[3] == "Gonorreia" and linha[4] == "Masculino" and linha[5] == "15-24 anos" and linha[2] == "Area Metropolitana de Lisboa":
            casos_gonorreia = casos_gonorreia + int(linha[6])

    print("O nº total de doenças notificadas foi de: ", len(lista_doencas), ", e o nº total de casos notificados foi de: ", total_casos, "\n")

    print("O nome das doenças é: ", lista_doencas, "\n")

    print("O nº de casos de Febre Q notificados no Algarve é: ", casos_febre_q, "\n")

    print("O nº de casos de Gonorreia em indivíduos do sexo masculino entre os 15 e os 24 anos de idade residentes na AML é de: ", casos_gonorreia, "\n")
    
    data.close()

contagens("C:\\Users\\jose.ferrao\\Desktop\\Curso_Python_Out2024\\Slides_novos_2024\\Sessao_4_5_6\\doencas-de-declaracao-obrigatoria.csv")
        
        
