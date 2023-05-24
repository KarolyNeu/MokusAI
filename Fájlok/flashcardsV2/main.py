import eel

kerdesek = []
curquest = 0
curans = 0
helyes = 0
helytelen = 0
with open("kerdesek.txt", "r", encoding="UTF-8") as f:
    sorok = f.readlines()
    for sor in sorok:
        sor = sor.split("||")
        sv = {}
        sv["NUM"] = int(sor[0])
        sv["QUEST"] = sor[1]
        sv["ANS"] = int(sor[2])
        kerdesek.append(sv)
print(kerdesek)


eel.init('web')

@eel.expose
def Login(usr, pw):
    print(f"Login successful: username: {usr}, password: {pw}")


@eel.expose
def question():
    global curquest
    quest = kerdesek[curquest]
    print(quest)
    eel.cardBuilder(f"{quest['NUM']}. kérdés", "Title", quest['QUEST'], quest['ANS'])
    global curans
    curans = quest['ANS']
    curquest += 1
 
@eel.expose
def answer(ans):
    global helyes
    global helytelen

    if ans == curans:
        helyes += 1
        print(helyes)
        print(helytelen)
    else: 
        helytelen += 1
        print(helyes)
        print(helytelen)
    question()






eel.start('flash.html')
question()