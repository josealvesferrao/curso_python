file = open(r"C:\Users\lmrvr_000\Desktop\Curso_Python_OBIO\exercícios\Homo_sapiens_beta-globin_gene_sequence.txt", "r")
seq = file.read()
for i in range(0, 1612):
    if seq[i:i+6] == "ATAAAA":
        print (i, "-", i+6)
        

