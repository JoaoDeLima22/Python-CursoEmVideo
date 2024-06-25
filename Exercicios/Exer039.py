from datetime import date

ano = date.today().year

n1 = int(input('informe o ano do seu aniversário'))
idade=(ano-n1)
if idade < 18:
  print('Ainda não esta na a época de você se alistar')
  
elif idade > 18:
  print('Vá rapido procurar se alistar, pois ja passou da época de se alistar')

elif idade ==18:
  print('Você deve se alistar esse ano')