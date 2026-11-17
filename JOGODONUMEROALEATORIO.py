import random 


numsort = random.randint(1,20)

win = False

while win == False:
  numChoose = int(input("Escolha um numero de entre 1 a 20"))
  if numChoose == int:
    if numChoose >= 1 and < 20:
          if numsort > numChoose:
            print("Errouuu!!! O numero é maior que "+str(numChoose)+"...")
          elif numsort < numChoose:
            print("Errouuu!!! O numero é menor que "+str(numChoose)+"...")
          elif numsort == numChoose:
            print("Acertou! Boa!! Então o numero era "+str(numsort))
            
      else:
      print("Numero fora do escopo!")
