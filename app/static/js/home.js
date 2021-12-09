target = 1655555555555

function countdown (){
    var timeTill = Math.max(0, parseInt((target-Date.now())/1000))
    var clock = [timeTill]
    for(let [i,v] of [60,60,24].entries()){
        clock.push(parseInt(clock[i]/v))
        clock[i]%=v
    }
    for(let i in clock){
        clock[i] = String(clock[i])
        while(clock[i].length<2){clock[i]="0"+clock[i]}
    }
    for(let i of document.getElementsByTagName("countdown")){
        i.innerHTML = clock.reverse().join(":")
    }
}
setInterval(countdown, 500)