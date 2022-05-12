target = 1656658800000

// https://loading.io/progress/
function countdown() {
    console.log(3)
    var dayCd = document.getElementById('day-cd').ldBar;
    var hrCd = document.getElementById('hr-cd').ldBar;
    var minCd = document.getElementById('min-cd').ldBar;
    var secCd = document.getElementById('sec-cd').ldBar;
    if (!dayCd||!hrCd||!minCd||!secCd){return;}

    var timeTill = Math.max(0, parseInt((target - Date.now()) / 1000))
    var clock = [timeTill]
    for (let [i, v] of [60, 60, 24].entries()) {
        clock.push(parseInt(clock[i] / v))
        clock[i] %= v
    }
    for (let i in clock) {
        clock[i] = String(clock[i])
    }

    if (clock[0] == 0) {
        clock[0] = 60;
    }

    dayCd.set(clock[3], false);
    hrCd.set(clock[2], false);
    minCd.set(clock[1], false);
    secCd.set(clock[0], false);
    
    // $("countdown").text(clock[3] + "d : " + clock[2] + "h : " + clock[1] + "m : " + clock[0] + "s")
}

var inter

function loadhome(){
    cleanup = ()=>{ 
        console.log('sweeping')
        clearInterval(inter)
    }
    console.log(cleanup)
    inter=setInterval(countdown, 500)
}
