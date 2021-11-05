#!/bin/python3
import sys


def type_players():
    print("Choose Characters: " + "\n")
    print("1.The_bookworn -> Stats: 25 HP and 9 DMG")
    print("2.The_worker -> Stats: 40 HP and 10 DMG")
    print("3.The_whatsapper -> Stats: 20 HP and 6 DMG")
    print("4.The_procrastinator-> Stats: 30 HP and 6 DMG")


def main():

    if len(sys.argv) == 3:
        if (sys.argv[1] == "-s") and (sys.argv[2] == "5"):
            print("Partida 2 jugadores con 5 niveles")
            type_players()


        if (sys.argv[1] == "-f") and (sys.argv[2] == "saved"):
            print(sys.argv[2] + " Nombre fichero incorrecto")

    if len(sys.argv) == 4:
        if (sys.argv[1] == "--file=saved.txt") and (sys.argv[2] == "-s") and (sys.argv[3] == "5"):
            print("Relanzamos partida guardada en saved.txt teniendo en cuenta el numero de niveles")

    if (len(sys.argv) == 2) and (sys.argv[1] == "--file=saved.txt"):
        print("Relanzamos la partida guardada en saved.txt")

    if (len(sys.argv) == 1) and (sys.argv[0] == "main.py"):
        type_players()


if __name__ == '__main__':
    main()

