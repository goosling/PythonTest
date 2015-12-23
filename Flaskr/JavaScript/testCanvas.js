/**
 * Created by joe on 2015/12/23.
 */
'use strict'
var
    canvas = document.getElementById('test-shape-canvas'),
    cancon = canvas.getContext('2d');
//擦除位置大小为200X200的矩形
cancon.clearRect(0, 0, 200, 200);
//设置颜色
cancon.fillStyle = '#dddddd';
//涂色
cancon.fillRect(10, 10, 130, 130);
//利用path绘制复杂路径
var path = new Path2D();
path.arc(75, 75, 50, 0, Math.PI*2, true);
path.moveTo(110,75);
path.arc(75, 75, 35, 0, Math.PI, false);
path.moveTo(65, 65);
path.arc(60, 65, 5, 0, Math.PI*2, true);
path.moveTo(95, 65);
path.arc(90, 65, 5, 0, Math.PI*2, true);
ctx.strokeStyle = '#0000ff';
ctx.stroke(path);

//绘制文字
ctx.clearRect(0, 0, canvas.width, canvas.height);
ctx.shadowOffsetX = 2;
ctx.shadowOffsetY = 2;
ctx.shadowBlur = 2;
ctx.shadowColor = '#666666';
ctx.font = '24px Arial';
ctx.fillStyle = '#333333';
ctx.fillText('带阴影的文字', 20, 40);
