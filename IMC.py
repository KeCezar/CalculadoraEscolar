try:
  peso_input= input("Peso(Kg): ").replace(',', '.').replace('kg', '')
  peso = float(peso_input)
  altura_input = input("Altura(m ou cm): ").replace(',', '.').replace('m', '').replace('cm', '')
  # Lista de variações para "sim" e "não"
  variacoes_sim = ["sim", "s", "yes", "Yes", "Sim", "SIM", "SIm", "SiM", "sIM", "sIm", "siM", "Yes", "YeS", "yES", "yeS", "Y", "S", "y"]  
  variacoes_nao = ["não", "nao", "n", "no", "Não", "NÃo", "NÃO", "Nao", "N", "No", "NãO", "nÃO", "nAO", "nAo", "nÃo", "NO"]
  
  if '.' in altura_input:
      altura = float(altura_input)
  else:
      altura = float(altura_input) / 100
      
  if peso <= 0 or altura <= 0:
      print("Peso e altura devem ser valores positivos maiores que zero.")
      exit()
  
  IMC = peso / altura**2
  
  if IMC >= 60:
      print("Este valor está acima da média mundial de saúde. Caso tenha alguma dúvida sobre os dados preenchidos digite 'Não' ou feche e abra novamente o programa.")
      resposta = input("Gostaria de continuar com o cálculo? (Sim/Não): ").strip().lower()
      if resposta in variacoes_nao:
          print("Resetando...")
          exit()
      elif resposta not in variacoes_sim:
          print("Resposta inválida. Reiniciando...")
          exit()
  elif IMC <= 18.5:
      classificacao = "abaixo do peso"
  elif IMC <= 24.9:
      classificacao = "peso ideal"
  elif IMC <= 29.9:
      classificacao = "levemente acima do peso"
  elif IMC <= 34.9:
      classificacao = "obesidade grau I"
  elif IMC <= 39.9:
      classificacao = "obesidade grau II (severa)"
  else:
      classificacao = "obesidade grau III (mórbida)"

  print(f"Seu IMC é {IMC:.1f}, ou seja, {classificacao}.")
          
except ValueError:
    print("Digite apenas números.")
except ZeroDivisionError:
    print("Altura não pode ser zero.")

# Abaixo de 18,5   | Abaixo do peso          

# Entre 18,6 e 24,9 | Peso ideal (parabéns)  

# Entre 25,0 e 29,9 | leevmente acima do peso

# Entre 30,0 e 34,9 | Obesidade grau I 

# Entre 35,0 e 39,9 | Obesidade grau II (severa)

#Maior ou igual a 40 | Obesidade grau III (mórbida) 