// Where is the circle
let x, y;

function setup() {
  createCanvas(900, 600);
  // Starts in the middle
  x = 0;
  y = 600;
}

function draw() {
  background(0);
  // Draw a circle
  stroke(50);
  fill(255);
  circle(x, y, 20);
  // Moving up at a constant speed
  y = y - 1;
  x = x + 1;

}

