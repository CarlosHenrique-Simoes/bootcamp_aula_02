print("Bem vindo a calculadora de gorjetas.")
valor_da_conta = float(input("Digite o valor total da conta: "))
porcentual = float(input("Digite o percentual de gorjeta 10, 12 ou 15: "))

if porcentual == 10:
    valor_da_conta = valor_da_conta * 1.1

elif porcentual == 12:
    valor_da_conta = valor_da_conta * 1.12

elif porcentual == 15:
    valor_da_conta = valor_da_conta * 1.15

else:
    print("Opção inválida")

quantidade_de_pessoas = int(input("Digite a quantidade de pessoas: "))
valor_da_conta = valor_da_conta / quantidade_de_pessoas

print(f"Cada pessoa deve pagar R$ {valor_da_conta:.2f}")
