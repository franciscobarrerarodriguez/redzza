// https://developer.mozilla.org/en-US/docs/Web/API

var isOpen = false; //nav-menu status

(function () {
  /* form-login actions */
  $('#form-login').submit(function (e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url: form.attr('data-url'),
      data: form.serialize(),
      dataType: 'json',
      success: function (json) {
        alert(json);/*Falta terminar*/
      }
    });
  });

  /* form-signup actions */
  $('#form-signup').submit(function (e) {
    e.preventDefault();
    var form = $(this);
    $.ajax({
      url: form.attr('data-url'),
      data: form.serialize(),
      dataType: 'json',
      success: function (json) {
        alert(json);/*Falta terminar*/
      }
    });
  });

  /* Listener open menu */
  document.getElementById('nav-button').addEventListener('click', openMenu);
  /* /Open menu */

  /* Close menu */
  document.getElementById('nav-close-button').addEventListener('click', closeMenu);
  /* /Close menu  */

  /* closeMenu */
  document.getElementById('container-all').addEventListener('click', function () {
    if (isOpen) {
      closeMenu();
    }
  });
  /* /closeMenu */

  /* not member modal */
  document.getElementById('button-not-member').addEventListener('click', function () {
    closeModal('modal-login');
    getModal('modal-signup');
  });

  /* Email validation */
  document.getElementById('signup-input').addEventListener("keyup", function (e) {
    var url = $('#signup-input').attr('data-url') +"?email="+ this.value;
        $.get(url, function (data) {
      console.log(data.is_taken);
    });
  });

})();

/* === Modal actions
* Display de modal by id */
function getModal(modalId) {
  var modal = document.getElementById(modalId);
  modal.style.display = 'block';
  window.onclick = function(event) {
    if (event.target == modal) {
      modal.style.display = "none";
    }
  }
}

/* Hidde modal by id */
function closeModal(modalId) {
  document.getElementById(modalId).style.display = 'none';
}

function openMenu() {
  document.getElementById('nav-menu').style.width = '250px';
  document.getElementById('all').style.marginLeft = '250px';
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  isOpen = true;
}

function closeMenu() {
  document.getElementById('nav-menu').style.width = '0';
  document.getElementById('all').style.marginLeft = '0';
  document.body.style.backgroundColor = "white";
  isOpen = false;
}
