# Alexander Levin
# Amjad Alakrami
# 11/09/2022

#uf står för uppmuntrande fras, funktionen printar ut en uppmuntrande fras.
def uf():
    print("Det blir ju lunch kl: 12:00!")

#den här funktionen skriver ut ett skämt när den blir kallad på.
def skämt():
    print("Vet du vilket djur som är sämst på att gå? ........nämligen GÅRILLAN!!!")

while(True):
    svar = str(input("Vill du ha uppmuntran eller humor?").capitalize().replace(" ", ""))
    if(svar=="Uppmuntran"):
        uf()
        break
    elif(svar=="Humor"):
        skämt()
        break
    else:
        print("Försök svara igen")
