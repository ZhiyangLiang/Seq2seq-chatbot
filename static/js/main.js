/*jshint esversion: 6 */
let btn = document.querySelector("button");//获得button元素
let textArea = document.querySelector("textarea");
let inp = document.querySelector(".inp");
let msg = document.querySelector(".msg");
btn.onclick=function(e){
    // if (textArea.value) {
    e.preventDefault();
    let formElement = document.querySelector('form');
    let formData = new FormData(formElement);
    // let rec_text = [formData.get()];
    // msg.innerHTML="<li class='msg_transfer'>"+textArea.value+"</li>";//将标签信息添加到ul中
    // textArea.value="";//清空输入框
    let xhr = new XMLHttpRequest();
    xhr.responseType = 'text';
    xhr.open('POST', 'http://127.0.0.1:5000/processText', true);
    xhr.onload = function (e) {
        // text = xhr.response
        inp.innerHTML="<li class='input_msg'>"+textArea.value+"</li>";
        msg.innerHTML="<li class='msg_transfer'>"+xhr.response+"</li>";
        // transfer_text.src = xhr.response;
        // document.querySelector('.transfer_msg').appendChild(transfer_text);

    };
    xhr.send(formData);
    // } else {
    //     alert("请输入测试文本");
    // }
}