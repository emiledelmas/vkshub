// Where is the circle
let x, y;
let speedx = 1;
let speedy = 1;

function setup() {
  createCanvas(900, 600);
  // Starts in the middle
  x = 450;
  y = 300;
  rSlider = createSlider(1, 10, 2);
  rSlider.position(20, 20);
  img = loadImage('../static/main_hub/dvd.png');
}

function draw() {
  background(0);
  stroke(255);
  textSize(32);
  text(rSlider.value(),100,70);
  textSize(20);
  text('Speed',200,40);
  // Draw a circle
  stroke(50);
  fill(255);
  image(img,x, y,100,100);
  r=random(255);g=random(255);b=random(255);
  if (speedx<0 && speedy<0)
  {
      speedx=-rSlider.value();
      speedy=-rSlider.value();
  }
  else if (speedx>0 && speedy<0)
  {
      speedx=rSlider.value();
      speedy=-rSlider.value();
  }
  else if (speedx<0 && speedy>0)
  {
      speedx=-rSlider.value();
      speedy=rSlider.value();
  }
  else
  {
    speedy=rSlider.value();
    speedx=rSlider.value();
  }
  y = y + speedx;
  x = x + speedy;
  if (x<=-5 || x>=800)
  {
    speedx = speedx;
    speedy = -speedy;
    tint(r, g, b);
  }
  else if (y<=-10 || y>=520)
  {
  speedy = speedy;
  speedx = -speedx;
  tint(r, g, b);
  }

}


/*
// Where is the circle
let x, y;
let speedx = 1;
let speedy = 1;

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
  text('Speed',200,40);
  // Draw a circle
  stroke(50);
  fill(255);
  circle(x, y, 20);
  if (speedx<0 && speedy<0)
  {
      speedx=-rSlider.value();
      speedy=-rSlider.value();
  }
  else if (speedx>0 && speedy<0)
  {
      speedx=rSlider.value();
      speedy=-rSlider.value();
  }
  else if (speedx<0 && speedy>0)
  {
      speedx=-rSlider.value();
      speedy=rSlider.value();
  }
  else
  {
    speedy=rSlider.value();
    speedx=rSlider.value();
  }
  y = y + speedx;
  x = x + speedy;
  if (x<=20 || x>=880)
  {
    speedx = speedx;
    speedy = -speedy;
  }
  else if (y<=20 || y>=580)
  {
  speedy = speedy;
  speedx = -speedx;
  }

}
*/

