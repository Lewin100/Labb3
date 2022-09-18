# Alexander Levin
# Amjad Alakrami
# 11/09/2022

def glosfunktion(ord1, ord2):
    svar = input("Vad betyder " + ord1 + " på engelska?").capitalize().replace(" ", "")

    if svar == ord2:
        print("Bra Jobbat!")
        return True
    else:
        print("Attans! Rätt svar är", ord2)
        return False

score=0
returnchecker= True

for i in range(1):
        returnchekcer = glosfunktion("Bil", "Car")
        if returnchecker==True:
            score += 1
print("Du fick ", score,"korrekt!")

