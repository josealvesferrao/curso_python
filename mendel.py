def mendel (pl):
    """Esta função simula a proporção de flores brancas obtidas na
    geração F2 da experiência de Mendel. A função tem como argumento
    número de plantas usadas para determinar essa proporção."""

    import random
    flores = ["roxa", "roxa", "roxa", "branca"]
    rx = 0
    br = 0
    for i in range (0, pl):
        random.shuffle(flores)
        flor = random.choice(flores)
        if flor == "roxa":
            rx += 1
        else:
            br += 1
    print("Proporção de flores brancas:", br/pl)

mendel(10000)
