function setup() {
  createCanvas(900, 600);
}
let i = 0;
let value = 0;
function draw() {
  background(0);
  fill(value);
  stroke(255);
  rect(400, 250,100, 100);
  textSize(32);
  text(i,10,30);
}
function mouseClicked() {
  if (i<20 && mouseX>=400 && mouseY >= 250 && mouseX<=500 && mouseY >= 250 )
  {
  if (value === 0) {
    value = 255;
  } else {
    value = 0;
  }
    i++;
  }
}