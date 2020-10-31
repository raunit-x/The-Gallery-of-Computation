let symmetry = 24;

let angle = 360 / symmetry;


// function initialize()
// {
//     background(255);
//     noFill();
//     stroke(0);
//     strokeWeight(2);
//     rect(0, 0, width, height);
//     angleMode(DEGREES);
// }

function setup() {
    let canvas = createCanvas(0.8 * windowWidth, 0.8 * windowHeight);
    canvas.parent('sketch-holder');
    background(255);
    noFill();
    stroke(0);
    strokeWeight(2);
    rect(0, 0, width, height);
    angleMode(DEGREES);
}

function windowResized() {
    resizeCanvas(0.8 * windowWidth, 0.8 * windowHeight);
}


function keyPressed() {
    if (keyCode === ENTER) {
        setup();
    }

    if (key === 's') {
        save('Mandala Sketch.png');
        setup();
        setup();
    }
}


function drawMandala() {
    // console.log('here');
    translate(width / 2, height / 2);
    if (mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
        let mx = mouseX - width / 2;
        let my = mouseY - height / 2;
        let pmx = pmouseX - width / 2;
        let pmy = pmouseY - height / 2;
        if (mouseIsPressed) {
            for (let i = 0; i < symmetry; i++) {
                rotate(angle);
                let sw = 2;
                strokeWeight(sw);
                stroke(100, 100);
                line(mx, my, pmx, pmy);
                push();
                scale(1, -1);
                line(mx, my, pmx, pmy);
                pop();
            }
        }
    }
}


function draw() {
    // console.log('here');
    drawMandala();
}