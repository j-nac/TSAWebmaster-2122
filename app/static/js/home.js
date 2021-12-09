target = 1655555555555

function countdown (){
    var timeTill = Math.max(0, parseInt((target-Date.now())/1000))
    var minutes = parseInt(timeTill/60)
    var seconds = timeTill%60
    var hours = parseInt(minutes/60)
    minutes=minutes%60
    var days = parseInt(hours/24)
    hours = hours % 24
    for(let i of document.getElementsByTagName("countdown")){
        i.innerHTML = String(days)+":"+String(hours)+":"+String(minutes)+":"+String(seconds)
    }
}
setInterval(countdown, 500)