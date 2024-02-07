def verificar_permuta(texto1, texto2) -> bool:
  if(''.join(sorted(texto1.upper()))==''.join(sorted(texto2.upper()))):
    return 1
  
  return 0

texto1 = input('Insira uma palavra: ')
texto2 = input('Insira uma palavra: ')

if(verificar_permuta(texto1,texto2)):
    print('Uma palavra e permutacao da outra')
    exit()  
  
print('Uma palavra NAO e permutacao da outra')
