
let drops;

class rainDrop {
    constructor()
    {
        this.x = 0;
        this.y = 0;
        this.reinitialize();
        this.vel = 50;
        this.length = 60;
    }


    reinitialize()
    {
        this.x = random(0, width);
        this.y = random(0, height / 2);
    }

    update()
    {
        if(this.x > width || this.x < 0)
        {
            this.reinitialize();
        }
        if(this.y > height / 2)
        {
            this.reinitialize();
        }
        this.x -= 0.1 * this.vel;
        this.y += 0.06 * this.vel;
    }

    show()
    {
        strokeWeight(0.5);
        stroke(color(100, 100, 100, 10));
        line(this.x, this.y, this.x - this.length, this.y + 0.6 * this.length);
    }
}


function setup()
{
    let canvasBackground = createCanvas(windowWidth, windowHeight);
    canvasBackground.style('z-index', '-1');
    canvasBackground.position(0, 0);
    background(255);
    drops = new Array(20);
    for(let i = 0; i < drops.length; ++i)
        drops[i] = new rainDrop();
}
function draw() {
    noLoop();
    // background(255);
    for(let drop of drops)
    {
        drop.update();
        drop.show();
    }
}

