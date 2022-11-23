function logoutClick() {
    document.getElementById("form_logout").submit();
}

function verproduto(){
    document.getElementById("verprod").submit();
}

function verproduto2(){
    document.getElementById("verprod2").submit();
}

function verproduto3(){
    document.getElementById("verprod3").submit();
}

function buy(){
    document.getElementById("buying").submit();
}

setTimeout(function () {
    let c = document.getElementById("msg")
    c.remove()
  }, 2000)