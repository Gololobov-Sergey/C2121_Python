'''a = 9
var1 = a

def func():
    global var1
    var1 += 10
    print(var1)

func()
print(var1)'''


import random

def game(user_choice):
    computer_choice = random.choice("KNB")
    user_choice = str.upper(user_choice)
    print(f"Комп'ютер - {computer_choice}, Гравець - {user_choice}")
    if user_choice == computer_choice:
        return "D"
    elif user_choice == 'K' and computer_choice == "B" or \
         user_choice == 'B' and computer_choice == "N" or \
         user_choice == 'N' and computer_choice == "K":
        return "C"
    elif user_choice == 'K' and computer_choice == "N" or \
         user_choice == 'B' and computer_choice == "K" or \
         user_choice == 'N' and computer_choice == "B":
        return "U"

def print_result(winner, result):
    if winner == "D":
        print("В цьому раунді нічья")
    elif winner == "U":
        print("В цьому раунді переміг гравець")
        result["user"] += 1
    elif winner == "C":
        print("В цьому раунді переміг коп'ютер")
        result["comp"] += 1
    print("Поточний рахунок")
    print(f'Комп\'ютер - {result["comp"]}, Гравець - {result["user"]}')


result = {"user":0, "comp":0}

for i in range(3):
    print()
    print(f"======= РАУНД №{i+1} =======")
    choice = input("Виберіть K, N, B - ")
    print_result(game(choice), result)