
function like(btn){
    btn.removeAttribute('onclick');
    var formData = new FormData();
    var parent = btn.parentNode;
    formData.append('id',parent.getAttribute('id'));
    var mark = Number(parent.lastChild.innerHTML);
    var name = document.getElementById('user');
    if(name){
        console.log('fds');
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
  