function setup() 
{
  createCanvas(900, 600);
}
let x = -100;
let y = -100;

function draw() 
{
  background(0);
  if (x%2==0 && y%2==0)
  {
    stroke('red');
    circle(x, y, 50);
    noFill();
  }
  else if (x%2!=0 && y%2==0)
  {
    stroke('yellow');
    circle(x, y, 50);
    noFill();
  }
  else if (x%2==0 && y%2!=0)
  {
    stroke('blue');
    circle(x, y, 50);
    noFill();
  }
  else
  {
    stroke('green');
    circle(x, y, 50);
    noFill();
  }
}

function mouseClicked() 
{
  x=Math.floor(mouseX)
  y=Math.floor(mouseY)
  console.log("CoordX:"+x)
  console.log("CoordY:"+y)
}