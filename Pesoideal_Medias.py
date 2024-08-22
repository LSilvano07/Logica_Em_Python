#1) Desenvolva um código python que calcula o peso ideal de 100 pessoas. Deve receber a altura e o sexo. Usar um loop para validar se o sexo está correto (H ou M).
#para Homens: Peso Ideal = (72.7*altura) - 58
#para Mulheres: Peso Ideal = (62.1*altura) - 44.

#for _ in range(101):
    #altura = float(input("Digite sua altura (1.73ex): "))
    #sexo = input("Digite H ou M: ").upper()
    #while sexo not in ["H", "M"]:
        #sexo = input("Digite H homemou M para mulher: ").upper()
    #if "H" in sexo:
        #print(f"H e Seu peso ideal é: {(72.7 * altura) - 58:.2f}")
    #elif "M" in sexo:
        #print(f"M e Seu peso ideal é: {(62.1 * altura)- 44:.2f}")

#2 Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em um dicionário.
#Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram.
meses = {
    "Janeiro": 0, 
    "Fevereiro": 0, 
    "Março": 0,
    "Abril": 0,
    "Maio": 0,
    "Junho": 0, 
    "Julho": 0,
    "Agosto": 0,
    "Setembro": 0,
    "Outubro": 0,
    "Novembro": 0,
    "Dezembro": 0
    }
for mes, media in meses.items(): 
    temperatura = float(input(f"Digite a temperatura do mês {mes}: "))
    meses[mes] = temperatura

media_anual = sum(meses.values()) / len(meses)
acima_media = {mes: temp for mes, temp in meses.items() if temp > media_anual}
print(f"meses acima da média: {acima_media}")