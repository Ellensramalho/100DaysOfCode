import random;
chances_maximas = 5
tentativas_restantes = chances_maximas

palavras = ["Livros", "Bolsa", "Programação", "Celular", "Chave", "Fichario", "Tablet"]
palavra_aleatoria = random.choice(palavras)

while tentativas_restantes <= 5:
  palavra = input("Digite palavra: ")
  if palavra == palavra_aleatoria:
    print("A palavra está certa")
    break
  else: 
    print("A palavra não é essa, tente novamente")
    tentativas_restantes -= 1
    print("Você tem mais : ", tentativas_restantes)
  if tentativas_restantes == 0:
    print("Suas tentativas acabaram")
    print ("A palavra aleatoria é:", palavra_aleatoria)
    break