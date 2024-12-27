print("Bem vindo a calculadora de IMC")

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

imc = peso / (altura ** 2)

print(f"Seu IMC é {imc}")

if imc < 18.5:
    print("Magreza")
elif imc >= 18.5 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obesidade")
else:
    print("Obesidade Grave")