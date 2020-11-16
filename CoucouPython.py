# Ceci est un Commentaire
# https://www.w3schools.com/python/default.asp
print("Coucou")
nom=input("Quel est ton nom?\n")
print("Tu t'appelles " + nom.capitalize())
print("Ton nom a " + str(len(nom)) + " caractères")
print("La deuxième lettre de ton nom est " + nom[1])

age=input("Tu as quel âge ? ")
print(f"Tu as {age} ans")
if int(age) >= 18:
  xxxeur = "majeur"
elif int(age) < 12:
  xxxeur = "jeune mineur" 
else:
  xxxeur = "mineur"
print("et " + xxxeur)

anneeDeNaissance = int(input("Quel est ton année de naissance ? "))
if anneeDeNaissance % 4 == 0:
  if anneeDeNaissance % 100 == 0:
    if anneeDeNaissance % 400:
      print("C'était une année bisextile")
    else:
      print("Ce n'était pas une année bisextile")
  else:
    print("C'était une année bisextile")   
else:
  print("Ce n'était pas une année bisextile")

print("Tu es né à "+input("Tu es né où ? "))

print("Tes enfants sont:")
enfants = ["Kevin", "Marine", "Lucas"]
for i in enfants:
  print(i)

taille=input("Combien mesures-tu ? ")
poids=input("Quel est ton poids ? ")
#print("Ton BMI est " + str(round(int(poids) / (float(taille) ** 2),2)))

def maFonctionBMI(t, p):
  print("Ton BMI est " + str(round(int(p) / (float(t) ** 2),2)))

maFonctionBMI(taille, poids) # l'appel de la fct doit être après sa déclaration 

# Angela - Chasse au trésor
print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Tresure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")

# Angela - Rock, paper, scissors
import random

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
game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
