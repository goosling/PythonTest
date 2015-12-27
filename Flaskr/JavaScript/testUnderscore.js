/**
 * Created by joe on 2015/12/25.
 */
//mapObject

var obj = {a:1, b:2, c:3};
_.mapObject(obj, (v,k)=>100+v);

//invert
var obj = {
    Adam: 90,
    Lisa: 96,
    Bart: 20
};
_.invert(obj);

//extend/extendOwn
//extend()把多个object的key-value合并到第一个object并返回
// ,extendOwn()和extend()类似，但获取属性时忽略从原型链继承下来的属性

var a = {name: 'Bob', age: 20};
_.extend(a, {age: 15}, {age: 88, city: 'Beijing'}); // {name: 'Bob', age: 88, city: 'Beijing'}
// 变量a的内容也改变了：
a; // {name: 'Bob', age: 88, city: 'Beijing'}

//clone,浅复制，指针指向统一位置
var source = {
    name: '小明',
    age: 20,
    skills: ['JavaScript', 'CSS', 'HTML']
};
var copied = _.clone(source);

//chain()链式调用
_.chain([1, 4, 9, 16, 25])
 .map(Math.sqrt)
 .filter(x => x % 2 === 1)
 .value();