def preg_fig (brad_org, brad_pelo, chol_org, chol_pelo):
    """..."""
    
    from matplotlib import pyplot as plt
    
    #Cria uma figura e exibe
    fig = plt.figure()
    fig.suptitle("Número de organismos no pelo das preguiças", fontsize = 18)

    plt.subplot(121)
    plt.plot(brad_pelo, brad_org)
    plt.title("Bradypus", fontsize = 15)
    plt.xlabel("comprimento do pelo (cm)", fontsize = 13)
    plt.ylabel("número de organismos", fontsize = 13)
    plt.grid(which = "major", axis = "y", color='k', linestyle='--', linewidth=0.5)

    plt.subplot(122)
    plt.plot(chol_pelo, chol_org, color = "r")
    plt.title("Choloepus", fontsize = 15)
    plt.xlabel("comprimento do pelo (cm)", fontsize = 13)
    plt.ylabel("número de organismos", fontsize = 13)
    plt.grid(which = "major", axis = "y", color='k', linestyle='--', linewidth=0.5)

    fig.show()

