agentes = ((“bactéria, “Streptococcus tipo A”), (“vírus”, “hepatite C”), ("vírus", "VIH-1"), (“bactéria”, "Klebsiella pneumoniae”), (“vírus”, “citomegalovírus”), (“vírus”, “influenza”), (“parasita”, “Leishmania”), (“bactéria”, “Salmonella”), (“vírus”, “norovírus”), (“parasita”, “Plasmodium falciparum”), (“bactéria”, “Shigella”), (“bactéria”, “Staphylococcus aureus”), (“vírus”, “dengue”), (“bactéria”, “Streptococcus tipo B”), (“bactéria”, “Escherichia coli”), (“bactéria”, “Mycobacterium tuberculosis”), (“vírus”, “vírus sincicial respiratório”))
print ("As bactérias são:")
for i in range(0, len(agentes)):
    if agentes[i][0] == "bactéria":
        print(agentes[i][1])
