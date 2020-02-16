function setup() 
{
  createCanvas(900, 600);
}
let x = -100;
let y = -100;
let x1;
let y1;

let value = 0;

function draw() 
{
  background(0);

  stroke(255);
  line(450, 0, 450, 600);

  if (x<450 && x1<450)
  {
    stroke('blue');
    line(x, y, x1, y1);
    noFill();
  }
  else if (x>=450 && x1>=450)
  {
    stroke('blue');
    line(x, y, x1, y1);
    noFill();
  }
  else
  {
    stroke('red');
    line(x, y, x1, y1);
    noFill();
  }
}

function mouseClicked() 
{
if (value === 0)
{
  x=mouseX;
  y=mouseY;
  value = 1;
}
else 
{
  x1=mouseX;
  y1=mouseY;
  value = 0;
}
}