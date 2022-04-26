rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random
random.seed()

choices = ["r", "p", "s"]
choices_ascii = [rock, paper, scissors]

user_choice = input("Choose rock, paper, or scissors: ").lower()[0]
comp_choice = choices[random.randint(0, len(choices) - 1)]

# doing 0 for lose, 1 for win, 2 for tie
result_matrix = [[2, 0, 1], [1, 2, 0], [0, 1, 2]]

row = choices.index(user_choice)
col = choices.index(comp_choice)
win_result = result_matrix[row][col]
win_text = ["lose", "win", "tie"][win_result]

print(f'You chose {user_choice}:\n{choices_ascii[row]}\nComputer chose: {comp_choice}\n{choices_ascii[col]}\n\nYou {win_text}')
