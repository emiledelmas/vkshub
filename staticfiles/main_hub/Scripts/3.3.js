function setup() 
{
  createCanvas(900, 600);
}
let i;
let arrayX= [];
let arrayY= [];
function draw() 
{
  background(0);
  stroke(255);
  line(450, 0,450, 900);
  for (i=0;i<arrayX.length;i++) 
  {
      circle(arrayX[i],arrayY[i],20);
  }
}

function mousePressed() 
{
  if (mouseX<450)
  {
      arrayX.push(mouseX);
      arrayY.push(mouseY);
  }
}