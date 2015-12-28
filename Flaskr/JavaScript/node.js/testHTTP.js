/**
 * Created by joe on 2015/12/28.
 */
'use strict'

//导入http模块
var http = require('http');

//创建http server， 并传入回调函数
var server = http.createServer(function(request, response){
    //回调函数接收request，response对象
    //获得http请求的method和url
    console.log(request.method+':'+request.url);
    //将相应200写入response，同时设置content-Type：text/html
    response.writeHead(200, {'Content-Type': 'text/html'});
    //将http相应的内容写入response
    response.end('<h1>Hello world</h1>')
});

//让服务器监听8080端口
server.listen(8080);

console.log('server is running at http://127.0.0.1:8080');

//构造目录
var path = require('path');

// 解析当前目录:
var workDir = path.resolve('.'); // '/Users/michael'

// 组合完整的文件路径:当前目录+'pub'+'index.html':
var filePath = path.join(workDir, 'pub', 'index.html');
// '/Users/michael/pub/index.html'