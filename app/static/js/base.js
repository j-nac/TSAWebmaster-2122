var cleanup
if(!cleanup){
    cleanup = ()=>{}
}
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
    window.history.pushState('Home', 'Home', this.getAttribute('link'));
    window.scrollTo(0, 0);
    cleanup()
    var request = new XMLHttpRequest();
    request.js = this.getAttribute('js')
    request.onload = function(){
        let group = document.getElementById('page')
        let newpage = document.createElement('div')
        newpage.innerHTML = this.responseText
        group.children[0].remove()
        newpage.id = 'newpage'
        group.appendChild(newpage)
        eval(this.js)
    }
    request.open('STATIC', this.getAttribute('link'));
    request.send();
}

document.addEventListener('DOMContentLoaded', () => {
	document.querySelectorAll('button.page-nav').forEach(button => {
		button.onclick = redirect
	});
});

document.getElementsByClassName('navbox')[0].addEventListener('keyup', (e)=>{
    if (e.keycode=='esc'){$(".navbox:first").css("display", "flex")}
})

document.getElementById('newsletter').onsubmit = function(){
    let form = $('#searchbox').serializeArray()
    let data = {}
    for(i of form){
        data[i['name']]=i['value']
    }
    $.ajax({
        'url':'/news',
        'type': 'POST',
        'contentType':'application/x-www-form-urlencoded',
        'data': data
    })
    return false
}