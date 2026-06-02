# ============================================
#   GESTIONNAIRE DE DÉPENSES
#   Mon projet pour apprendre Python
# ============================================

print("Bienvenue dans mon gestionnaire de dépenses !")

print("1. Ajouter une dépense")
print("2. Voir les dépenses")
print("3. Quitter")

choix = input("Veuillez choisir une option (1, 2 ou 3) : ")
print("Vous avez choisi l'option :" + choix)

if choix == "1":
    print("Ajouter une dépense")
elif choix == "2":
    print("Voir les dépenses")
elif choix == "3":
    print("Au revoir !")
else:
    print("Choix invalide")