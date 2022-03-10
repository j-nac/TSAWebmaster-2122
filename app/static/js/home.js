target = 1647553337000

function countdown() {
    var timeTill = Math.max(0, parseInt((target - Date.now()) / 1000))
    var clock = [timeTill]
    for (let [i, v] of [60, 60, 24].entries()) {
        clock.push(parseInt(clock[i] / v))
        clock[i] %= v
    }
    for (let i in clock) {
        clock[i] = String(clock[i])
        while (clock[i].length < 2) {
            clock[i] = "0" + clock[i]
        }
    }
    
    $("countdown").text(clock[3] + "d : " + clock[2] + "h : " + clock[1] + "m : " + clock[0] + "s")
}
setInterval(countdown, 500)