function setup() 
{
  createCanvas(900, 600);
}
let i;

function draw() 
{
  background(0);
  stroke(255);
  for (i=1;i<9;i++)
  {
    line(i*100, 0, i*100, 600);
  }
  
}