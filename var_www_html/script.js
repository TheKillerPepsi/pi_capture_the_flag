var m_x = 0,m_y = 0;
var d = 999;

window.setInterval(function(){
    var el = document.getElementById('secret');
    d = getDistance(getOffset(el).x,getOffset(el).y,m_x,m_y);
    console.log(d);
    pyInterface(d);
}, 500);


function getOffset( el ) {
    var _x = 0;
    var _y = 0;
    while( el && !isNaN( el.offsetLeft ) && !isNaN( el.offsetTop ) ) {
        _x += el.offsetLeft - el.scrollLeft;
        _y += el.offsetTop - el.scrollTop;
        el = el.offsetParent;
    }
    return { y: _y, x: _x };
}

var x = getOffset( document.getElementById('secret') ).x; 

function getDistance(x1,y1,x2,y2) {
    return Math.sqrt(Math.pow(x1-x2,2)+Math.pow(y1-y2,2));
}

window.onload = init;
function init() {
    document.onmousemove = getCursorXY;
    setTimeout(function(){window.scrollTo(0,0);},1);
}

function getCursorXY(e) {
    m_x = typeof e.pageX !== 'undefined' ? e.pageX : 0;
    m_y = typeof e.pageY !== 'undefined' ? e.pageY : 0;
}

function pyInterface(input) {
    var js2Py = $.ajax({
        type: "POST",
        url: "/interface",
        async: false,
        data: { dis: input }
    });
}