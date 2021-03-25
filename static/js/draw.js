window.addEventListener("DOMContentLoaded", function()
{
    var image =  new Image();
    image.src = 'static/outputs/input_e.jpg';
    image.addEventListener('load', e => {
    var canvas = document.getElementById("canvasimg");

    canvas.width  = image.width;
    canvas.height = image.height;

    var context = canvas.getContext("2d");

    console.log(context.drawImage(image, 0, 0));

    var img = d3.select("canvas");
    img.on("click", createDot);
    var flag =0;
    var x,y;
    function createDot() {
        if(flag==0){
        flag = 1;
        let pos = d3.mouse(this);
        var canvas = document.getElementById("canvasimg");
        if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        console.log(pos);
        ctx.fillStyle = 'rgb(255,0,0)';
        var radius = 4; // Arc radius
        var startAngle = 0; // Starting point on circle
        var endAngle = Math.PI*2; // End point on circle
        var anticlockwise = false;
        ctx.arc(pos[0], pos[1], radius, startAngle, endAngle, true);
        ctx.fill();

        x = Math.round(pos[0]);
        y = Math.round(pos[1]);
        console.log(x,y);
        }
    }
    var p = document.getElementById("det");
    p.innerHTML = `The selected point is (${y},${x})`;
    document.getElementById("x").value = y;
    document.getElementById("y").value = x;
    };
    });   
});