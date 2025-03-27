def mendel_2 ():
    """Esta função calcula o número mínimo de plantas necessário para que a
    proporção de flores brancas seja de 0.25."""

    import random
    flores = ["roxa", "roxa", "roxa", "branca"]
    rx = 0
    br = 0
    p = 0
    while p != 0.25:
        flor = random.choice(flores)
        if flor == "roxa":
            rx += 1
        else:
            br += 1
        p = br/(br+rx)
        print(p)#opcional
        
    print("Número de plantas:", br+rx)

mendel_2()
