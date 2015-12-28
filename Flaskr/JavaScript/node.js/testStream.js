/**
 * Created by joe on 2015/12/28.
 */
'use strict'

var fs = require('fs');

//打开一个流,读取文件中信息
var rs = fs.createReadStream('sample.txt', 'utf-8');

rs.on('data', function(chunk){
    console.log('DATA:');
    console.log(chunk);
});

rs.on('end', function(){
    console.log('END');
});

rs.on('error', function(err){
    console.log('ERROR:'+err)
});

//要以流的形式写入文件，只需要不断调用write()方法，最后以end()结束
var ws1 = fs.createWirteStream('output1.txt', 'utf-8');
ws1.write('使用Stream写入文本数据。。。\n');
ws1.write('END');
ws1.end();

var ws2 = fs.createWriteStream('output2.txt');
ws2.write(new Buffer('使用Stream写入二进制数据...\n', 'utf-8'));
ws2.write(new Buffer('END.', 'utf-8'));
ws2.end();

//pipe(),实际上是一个复制文件的程序
var rs = fs.createReadStream('sample.txt');
var ws = fs.createWriteStream('copied.txt');

rs.pipe(ws);

//如果我们不希望自动关闭Writable流，需要传入参数：
readable.pipe(writable, { end: false });