fish_weight = float(input('Enter the weight of the fish (pound) : '))#Get weight of the fish from user
payment = float(input('how many dollars do you have? '))#Asking the amount of money from the user

fish_weight_kg = round(fish_weight * 0.453592, 2)#Pound to kg
print(f'its means {fish_weight_kg}kg')

fish_weight_balance = fish_weight_kg * 2

#The rules
if fish_weight_balance == payment:
    print('Everything is fine, bye')
elif fish_weight_balance > payment:
    print('You should buy a fishing rod for the fisherman')
else:
    print(f'The fisher man should give you another {round(payment - fish_weight_balance, 2)} kilos of fish')