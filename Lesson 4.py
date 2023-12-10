
def func(*args):
    print(type(args))
    for arg in args:
        print(arg)


def func1(**kwargs):
    print(type(kwargs))
    for key in kwargs.keys():
        print(key, kwargs[key])


def func2(*args, **kwargs):
    for arg in args:
        print(arg)
    for key in kwargs.keys():
        print(key, kwargs[key])
    print(kwargs["word"])

'''func(1, 23, 4, "3", 4.44, True)
func1(name=1, temp=23, press=4, word="3")
func2(1,2,3,4, press=4, word="3")'''


import random

players = []
list_action = ["Помий посуд", "Зроби уроки", "Сходи за хлібом"]
list_question = ["Як тебе називають у школі?", "Хто твій найкращій друг?", "Як пройшов твій день?"]

def get_players(players):
    while True:
        name = input("Введіть ім'я гравця : ")
        players.append(name)
        if len(players) < 2:
            continue
        else:
            next = input("Чи хочете додати ще гравця? (Y/N)")
            if str.upper(next) == "Y":
                continue
            else:
                break


def game(list_action, list_question, players):
    for name in players:
        choice = input(f"Вибір для {name}: Правда або Дія? (P/D) ")
        if str.upper(choice) == "P":
            q_index = random.randint(0, len(list_question) - 1)
            print(list_question[q_index])
            list_question.pop(q_index)
        elif str.upper(choice) == "D":
            a_index = random.randint(0, len(list_action) - 1)
            print(list_action[a_index])
            list_action.pop(a_index)

        if len(list_action) == 0 or len(list_question) == 0:
            return False
    return True

get_players(players)
while True:
    if not game(list_action,list_question, players):
        print("Нажаль закінчилися запитання. Кінець гри.....!")
        break

