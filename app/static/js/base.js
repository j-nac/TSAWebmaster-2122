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
			request.open('GET', button.getAttribute('link'));
			request.send();
            document.getElementById('page')
            let newpage = document.makeElement('div')
            alert(request.responseText)
		};
	});
});
