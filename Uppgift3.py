# Alexander Levin
# Amjad Alakrami
# 11/09/2022

# funktionen frågar om heltal inom spannet 1-10 och fortsätter fråga om
# så länge användaren matar in ett heltal utanför spannet. Sedan skickas värdet
# tillbaka till resten av programmet och lagras i variabeln lr.
def frågaheltal():

    while(True):
        svar = int(input("Skriv in ett tal mellan 1-10?"))

        if svar<=10 and svar>=1:
            return svar
            break
        else:
            print("Du följde inte instruktionen!")

#lr står för lagrat resultat
lr=frågaheltal()
print(lr)