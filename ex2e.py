file = open(r"C:\Users\lmrvr_000\Desktop\Curso_Python_OBIO\exercícios\Homo_sapiens_beta-globin_gene_sequence.txt", "r")
seq = file.read()
inv_comp = ""
for i in range(0, len(seq)):
    if seq[i] == "A":
        inv_comp = inv_comp + "T" #(ou inv_comp += 'T')
    elif seq[i] == "C":
        inv_comp = inv_comp + "G"
    elif seq[i] == "G":
        inv_comp = inv_comp + "C"
    elif seq[i] == "T":
        inv_comp = inv_comp + "A"
    else:
        inv_comp = inv_comp + "N"
print (inv_comp[::-1])
file.close()
