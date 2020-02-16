let len,angle,lenmult;
function setup() {
  createCanvas(400, 400);
  slider = createSlider(0,TWO_PI,PI/4,0.001);
  slider2 = createSlider(0,0.75,0.67,0.001);
}
function draw() {
  background(255);
  stroke(0);
  angle = slider.value();
  lenmult = slider2.value();
  translate(200,height);
  branch(100);
}
function branch(len){
    line(0,0,0,-len); 
    translate(0,-len);
    if (len>4)
    {
      push();
      rotate(angle);
      branch(len*lenmult);
      pop();
      rotate(-angle);
      branch(len*lenmult);
    }
}