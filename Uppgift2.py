# Alexander Levin
# Amjad Alakrami
# 11/09/2022

#Den här funktionen presenterar programmet för användaren
def presentering():
    print("Det här är ett glosförhörs program!")

presentering()

score = 0
svenskalista=["Hund", "Katt", "Bil","Mat","Skola","Dator"]
engelskalista=["Dog", "Cat", "Car","Food","School","Computer"]

for i in range(len(svenskalista)):
    svar=input("Vad betyder " + svenskalista[i] + " på engelska?").capitalize().replace(" ","")
    if svar == engelskalista[i]:
        print("Bra Jobbat! Vi går vidare till nästa")
        score += 1
    else:
        print("Attans! Rätt svar är", engelskalista[i])

print("Du fick ", score, "av", len(svenskalista) ,"korrekt!")
