
def preguicas (ficheiro):

    """Esta função recebe uma tabela Excel com medidas do comprimento do pelo e do
    número de algas e de insectos presentes no pelo de 2 géneros de preguiças.
    A função devolve uma lista dos valores do comprimento do pelo e uma lista do
    número total de organismos (algas + insectos) emparelhados, por cada género de
    preguiça. O argumento da função é a localização/nome do ficheiro Excel."""

    import csv
    data = open (ficheiro)
    tabela = csv.reader (data, delimiter =';')
    headers = next(tabela)
    brad_org = []
    brad_pelo = []
    chol_org = []
    chol_pelo = []
    for linha in tabela:
        num_org = int(linha[3]) + int(linha[4])
        if linha[0] == "Bradypus":
            brad_org.append(num_org)
            brad_pelo.append(float(linha[2]))
        else:
            chol_org.append(num_org)
            chol_pelo.append(float(linha[2]))
    data.close()
    return brad_pelo
 
