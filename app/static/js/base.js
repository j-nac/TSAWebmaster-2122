function toggleNavbar() {
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

function redirect(){
    cleanup()
    var request = new XMLHttpRequest();
    request.onload = function(){
        let group = document.getElementById('page')
        let newpage = document.createElement('div')
        newpage.innerHTML = this.responseText
        group.children[0].remove()
        newpage.id = 'newpage'
        group.appendChild(newpage)
    }
    request.open('STATIC', this.getAttribute('link'));
    request.send();
}

document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('button.page-nav').forEach(button => {
		button.onclick = redirect
	});
});

var cleanup;
if(!cleanup){cleanup=()=>{}}