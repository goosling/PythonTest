/**
 * Created by joe on 2015/12/25.
 */
//扩展
//在jQuery中高亮某一行
$('span.hl').css('backgroundColor', '#fffceb').css('color','#d85030');
$('p a.hl').css('backgroundColor', '#fffceb').css('color', '#d85030');

//jQuery插件
$.fn.hilight1 = function() {
    //this绑定为当前jQuery对象
    this.css('backgroundColor','#fffceb').css('color','#d85030');
    //return this可以支持链式操作
    return this;
}

//带参数版本
$.fn.highlight2 = function(options){
    var bgcolor = options && options.backgroundColor || '#fffceb';
    var color = options && options.color || '#d85030';
    this.css('backgroundColor', bgcolor).css('color', color);
    return this;
}

//$.extend(target, obj1, obj2....)
//把多个object对象的属性合并到第一个target对象中，遇到同名属性，
// 总是使用靠后的对象的值，也就是越往后优先级越高
var opts = $.extend({}, {
    backgroundColor: '#00a8e6',
    color: '#ffffff'
}, options);

//最终版
$.fn.highlight = function (options) {
    // 合并默认值和用户设定值:
    var opts = $.extend({}, $.fn.highlight.defaults, options);
    this.css('backgroundColor', opts.backgroundColor).css('color', opts.color);
    return this;
}

// 设定默认值:
$.fn.highlight.defaults = {
    color: '#d85030',
    backgroundColor: '#fff8de'
}


//----------------------------------------------------
//COLLECTIONS
//every/some
//_.every([1,4,7,-3,-9], (x)=>x>0);  false

//groupBy()
var scores = [20, 81, 77,99,23,33, 43, 66, 64, 73 ,33]
var groups = _.groupBy(scores, function(){
    if(x<60){
        return 'C';
    }else if(x<80) {
        return 'B';
    }else{
        return 'A';
    }
});

//partial偏函数
//求2的N次方
var pow2N = _.partial(Math.pow, 2);
//求N的3次方
var cube = _.partial(Math.pow, _, 3);

//memorize
var factorial = _.memoize(function(n) {
    console.log('start calculate ' + n + '!...');
    var s = 1, i = n;
    while (i > 1) {
        s = s * i;
        i --;
    }
    console.log(n + '! = ' + s);
    return s;
});