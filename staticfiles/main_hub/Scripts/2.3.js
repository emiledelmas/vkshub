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
  line(300, 0, 300, 600);
  line(600, 0, 600, 600);
  
  
  if (x<300 || x>600)
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