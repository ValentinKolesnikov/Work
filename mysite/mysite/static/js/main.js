
function like(btn){
    btn.removeAttribute('onclick');
    var formData = new FormData();
    var parent = btn.parentNode;
    formData.append('id',parent.getAttribute('id'));
    var mark = Number(parent.lastChild.innerHTML);
    var name = document.getElementById('user');
    if(name){
      console.log(parent.getAttribute('id'));
      if (parent.getAttribute('class') == 'like-added'){
        parent.removeAttribute('class');
        mark--;
      } else {
        parent.setAttribute('class', 'like-added')
        mark++;
      }
      parent.lastChild.innerHTML = " " + mark;
      var xhr = new XMLHttpRequest();
      xhr.open("POST", "/work/like");
      xhr.send(formData);
    }
    setTimeout(function () {
      btn.setAttribute('onclick', 'like(this)');
    }, 300)
  }
  
  function newMessage(){

    var formData = new FormData(document.forms.postmessage);
    var xhr = new XMLHttpRequest();
    xhr.open("POST", window.location.href);
    xhr.send(formData);
    var name = document.getElementById('user');
    var messageBlock = document.getElementById('messages');
    var input = document.getElementById('text');
    if(input.value != ""){
      messageBlock.innerHTML += `<div class="message">
        <div >`+name.textContent+` только что</div>
        <div>`+input.value+`</div>
      </div>`;
      input.value = "";
    }
  }