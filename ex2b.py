file = open(r"Homo_sapiens_beta-globin_gene_sequence.txt", "r")
seq = file.read()
number_of_A = 0
number_of_C = 0
number_of_G = 0
number_of_T = 0
for base in seq:
    if base == "A":
        number_of_A = number_of_A + 1
    if base == "C":
        number_of_C = number_of_C + 1
    if base == "G":
        number_of_G = number_of_G + 1
    if base == "T":
        number_of_T = number_of_T + 1
number_of_N = len(seq) - number_of_A - number_of_C - number_of_G - number_of_T
print ("A:",number_of_A, "C:", number_of_C, "G:", number_of_G, "T:", number_of_T, "N:", number_of_N)
file.close()
