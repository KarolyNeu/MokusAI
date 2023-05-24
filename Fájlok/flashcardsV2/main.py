import eel

user = {}
users = []
kerdesek = []
curquest = 0
curans = 0
helyes = 0
helytelen = 0
USERDATA = {}
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


def createUser(username, password):
    global kerdesek
    with open("userdata/users.txt", "a", encoding="UTF-8") as f:
        f.write(f"{username}||{password}\n")
    with open(f"userdata/{username}.txt", "w", encoding="UTF-8") as f:
        text = ""
        f.write(text)
    with open(f"userdata/{username}.txt", "a", encoding="UTF-8") as f:
        for i in range(len(kerdesek)+2):
            f.write("0||")


    Login(username, password)



@eel.expose
def Login(usr, pw):
    global user
    global users
    with open("userdata/users.txt", "r", encoding="UTF-8") as f:
        sorok = f.readlines()
        for sor in sorok:
            sor = sor.rstrip()
            sor = sor.split("||")
            sv = {}
            sv["USERNAME"] = sor[0]
            sv["PASSWORD"] = sor[1]
            users.append(sv)
            print(sv)
    user["USERNAME"] = usr
    user["PASSWORD"] = pw
    print(user)
    if user in users:
        with open(f"userdata/{usr}.txt", "r", encoding="UTF-8") as f:
            sorok = f.readlines()
            sor = sorok[0].split("||")
            USERDATA["HELYES"] = sor[0]
            USERDATA["HELYTELEN"] = sor[1]
            for i in range(13):
                USERDATA[str(i+1)] = sor[i+2]
            print(USERDATA)
        print(f"Login successful: username: {usr}, password: {pw}")
    else:
        createUser(usr, pw)


@eel.expose
def logOutPY():
    global user
    global USERDATA
    user = {}
    USERDATA = {}
    eel.logOutJS()



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