import random,os

n = 1
cont = 0
soma = 0
posi = 0
nega = 0
posiPer = 0
negaPer = 0
posiCont = 0
negaCont = 0

while ( n < 10):
  n = random.randint(-5,10)
  print(n)
  cont = cont + 1
  soma = soma + n
  media  = soma / cont
  #se for positivo
  if( n > 0):
    posi = posi + 1
  #se for negativo
  if ( n < 0 ):
    nega = nega + 1
 
    
else:
  #calculo Percentual positivo
  posiPer = posi / cont
  positPer2 = posiPer * 100
  
  #calculo Percentual negativo
  negaPer = nega / cont
  negaPer2 = negaPer * 100
  
  #resultados
  os.system('clear')
  print(f"Média:{media:.2f}")
  print("Quantidade Positivos:",posi)
  print("Quantidade Positivos:",nega)
  print(f"Percentual negativo:{negaPer2:.2f}")
  print(f"Percentual positivo:{positPer2:.2f}")
  