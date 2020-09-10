# Game Rock-Paper-Scissors in Python


## 1) step
  --------------------------------------------------------------------
  ```python
  elemnts = ['water', 'dragon', 'devil', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponger', 'paper', 'air', 'lightning']

  
 
  winning_cases = {
    'water' : ['scissors', 'fire', 'rock', 'hun', 'lightning', 'devil', 'dragon'],
    'dragon' : ['snake', 'scissors', 'fire', 'rock', 'gun', 'lightning', 'devil'],
    'devil' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun'],
    'gun' : ['wolf', 'tree', 'human', 'snake', 'scissors', 'fire', 'rock'],
    'rock' : ['sponge', 'wolf', 'tree', 'human', 'snake', 'scissors', 'fire'],
    'fire' : ['paper', 'sponge', 'wolf', 'tree', 'human', 'snake', 'scissors'],
    'scissors' : ['air', 'paper', 'sponge', 'wolf', 'tree', 'human', 'snake'],
    'snake' : ['water', 'air', 'paper', 'sponge', 'wolf', 'tree', 'human'],
    'human' : ['dragon', 'water', 'air', 'paper', 'sponge', 'wolf', 'tree'],
    'tree' : ['devil', 'dragon', 'water', 'air', 'paper', 'sponge', 'wolf'],
    'wolf' : ['lightning', 'devil', 'dragon', 'water', 'air', 'paper', 'sponge'],
    'sponge' : ['gun', 'lightning', 'devil', 'dragon', 'water', 'air', 'paper'],
    'paper' : ['rock', 'gun', 'lightning', 'devil', 'dragon', 'water', 'air'],
    'air' : ['fire', 'rock', 'gun', 'lightning', 'devil', 'dragon', 'water'],
    'lightning' : ['tree', 'human', 'snake', 'scissors', 'fire', 'rock', 'gun']
}
```
## 2) step - creating 'class game' and import module 'random'
```python
import random


class game:
    __elemnts = ['water', 'dragon', 'devil', 'gun', 'rock', 'fire', 'scissors',
               'snake', 'human', 'tree', 'wolf', 'sponger', 'paper', 'air', 'lightning']

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

        


if __name__ == "__main__":
    game()
    
    
```
