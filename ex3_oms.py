# Sugestão de resolução dos exercícios da sessão 3

# Escreva um pequeno script que percorra o seguinte tuplo usando um ciclo for e imprima na Shell do Python todas as bactérias

# Copiar o tuplo "agentes_tuplo" a partir do ficheiro agentes.txt

agentes_tuplo = (("bactéria", "Streptococcus tipo A"), ("vírus", "hepatite C"), ("vírus", "VIH-1"), ("bactéria", "Klebsiella pneumoniae"),
           ("vírus", "citomegalovírus"), ("vírus", "influenza"), ("parasita", "Leishmania"), ("bactéria", "Salmonella"), ("vírus", "norovírus"),
           ("parasita", "Plasmodium falciparum"), ("bactéria", "Shigella"), ("bactéria", "Staphylococcus aureus"), ("vírus", "dengue"),
           ("bactéria", "Streptococcus tipo B"), ("bactéria", "Escherichia coli"), ("bactéria", "Mycobacterium tuberculosis"), ("vírus", "vírus sincicial respiratório"))

#print(agentes_tuplo)

print("As bactérias são:\n")

for i in range(0,len(agentes_tuplo)): # Ciclo for para iterar em sequência numérica com a dimensão do tuplo, de modo a usar-se o número para consultar o tipo de agente usando a indexação de tuplo do Python
    if agentes_tuplo[i][0] == "bactéria": # Condição que compara o agente identificado em cada iteração com a string "bactéria", quando é verdadeira imprime o agente. Ex: na primeira iteração o valor/conteúdo da variável "i" é "zero", sendo assim a condição é "se agentes_tuplo[0][0] for igual a bactéria", imprimir o respetivo agente, que na primeira iteração será "agentes_tuplo[0][1] igual Streptococcus tipo A"
        print(agentes_tuplo[i][1])

# Em alternativa usar o método de descompactação de um tuplo, por atribuição dos itens a novas variáveis, pex:

print("\nAs bactérias são:\n")

for tuplo in agentes_tuplo: # Ciclo for para iterar dentro do tuplo, a cada iteração a variável tuplo vai "conter" um tuplo interno
    #print(tuplo) # Sugestão de descomentar este print para observar na shell qual o valor/conteúdo da variável tuplo a cada iteração. Vai ser um tuplo (singular), correspondente a cada tuplo interno ("subtuplo") do tuplo agentes_tuplo
    (agente, especie) = tuplo
    if agente == "bactéria":
        print(especie)



# Efetue uma atualização da lista de agentes de acordo com as seguintes alterações e, no final, ordene e imprima a lista:

# Inclua a bactéria Yersinia

# Copiar a lista "agentes_lista" a partir do ficheiro agentes.txt

agentes_lista = ["Streptococcus tipo A", "hepatite C", "VIH-1", "Klebsiella pneumoniae",
                 "citomegalovírus", "influenza", "Leishmania", "Salmonella", "norovírus",
                 "Plasmodium falciparum", "Shigella", "Staphylococcus aureus", "dengue",
                 "Streptococcus tipo B", "Escherichia coli", "Mycobacterium tuberculosis",
                 "vírus sincicial respiratório"]

agentes_lista.append("Yersinia") # Usar o método append() para adicionar um novo elemento à lista

# Elimine o vírus dengue

agentes_lista.remove("dengue") # Usar o método remove() para eliminar um elemento da lista

# Substitua a "Escherichia coli" pela "Escherichia coliextraintestinal"

agentes_lista[13] = "Escherichia coli extraintestinal" # Apenas se conseguirmos saber facilmente o índice do elemento que se pretende substituir

# Em alternativa, implementar um método que permite fazer esta alteração, ou generalizar para qq outra substituição, quando temos listas muito grandes. Usar um ciclo.

nome_original = "Escherichia coli"
nome_novo = "Escherichia coli extraintestinal"

for index in range(0, len(agentes_lista)):
    if agentes_lista[index] == nome_original:
        agentes_lista[index] = nome_novo

agentes_lista.sort()

print("\nA nova lista, ordenada, de agentes patogénicos da OMS 2025 é:", agentes_lista)


# Criar um programa que faça a tradução proteica e apresente a sequência da proteína beta-globina

# Copiar o dicionário cod_gen a partir do ficheiro 'codigo_genetico' 

cod_gen = {'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
           'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
           'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
           'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
           'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
           'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
           'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
           'TAC':'Y', 'TAT':'Y', 'TAA':'X', 'TAG':'X', 'TGC':'C', 'TGT':'C', 'TGA':'X', 'TGG':'W'}

# Copiar a sequência codificante do gene da beta-globina obtida no exercício da sessão 2 e guardar numa variável, ou usar a variável onde ficou armazenada se esta estiver criada previamente no mesmo ficheiro do editor de Python

cod_seq = "ATGGTGCACCTGACTCCTGAGGAGAAGTCTGCCGTTACTGCCCTGTGGGGCAAGGTGAACGTGGATGAAGTTGGTGGTGAGGCCCTGGGCAGGCTGCTGGTGGTCTACCCTTGGACCCAGAGGTTCTTTGAGTCCTTTGGGGATCTGTCCACTCCTGATGCTGTTATGGGCAACCCTAAGGTGAAGGCTCATGGCAAGAAAGTGCTCGGTGCCTTTAGTGATGGCCTGGCTCACCTGGACAACCTCAAGGGCACCTTTGCCACACTGAGTGAGCTGCACTGTGACAAGCTGCACGTGGATCCTGAGAACTTCAGGCTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAAGAATTCACCCCACCAGTGCAGCCACACCTATCAGTGGTGTGGCTAATGCCCTGGCCCACAACTCCTGGGCAACGTGCTGGTCTGTGTGCTGGCCCATCACTTTGGCAAATAATTCACCCCACCAGTGCAGGCTGCCTATCAGAAAGTGGTGGCTGGTGTGGC"

proteina = "" # Criar variável vazia de tipo/classe string para armazenar a sequência da proteína, permitindo concatenar (ir adicionando) a letras (aminoácidos) sequencialmente

for index in range(0, len(cod_seq),3):
    proteina = proteina + cod_gen[cod_seq[index:index+3]]
print("\nA sequência da proteína beta-globina é:\n", proteina)


