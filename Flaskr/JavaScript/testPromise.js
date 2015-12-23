/**
 * Created by joe on 2015/12/23.
 */
function test(resolve, reject){
    var timeOut = Math.random() * 2;
    log("set timeout to:"+timeout+'seconds...');
    setTimeout(function(){
        if(timeOut<1){
            log('call resolve()');
            resolve('200 0K');
        }else{
            log('call reject()....');
            reject('timeout in'+timeOut+'seconds...');
        }
    }, timeOut*1000);
}

var p1 = new Promise(test);
var p2 = p1.then(function (result) {
    console.log('成功：' + result);
});
var p3 = p2.catch(function (reason) {
    console.log('失败：' + reason);
});


//实际测试清除log
'use strict'
//清除log
var logging = document.getElementById('test-promise-log');
while(logging.children.length>1){
    logging.removeChild(logging.children[logging.children.length-1]);
}

//输出log到页面
function log(s) {
    var p = document.createElement('p');
    p.innerHTML = s;
    logging.appendChild(p);
}

new Promise(function(reslove, reject){
    log('start new promise');
    var timeOut = Math.random()*2;
    log('set timeout to:'+timeOut+'seconds');
    setTimeout(function(){
        if(timeOut<1){
            log('call resolve()...');
            resolve('200 0k');
        }else{
            log('call reject()...');
            reject('timeout in '+ timeOut+'seconds');
        }
    }, timeOut*1000);
}).then(function(r){
        log('Done:'+r);
    }).catch(function(reason){
        log('failed:'+reason)
    });


//多步操作
// 0.5秒后返回input*input的计算结果:
function multiply(input) {
    return new Promise(function (resolve, reject) {
        log('calculating ' + input + ' x ' + input + '...');
        setTimeout(resolve, 500, input * input);
    });
}

// 0.5秒后返回input+input的计算结果:
function add(input) {
    return new Promise(function (resolve, reject) {
        log('calculating ' + input + ' + ' + input + '...');
        setTimeout(resolve, 500, input + input);
    });
}

var p = new Promise(function (resolve, reject) {
    log('start new Promise...');
    resolve(123);
});

p.then(multiply)
 .then(add)
 .then(multiply)
 .then(add)
 .then(function (result) {
    log('Got value: ' + result);
});
