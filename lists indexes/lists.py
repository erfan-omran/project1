name_list = ["erfan" , "ali", "mohammad", "mobin", "parsa", "artan", "korosh", "mahan", "amir", "arsham"]
family_list = ["omran" , "vafai", "akbari", "ghanbary", "kalanpay", "zadsar", "zar andoz", "ebrahimi", "alavi", "davari"]
car_list = ["samand" , "BMW", "benz", "206", "pars", "207", "lamborgini", "peykan", "patrol", "perayd"]

name_list.extend(["safa","taha"])#extend
family_list.append("ali zadeh")#append
car_list.insert(1,"bogati")#insert

print(f'{name_list[5]} {family_list[0]} has {car_list[1]} and is biger than {name_list[-4]} {family_list[-7]} with {car_list[-1]}')