x = 100 # Variável global

def massa_corp(p, a):
    """
    Esta função calcula o índice de massa corporal (IMC) usando os valores de peso (kilogramas) e altura (metros).
    A função usa 2 argumentos, o peso (p) e a altura (a), por esta ordem.
    """
    x = 500 # Variável local
    IMC = p / a**2
    print("O seu IMC é ", round(IMC, 2))
    print("o valor da variável x dentro da função, ou seja, como variável local, é ", x)
massa_corp(65, 1.70)

print("o valor da variável x fora da função, ou seja, como variável global, é ", x)
