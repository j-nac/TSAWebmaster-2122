function toggleNavbar(){
    for(let element of document.getElementsByClassName("pageNav")){
        element.style.display=="none"?element.style.display="block":element.style.display="none"
    }
}