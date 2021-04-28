function scrollToID(id)
{
    var getID = document.getElementById(id)
    // getID.scrollIntoView()
    window.scroll(0,findPos(getID));
}
function findPos(obj) {
    var curtop = 0;
    if (obj.offsetParent) {
        do {
            curtop += obj.offsetTop;
        } while (obj = obj.offsetParent);
    curtop-=130 
    return [curtop];
    }
}