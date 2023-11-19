elephant = "elephant"
lion = "lion"
dog = "dog"
cat = "cat"
mouse = "mouse"

print("Welcome to jungle game")
print("We have elephant, dog, cat, lion and mouse , The strongest animal wins")

player_choose = input("Choose your animal : ")#Player choose

#Game ruls
if player_choose == elephant:
    print("You killed all the animals and won")
elif player_choose == lion:
    print("You killed all the animals, but you could not compete with the elephant")
elif player_choose == dog:
    print("You killed all the animals, but you could not compete with the lion")
elif player_choose == cat:
    print("You killed all the animals, but you could not compete with the dog")
elif player_choose == mouse:
    print("You killed all the animals, but you could not compete with the cat")

