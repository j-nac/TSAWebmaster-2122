/*
BASE FILE
*/
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
        navElement.addClass('fadingnav');
        toggleButton.text("menu");
        navElement.on('animationend',()=>{
            navElement.removeClass('fadingnav');
            navElement.css("display", "none");
            navElement.off('animationend');
        });
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

document.addEventListener('keyup', (e) => {
    if (e.code=='Escape'){
        toggleNavbar()
    }
})

/*
HOME FILE
*/
var target = 1656658800000

function countdown() {
    var timeTill = Math.max(0, ((target - Date.now()) / 1000))
    var clock = [timeTill]
    for (let [i, v] of [60, 60, 24].entries()) {
        clock.push(clock[i] / v)
        clock[i] %= v
    }
    $('#day-cd').css('width', (clock[3]/365*100).toString()+'%');
    $('#hr-cd').css('width', (clock[2]/24*100).toString()+'%');
    $('#min-cd').css('width', (clock[1]/60*100).toString()+'%');
    $('#sec-cd').css('width', (clock[0]/60*100).toString()+'%');
    $('#days').html(parseInt(clock[3]))
    $('#hrs').html(parseInt(clock[2]))
    $('#mins').html(parseInt(clock[1]))
    $('#secs').html(parseInt(clock[0]))
    
    // $("countdown").text(clock[3] + "d : " + clock[2] + "h : " + clock[1] + "m : " + clock[0] + "s")
}

var inter;

function loadhome(){
    cleanup = ()=>{
        console.log('sweeping');
        clearInterval(inter);
    };
    inter=setInterval(countdown, 500);

    // https://simpleparallax.com/
    var image = document.getElementsByClassName('countdown-background');
    new simpleParallax(image, {
        delay: .3,
        scale: 1.5,
        transition: 'cubic-bezier(0,0,0,1)'
    });
}

/* 
STORE FILE
*/
function mason(){
	var $grid = $('.grid').masonry({'isFitWidth': true});
	$grid.imagesLoaded().progress( function() {
		$grid.masonry('layout')
	})
}

function loadstore(){
	Promise.all(Array.from(document.images).filter(img => !img.complete).map(img => new Promise(resolve => { img.onload = img.onerror = resolve; }))).then(() => {
		mason()
	});

	document.querySelectorAll('button.store-card').forEach(button => {
		button.onclick = redirect
	});
	document.getElementById('searchbox').onsubmit = function(){
		$.ajax({
			url:'/store?'+$('#searchbox').serializeArray().map(e=>e['name']+'='+e['value']).join('&'),
			type: 'STATIC',
			success: function(data){
				let group = document.getElementById('page')
				let newpage = document.createElement('div')
				newpage.innerHTML = data
				group.children[0].remove()
				newpage.id = 'newpage'
				group.appendChild(newpage)
				loadstore()
			}
		})
		return false
	}
}
