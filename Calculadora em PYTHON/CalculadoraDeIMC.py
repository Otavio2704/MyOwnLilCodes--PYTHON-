#Pega o peso e a altura em Quilos e Metros respectivamente
def obter_dados():
    peso = float(input('Insira seu peso em quilos (exemplo: 70kg): '))
    altura = float(input('Agora insira sua altura em metros (ex: 1.80): '))
    return peso, altura

#Calculado o IMC
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

#Classificar o resultado de IMC
def classificar_imc(imc):
    if imc < 18.5:
        return f'Seu IMC é de {imc:.2f}, então você está abaixo do peso normal.'
    elif 18.5 <= imc <= 24.9:
        return f'Seu IMC é de {imc:.2f}, então você está no peso normal.'
    elif 25 <= imc <= 29.9:
        return f'Seu IMC é de {imc:.2f}, então você está com excesso de peso.'
    elif 30 <= imc <= 34.9:
        return f'Seu IMC é de {imc:.2f}, então você é um obeso de classe I.'
    elif 35 <= imc <= 39.9:
        return f'Seu IMC é de {imc:.2f}, então você é um obeso de classe II.'
    elif imc >= 40:
        return f'Seu IMC é de {imc:.2f}, então você é um obeso de classe III.'
    else:
        return 'Verifique se você inseriu os dados corretos.'

def main():
    peso, altura = obter_dados()
    imc = calcular_imc(peso, altura)
    resultado = classificar_imc(imc)
    print(resultado)

# Executa o programa
main()
