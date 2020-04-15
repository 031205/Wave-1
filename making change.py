cents = int(input('Input the number of cents:'))
toonies = cents//200
loonies = (cents%200)//100
quarters = (cents%100)//25
dimes =  (cents%25)//10
nickels = (cents-toonies*200-loonies*100-quarters*25-dimes*10)//5
pennies = cents%5
print(toonies,'toonies')
print(loonies,'loonies')
print(quarters,'quarters')
print(dimes,'dimes')
print(nickels,'nickels')
print(pennies,"pennies")
