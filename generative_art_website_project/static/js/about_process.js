let a;
let b;
let c;
let d;
let x;
let y;
let count = 0;
let rows = 2, cols = 2;
let rowWidth, colWidth;
let sketches = new Array(rows * cols);
let values = [
    [1.6206032928103675, -2.210137483122419, 2.2831205728573134, -2.5580894710091657],
    [1.2360674672988272, -2.68185712576419, 2.3133281865976856, -2.0342995997849718],
    [1.1607646863313583, -1.8802111358354563, 2.4561795420211245, -2.4614173799640806],
    [1.8426815939517394, -1.823108105996831, 2.5250463329580364, -1.7270889614794787]
];


function setup() {
    let canvas = createCanvas(400, 400);
    canvas.parent('ifs-holder');
    rowWidth = width / rows;
    colWidth = height / cols;
    let idx = 0;
    for (let i = 0; i < rows; ++i) {
        for (let j = 0; j < cols; ++j) {
            a = values[idx][0];
            b = values[idx][1];
            c = values[idx][2];
            d = values[idx][3];
            idx++;
            values.push([a, b, c, d]);
            sketches[i * rows + j] = new DeJongIFS(a, b, c, d, i, j);
        }
    }
    background(color('#F4F0DB'));
    noFill();
    rect(0, 0, width, height);
}

function draw() {
    noFill();
    stroke(0);
    strokeWeight(2);
    rect(0, 0, width, height);
    for (let sketch of sketches)
        sketch.nextIteration();
    if (++count === 500) {
        noLoop();
    }
}