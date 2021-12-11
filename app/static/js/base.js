function toggleNavbar(){
    element = document.getElementsByClassName("navbox")[0]
    if(element.style.display=="none"){
        element.style.display="flex"
    } else {
        element.style.display="none"
    }
}