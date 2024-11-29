'''Este programa calcula o índice de massa corporal (IMC) a partir dos valores
de altura e peso introduzidos pelo utilizador, e devolve o respetivo estado
nutricional'''


peso = int(input ("Qual é o seu peso?"))
altura = float(input("Qual é a sua altura?"))
IMC = peso/altura**2
if IMC < 18.5:
    estado = "baixo peso"
elif 18.5<=IMC<25:
    estado = "peso normal"
elif 25<=IMC<29.9:
    estado = "excesso de peso"
else:
    estado = "obesidade"
print("O seu IMC é", round(IMC,2), "e corresponde a um estado nutricional de", estado)



              
