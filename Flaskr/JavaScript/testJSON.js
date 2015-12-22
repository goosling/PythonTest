/**
 * Created by joe on 2015/12/22.
 */

var xiaoming = {
    name: '小明',
    age: 14,
    gender: true,
    height: 1.70,
    grade: null,
    'middle-school': 'normal Middle School',
    skills: ['Java', 'Python']
};

JSON.stringify(xiaoming);
//照缩进输出,第二个参数用于控制如何筛选对象的键值，如果我们只想输出指定的属性，
// 可以传入Array,JSON.stringify(xiaoming, ['name', 'skills'], '  ')
JSON.stringify(xiaoming, null, ' ');

// 原型对象
var Student = {
    name: 'Robot',
    height: 1.2,
    run: function() {
        console.log(this.name+' is running');
    }
};

function createStudent(name) {
    //基于Student原型创建一个新对象
    var s = Object.create(Student);
    s.name = name;
    return s;
}

var xiaohong = createStudent('小红');
xiaohong.run();
xiaohong.__proto__ === Student


//构造函数
function Student(name){
    this.name = name;
    this.hello = function () {
        alert('Hello,'+this.name+'!');
    }
}

var xiaogang = new Student('小刚');
xiaogang.name;//小刚
xiaogang.hello();


//内部封装new操作
function Student(props){
    this.name = props.name;
    this.grade = props.grade;
}
Student.prototype.hello = function(){
    alert('Hello,'+this.name+'!');
}
function createStudent1(props){
    return new Student(props||{});
}

//原型继承
function inherits(Child, Parent){
    var F = function(){};
    F.prototype = Parent.prototype;
    Child.prototype = new F();
    Child.prototype.constructor = Child;
}