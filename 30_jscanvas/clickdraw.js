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
        mode = "circ";
    }
    else {
        mode = "rect";
    }
}

var drawRect = function(e) {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle = "#FF0000";
    ctx.fillRect(mouseX, mouseY, 100, 200)
}

var drawCircle = (e) => {
    var mouseX = e.offsetX; //gets X-coor of mouse when event is fired
    var mouseY = e.offsetY; //gets Y-coor of mouse when event is fired
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.beginPath();
    ctx.fillStyle = "#FF0000";
    ctx.arc(mouseX, mouseY, 50, 0,2 *Math.PI);
    ctx.fillstyle = "red";
    ctx.fill();
}

var draw = (e) => {
    if (mode == "rect"){
        drawRect(e);
    } else{
        drawCircle(e);
    }
}

var wipeCanvas = () => {
    ctx.clearRect(0,0, 600, 600);
}

c.addEventListener("click", draw) //passes the mouse event as parameter for the function
var bToggler = document.getElementById("buttonToggle");
bToggler.addEventListener('click', () =>{
    toggleMode();

});

var clearB = document.getElementById("buttonClear");
clearB.addEventListener('click', () =>{
    wipeCanvas();
});