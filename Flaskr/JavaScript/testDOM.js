/**
 * Created by joe on 2015/12/22.
 */
//插入节点
var js = ducument.getElementById('js');
var list = document.getElementById('list');
list.appendChild(js)

//新建一个节点插入到指定位置
var
    list = document.getElementById('list');
    haskell = document.createElement('p');
haskell.id = 'haskell';
haskell.innerText = 'Haskell';
list.appendChild(haskell);

//动态创建新的节点
var d = document.createElement('style');
d.setAttribute('type', 'text/css');
d.innerHTML = 'p{color: red}';
document.getElementsByTagName('head')[0].appendChild(d)
