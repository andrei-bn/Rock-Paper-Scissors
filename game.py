import random


def main():
    name = greeting()
    score = read_rating(name)
    mode = game_mode()
    game_play(mode, score)


def greeting():
    name = input("Enter your name: ")
    print("Hello,", name)
    return name


def read_rating(name):
    file_ = open("rating.txt", 'r')
    score = 0
    for line in file_:
        if name == line[:line.index(' ')]:
            score = int(line[line.index(' ') + 1:])
    file_.close()
    return score


def game_mode():
    base_parameters = ['rock', 'paper', 'scissors']
    main_parameters = input()
    start = "Okay, let's start"

    if main_parameters == "":
        print(start)
        return base_parameters
    elif main_parameters != "":
        main_parameters = main_parameters.split(',')
        print(start)
        return main_parameters


def game_play(game_parameters, score):
    while True:
        figure = input()
        if figure == "!exit":
            print("Bye!")
            break
        if figure == "!rating":
            print("Your rating:", score)
            continue
        if figure not in game_parameters:
            print("Invalid input")
            continue

        comp_figure = random.choice(game_parameters)

        shift__ = int((len(game_parameters) - 1) / 2 - game_parameters.index(figure))

        def shift(parameters, shift_):
            a = shift_ % len(parameters)
            return parameters[-a:] + parameters[:-a]

        game_parameters = shift(game_parameters, shift__)

        if figure == comp_figure:
            score += 50
            print(f"There is a draw ({comp_figure})")
        elif game_parameters.index(figure) > game_parameters.index(comp_figure):
            score += 100
            print(f"Well done. The computer chose {comp_figure} and failed")
        elif game_parameters.index(figure) < game_parameters.index(comp_figure):
            print(f"Sorry, but the computer chose {comp_figure}")


main()
