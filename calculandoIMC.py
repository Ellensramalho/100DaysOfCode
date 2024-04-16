#Declarar variavéis 
altura= input("Forneça a altura:")
peso = input("Forneça o peso: ")

#Expressão de calcular o IMC
valor = (float(peso)/float(altura)**2)

#Arredondar valor 
valor_arrendodado= round(valor,2)

print("Seu imc é ", + valor_arrendodado)