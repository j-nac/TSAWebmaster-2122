var target = 1656658800000

// https://loading.io/progress/
function countdown() {
    console.log(3)
    var dayCd = document.getElementById('day-cd')
    var hrCd = document.getElementById('hr-cd')
    var minCd = document.getElementById('min-cd')
    var secCd = document.getElementById('sec-cd')
    if (!dayCd||!hrCd||!minCd||!secCd){return;}

    var timeTill = Math.max(0, parseInt((target - Date.now()) / 1000))
    var clock = [timeTill]
    for (let [i, v] of [60, 60, 24].entries()) {
        clock.push(parseInt(clock[i] / v))
        clock[i] %= v
    }

    alert((clock[3]/365).toString()+'%')
    dayCd.style.width = (clock[3]/365).toString()+'%';
    hrCd.style.width = (clock[2]/24).toString()+'%';
    minCd.style.width = (clock[1]/60).toString()+'%';
    secCd.style.width = (clock[0]/60).toString()+'%';
    
    // $("countdown").text(clock[3] + "d : " + clock[2] + "h : " + clock[1] + "m : " + clock[0] + "s")
}

var inter

function loadhome(){
    cleanup = ()=>{ 
        console.log('sweeping')
        clearInterval(inter)
    }
    inter=setInterval(countdown, 500)
}
