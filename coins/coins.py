# name of student: Rob Koster 
# number of student: 99067170
# purpose of program: wissel geld terug geven
# function of program: bereken hoe veel wissel geld iemand terug krijgt
# structure of program: sequenties

import builtins


toPay = int(float(input('Amount to pay: '))* 100) # hier mee vraag je aan de gebruiker hoeveel ze nog moeten betalen 
payed = int(float(input('Payed amount ')) * 100) # hier mee vraag je aan de gebruiker hoeveel ze all betalen hebben
change = payed - toPay # hier mee bereken je hoeveel wissel geld terug krijgen


result = []
if change > 0: # als het nog te moeten betalen gelijk is aan 0 worden de stappen van regel 17 tot 61 overgeslagen 
  coinValue = 500 # dit geeft coin een warden van 500
  
  while change > 0 and coinValue > 0: # dit kijkt of dat change en coinvalue bijden 0 zijn
    nrCoins = change // coinValue # dit deelt change door coinvalue en rond het af
    
    
    if nrCoins > 0: # dit kijkt of dat nr coins groter is dan 0
      print('return maximal ', nrCoins, ' coins of ', coinValue, ' cents!' ) # dit print hoeveel coins je moet terug geven
      nrCoinsReturned = int(input('How many coins of ' + str(coinValue) +  ' cents did you return? ')) # dit vraag hoe veel cent je terug hebt gegeven
      change -= nrCoinsReturned * coinValue # dit doet de coins terug gegeven keer de coin warden
      result.append(nrCoinsReturned)
      result.append(coinValue)
      

# comment on code below: dit geeft coin de goede waarden 
    if coinValue == 500:
      coinValue = 300
    elif coinValue == 300:
      coinValue = 200
    elif coinValue == 200:
      coinValue = 50
    elif coinValue == 50:
      coinValue = 20
    elif coinValue == 20:
      coinValue = 10
    elif coinValue == 10:
      coinValue = 5
    elif coinValue == 5:
      coinValue = 2
    elif coinValue == 2:
      coinValue = 1
    else:
      coinValue = 0


lengte = (len(result))
i = 0

while lengte > i:
    print(str(result[i]) + ' coins van: ' + str(result[i + 1])) 
    i += 2


if change > 0: # dit kijkt of dat of dat change gelijk is aan 0 als dat zo is dan print hij de text hier onder
  print('Change not returned: ', str(change) + ' cents')
else:
  print('done')