target = 1655555555555

function countdown (){
    timeTill = Math.max(0, (target-Date.now)/1000)
    days = timeTill % (60*60*24)
    timeTill -= days*(60*60*24)
    hours = timeTill % (60*60)
    timeTill -= hours*(60*60)
    minutes = timeTill%60
    timeTill -= minute*60
    seconds = timeTill
    for(let i of Document.getElementByTagName("countdown")){
        i.innerHTML = String(days)+":"+String(hours)+":"+String(minutes)+":"+String(seconds)
    }
}