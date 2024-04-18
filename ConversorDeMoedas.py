print("---------------------------------------------" "\n1 - Dólar",
"\n2 - Euro",
"\n3 - Libra","\n---------------------------------------------")

tipoMoeda = int(input("Escolha qual tipo de moeda você quer converter: "))

def converter(tipoMoeda):
    if tipoMoeda == 1:
      print("O valor será convertido de dólar para real")
      valor = float(input("Digite qual valor você quer converter:"))
      valor = valor * 5.23
      valor_arredondado = round(valor, 2)
      print("O valor após a conversão é de:", valor_arredondado)
    
    elif tipoMoeda == 2: 
      print("O valor será convertido de Euro para Real: ")
      valor = float(input("Digite qual valor você quer converter: "))
      valor = valor * 5.59
      valor_arredondado = round(valor, 2)
      print("O valor após a conversão é de:", valor_arredondado)
    
    elif tipoMoeda == 3:
      print("O valor será convertido de Libra para Real: ")
      valor = float(input("Digite qual valor você quer converter: "))
      valor = valor * 6.52
      valor_arredondado = round(valor, 2)
      print("O valor após a conversão é de:", valor_arredondado)
converter(tipoMoeda)
