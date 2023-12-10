final_price = 0
order = "NULL"
other_order = "Y"

order_list = []
order_count_list = []                   # Variables

breads = {
    "barbari": 1000,
    "sangak" : 3000,
    "lavash" : 500,     # this is dict
    "taftoon": 2500,
    "shirmal": 1750
}

print ("welcame to erfan bakery")

while other_order != "N":
    order = input("Enter the name of the bread you want : ")
    order_count = input("How many do you want : ")                              # Ask from user

    if int(order_count) <= 0:
        print("Are you kidding me?")

    if order in breads:
        final_price += breads[order] * int(order_count)
        order_list.append(order)                                                # Get order and calculate it
        order_count_list.append(order_count)
        other_order = input("Do you have another order (Y/N) ? ")

    else:
        print("Sorry, we do not have this type of bread ")
        other_order = input("Do you have another order (Y/N) ? ")

print("-----------------------\nWell, your order included\n")

for item in range(0 ,len(order_list)) :
    print(order_list[item] + f" : {order_count_list[item]}")                    # Display the order to the user

print(f"\n-----------------------\nand the price of your order is equal to  {final_price}")
#The end