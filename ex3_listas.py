agentes = [“Streptococcus tipo A”, “hepatite C”, "VIH-1", "Klebsiella pneumoniae”, “citomegalovírus”, “influenza”, “Leishmania”, “Salmonella”, “norovírus”, “Plasmodium falciparum”, “Shigella”, “Staphylococcus aureus”, “dengue”, “Streptococcus tipo B”, “Escherichia coli”, “Mycobacterium tuberculosis”, “vírus sincicial respiratório”]
agentes.append("Yersinia")
agentes.remove("dengue")
agentes[15] = "Escherichia coli extraintestinal"
agentes.sort()
print (agentes)
