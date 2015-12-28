/**
 * Created by joe on 2015/12/28.
 */
'use strict'

//按照js标准，异步读取一个文本文件代码

var fs = require('fs');

fs.readFile('sample.txt', 'utf-8', function(err, data){
    if(err){
        console.log(err);
    }else{
        console.log(data);
    }
});

//如何读取二进制文件-》图片文件,
// 不传入文件编码时，回调函数的data参数将返回一个Buffer对象
fs.readFile('sample.png', function(err, data){
    if(err){
        console.log(err);
    }else{
        console.log(data);
        console.log(data.length+'bytes');
    }
});

//buffer和string互相转换
//buffer->string
var text = data.toString('utf-8');
console.log(text);

//string->buffer
var buffer = new Buffer(text, 'utf-8');
console.log(buffer);


//同步读取文件，不加回调函数
try{
    var dataSync = fs.readFileSync('sample.txt', 'utf-8');
    console.log(data);
}catch(err){
    console.log('error');
}

//写文件 fs.writeFile()
var data2 = 'Hello, Node.js';
fs.writeFile('output.txt', data2, function(err){
    if(err){
        console.log(err);
    }else{
        console.log('ok')
    }
});

//同步写入
fs.wirteFileSync('output.txt', data2);


//stat
fs.stat('sample.txt', function (err, stat) {
    if (err) {
        console.log(err);
    } else {
        // 是否是文件:
        console.log('isFile: ' + stat.isFile());
        // 是否是目录:
        console.log('isDirectory: ' + stat.isDirectory());
        if (stat.isFile()) {
            // 文件大小:
            console.log('size: ' + stat.size);
            // 创建时间, Date对象:
            console.log('birth time: ' + stat.birthtime);
            // 修改时间, Date对象:
            console.log('modified time: ' + stat.mtime);
        }
    }
});

