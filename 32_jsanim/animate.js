// Team Purple Spikes :: Joseph Wu, Aahan Mehta
//SoftDev pd8
//K31 -- canvas based JS animation
//2023-04-25

var c = document.getElementById("playground");

var dotButton = document.getElementById("circle");
var stopButton = document.getElementById("stop");
var dvdButton = document.getElementById("dvd")

var ctx = c.getContext("2d");

ctx.fillStyle = "blue";

var requestID;

var clear = (e) => {
  //e.preventDefault();
  ctx.clearRect(0, 0, 500, 500);
};

var dvdLogoSetup = function() {
  window.cancelAnimationFrame(requestID);
  
  var rectWidth = 200;
  var rectHeight = 100;
  
  var rectX = Math.floor(Math.random()*(500-rectWidth));
  var rectY = Math.floor(Math.random()*(500 - rectHeight));
  
  var xVel = 2;
  var yVel = 2;
  
  var logo = new Image();
  logo.src = "logo_dvd.jpg";
  
  var dvdLogo = function() {
    ctx.clearRect(0,0,c.width,c.height);
    ctx.drawImage(logo, rectX, rectY, rectWidth, rectHeight);
    if(rectX >= (500-rectWidth) || rectX <= 0){
      xVel *= -1;
    }
    if(rectY >= (500 - rectHeight) || rectY <= 0){
      yVel *= -1;
    }
    rectX += xVel;
    rectY += yVel;
    requestID = window.requestAnimationFrame(dvdLogo);  
  };
  dvdLogo();
}


var radius = 0;
var growing = true;

var drawDot = (e) => {
    console.log(e); 
    clear(e);
    
    ctx.beginPath();
    ctx.arc(250, 250, radius, 0, Math.PI*2, true);
    ctx.fill();
    ctx.closePath();
    
    if (growing && radius > 250) {
        growing = false;
    } else if (growing ==false && radius < 1) {
        growing = true;
    }

    if (growing) {
        radius++; 
    } else {
        radius--;
    }

    window.cancelAnimationFrame(requestID);
    requestID = window.requestAnimationFrame(drawDot);
}

var stopIt = () => {
    console.log(requestID)
    window.cancelAnimationFrame(requestID)
}

dotButton.addEventListener("click", drawDot);
dvdButton.addEventListener("click", dvdLogoSetup);
stopButton.addEventListener("click", stopIt);