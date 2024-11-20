import urllib
import requests
from bs4 import BeautifulSoup
import re
url = "https://olhonavaga.com.br/rankings/ranking?id=72022"
nome_candidato = "Ormazabal"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

specific_div = soup.find('label', id='form:j_idt457')
if specific_div:
  child_element = specific_div.find('span', class_='ui-outputlabel-label')
  inscritos = int(child_element.text.replace(".",""))
  print("numero de inscritos:", inscritos)

specific_div = soup.find('label', id='form:participants')
if specific_div:
  child_element = specific_div.find('span', class_='ui-outputlabel-label')
  participantes = int(child_element.text.replace(".",""))
  print("numero de participantes do ranking:", participantes)

fator_multiplicador = inscritos/participantes
#print("fator multiplicador:", fator_multiplicador)

child_soup = soup.find_all('label')
for i in child_soup:
    if(i.string == nome_candidato + " "):
      #print(i)
      res = [j for j in range(len(str(i))) if str(i).startswith(":", j)] 
      #print(str(res))

      pos = ""
      j = int(res[2])
      while j+1 < int(res[3]):
        pos = pos + str(i)[j+1]
        j = j + 1

      pos = int(pos)+1
      #pos = int(str(i)[68]+str(i)[69])+1
      print("posição no ranking: ", pos)
      posicao_final = int(pos*fator_multiplicador)
      print("possível posição no resultado final: ", posicao_final)
      break

if posicao_final > 126:
  print("REPROVADO")
elif posicao_final > 21 and posicao_final < 80:
  print("CADASTRO RESERVA PREMIUM")
elif posicao_final > 80 and posicao_final < 127:
  print("CADASTRO RESERVA")
else:
  print("APROVADO")
