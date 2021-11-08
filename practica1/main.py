#!/bin/python3


import sys
from game import Person
import random

"""
def save_in_file():
"""
#def battle_options(options):

def battle_ground(character, enemy, levels):
    counter_levels = 1

    print(character[0], character[1])
    print(enemy)

    print("select your option")
    options = input("insert (a) for attack | insert (s) to save | insert (exit) to quit without save game: ")
    if options.lower() == 'a':
        attack = character[0][1] + character[1][1]
        enemy[0] = enemy[0] - attack
        if enemy[0] <= 0:
            enemy[0] = 0
            counter_levels += 1
            if counter_levels <= levels:
                print("Stage: ", counter_levels)
                enemy_spotted(counter_levels)
        print("enemy actual: ", enemy)

    if options.lower() == 's':
        print("save game")
    if options.lower() == "exit":
        print("exit")
    if options not in ('a', 's', "exit"):
        print(options, "Invalid input, insert (a) for attack, (s) for save, (exit) to exit without saving")


def character_selection(characters):

    game_characters = {1: Person(25, 9), 2: Person(40, 10), 3: Person(20, 6), 4: Person(30, 6)}

    play_character1 = game_characters.get(characters[0])
    play_character2 = game_characters.get(characters[1])

    selected_characters = {"character1": [play_character1.hp, play_character1.dmg],
                           "character2": [play_character2.hp, play_character2.dmg]}
    return [selected_characters.get("character1"), selected_characters.get("character2")]


def enemy_spotted(level):

    partial = Person(20, 6)
    final_exam = Person(40, 12)
    theorical_class = Person(8, 4 + level)
    teacher = Person(15, 7)

    if teacher.dmg == 7:
        teacher.dmg = 14

    enemies = [partial, final_exam, theorical_class, teacher]

    if level <= 2:
        enemies.remove(final_exam)
        return enemies
    if level >= 3:
        random_number = random.randint(0, 3)
        return [enemies[random_number].hp, enemies[random_number].dmg]


def type_players():

    print("Choose Characters: ")
    print("***************************" + "\n")

    option_1 = "1.The_bookworn -> Stats: 25 HP and 9 DMG"
    option_2 = "2.The_worker -> Stats: 40 HP and 10 DMG"
    option_3 = "3.The_whatsapper -> Stats: 20 HP and 6 DMG"
    option_4 = "4.The_procrastinator-> Stats: 30 HP and 6 DMG"

    return option_1 + "\n" + option_2 + "\n" + option_3 + "\n" + option_4 + "\n"


def main():
    k = range(1, 10, 1)

    try:
        if len(sys.argv) == 3:
            if (sys.argv[1] == "-s") and (int(sys.argv[2]) in k):
                print("Partida 2 jugadores con " + sys.argv[2] + " niveles")
                print(type_players())

                char_election_1 = int(input('selec first character: '))
                char_election_2 = int(input("select second character: "))

                characters = [char_election_1, char_election_2]

                selected_enemy = enemy_spotted(int(sys.argv[2]))
                selected_chars = character_selection(characters)

                battle_ground(selected_chars, selected_enemy, int(sys.argv[2]))

            if (sys.argv[1] == "-f") and (sys.argv[2] == "saved"):
                print(sys.argv[2] + " Nombre fichero incorrecto")

        if len(sys.argv) == 4:
            if (sys.argv[1] == "--file=saved.txt") and (sys.argv[2] == "-s") and (sys.argv[3] == "5"):
                print("Relanzamos partida guardada en saved.txt teniendo en cuenta el numero de niveles")

        if (len(sys.argv) == 2) and (sys.argv[1] == "--file=saved.txt"):
            print("Relanzamos la partida guardada en saved.txt")

        if (len(sys.argv) == 1) and (sys.argv[0] == "main.py"):
            type_players()

    except TypeError:
        print("fatal error")
    except KeyboardInterrupt:
        print("Exit program")
       # save_game = input("Do you want to save game (y/n): ")
       # if save_game == 'y' or save_game=='s':
        #    save_in_file()
        #else:
         #   print('')


if __name__ == '__main__':
    main()

