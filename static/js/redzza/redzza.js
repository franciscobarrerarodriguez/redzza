// https://developer.mozilla.org/en-US/docs/Web/API

/* Menu variables */
var isOpen = false; //nav-menu status
var navButton = document.getElementById('nav-button');
var closeButton = document.getElementById('nav-close-button');
var buttonNotMember = document.getElementById('button-not-member');
var navMenu = document.getElementById('nav-menu');

/* Body variables */
var all = document.getElementById('all');
var containerAll = document.getElementById('container-all');

(function () {
  navButton.addEventListener('click', openMenu); // Listener open menu
  closeButton.addEventListener('click', closeMenu); // Close menu

  containerAll.addEventListener('click', function () { // Close menu when it's open
    if (isOpen) {
      closeMenu();
    }
  });

  buttonNotMember.addEventListener('click', function () { // Listener button Not Member
    closeModal('modal-login');
    getModal('modal-signup');
  });

  /* form-signup actions */
  $('#form-signup').submit(function (e) {
    e.preventDefault();
    //Estado del checkbox
    var url = $('#signup-input').attr('data-url') + "?email=" + $('#signup-input').val();
    $.get(url, function (data) {
        if (data.is_taken) {
          document.getElementById('signup-response').innerHTML = `<p>Este correo ya tiene una cuenta asociada, prueba iniciando sesion.</p>`;
        }else{
localStorage.setItem("email", $('#signup-input').val()); // Save email in localStorage
window.location.href = $('#form-signup').attr('data-url'); // Redirecting to step1
        }
      });
  });

  // /* Email validation Listener, when key is pressed */
  // document.getElementById('signup-input').addEventListener("keyup", function (e) {
  //   var url = $('#signup-input').attr('data-url') +"?email="+ this.value;
  //       $.get(url, function (data) {
  //     console.log(data.is_taken); //
  //   });
  // });

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
  navMenu.style.width = '250px';
  all.style.marginLeft = '250px';
  document.body.style.backgroundColor = "rgba(0,0,0,0.4)";
  isOpen = true;
}

function closeMenu() {
  navMenu.style.width = '0';
  all.style.marginLeft = '0';
  document.body.style.backgroundColor = "white";
  isOpen = false;
}
