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

document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('button.page-nav').forEach(button => {
		button.onclick = () => {
			var request = new XMLHttpRequest();
            request.onload = function(){
                let group = document.getElementById('page')
                let newpage = document.createElement('div')
                newpage.innerHTML = this.responseText
                for(let i of group.children){
                    i.remove()
                }
                newpage.id = 'newpage'
                group.appendChild(newpage)
            }
			request.open('STATIC', button.getAttribute('link'));
			request.send();
		};
	});
});
