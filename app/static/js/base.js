function toggleNavbar(){
    navElement = $(".navbox:first");
    toggleButton = $("#menu-icon");

    if (navElement.css("display") == "none") {
        navElement.css("display", "flex");
        toggleButton.text("close");
    } else {
        navElement.css("display", "none");
        toggleButton.text("menu");
    }
}