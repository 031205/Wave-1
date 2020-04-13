openingbalance = int(input('Input the amount of maney deposited into the account:'))
firstyearbalance = openingbalance*1.04
secondyearbalance = openingbalance*1.04**2
thirdyearbalance = openingbalance*1.04**3
print('The amount after 1 year is',round(firstyearbalance,2))
print('The amount after 2 years is',round(secondyearbalance,2))
print('The amount after 3 tears is',round(thirdyearbalance,2))