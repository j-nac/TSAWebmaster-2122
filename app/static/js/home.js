var target = 1656658800000

// https://loading.io/progress/
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

function check_artist(){
    window.history.pushState('Arch', '', '/artists');
    cleanup()
    var request = new XMLHttpRequest();
    request.id = this.getAttribute('target')
    request.onload = function(){
        insert_page(this.responseText)
        document.getElementById(this.id).scrollIntoView(true)
    }
    request.open('STATIC', '/artists');
    request.send();
}

var inter;

function loadhome(){
    document.querySelectorAll('button.artist-card').forEach(div => {
		div.onclick = check_artist
	});
    
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
