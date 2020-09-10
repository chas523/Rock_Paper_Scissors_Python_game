import random


class game:
    __all_elements = ['water', 'dragon', 'devil', 'gun', 'rock', 'fire', 'scissors',
                      'snake', 'human', 'tree', 'wolf', 'sponger', 'paper', 'air', 'lightning']
    __default_elements = ['rock', 'paper', 'scissors']
    __winning_cases = {
        'water': ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
        'dragon': ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
        'devil': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
        'gun': ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
        'rock': ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
        'fire': ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
        'scissors': ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
        'snake': ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
        'human': ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
        'tree': ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
        'wolf': ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
        'sponge': ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
        'paper': ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
        'air': ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
        'lightning': ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
    }

    #konstruktor
    def __init__(self):
        self.__name_player = input("Enter your name: ")
        print("Hello, " + self.__name_player)
        self.__rating_player = self.__check_rating()
        self.__rating_first = self.__rating_player  # for function __save_rating

        # while True:
       #     self.__elemets_selected = input()
       #     if self.__elemets_selected == "":
       #         self.__default_game()
       #         break
       #     for element in self.__elemets_selected.split(","):
       #         if element not in self.__all_elements:
       #             print("Invalid input")
       #         else:
       #             self.__new_game()
       #             break
        
       
        self.__elemets_selected = input()
        if self.__elemets_selected == "":
            self.__default_game()
        else:
            self.__new_game()

    #update game

    def __new_game(self):
        symbols_for_game = self.__elemets_selected.split(",")
        print("Okay, let's start")
        while True:
            bot_symbols = random.choice(symbols_for_game)
            player_symbols = input()
            if player_symbols == "!exit":
                print("Bye!")
                self.__save_rating()
                break
            elif player_symbols == "!rating":
                print(self.__name_player + " " + str(self.__rating_player))
            elif player_symbols not in symbols_for_game and player_symbols != "!exit" and player_symbols != "!rating":
                print("Invalid input")
            else:
               self.__who_win(player_symbols, bot_symbols)

    # default game
    def __default_game(self):
        print("Okay, let's start")
        while True:
            bot_symbols = random.choice(self.__default_elements)
            player_symbols = input()
            if player_symbols == "!exit":
                print("Bye!")
                self.__save_rating()
                break
            elif player_symbols == "!rating":
                print(self.__name_player + " " + str(self.__rating_player))
            elif player_symbols not in self.__default_elements and player_symbols != "!exit" and player_symbols != "!rating":
                print("Invalid input")
            else:
               self.__who_win(player_symbols, bot_symbols)

    # return rating

    def __check_rating(self):
        try:
            file_rating = open("rating.txt", "r+")
            for line in file_rating:
                if line.split()[0] == self.__name_player:
                    return int(line.split()[-1])
            file_rating.write(self.__name_player + " 0\n")
            file_rating.close()

            return 0
        except IOError:
            file_rating = open("rating.txt", "w+")
            file_rating.close()
            return 0

    # playing
    def __who_win(self, player_symbols, bot_symbols):
        if player_symbols == bot_symbols:
            print("There is a draw (" + bot_symbols + ")")
            self.__rating_player = self.__rating_player + 50
        else:
            for key, value in self.__winning_cases.items():
                if player_symbols == key:
                    if bot_symbols not in value:
                        print("Sorry, but the computer chose " + bot_symbols)
                        break
                    else:
                        self.__rating_player = self.__rating_player + 100
                        print("Well done. The computer chose " +
                              bot_symbols + " and failed")
                        break

    def __save_rating(self):
        file_rating = open("rating.txt", "r")
        text_into_file = file_rating.readlines()
        file_rating.close()
        for line in range(len(text_into_file)):
            if text_into_file[line] == self.__name_player + " " + str(self.__rating_first) + "\n":
                text_into_file[line] = self.__name_player + \
                    " " + str(self.__rating_player) + "\n"
        file_rating = open("rating.txt", "w")
        for line in text_into_file:
            file_rating.write(line)
        file_rating.close()


if __name__ == "__main__":
    game()
