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
    let pw = document.getElementById("loginpw").value
    console.log(usr)
    console.log(pw)
    document.getElementById("loginpage").style.display = "none"
    eel.Login(usr, pw)
    document.getElementById("FLASHCARD").style.display = "block"
}

eel.expose(cardBuilder)
function cardBuilder(num, title, description, ans) {
    document.getElementById("num").innerHTML = num
    document.getElementById("title").innerHTML = title
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

const offCanvas = document.getElementById("offcanvasRight")
offCanvas.addEventListener("hide.bs.offcanvas", show())

const menu = document.getElementById("menuicon")
menu.addEventListener("click", hide())

function hide(){
    document.getElementById("menuicon").style.opacity = 0
    console.log("hide")
}

function show(){
    document.getElementById("menuicon").style.opacity = 1
    console.log("show")
}