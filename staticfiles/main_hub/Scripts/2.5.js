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
  line(450, 0, 450, 600);
  line(0, 300, 900, 300);

  
  if ((x>450 && y<300) || (x<450 && y>300))
  {
    stroke('red');
    circle(x, y, 50);
    noFill();
  }
  else
  {
    stroke('blue');
    circle(x, y, 50);
    noFill();
  }
}

function mouseClicked() 
{
  x=mouseX;
  y=mouseY;
}