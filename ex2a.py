file = open(r"Homo_sapiens_beta-globin_gene_sequence.txt", "r")
seq = file.read()
print (len(seq))
file.close()
