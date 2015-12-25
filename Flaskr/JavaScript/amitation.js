/**
 * Created by joe on 2015/12/25.
 */
//动画效果，show()和hide()传入参数

var div = $('#test-show-hide');
div.hide(3000);//将在3s内消失，时间也可以是‘slow''fast'这些字符串
div.toggle('slow');//根据当前状态决定是show还是hide

var slideDiv = $('#test-slide-down-up');
slideDiv.slideDown(3000);
slideDiv.slideUp(3000);

//淡入淡出
var fadeDiv = $('#test-fade');
fadeDiv.fadeIn(3000);
fadeDiv.fadeToggle(3000);


//animate()
var animateDiv = $('#test-animate');
animateDiv.animate({
    opacity: 025,
    width: '256px',
    height: '256px'
}, 3000);//在3s钟内css过渡到设定值

//还可以再传入一个函数，动画结束时该函数被调用
animateDiv.animate({
    opacity: 025,
    width: '256px',
    height: '256px'
}, 3000, function(){
    console.log('动画已结束');
    //恢复初始状态
    $(this).css('opacity', '1.0').css('width', '128px').
        css('height', '128px');
});

//串行动画
var div = $('#test-animates');
// 动画效果：slideDown - 暂停 - 放大 - 暂停 - 缩小
div.slideDown(2000)
   .delay(1000)
   .animate({
       width: '256px',
       height: '256px'
   }, 2000)
   .delay(1000)
   .animate({
       width: '128px',
       height: '128px'
   }, 2000);
