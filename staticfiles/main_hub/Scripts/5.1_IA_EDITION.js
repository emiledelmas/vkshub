let model;
let targetLabel = 'R';

let state = 'collection';

function setup() {
  createCanvas(400, 400);

  let options = {
    inputs: ['x', 'y'],
    outputs: ['label'],
    task: 'classification',
    debug: 'true'
  };
  model = ml5.neuralNetwork(options);
  background(0);
}

function keyPressed() {

  if (key == 't') {
    state = 'training';
    console.log('starting training');
    model.normalizeData();
    let options = {
      epochs: 300
    }
    model.train(options, whileTraining, finishedTraining);
  } else {
    targetLabel = key.toUpperCase();
  }
}

function whileTraining(epoch, loss) {
  console.log(epoch);
}

function finishedTraining() {
  console.log('finished training.');
  state = 'prediction';
}


function mousePressed() {
  
  let inputs = {
    x: mouseX,
    y: mouseY
  }
  if (targetLabel == 'R')
    targetLabel = 'red'
  else if (targetLabel == 'G')
    targetLabel = 'green'
  else if (targetLabel == 'B')
    targetLabel = 'blue'
  else if (targetLabel == 'Y')
    targetLabel = 'yellow'
    
  if (state == 'collection') {
    let target = {
      label: targetLabel
    }
    model.addData(inputs, target);
    stroke(targetLabel);
    noFill();
    ellipse(mouseX, mouseY, 24);
  
    
  } else if (state == 'prediction') {
    model.classify(inputs, gotResults);

  }

}

function gotResults(error, results) {
  if (error) {
    console.error(error);
    return;
  }
  console.log(results);
  let label = results[0].label;
  stroke(label);
  ellipse(mouseX, mouseY, 24);
}