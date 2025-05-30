#Função que verifica a idade do usuário
def verificar_idade():
    idade = int(input('\nQual sua idade? '))
    if 16 <= idade <= 69:
        print('Sua idade é adequada para a doação')
    elif idade < 16:
        print('Você é menor de idade para realizar a doação')
    else:
        print('Sua idade é avançada para a doação')
    return idade

#Função que verifica o peso do usuário
def verificar_peso():
    peso = float(input("\nInsira seu peso: "))
    if peso >= 50:
        print('Você possui um peso adequado para a doação')
    else:
        print('Seu peso é inadequado para a doação')
    return peso

#Função que verifica horas de descanso do usuário
def verificar_descanso():
    desc = input("\nVocê dormiu pelo menos 5 horas nas últimas 24 horas? ").lower()
    if desc == "sim":
        print('Ótimo, você possui horas adequadas de descanso para a doação')
        return True
    else:
        print('Necessita mais horas de descanso para a doação')
        return False

#Função que verifica se o usuário está se alimentando bem
def verificar_alimentacao():
    alim = input('\nEvitou alimentação gordurosa nas 4 horas que antecedem a doação? ').lower()
    if alim == "sim":
        print('Ótimo, você possui ótimos hábitos alimentares para a doação')
        return True
    else:
        print('Necessita de uma alimentação mais adequada para a doação')
        return False

#Função que verifica se o usuário possui alguma doença
def verificar_doencas():
    doenca = input ("\nPossui Hepatites B e C, AIDS (vírus HIV), doenças associadas aos vírus HTLV I e II ou Doença de Chagas? ").lower()
    if doenca == "sim":
        print('Então não poderá realizar a doação')
        return True
    else:
        print('Ótimo, está saudável')
        return False

#Função que exibe as considerações finais
def exibir_instrucoes_finais():
    print('\n1- Caso você tenha entre 16 e 17 anos, peça autorização para seu responsável; '
          'caso tenha entre 18 e 69 anos, poderá realizar a doação')
    print('2- Caso tenha menos de 50 Kg, não poderá realizar a doação; senão, poderá realizar a doação normalmente')
    print('3- Se você dormiu menos de 5 horas nas últimas 24 horas, não poderá realizar a doação')
    print('4- Se caso tenha uma alimentação inadequada antes da doação, não poderá efetuar ela')
    print('5- E caso possua alguma doença citada na pesquisa, também não poderá doar sangue')
    print('\nTenha um ótimo dia, uma ótima tarde e uma ótima noite :)')

#Função que realiza a pesquisa
def pesquisa_doacao_sangue():
    print('\nEsta é uma pesquisa para analisar se você é uma pessoa apta para realizar doação de sangue:')
    idade = verificar_idade()
    peso = verificar_peso()
    descanso = verificar_descanso()
    alimentacao = verificar_alimentacao()
    doencas = verificar_doencas()
    exibir_instrucoes_finais()

# Executar a pesquisa
pesquisa_doacao_sangue()
