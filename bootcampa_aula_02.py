print("Bem vindo a calculadora de gorjetas.")
valor_da_conta = float(input("Digite o valor total da conta: "))
porcentual = float(input("Digite o percentual de gorjeta 10, 12 ou 15: "))
quantidade_de_pessoas = int(input("Digite a quantidade de pessoas: "))
porcentual = porcentual / 100
valor_da_gorjeta = valor_da_conta * porcentual
valor_total = valor_da_conta + valor_da_gorjeta
valor_da_conta = valor_total / quantidade_de_pessoas
print(f"Cada pessoa deve pagar R$ {valor_da_conta:.2f}")
