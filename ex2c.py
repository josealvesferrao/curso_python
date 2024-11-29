file = open(r"C:\Users\lmrvr_000\Desktop\Curso_Python_OBIO\exercícios\Homo_sapiens_beta-globin_gene_sequence.txt", "r")
seq = file.read()
cod_seq = seq[1611:1703] + seq[1833:2056] + seq[2906:3015] + seq[3971:4072] 
print (cod_seq, len(cod_seq), len(cod_seq)//3)
file.close()
