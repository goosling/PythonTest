/**
 * Created by joe on 2015/12/23.
 */
'use strict'
function success(text){
    var textarea = document.getElementById('test-response-text');
    textarea.value = text;
}

function fail(code){
    var textarea = document.getElementById('test-response-text');
    textarea.value = 'Error code:'+code;
}

var request = new XMLHttpRequest();//新建XMLHttpRequest对象
request.onreadystatechange = function(){
    //状态发生变化时，函数被回调
    if(request.readyState === 4){
        //成功完成，判断响应结果
        if(request.status === 200) {
            //成功，通过responseText拿到响应文本
            return success(request.responseText);
        }else{
            return fail(request.status);
        }
    }else{
        //Http请求还在继续
    }
}

//发送请求
request.open('GET', '/api/categories');
request.send();

alert('请求已发送，请等待响应');


//JSONP请求外域URL，以函数调用的形式返回，可以先在页面中准备好回调函数
function refreshPrice(data){
    var p = document.getElementById('test-jsonp');
    p.innerHTML =  '当前价格：' +
        data['0000001'].name +': ' +
        data['0000001'].price + '；' +
        data['1399001'].name + ': ' +
        data['1399001'].price;
}
//然后用getPrice函数触发
function getPrice() {
    var
        js = document.createElement('script'),
        head = document.getElementsByTagName('head')[0];
    js.src = 'http://api.money.126.net/data/feed/0000001,1399001?callback=refreshPrice';
    head.appendChild(js);
}


//promise简化AJAX
'use strict';

// ajax函数将返回Promise对象:
function ajax(method, url, data) {
    var request = new XMLHttpRequest();
    return new Promise(function (resolve, reject) {
        request.onreadystatechange = function () {
            if (request.readyState === 4) {
                if (request.status === 200) {
                    resolve(request.responseText);
                } else {
                    reject(request.status);
                }
            }
        };
        request.open(method, url);
        request.send(data);
    });
}

var log = document.getElementById('test-promise-ajax-result');
var p = ajax('GET', '/api/categories');
p.then(function (text) { // 如果AJAX成功，获得响应内容
    log.innerText = text;
}).catch(function (status) { // 如果AJAX失败，获得响应代码
    log.innerText = 'ERROR: ' + status;
});