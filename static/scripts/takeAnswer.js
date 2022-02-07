var buttonNo = document.getElementById('button-no');
buttonNo.addEventListener('click', () =>{
    var input1 = document.getElementById('question-no');
    input1.value = 'no';
});

var buttonYes = document.getElementById('button-yes');
buttonYes.addEventListener('click', () => {
    var input1 = document.getElementById('question-no');
    input1.value = 'yes';
});

function sendRequest(questionNo, answer){
    var xhr = new XMLHttpRequest();
    xhr.open('GET', '/take_answer?questionNo=' + questionNo + '&answer=' + answer);
    xhr.send();
}

function redirect(questionNo){
    pom = parseInt(questionNo) + 1;
    console.log(pom);
    window.location.replace("http://127.0.0.1:8000/pitanje" + String(pom));
}