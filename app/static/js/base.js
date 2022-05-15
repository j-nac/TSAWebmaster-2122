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

function insert_page(txt){
    let group = document.getElementById('page')
    let newpage = document.createElement('div')
    newpage.innerHTML = txt
    group.children[0].remove()
    newpage.id = 'newpage'
    group.appendChild(newpage)
}

function redirect(){
    window.history.pushState('Arch', '', this.getAttribute('link'));
    window.scrollTo(0, 0);
    cleanup()
    var request = new XMLHttpRequest();
    request.js = this.getAttribute('js')
    request.onload = function(){
        insert_page(this.responseText)
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

$(document).on('submit','#newsletter-form',function(e) {
    e.preventDefault();
    $.ajax({
        type:'POST',
        url:'',
        data: {
            email:$("#newsletter-email-box").val(),
            csrf_token:$("#csrf_token").val()
        },
        success: function() {
            $("html, body").animate({ scrollTop: 0 }, "slow");
            $("#newsletter-email-box").val('');
        }
    })
});

ScrollReveal().reveal('.reveal', { duration: 1500, reset: true });

/*
document.getElementsByClassName('navbox')[0].addEventListener('keyup', (e)=>{
    if (e.keycode=='esc') {
        $(".navbox:before").css("display", "flex");
    }
})
*/
