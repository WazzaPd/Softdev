//retrieve node in DOM via ID
var c = document.getElementById("slate");

//instantiate a CanvasRenderingContext2D object
var ctx = c.getContext("2d");

//init globar state var
var mode = "rect";

//var toggleMode = function(e){
var toggleMode = (e) => {
    console.log("toggling...");
    if (mode === "rect") {
        mode = "circ"
    }
    else {
        mode = "rect"
    }
}

var drawRect = function(e) {
    var mouseX = e.clientX //gets X-coor of mouse when event is fired
    var mouseY = e.clientY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.fillRect(mouseX, mouseY, 10, 10)
}

var drawCircle = (e) => {
    var mouseX = e.clientX //gets X-coor of mouse when event is fired
    var mouseY = e.clientY //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY)
    ctx.beginPath()
    ctx.arc(mouseX, mouseY, 10, 0,2 *Math.PI)
    ctx.stroke()
}

var draw = (e) => {
    if (mode == "rect"){
        drawRect(e)
    } else{
        drawCircle(e)
    }
}

var wipeCanvas = () => {
    ctx.clearRect(0,0, 600, 600)
}

c.addEventListener("click", drawRect) //passes the mouse event as parameter for the function
