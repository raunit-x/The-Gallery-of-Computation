class DeJongIFS {
    constructor(a, b, c, d, x = 0, y = 0) {
        this.a = a;
        this.b = b;
        this.c = c;
        this.d = d;
        this.x = x;
        this.y = y;
        this.size = (width / 12);
        this.cal = 1;
        this.xTranslation = x * rowWidth + rowWidth / 2;
        this.yTranslation = y * rowWidth + rowWidth / 2;
    }
    nextIteration()
    {
        stroke(0);
        strokeWeight(1);
        noFill();
        rect(this.xTranslation - colWidth / 2, this.yTranslation - rowWidth / 2, rowWidth, colWidth);
        noStroke();
        translate(this.xTranslation, this.yTranslation);
        for (let i = 0; i < 1000; i++)
        {
            let x_next = sin(this.a * this.y) - cos(this.b * this.x);
            let y_next = sin(this.c * this.x) - cos(this.d * this.y);
            fill(color(0, 0, 0, 10));
            ellipse(x_next * this.size, y_next * this.size, 1, 1);
            this.x = x_next;
            this.y = y_next;
        }
        translate(-this.xTranslation, -this.yTranslation);
    }
}