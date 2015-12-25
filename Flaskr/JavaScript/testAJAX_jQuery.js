/**
 * Created by joe on 2015/12/25.
 */
//jQuery在全局对象jQuery（也就是$）绑定了ajax()函数，可以处理AJAX请求。
// ajax(url, settings)函数需要接收一个URL和一个可选的settings对象，常用的选项如下：
//async：是否异步执行AJAX请求，默认为true，千万不要指定为false；
//
//method：发送的Method，缺省为'GET'，可指定为'POST'、'PUT'等；
//
//contentType：发送POST请求的格式，默认值为'application/x-www-form-urlencoded; charset=UTF-8'，也可以指定为text/plain、application/json；
//
//data：发送的数据，可以是字符串、数组或object。如果是GET请求，data将被转换成query附加到URL上，如果是POST请求，根据contentType把data序列化成合适的格式；
//
//headers：发送的额外的HTTP头，必须是一个object；
//
//dataType：接收的数据格式，可以指定为'html'、'xml'、'json'、'text'等，缺省情况下根据响应的Content-Type猜测。

//发送一个GET请求，并返回一个JSON格式的数据
var jqxhr = $.ajax('/api/categories', {
    dataType: 'json'
});



//get方法，第二个参数如果是object，jQuery自动把它变成query string然后加到URL后面
var jqxhr = $.get('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
});
//实际URL是/path/to/resource?name=Bob%20Lee&check=1

//post方法，但是传入的第二个参数默认被序列化为application/x-www-form-urlencoded
var jqxhr = $.post('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
});

//getJSON()方法
var jqxhr = $.getJSON('/path/to/resource', {
    name: 'Bob Lee',
    check: 1
}).done(function (data) {
    // data已经被解析为JSON对象了
});