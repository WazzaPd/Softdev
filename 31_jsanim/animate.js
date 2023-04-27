var c = document.getElementById("playground");
var dotButton = document.getElementById("buttonCircle");
var stopButton = document.getElementById("buttonStop");

ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
    e.clearRect(0,0, 600, 600);
};

var radius = 0;
var growing = true;

var start;

function step(timestamp) {
    if (!start) start = timestamp;
    const elapse = timestamp - start;;
    
    window.requestAnimationFrame(step);
}

var drawCircle = (radius) => {
    var X = 250;
    var Y = 250; 
    console.log("mouseclick registered at ", X, Y);
    ctx.beginPath();
    ctx.arc(X, Y, radius, 0,2 *Math.PI);
    ctx.fillstyle = "blue";
    ctx.fill();
}

var start;
var lastTime = new Date().getTime();
var speed = 5; // adjust this to change the animation speed

function step() {
    const now = new Date().getTime();
    const elapsed = now - lastTime;
    const frameTime = elapsed * speed;

    if (frameTime > 16.7) { // limit the frame rate to 60 fps
        clear(ctx);
        drawCircle(radius);
    
        // animate
        if (growing) {
            radius++;
            if (radius == 250) {
                growing = false;
            }
        } else {
            radius--;
            if (radius == 0) {
                growing = true;
            }
        }
        lastTime = now;
    }

    requestID = window.requestAnimationFrame(step);
}

var drawDot = () => {
    if (!requestID) {
        lastTime = new Date().getTime();
        requestID = window.requestAnimationFrame(step);
    }
};

var stopIt = () => {
    console.log("stopIt invoked...");
    console.log( requestID );

    cancelAnimationFrame(requestID);
    clearTimeout(requestID);
    requestID = undefined;
}

dotButton.addEventListener("click", drawDot);
stopButton .addEventListener("click", stopIt);