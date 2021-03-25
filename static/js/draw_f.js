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
    
    var d = $('#my-data').data('d');
    var tx = $('#my-data').data('tx');
    var ty = $('#my-data').data('ty');
    var x = $('#my-data').data('x')
    var y = $('#my-data').data('y');

        console.log(d,tx)
    
    var canvas = document.getElementById("canvasimg");
        if (canvas.getContext) {
        var ctx = canvas.getContext('2d');
        ctx.fillStyle = 'rgb(255,0,0)';
        var radius = 4; // Arc radius
        var startAngle = 0; // Starting point on circle
        var endAngle = Math.PI*2; // End point on circle
        var anticlockwise = false;
        ctx.beginPath();
        ctx.arc(y, x, radius, startAngle, endAngle, true);
        ctx.closePath();
        ctx.fill();

        ctx = canvas.getContext('2d');
        ctx.fillStyle = 'rgb(0,255,0)';
        var radius = 4; // Arc radius
        var startAngle = 0; // Starting point on circle
        var endAngle = Math.PI*2; // End point on circle
        var anticlockwise = false;
        ctx.beginPath();
        ctx.arc(ty, tx, radius, startAngle, endAngle, true);
        ctx.closePath();
        ctx.fill();

        }
    
    });   
});