// Where is the circle
let x, y;
let speedx = 1;
let speedy = 1;
let increase;

function setup() {
  createCanvas(900, 600);
  // Starts in the middle
  x = 450;
  y = 300;
  rSlider = createSlider(1, 10, 2);
  rSlider.position(20, 20);
}

function draw() {
  background(0);
  stroke(255);
  textSize(32);
  text(rSlider.value(),100,70);
  textSize(20);
  text('Value of speed increasing',200,40);
  // Draw a circle
  stroke(50);
  fill(255);
  circle(x, y, 20);
  y = y - speedx;
  x = x + speedy;
  if (x<=20 || x>=880)
  {
    increase = rSlider.value();
    speedx = increase*speedx;
    speedy = -increase*speedy;
  }
  else if (y<=20 || y>=580)
  {
  increase = rSlider.value();
  speedy = increase*speedy;
  speedx = -increase*speedx;
  }

}

