function logoutClick() {
    document.getElementById("form_logout").submit();
}

function logout(){
    logoutClick()
}

function verproduto(){
    document.getElementById("verprod").submit();
}

function buy(){
    document.getElementById("buying").submit();
}

setTimeout(function () {
    let c = document.getElementById("msg")
    c.remove()
  }, 2000)