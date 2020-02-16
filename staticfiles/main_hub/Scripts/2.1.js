function setup() 
{
  createCanvas(900, 600);
}
let x = -100;
let y = -100;

function draw() 
{
  background(0);

  stroke(255);
  line(450, 0, 450, 900);
  
  if (x<450)
  {
    stroke('blue');
    circle(x, y, 50);
    noFill();
  }
  else
  {
    stroke('red');
    circle(x, y, 50);
    noFill();
  }
}

function mouseClicked() 
{
  x=mouseX
  y=mouseY
}