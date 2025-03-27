# Sugestão de resolução dos exercícios da sessão 2

# a) Comprimento total da sequência do gene da beta-globina

gene_seq_file = open("Homo_sapiens_beta-globin_gene_sequence.txt", "r") # Abrir o ficheiro em modo de leitura ("r"), associando-o à variável gene_seq_file

gene_seq = gene_seq_file.read() # Ler o conteúdo do ficheiro e guardá-lo na variável gene_seq

#print(gene_seq)

print("O comprimento total da sequência do gene da beta-globina é:", len(gene_seq))

  
# b) Número total de nucleótidos A (adenina)

number_A = 0 # Inicializar contador de A´s (adenina)

number_others = 0 # Inicializar um contador para os restantes nucleótidos (C, G, T, N)

for nucleotide in gene_seq: # Ciclo for para iterar sobre a sequência do gene
    if nucleotide == "A": # Condição, se for verdadeira, o bloco de código indentado abaixo vai incrementar a contagem no contador number_A
        number_A = number_A + 1 # Incremento do contador number_A
    else: # Se a condição não for satisfeita, ié, se for falsa, incrementa o contador dos restantes nucleótidos, o number_others
        number_others = number_others + 1 # Incremento do contador number_others

print("O número total de A´s é:", number_A)

# Em alternativa pode usar-se o elif para aproveitar o mesmo ciclo para contabilizar os restantes nucleótidos individualmente, inicializando os respetivos contadores previamente


# c) Concatenar as sequências dos 4 exões da beta-globina

exao1 = gene_seq[1611:1703] # Utilizar o slicing para obter substring correspondente a cada exão. Nota: Ajustar posição inicial devido à indexação do Python começar em zero
exao2 = gene_seq[1833:2056]
exao3 = gene_seq[2906:3015]
exao4 = gene_seq[3971:4072]

seq_cod = exao1 + exao2 + exao3 + exao4 # Concatenar as substrings dos exões para obter sequência codificante

print("A sequência codificante do gene é:\n", seq_cod)
    

# d) Determinar o comprimento total da sequência codificante

print("O comprimento da sequência codificante é:", len(seq_cod))


# e) Determinar o número de aminoácidos da proteína

print("O número de aa da proteína é:", len(seq_cod)//3) # Como cada aa é codificado por 3 nucleótidos, dividir o comprimento da sequência codificante por 3. Nota: usar divisão com duas barras para obter número inteiro e não decimal



# f) Identificar a localização (posições de início e fim) da sequência génica reguladora 'TATA_box‘ (motivo “ATAAAA”)

for index in range(0, 1612): # Ciclo for que itera sobre sequência numérica entre 0 e 1611, permitindo usá-los para fazer correspondência com as posições dos nucleótidos na sequência do gene e limitando a pesquisa do motivo à parte inicial do gene, antes do primeiro exão, uma vez que a TATA_box está associada ao promotor e à iniciação da transcrição. Se a pesquisa for feita na sequência completa do gene irão surgir mais ocorrências deste motivo, mas apenas o primeiro corresponde à TATA_box
    if gene_seq[index:index+6] == "ATAAAA": # Utiliza-se o conteúdo da variável index (zero na 1ª iteração, um na 2ª iteração, dois na 3ª iteração, etc até 1611) a cada iteração na sequência numérica entre 0 e 1611, para fazer slicing da sequência do gene (o início corresponde ao valor de index e o fim a index+6) e obter uma substring que é comparada com o motivo que pretendemos identificar. Quando a condição for verdadeira, imprimimos as respetivas posições identificadas.
        print("As posições da TATA_box são:", index+1, "-", index+6) # Adicionar +1 à posição de início para adequar à posição correcta no gene, devido à indexação do Python começar em zero.


# g) Obter a sequência inversa e complementar do gene da beta-globina

complementary_seq = "" # Criar variável vazia de tipo/classe string para armazenar a sequência complementar, permitindo concatenar (ir adicionando) os nucleótidos progressivamente

for nucleotide in gene_seq:
    if nucleotide == "A":
        complementary_seq = complementary_seq + "T"
    elif nucleotide == "T":
        complementary_seq = complementary_seq + "A"
    elif nucleotide == "C":
        complementary_seq = complementary_seq + "G"
    elif nucleotide == "G":
        complementary_seq = complementary_seq + "C"
    else:
        complementary_seq = complementary_seq + "N"

reverse_comp_seq = complementary_seq[::-1]

print("A sequência reversa e complementar é:\n", reverse_comp_seq)

# Em alternativa pode usar-se a função range no ciclo for para iterar numa sequência numérica (entre 0 e 4355) de modo a usar a indexação da string da sequência do gene, acedendo assim a cada nucleótido e fazendo a condição de comparação para obter a sequência complementar

rev_comp = ""

for i in range(0, len(gene_seq)): # Ciclo for para iterar numa sequência numérica entre 0 e 4355
    if gene_seq[i] == "A":
        rev_comp = rev_comp + "T"
    elif gene_seq[i] == "C":
        rev_comp = rev_comp + "G"
    elif gene_seq[i] == "G":
        rev_comp = rev_comp + "C"
    elif gene_seq[i] == "T":
        rev_comp = rev_comp + "A"
    else:
        rev_comp = rev_comp + "N"

#print("A sequência reversa e complementar é:\n", rev_comp[::-1])

gene_seq_file.close()
