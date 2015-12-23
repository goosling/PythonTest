/**
 * Created by joe on 2015/12/23.
 */
// 文本框
//<input type="text">
// 口令框
//<input type="password">
// 单选框
//<input type="radio">

//复选框
//<input type="checkbox">
//下拉框
//<select>
//隐藏文本
//<input type="hidden">

//获取值
//<input type="text" id="email">
var input = document.getElementById('email');
//设置值
input.value = "test@example.com"
input.value;


// <label><input type="radio" name="weekday" id="monday" value="1"> Monday</label>
// <label><input type="radio" name="weekday" id="tuesday" value="2"> Thurthday</label>
var mon = document.getElementById('monday');
var tue = document.getElementById('tuesday');
mon.value; // '1'
tue.value; // '2'
mon.checked; // true或者false
tue.checked;// true或者false,对于复选框，设置checked为true或者false即可


//<!--html-->
//<form id='test-form'>
//    <input type="text" name="test">
//    <button type="button" onclick="doSubmitForm()">Submit</button>
//</form>
function doSubmitForm(){
    var form = document.getElementById("test-form");
    //可以在此修改form的input
    form.submit();
}

//查看文件名是否合法
var f = document.getElementById('test-file-upload');
var filename = f.value; // 'C:\fakepath\test.png'
if (!filename || !(filename.endsWith('.jpg') || filename.endsWith('.png') || filename.endsWith('.gif'))) {
    alert('Can only upload image file.');
    return false;
}


//如何读取用户选取的图片文件，并在一个div中显示
var
    fileInput = document.getElementById("test-image-file"),
    info = document.getElementById('test-file-info'),
    preview = document.getElementById('test-image-preview');
//监听change事件
fileInput.addEventListener('change', function(){
    //清除背景图片
    preview.style.backgroundImage = '';
    //检查文件是否存在
    if(!fileInput.value){
        info.innerHTML = '没有选择文件';
        return;
    }
    //获取file引用
    var file = fileInput.file[0];
    //获取file信息
    info.innerHTML = '文件：'+file.name+'<br>'+'大小：'+
        file.size+'<br>'+'修改：'+file.lastModifiedDate;
    if(file.type !== 'image/jpeg' && file.type!=='image/png'
        && file.type !== 'image/gif'){
        alert('不是有效的图片');
        return;
    }
    //读取文件
    var reader = new FileReader();
    reader.onload = function(e){
        var data = e.target.result;
        preview.style.backgroundImage = 'url('+data+')';
    };
    reader.readAsDataURL(file);

})