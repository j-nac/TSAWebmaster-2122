var cleanup
if(!cleanup){
    cleanup = ()=>{}
}
function toggleNavbar() {
    let navElement = $(".navbox:first");
    let toggleButton = $("#menu-icon");

    if (navElement.css("display") == "none") {
        navElement.css("display", "flex");
        toggleButton.text("close");
    } else {
        navElement.addClass('fadingnav')
        navElement.on('animationend',()=>{
            let navElement = $(".navbox:first");
            let toggleButton = $("#menu-icon");
            navElement.removeClass('fadingnav')
            navElement.css("display", "none");
            toggleButton.text("menu");
            navElement.off('animationend')
        })
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
        for(let i=0;i<group.children.length-1;i++){
            group.children[i].remove()
        }
        group.children[0].classList.add('oldpage')
        newpage.classList.add('newpage')
        newpage.classList.add('pagein')
        group.appendChild(newpage)
        $('.oldpage:first').on('transitionend',()=>{
            $('.oldpage:first').remove()
        })
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
