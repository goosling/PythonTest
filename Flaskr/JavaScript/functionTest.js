/**
 * Created by joe on 2015/12/22.
 */

// 闭包，借助闭包，可以封装一个私有变量
'use strict'
// 创建计数器
function create_counter(initial){
    var x = initial || 0;
    return {
        inc : function(){
            x += 1;
            return x;
        }
    }
}

var c1 = create_counter();
c1.inc();//1
c1.inc();//2
c1.inc();//3

var c2 = create_counter(10);
c2.inc();//11
c2.inc();//12
c2.inc();//13

// 计算次方
function make_pow(n){
    return function(x){
        return Math.pow(x, n);
    }
}


var pow2 = make_pow(2);
var pow3 = make_pow(3);

pow2(5);
pow3(7);


// 箭头函数
(x, y, ...rest) => {
    var i, sum = x + y;
    for (i=0; i<rest.length; i++) {
        sum += rest[i];
    }
    return sum;
}

var obj = {
    birth: 1990,
    getAge: function () {
        var b = this.birth; // 1990
        var fn = () => new Date().getFullYear() - this.birth; // this指向obj对象
        return fn();
    }
};
obj.getAge(); // 25


//生成器，generator
function* foo(x){
    yield x+1;
    yield x+2;
    yield x+3;
}

// 斐波那契数列
function fib(max){
    var t,
        a = 0,
        b = 1,
        arr = [0, 1];
    while(arr.length<max){
        t = a + b;
        a = b;
        b = t;
        arr.push(t);
    }
    return arr;
}
fib(5); //[0,1,1,2,3]
fib(10);// [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


//generator
function* fib(max) {
    var
        t,
        a = 0,
        b = 1,
        n = 1;
    while (n < max) {
        yield a;
        t = a + b;
        a = b;
        b = t;
        n ++;
    }
    return a;
}
//1. 不断调用generator对象
var f = fib(5);
f.next();
f.next();
f.next();
f.next();
f.next();

//2. 直接for...of循环
for(var x of fib(5)){
    console.log(x);
}