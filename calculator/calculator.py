nums = []
operators = []
show_user = []  

user_enter = ""           # Variables

i = 1
result = -1

while user_enter != "=" :

    user_enter = float(input(f"num {i} : "))
    nums.append(user_enter)
    show_user.append(user_enter)
    user_enter = input("operators : ")              # Get numbers from user
    operators.append(user_enter)
    show_user.append(user_enter)
    i += 1

i = 0

while '*' in operators or '/' in operators:

    for item in range(len(operators)):  

        if operators[i] == "*" :
           result = nums[i] * nums[i + 1]
           nums.remove(nums[i])
           nums.remove(nums[i])
           nums.insert(i , result)
           operators.remove(operators[i])
           i -= 1                                   # Calculate priority

        elif operators[i] == "/" :
           result = nums[i] / nums[i + 1]
           nums.remove(nums[i])
           nums.remove(nums[i])
           nums.insert(i , result)
           operators.remove(operators[i])
           i -= 1   

        i += 1

i = 0

for item in range(len(operators)):
    
    if operators[i] == "+" :
        result = nums[i] + nums[i + 1]
        nums.remove(nums[i])
        nums.remove(nums[i])
        nums.insert(i , result)
        operators.remove(operators[i])
        i -= 1                                   # Calculate addition and subtraction

    elif operators[i] == "-" :
        result = nums[i] - nums[i + 1]
        nums.remove(nums[i])
        nums.remove(nums[i])
        nums.insert(i , result)
        operators.remove(operators[i])
        i -= 1

    i += 1

print("-----------------------")
print(*show_user , result)
print("-----------------------")