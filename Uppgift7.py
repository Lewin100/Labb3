# Alexander Levin
# Amjad Alakrami
# 11/09/2022

#den här funktionen tar in två strings och tar input från användaren
# för vad översättningen av det ena ordet bör vara. Sedan returneras en bollean
# till funktionen slingchecker som med hjälp av boolean värdet kan hålla koll
# på om användaren fått poäng eller inte.
def gloschecker(sveord, engord):
    svar = input("Vad betyder " + sveord + " på engelska?").capitalize().replace(" ", "")

    if svar == engord:
        print("Bra Jobbat! Vi går vidare")
        return True
    else:
        print("Attans! Rätt svar är", engord)
        return False

#Den här funktionen tar in två listor och returnerar antal rätt efer
# att den har skickat glosorna i par till funktionen gloschecker. SLingchecker använder
# sig av en slinga och elementen av listorna för att skcika paren ett i taget. Antalet
# rätt lagras i variabeln score. Användaren får poäng om gloschecker() returnerar värdet True.
def slingchecker(svenskalista, engelskalista):
    score = 0
    returnchecker=bool
    for i in range(len(svenskalista)):
        returnchecker = gloschecker(svenskalista[i], engelskalista[i])
        if returnchecker==True:
            score += 1
    return score

#main() innehåller koden som annars hade varit "fri".
def main():
    svenskalista=["Hund", "Katt", "Bil","Mat","Skola","Dator"]
    engelskalista=["Dog", "Cat", "Car","Food","School","Computer"]

    print("Du fick ", slingchecker(svenskalista, engelskalista) , "av", len(svenskalista) ,"korrekt!")

main()
