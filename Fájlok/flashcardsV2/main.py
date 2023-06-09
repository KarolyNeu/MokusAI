import random
import eel

user = {}
users = []
kerdesek = []
curquest = 0
curans = 0
helyes = 0
helytelen = 0
USERDATA = {}
nthquest = 1
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


def createUser(username):
    global kerdesek
    with open("userdata/users.txt", "a", encoding="UTF-8") as f:
        f.write(f"{username}\n")
    with open(f"userdata/{username}.txt", "w", encoding="UTF-8") as f:
        text = ""
        f.write(text)
    with open(f"userdata/{username}.txt", "a", encoding="UTF-8") as f:
        for i in range(len(kerdesek)+2):
            f.write("1||")


    Login(username)



@eel.expose
def Login(usr):
    global nthquest
    global user
    global USERDATA
    global helyes
    global helytelen
    global users
    nthquest = 1
    with open("userdata/users.txt", "r", encoding="UTF-8") as f:
        sorok = f.readlines()
        for sor in sorok:
            sor = sor.rstrip()
            sor = sor.split("||")
            sv = {}
            sv["USERNAME"] = sor[0]
            users.append(sv)
            print(sv)
    user["USERNAME"] = usr
    print(user)
    if user in users:
        with open(f"userdata/{usr}.txt", "r", encoding="UTF-8") as f:
            sorok = f.readlines()
            sor = sorok[0].split("||")
            USERDATA["HELYES"] = sor[0]
            USERDATA["HELYTELEN"] = sor[1]
            helyes = int(sor[0])
            helytelen = int(sor[1])


            for i in range(13):
                USERDATA[str(i+1)] = sor[i+2]
            print(USERDATA)
        print(f"Login successful: username: {usr}")
    else:
        createUser(usr)
    question()
    eel.stats(helyes,helytelen)


@eel.expose
def logOutPY():
    global user
    global USERDATA
    user = {}
    USERDATA = {}
    eel.logOutJS()


def weightedChoice():
    global user
    global USERDATA
    global kerdesek
    global quest
    weight = []
    for i in range(13):
        weight.append(int(USERDATA[str(i+1)]))
    print(weight)
    choice = random.choices(kerdesek, weights=weight, k=1)
    print(choice)
    quest = choice[0]


@eel.expose
def question():
    global curquest
    global curans
    global nthquest
    weightedChoice()
    print(quest)
    eel.cardBuilder(f"{nthquest}. kérdés", quest['QUEST'], quest['ANS'])
    curans = quest['ANS']
    curquest = quest['NUM']
    print(curquest)

 
@eel.expose
def answer(ans):
    global nthquest
    global helyes
    global helytelen
    global user
    nthquest += 1
    if ans == curans:
        helyes += 1
        print(helyes)
        print(helytelen)
    else: 
        helytelen += 1
        print(helyes)
        print(helytelen)
    question()
    eel.stats(helyes,helytelen)





eel.start('flash.html', mode=None)
