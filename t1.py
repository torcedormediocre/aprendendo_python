def verificar_permuta(texto1, texto2) -> bool:
  # Seu código aqui
  if(''.join(sorted(texto1.upper()))==''.join(sorted(texto2.upper()))):
    return 1
  
  return 0

texto1 = 'bambi'
texto2 = 'bimba'

if(verificar_permuta(texto1,texto2)):
    print('Foi')
    #exit()  
  
print('Nao foi')
