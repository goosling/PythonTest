/**
 * Created by joe on 2015/12/23.
 */
//<ul class="lang">
//    <li class="js dy">JavaScript</li>
//    <li class="dy">Python</li>
//    <li id="swift">Swift</li>
//    <li class="dy">Scheme</li>
//    <li name="haskell">Haskell</li>
//</ul>

var ul = $('ul.lang');
var dy = ul.find('.dy');
var swf = ul.find('#swift');
var hsk = ul.find('[name=haskell]');
//从当前节点向上查找
var parent = swf.parent();
//同一级可以使用
swf.next();
swf.prev();


//过滤
var langs = $('ul.lang li');
langs.filter(function() {
    return this.innerHTML.indexOf('S') === 0;
});

//map方法把一个jQuery对象包含的若干DOM节点转化为其他对象：
var arr = langs.map(function(){
    return this.innerHTML;
}).get();

var js = langs.first();
var haskell = langs.last();
var sub = langs.slice(2, 4);

//修改css，批量操作
$('#test-css li.dy>span').css('background-color', '#ffd351').css('color','red');


//nice code
var ul=$("#test-div ul");
["Pascal","Lua","Ruby"].map(
function(x){
   ul.append("<li><span>"+x+"</span></li>");}
);
var li =ul.find('li');
//根据字母排序
li.sort(function(x,y){
if($(x).text()>$(y).text()) return 1;
else return -1;
});
ul.append(li);

//事件处理
$(document).on('ready', function(){
    $('#testForm').on('submit',function(){
        alert('submit!');
    });
});
//简化版本
$(document).ready(function(){
   $('#testForm').submit(function(){
       alert('submit');
   });
});

//再简化版,牢记这是document对象的ready事件处理函数
$(function(){
    $('#testForm').on('submit',function(){
        alert('submit!');
    });
});

//事件参数
$(function(){
    $('testMouseMoveDiv').mousemove(function(){
         $('#testMouseMoveSpan').text('pageX = ' + e.pageX + ', pageY = ' + e.pageY);
    });
});







<!-- HTML结构 -->
//<form id="test-form" action="test">
//    <legend>请选择想要学习的编程语言：</legend>
//    <fieldset>
//        <p><label class="selectAll"><input type="checkbox"> <span class="selectAll">全选</span><span class="deselectAll">全不选</span></label> <a href="#0" class="invertSelect">反选</a></p>
//        <p><label><input type="checkbox" name="lang" value="javascript"> JavaScript</label></p>
//        <p><label><input type="checkbox" name="lang" value="python"> Python</label></p>
//        <p><label><input type="checkbox" name="lang" value="ruby"> Ruby</label></p>
//        <p><label><input type="checkbox" name="lang" value="haskell"> Haskell</label></p>
//        <p><label><input type="checkbox" name="lang" value="scheme"> Scheme</label></p>
//        <p><button type="submit">Submit</button></p>
//    </fieldset>
//</form>




//改变状态
//当用户勾上全选时，自动选中所有语言，并把全选换成不选
// TODO:绑定事件
//当用户勾上“全选”时，自动选中所有语言，并把“全选”变成“全不选”；
//当用户去掉“全不选”时，自动不选中所有语言；
'use strict';

var
    form = $('#test-form'),
    langs = form.find('[name=lang]'),
    selectAll = form.find('label.selectAll :checkbox'),
    selectAllLabel = form.find('label.selectAll span.selectAll'),
    deselectAllLabel = form.find('label.selectAll span.deselectAll'),
    invertSelect = form.find('a.invertSelect');

// 重置初始化状态:
form.find('*').show().off();
form.find(':checkbox').prop('checked', false).off();
deselectAllLabel.hide();
// 拦截form提交事件:
form.off().submit(function (e) {
    e.preventDefault();
    alert(form.serialize());
});



selectAll.change(function(){
    langs.prop("checked", this.checked);
    if(selectAll.prop('checked')){
        selectAllLabel.hide();
        deselectAllLabel.show();
    }else{
        selectAllLabel.show();
        deselectAllLabel.hide();
    }
});

//当用户点击“反选”时，自动把所有语言状态反转（选中的变为未选，未选的变为选中）；
invertSelect.on('click', function(){
    langs.prop('checked', function(i, val){
        return !val;
    });
});

//当用户把所有语言都手动勾上时，“全选”被自动勾上，并变为“全不选”；
//当用户手动去掉选中至少一种语言时，“全不选”自动被去掉选中，并变为“全选”。
langs.on('change', function(){
    if(langs.length == $('input[name="lang"]:checked').length){
        selectAll.prop('checked', true);
        selectAllLabel.hide();
        deselectAllLabel.show();
    }else{
        selectAll.prop('checked', false);
        selectAllLabel.show();
        deselectAllLabel.hide();
    }
});