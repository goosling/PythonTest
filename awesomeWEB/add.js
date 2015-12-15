/**
 * Created by joe on 2015/12/10.
 */
function add(){
    var adder1=Number(document.form1.adder1.value);
    var adder2=Number(document.form1.adder2.value);
    var result=adder1+adder2;
    document.form1.result.value = result;
}

function minus(){
    var mi1 = Number(document.form2.mi1.value);
    var mi2=Number(document.form2.mi2.value);
    var result=mi1-mi2;
    document.form2.result.value=result;
}