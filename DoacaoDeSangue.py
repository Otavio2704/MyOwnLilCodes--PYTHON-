print('\nEsta é uma pesquisa para analisar se você é uma pessoa apta para realizar doação de sangue:')

idade = int(input('\nQual sua idade? '))
if idade >= 16 and idade <= 69:
    print('Sua idade é adequada para a doação')
elif idade < 16:
    print('Você menor de idade para realizar a doação')
else:
    print('Sua idade é avançada para a doação')

peso = float(input("\nInsira seu peso: "))
if peso >= 50:
    print('Você possui um peso adequado para a doação')
else:
    print('Seu peso é inadequado para a doação')


desc = input("\nVocê dormiu pelo menos 5 horas nas últimas 24 horas? ").lower()
if desc == "sim":
    print('ótimo, você possui horas adequadas de descanso para a doação')
else:
    print('Necessita mais horas de descanso para a doação')

alim = input('\nEvitou alimentação gordurosa nas 4 horas que antecedem a doação? ').lower()

if alim == "sim":
    print('ótimo, você possui ótimos hábitos alimentares para a doação')
else:
    print('Necessita de uma alimentação mais adequada para a doação')

doenca = input ("\nPossui Hepatites B e C, AIDS (vírus HIV), doenças associadas aos vírus HTLV I e II ou Doença de Chagas? ").lower()
if doenca == "sim":
    print('Então não poderá realizar a doação')
else:
    print('Ótimo, está saudável')

print('\n1- Caso você tenha entre 16 e 17 anos, peça autorização para seu responsável; caso tenha entre 18 e 69 anos, poderá realizar a doação')
print('2- Caso tenha menos de 50 Kg, não poderá realizar a doação; senão, poderá realizar a doação normalmente')
print('3- Se você dormiu menos de 5 horas nas últimas 24 horas, não poderá realizar a doação')
print('4- Se caso tenha uma alimentação inadequada antes da doação, não poderá efetuar ela')
print('5- E caso possui alguam doença citada na pesquisa, também não poderá doar sangue')
print('\nTenha um ótimo dia, uma ótima tarde e uma ótima anoite :)')
