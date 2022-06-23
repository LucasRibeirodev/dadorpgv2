import random as rd
import time as tm
# a lista dos dados ou dados disponiveis
print("Dados Disponíveis: D3 [3], D4 [4], D6 [6], D8 [8], D10 [10], D12 [12], D20 [20], D100 [100]")

# insere o lado do dado conform disponivel
num_dado = int(input('Digite a quantidade de lados do seu dado: '))

# insere a quantidade de dados que irei jogar
digite = int(input('Digite a quantidade de dados que quer jogar: '))
soma = 0
# estou gerando um valor aleatório para o numero do dado selecionado
for i in range(0,digite):
    resultado = rd.randint(1, num_dado)
    print(f'O o seu resultado é: {resultado}')
    soma += resultado
    tm.sleep(1)


print(f'\n A soma dos dados é: ', soma)
tm.sleep(1)

print('\n Obrigado por usar nosso Sistema!')