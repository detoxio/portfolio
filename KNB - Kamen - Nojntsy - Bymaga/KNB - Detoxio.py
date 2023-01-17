import random, time

def greet():
    print("--------------------------")
    print("     Приветсвуем вас      ")
    print("        в игре            ")
    print("  Камень--Ножницы--Бумага ")
    print("--------------------------")
    print("    формат ввода: k, n ,b ")


comp_turn = ["k", "n", "b"] #задаем список из трех вариантов
count = [ 0, 0]


def knd_choice(t):
    if t == "k":
        print("Камень")
    elif t == "n":
        print("Ножницы")  # иначе n
    elif t == "b":
        print("Бумага")  # или b

def main():
    gameloop = True
    while gameloop:  #Пока цикл истинен - игра продолжается
        turn = input("k - камень, n - ножницы, b - бумага, exit - Выход") #Ставим три переменные
        print()
        time.sleep(0.7)


        if turn == "exit":
            print("Выход")
            gameloop = False
        else:
            knd_choice(turn)
            c_turn = random.choice(comp_turn) #Прописываем 3 возможных кода ПК(Loses)
            knd_choice(c_turn)
            if (turn == "k" and c_turn == "n") or (turn == "n" and c_turn == "b") or (turn == "b" and c_turn == "k"):
                print("Ты Выйграл, Снимаю Свою Пиксельную Шляпу")
                count[0] += 1  # степень увеличивается на один
            if turn == ("n" and c_turn == "k") or (turn == "b" and c_turn == "n") or (turn == "k" and c_turn == "b"):
                print("Исскуственный Интеллект Безграничен, Я Одолел Тебя")
        print("Счет - ", count[0], ":", count [1])
        if 10 in count:
            gameloop = False
if __name__ == "__main__":
    main()

