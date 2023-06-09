var curans = 1

function logOut() {
    eel.logOutPY()
}

eel.expose(logOutJS)
function logOutJS(){
    document.getElementById("loginpage").style.display = "block"
    document.getElementById("FLASHCARD").style.display = "none"
}

function login() {
    let usr = document.getElementById("loginname").value
    console.log(usr)
    document.getElementById("loginpage").style.display = "none"
    eel.Login(usr)
    document.getElementById("FLASHCARD").style.display = "block"
}

eel.expose(cardBuilder)
function cardBuilder(num, description, ans) {
    document.getElementById("num").innerHTML = num
    document.getElementById("desc").innerHTML = description
    curans = ans
}

function answer(answer) {
    if (answer == curans){
        alert("A válaszod helyes")
        eel.answer(answer)
    }
    else{
        alert("A válaszod helytelen")
        eel.answer(answer)
    }
}

eel.expose(stats)
function stats(cor, incor) {
    document.getElementById("correctnum").innerHTML = cor
    document.getElementById("incorrectnum").innerHTML = incor
}