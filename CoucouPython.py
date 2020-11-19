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

# Année bissextile
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

# Boucle - Loop
print("Tes enfants sont:")
enfants = ["Kevin", "Marine", "Lucas"]
for i in enfants:
  print(i)

# BMI
taille=input("Combien mesures-tu ? ")
poids=input("Quel est ton poids ? ")
#print("Ton BMI est " + str(round(int(poids) / (float(taille) ** 2),2)))

def maFonctionBMI(t, p):
  print("Ton BMI est " + str(round(int(p) / (float(t) ** 2),2)))

maFonctionBMI(taille, poids) # l'appel de la fct doit être après sa déclaration 

